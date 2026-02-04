# 什么情况下，mysql 会出现死锁的情况？

---

## 一、结论

> **MySQL（InnoDB）出现死锁，本质原因只有一个：
> 多个事务以不同顺序持有并等待对方需要的锁，形成环。**

不是 bug，是**设计必然结果**。

---

## 二、最经典、一定会发生的死锁（顺序不一致）

### 表结构

```sql
CREATE TABLE t (
  id INT PRIMARY KEY,
  value INT
);
```

### 事务 A

```sql
START TRANSACTION;
UPDATE t SET value = value + 1 WHERE id = 1; -- 锁 id=1
UPDATE t SET value = value + 1 WHERE id = 2; -- 等待 id=2
```

### 事务 B

```sql
START TRANSACTION;
UPDATE t SET value = value + 1 WHERE id = 2; -- 锁 id=2
UPDATE t SET value = value + 1 WHERE id = 1; -- 等待 id=1
```

### 结果

```
A 持有 1，等 2
B 持有 2，等 1
```

👉 **死锁**

---

## 三、同一天、多行 update 是高频死锁源（你前面的问题正中）

```sql
UPDATE order_stat
SET cnt = cnt + 1
WHERE stat_date = '2026-02-03';
```

### 为什么会死锁？

* `stat_date` **不是唯一索引**
* 命中多行
* InnoDB 会：

  * 对命中的记录逐行加锁
  * **不同事务扫描顺序可能不同**
* 两个事务互相卡住

👉 **非常常见，线上高频**

---

## 四、范围查询 + 更新（间隙锁）

```sql
UPDATE t
SET value = value + 1
WHERE id BETWEEN 10 AND 20;
```

在 `REPEATABLE READ`（默认）下：

* 会加：

  * 行锁
  * **间隙锁（Gap Lock）**
* 另一个事务：

```sql
INSERT INTO t (id, value) VALUES (15, 1);
```

👉 **互相等待，死锁**

---

## 五、SELECT … FOR UPDATE 也能死锁（很多人误以为不会）

```sql
-- 事务 A
SELECT * FROM t WHERE id = 1 FOR UPDATE;
SELECT * FROM t WHERE id = 2 FOR UPDATE;

-- 事务 B
SELECT * FROM t WHERE id = 2 FOR UPDATE;
SELECT * FROM t WHERE id = 1 FOR UPDATE;
```

👉 **本质和 update 一样，一样死锁**

---

## 六、唯一索引 + 插入，也可能死锁（很反直觉）

```sql
INSERT INTO t (uk, value) VALUES (10, 1);
INSERT INTO t (uk, value) VALUES (20, 1);
```

两个事务交叉插入不同唯一键时：

* 会竞争：

  * 唯一索引
  * 主键
  * 插入意向锁

👉 **InnoDB 内部锁顺序不同 → 死锁**

---

## 七、delete / update + insert 组合（线上事故王）

```sql
-- 事务 A
DELETE FROM t WHERE id = 10;
INSERT INTO t VALUES (10, ...);

-- 事务 B
INSERT INTO t VALUES (10, ...);
```

* delete 持有记录锁
* insert 等待
* 再反向等待

👉 **死锁**

---

## 八、什么情况下“不会”死锁？

这是你在设计时要追求的状态。

### 1️⃣ 单行、唯一索引、固定顺序

```sql
UPDATE t SET v = v + 1 WHERE id = ?
```

👉 **几乎不会死锁**

---

### 2️⃣ 所有事务严格相同顺序访问资源

```text
先锁用户表 → 再锁订单表 → 再锁资产表
```

👉 **工程上最重要的死锁规约**

---

## 九、隔离级别对死锁的影响

| 隔离级别                | 死锁概率           |
| ----------------------- | ------------------ |
| READ COMMITTED          | 较低               |
| REPEATABLE READ（默认） | **最高**           |
| SERIALIZABLE            | 基本串行，但性能差 |

⚠️ 降隔离级别 **不能消灭死锁**，只能减少概率。

---

## 十、死锁发生时 MySQL 做了什么？

* InnoDB **一定会选一个事务回滚**
* 返回错误：

```text
ERROR 1213 (40001): Deadlock found when trying to get lock
```

👉 **你必须重试**

---

## 十一、工程级应对策略（非常重要）

### 1️⃣ 固定锁顺序（最重要）

* 所有事务
* 按相同顺序访问表 / 行

---

### 2️⃣ update 时尽量命中单行

* 用唯一索引
* 拆分统计表

---

### 3️⃣ 减少事务时间

* 不要在事务里：

  * 调接口
  * sleep
  * 写日志

---

### 4️⃣ 死锁必须重试（不是异常）

```java
for (int i = 0; i < 3; i++) {
  try {
    doTx();
    break;
  } catch (DeadlockException e) {
    // retry
  }
}
```
