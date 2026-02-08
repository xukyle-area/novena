# 数据库相关

### 关系型数据库

| 英文                | 音标                   | 中文       | 例句                        |
| ------------------- | ---------------------- | ---------- | --------------------------- |
| database            | /ˈdeɪtəbeɪs/           | 数据库     | Relational database         |
| table               | /ˈteɪbl/               | 表         | Database table              |
| row                 | /roʊ/                  | 行         | Table row                   |
| column              | /ˈkɑːləm/              | 列         | Table column                |
| record              | /ˈrekərd/              | 记录       | Database record             |
| field               | /fiːld/                | 字段       | Data field                  |
| schema              | /ˈskiːmə/              | 模式       | Database schema             |
| primary-key         | /ˈpraɪmeri kiː/        | 主键       | Primary key constraint      |
| foreign-key         | /ˈfɔːrən kiː/          | 外键       | Foreign key reference       |
| index               | /ˈɪndeks/              | 索引       | B-tree index                |
| unique              | /juˈniːk/              | 唯一       | Unique constraint           |
| constraint          | /kənˈstreɪnt/          | 约束       | Check constraint            |
| NULL                | /nʌl/                  | 空值       | NULL value                  |
| normalization       | /ˌnɔːrməlaɪˈzeɪʃn/     | 规范化     | Database normalization      |
| denormalization     | /diːˌnɔːrməlaɪˈzeɪʃn/  | 反规范化   | Denormalization             |
| transaction         | /trænˈzækʃn/           | 事务       | Database transaction        |
| ACID                | /ˈæsɪd/                | ACID特性   | ACID properties             |
| atomicity           | /ˌætəˈmɪsəti/          | 原子性     | Transaction atomicity       |
| consistency         | /kənˈsɪstənsi/         | 一致性     | Data consistency            |
| isolation           | /ˌaɪsəˈleɪʃn/          | 隔离性     | Transaction isolation       |
| durability          | /ˌdʊrəˈbɪləti/         | 持久性     | Data durability             |
| commit              | /kəˈmɪt/               | 提交       | Commit transaction          |
| rollback            | /ˈroʊlbæk/             | 回滚       | Rollback transaction        |
| savepoint           | /ˈseɪvpɔɪnt/           | 保存点     | Transaction savepoint       |
| lock                | /lɑːk/                 | 锁         | Row-level lock              |
| deadlock            | /ˈdedlɑːk/             | 死锁       | Database deadlock           |
| pessimistic-lock    | /ˌpesɪˈmɪstɪk lɑːk/    | 悲观锁     | Pessimistic locking         |
| optimistic-lock     | /ˌɑːptɪˈmɪstɪk lɑːk/   | 乐观锁     | Optimistic locking          |
| isolation-level     | /ˌaɪsəˈleɪʃn ˈlevl/    | 隔离级别   | Transaction isolation level |
| read-uncommitted    | /riːd ʌnkəˈmɪtɪd/      | 读未提交   | Read uncommitted            |
| read-committed      | /riːd kəˈmɪtɪd/        | 读已提交   | Read committed              |
| repeatable-read     | /rɪˈpiːtəbl riːd/      | 可重复读   | Repeatable read             |
| serializable        | /ˈsɪriəlaɪzəbl/        | 可串行化   | Serializable isolation      |
| dirty-read          | /ˈdɜːrti riːd/         | 脏读       | Dirty read problem          |
| non-repeatable-read | /nɑːn rɪˈpiːtəbl riːd/ | 不可重复读 | Non-repeatable read         |
| phantom-read        | /ˈfæntəm riːd/         | 幻读       | Phantom read                |
| query               | /ˈkwɪri/               | 查询       | SQL query                   |
| SELECT              | /sɪˈlekt/              | 查询       | SELECT statement            |
| INSERT              | /ɪnˈsɜːrt/             | 插入       | INSERT INTO                 |
| UPDATE              | /ʌpˈdeɪt/              | 更新       | UPDATE statement            |
| DELETE              | /dɪˈliːt/              | 删除       | DELETE FROM                 |
| JOIN                | /dʒɔɪn/                | 连接       | INNER JOIN                  |
| INNER-JOIN          | /ˈɪnər dʒɔɪn/          | 内连接     | Inner join                  |
| LEFT-JOIN           | /left dʒɔɪn/           | 左连接     | Left outer join             |
| RIGHT-JOIN          | /raɪt dʒɔɪn/           | 右连接     | Right join                  |
| FULL-JOIN           | /fʊl dʒɔɪn/            | 全连接     | Full outer join             |
| WHERE               | /wer/                  | 条件       | WHERE clause                |
| GROUP-BY            | /ɡruːp baɪ/            | 分组       | GROUP BY clause             |
| HAVING              | /ˈhævɪŋ/               | 分组条件   | HAVING clause               |
| ORDER-BY            | /ˈɔːrdər baɪ/          | 排序       | ORDER BY clause             |

