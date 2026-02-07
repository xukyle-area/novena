# mysql中如果出现了并发修改，应该怎么处理呢？

## 一、最常见情况：两个事务同时 update 同一行（同一天的记录）

假设表里有一条记录：

```sql
date = '2026-02-03'
count = 10
```

### 两个提交几乎同时执行

```sql
-- 事务 A
START TRANSACTION;
UPDATE t SET count = 11 WHERE date = '2026-02-03';
COMMIT;

-- 事务 B
START TRANSACTION;
UPDATE t SET count = 12 WHERE date = '2026-02-03';
COMMIT;
```

### 实际发生的事情

* InnoDB 会对 **同一行加行锁（X 锁）**
* **先拿到锁的事务执行**
* 后一个事务会：

  * 阻塞等待
  * 前一个事务 commit 后继续执行
* **最终结果是后提交的值覆盖前一个**

👉 **不会脏写，不会报错，但可能发生「更新丢失」**

---

## 二、危险情况：读 → 算 → 写（典型丢数据）

这是线上事故最多的一种。

### 伪代码

```sql
-- 事务 A
SELECT count FROM t WHERE date = '2026-02-03'; -- 读到 10
UPDATE t SET count = 11 WHERE date = '2026-02-03';

-- 事务 B
SELECT count FROM t WHERE date = '2026-02-03'; -- 也读到 10
UPDATE t SET count = 11 WHERE date = '2026-02-03';
```

### 结果

* 两个事务都基于旧值 10 计算
* 最终 `count = 11`
* **本来应该是 12，却丢了一次更新**

👉 **这叫「丢失更新（Lost Update）」**
👉 MySQL **不会帮你兜底**

---

## 三、安全写法 1：原子更新（强烈推荐）

### 正确姿势

```sql
UPDATE t
SET count = count + 1
WHERE date = '2026-02-03';
```

### 为什么安全

* 在行锁保护下
* 更新是原子的
* 并发 100 次，结果就是 +100

👉 **这是最推荐、最常见的写法**

---

## 四、安全写法 2：SELECT … FOR UPDATE

当你**必须先读再算**时：

```sql
START TRANSACTION;

SELECT count
FROM t
WHERE date = '2026-02-03'
FOR UPDATE;

-- 业务计算
UPDATE t
SET count = ?
WHERE date = '2026-02-03';

COMMIT;
```

### 作用

* `FOR UPDATE` 会直接加行锁
* 其他事务在你 commit 前读不到 / 改不了这行

👉 **避免丢更新，但事务时间一定要短**

---

## 五、不同隔离级别的影响（重点是这个）

| 隔离级别                | 并发 update 同一行     |
| ----------------------- | ---------------------- |
| READ UNCOMMITTED        | 有脏读，不推荐         |
| READ COMMITTED          | 不会脏写，但可能丢更新 |
| REPEATABLE READ（默认） | 同上                   |
| SERIALIZABLE            | 会变成串行，性能很差   |

⚠️ **隔离级别解决不了丢更新**
必须靠：

* 原子 update
* 显式锁

---

## 六、如果是「同一天但多行」呢？

```sql
UPDATE t
SET ...
WHERE date = '2026-02-03';
```

* 如果命中 **多行**
* InnoDB 会：

  * 对命中的每一行加锁
  * 锁顺序不同可能导致 **死锁**
* MySQL 会自动回滚其中一个事务