### 数据库优化

| 英文            | 音标                 | 中文       | 例句                     |
| --------------- | -------------------- | ---------- | ------------------------ |
| performance     | /pərˈfɔːrməns/       | 性能       | Query performance        |
| optimization    | /ˌɑːptɪməˈzeɪʃn/     | 优化       | Database optimization    |
| execution-plan  | /ˌeksɪˈkjuːʃn plæn/  | 执行计划   | Query execution plan     |
| explain         | /ɪkˈspleɪn/          | 解释       | EXPLAIN query            |
| slow-query      | /sloʊ ˈkwɪri/        | 慢查询     | Slow query log           |
| covering-index  | /ˈkʌvərɪŋ ˈɪndeks/   | 覆盖索引   | Covering index           |
| composite-index | /ˈkɑːmpəzɪt ˈɪndeks/ | 组合索引   | Composite index          |
| full-table-scan | /fʊl ˈteɪbl skæn/    | 全表扫描   | Full table scan          |
| index-scan      | /ˈɪndeks skæn/       | 索引扫描   | Index range scan         |
| cardinality     | /ˌkɑːrdɪˈnæləti/     | 基数       | Index cardinality        |
| selectivity     | /sɪˌlekˈtɪvəti/      | 选择性     | Query selectivity        |
| statistics      | /stəˈtɪstɪks/        | 统计信息   | Table statistics         |
| histogram       | /ˈhɪstəɡræm/         | 直方图     | Column histogram         |
| partitioning    | /pɑːrˈtɪʃnɪŋ/        | 分区       | Table partitioning       |
| sharding        | /ˈʃɑːrdɪŋ/           | 分片       | Database sharding        |
| replication     | /ˌreplɪˈkeɪʃn/       | 复制       | Master-slave replication |
| master          | /ˈmæstər/            | 主库       | Master database          |
| slave           | /sleɪv/              | 从库       | Slave replica            |
| read-replica    | /riːd ˈreplɪkə/      | 只读副本   | Read replica             |
| failover        | /ˈfeɪloʊvər/         | 故障转移   | Automatic failover       |
| backup          | /ˈbækʌp/             | 备份       | Database backup          |
| restore         | /rɪˈstɔːr/           | 恢复       | Data restore             |
| snapshot        | /ˈsnæpʃɑːt/          | 快照       | Database snapshot        |
| archive         | /ˈɑːrkaɪv/           | 归档       | Data archiving           |
| purge           | /pɜːrdʒ/             | 清除       | Data purging             |
| vacuum          | /ˈvækjuːm/           | 清理       | Vacuum operation         |
| analyze         | /ˈænəlaɪz/           | 分析       | Analyze table            |
| defragment      | /diːˈfræɡment/       | 碎片整理   | Defragmentation          |
| collation       | /kəˈleɪʃn/           | 排序规则   | Character collation      |
| charset         | /ˈtʃɑːrset/          | 字符集     | UTF-8 charset            |
| encoding        | /ɪnˈkoʊdɪŋ/          | 编码       | Character encoding       |
| buffer-pool     | /ˈbʌfər puːl/        | 缓冲池     | InnoDB buffer pool       |
| redo-log        | /ˈriːduː lɔːɡ/       | 重做日志   | Redo log                 |
| undo-log        | /ˈʌnduː lɔːɡ/        | 撤销日志   | Undo log                 |
| binlog          | /ˈbɪnlɔːɡ/           | 二进制日志 | Binary log               |

### NoSQL数据库

| 英文                  | 音标                      | 中文           | 例句                     |
| --------------------- | ------------------------- | -------------- | ------------------------ |
| NoSQL                 | /noʊ es kjuː ˈel/         | 非关系型数据库 | NoSQL database           |
| document              | /ˈdɑːkjumənt/             | 文档           | Document store           |
| collection            | /kəˈlekʃn/                | 集合           | MongoDB collection       |
| key-value             | /kiː ˈvæljuː/             | 键值           | Key-value store          |
| column-family         | /ˈkɑːləm ˈfæməli/         | 列族           | Column family            |
| graph                 | /ɡræf/                    | 图             | Graph database           |
| node                  | /noʊd/                    | 节点           | Graph node               |
| edge                  | /edʒ/                     | 边             | Graph edge               |
| relationship          | /rɪˈleɪʃnʃɪp/             | 关系           | Node relationship        |
| embedded              | /ɪmˈbedɪd/                | 嵌入           | Embedded document        |
| reference             | /ˈrefrəns/                | 引用           | Document reference       |
| denormalized          | /diːˈnɔːrməlaɪzd/         | 反规范化       | Denormalized data        |
| eventual-consistency  | /ɪˈventʃuəl kənˈsɪstənsi/ | 最终一致性     | Eventual consistency     |
| BASE                  | /beɪs/                    | BASE理论       | BASE properties          |
| basically-available   | /ˈbeɪsɪkli əˈveɪləbl/     | 基本可用       | Basically available      |
| soft-state            | /sɔːft steɪt/             | 软状态         | Soft state               |
| eventually-consistent | /ɪˈventʃuəli kənˈsɪstənt/ | 最终一致       | Eventually consistent    |
| CAP-theorem           | /siː eɪ piː ˈθɪrəm/       | CAP定理        | CAP theorem              |
| consistency           | /kənˈsɪstənsi/            | 一致性         | Strong consistency       |
| availability          | /əˌveɪləˈbɪləti/          | 可用性         | High availability        |
| partition-tolerance   | /pɑːrˈtɪʃn ˈtɑːlərəns/    | 分区容错       | Partition tolerance      |
| replica-set           | /ˈreplɪkə set/            | 副本集         | MongoDB replica set      |
| shard                 | /ʃɑːrd/                   | 分片           | Data shard               |
| chunk                 | /tʃʌŋk/                   | 数据块         | Shard chunk              |
| hash-based            | /hæʃ beɪst/               | 基于哈希       | Hash-based sharding      |
| range-based           | /reɪndʒ beɪst/            | 基于范围       | Range-based partitioning |
| aggregation           | /ˌæɡrɪˈɡeɪʃn/             | 聚合           | Aggregation pipeline     |
| pipeline              | /ˈpaɪplaɪn/               | 管道           | Aggregation pipeline     |
| projection            | /prəˈdʒekʃn/              | 投影           | Field projection         |
| upsert                | /ˈʌpsɜːrt/                | 插入或更新     | Upsert operation         |
| bulk                  | /bʌlk/                    | 批量           | Bulk operation           |
| time-to-live          | /taɪm tuː lɪv/            | 生存时间       | TTL index                |
| expiration            | /ˌekspəˈreɪʃn/            | 过期           | Data expiration          |
| compaction            | /kəmˈpækʃn/               | 压缩           | Log compaction           |
| rebalancing           | /ˌriːˈbælənsɪŋ/           | 重新平衡       | Shard rebalancing        |