# 分布式系统

### 分布式核心概念

| 英文                 | 音标                      | 中文       | 例句                     |
| -------------------- | ------------------------- | ---------- | ------------------------ |
| distributed          | /dɪˈstrɪbjuːtɪd/          | 分布式     | Distributed system       |
| cluster              | /ˈklʌstər/                | 集群       | Server cluster           |
| node                 | /noʊd/                    | 节点       | Cluster node             |
| peer                 | /pɪr/                     | 对等节点   | Peer-to-peer             |
| master               | /ˈmæstər/                 | 主节点     | Master node              |
| slave                | /sleɪv/                   | 从节点     | Slave node               |
| leader               | /ˈliːdər/                 | 领导者     | Leader election          |
| follower             | /ˈfɑːloʊər/               | 跟随者     | Follower node            |
| replica              | /ˈreplɪkə/                | 副本       | Data replica             |
| replication          | /ˌreplɪˈkeɪʃn/            | 复制       | Data replication         |
| synchronous          | /ˈsɪŋkrənəs/              | 同步       | Synchronous replication  |
| asynchronous         | /eɪˈsɪŋkrənəs/            | 异步       | Asynchronous replication |
| consensus            | /kənˈsensəs/              | 共识       | Consensus algorithm      |
| Paxos                | /ˈpæksɒs/                 | Paxos算法  | Paxos protocol           |
| Raft                 | /ræft/                    | Raft算法   | Raft consensus           |
| quorum               | /ˈkwɔːrəm/                | 法定人数   | Quorum consensus         |
| split-brain          | /splɪt breɪn/             | 脑裂       | Split-brain problem      |
| partition            | /pɑːrˈtɪʃn/               | 分区       | Network partition        |
| partition-tolerance  | /pɑːrˈtɪʃn ˈtɑːlərəns/    | 分区容错   | Partition tolerance      |
| failover             | /ˈfeɪloʊvər/              | 故障转移   | Automatic failover       |
| failback             | /ˈfeɪlbæk/                | 故障恢复   | Failback process         |
| degradation          | /ˌdeɡrəˈdeɪʃn/            | 降级       | Service degradation      |
| circuit-breaker      | /ˈsɜːrkɪt ˈbreɪkər/       | 熔断器     | Circuit breaker pattern  |
| bulkhead             | /ˈbʌlkhed/                | 舱壁       | Bulkhead isolation       |
| timeout              | /ˈtaɪmaʊt/                | 超时       | Request timeout          |
| retry                | /ˌriːˈtraɪ/               | 重试       | Retry mechanism          |
| backoff              | /ˈbækɔːf/                 | 退避       | Exponential backoff      |
| idempotency          | /ˌaɪdemˈpoʊtənsi/         | 幂等性     | Idempotency key          |
| eventual-consistency | /ɪˈventʃuəl kənˈsɪstənsi/ | 最终一致性 | Eventual consistency     |
| strong-consistency   | /strɔːŋ kənˈsɪstənsi/     | 强一致性   | Strong consistency       |
| weak-consistency     | /wiːk kənˈsɪstənsi/       | 弱一致性   | Weak consistency         |
| causal-consistency   | /ˈkɔːzl kənˈsɪstənsi/     | 因果一致性 | Causal consistency       |
| linearizability      | /ˌlɪniəraɪzəˈbɪləti/      | 线性一致性 | Linearizability          |
| serializability      | /ˌsɪriəlaɪzəˈbɪləti/      | 可串行化   | Serializability          |
| two-phase-commit     | /tuː feɪz kəˈmɪt/         | 两阶段提交 | 2PC protocol             |
| three-phase-commit   | /θriː feɪz kəˈmɪt/        | 三阶段提交 | 3PC protocol             |
| SAGA                 | /ˈsɑːɡə/                  | Saga模式   | Saga pattern             |
| compensation         | /ˌkɑːmpenˈseɪʃn/          | 补偿       | Compensating transaction |
| orchestration        | /ˌɔːrkɪˈstreɪʃn/          | 编排       | Service orchestration    |
| choreography         | /ˌkɔːriˈɑːɡrəfi/          | 协同       | Service choreography     |

### 分布式存储

| 英文                | 音标                       | 中文         | 例句                      |
| ------------------- | -------------------------- | ------------ | ------------------------- |
| distributed-storage | /dɪˈstrɪbjuːtɪd ˈstɔːrɪdʒ/ | 分布式存储   | Distributed file system   |
| object-storage      | /ˈɑːbdʒekt ˈstɔːrɪdʒ/      | 对象存储     | S3 object storage         |
| block-storage       | /blɑːk ˈstɔːrɪdʒ/          | 块存储       | Block storage device      |
| file-storage        | /faɪl ˈstɔːrɪdʒ/           | 文件存储     | Network file storage      |
| consistency-hash    | /kənˈsɪstənsi hæʃ/         | 一致性哈希   | Consistent hashing        |
| virtual-node        | /ˈvɜːrtʃuəl noʊd/          | 虚拟节点     | Virtual node mapping      |
| gossip-protocol     | /ˈɡɑːsɪp ˈproʊtəkɑːl/      | Gossip协议   | Gossip protocol           |
| vector-clock        | /ˈvektər klɑːk/            | 向量时钟     | Vector clock              |
| version-vector      | /ˈvɜːrʒn ˈvektər/          | 版本向量     | Version vector            |
| merkle-tree         | /ˈmɜːrkl triː/             | 默克尔树     | Merkle tree               |
| bloom-filter        | /bluːm ˈfɪltər/            | 布隆过滤器   | Bloom filter              |
| LSM-tree            | /ˌel es ˈem triː/          | LSM树        | Log-structured merge tree |
| compaction          | /kəmˈpækʃn/                | 压缩         | Log compaction            |
| write-ahead-log     | /raɪt əˈhed lɔːɡ/          | 预写日志     | Write-ahead log           |
| commit-log          | /kəˈmɪt lɔːɡ/              | 提交日志     | Commit log                |
| memtable            | /ˈmemteɪbl/                | 内存表       | Memtable structure        |
| SSTable             | /ˌes es ˈteɪbl/            | 有序字符串表 | Sorted string table       |
| tombstone           | /ˈtuːmstoʊn/               | 墓碑标记     | Tombstone marker          |
| anti-entropy        | /ˌænti ˈentrəpi/           | 反熵         | Anti-entropy repair       |
| read-repair         | /riːd rɪˈper/              | 读修复       | Read repair               |
| hinted-handoff      | /ˈhɪntɪd ˈhændɔːf/         | 暗示移交     | Hinted handoff            |
| sloppy-quorum       | /ˈslɑːpi ˈkwɔːrəm/         | 宽松法定人数 | Sloppy quorum             |
| erasure-coding      | /ɪˈreɪʒər ˈkoʊdɪŋ/         | 纠删码       | Erasure coding            |
| replication-factor  | /ˌreplɪˈkeɪʃn ˈfæktər/     | 复制因子     | Replication factor        |
| rack-awareness      | /ræk əˈwernəs/             | 机架感知     | Rack-aware placement      |
| data-locality       | /ˈdeɪtə loʊˈkæləti/        | 数据本地性   | Data locality             |
| hotspot             | /ˈhɑːtspɑːt/               | 热点         | Data hotspot              |
| cold-storage        | /koʊld ˈstɔːrɪdʒ/          | 冷存储       | Cold storage tier         |
| tiering             | /ˈtɪrɪŋ/                   | 分层         | Storage tiering           |
| deduplication       | /diːˌduːplɪˈkeɪʃn/         | 去重         | Data deduplication        |

### 分布式计算

| 英文            | 音标               | 中文       | 例句                   |
| --------------- | ------------------ | ---------- | ---------------------- |
| MapReduce       | /mæp rɪˈduːs/      | MapReduce  | MapReduce framework    |
| mapper          | /ˈmæpər/           | 映射器     | Mapper function        |
| reducer         | /rɪˈduːsər/        | 归约器     | Reducer function       |
| combiner        | /kəmˈbaɪnər/       | 合并器     | Combiner optimization  |
| partitioner     | /pɑːrˈtɪʃnər/      | 分区器     | Custom partitioner     |
| shuffle         | /ˈʃʌfl/            | 洗牌       | Shuffle phase          |
| sort            | /sɔːrt/            | 排序       | Sort phase             |
| merge           | /mɜːrdʒ/           | 合并       | Merge sort             |
| join            | /dʒɔɪn/            | 连接       | Map-side join          |
| broadcast       | /ˈbrɔːdkæst/       | 广播       | Broadcast join         |
| DAG             | /dæɡ/              | 有向无环图 | DAG execution          |
| stage           | /steɪdʒ/           | 阶段       | Execution stage        |
| task            | /tæsk/             | 任务       | Distributed task       |
| executor        | /ɪɡˈzekjətər/      | 执行器     | Task executor          |
| driver          | /ˈdraɪvər/         | 驱动器     | Driver program         |
| worker          | /ˈwɜːrkər/         | 工作节点   | Worker node            |
| batch           | /bætʃ/             | 批处理     | Batch processing       |
| streaming       | /ˈstriːmɪŋ/        | 流处理     | Stream processing      |
| micro-batch     | /ˈmaɪkroʊ bætʃ/    | 微批处理   | Micro-batch processing |
| window          | /ˈwɪndoʊ/          | 窗口       | Time window            |
| tumbling-window | /ˈtʌmblɪŋ ˈwɪndoʊ/ | 滚动窗口   | Tumbling window        |
| sliding-window  | /ˈslaɪdɪŋ ˈwɪndoʊ/ | 滑动窗口   | Sliding window         |
| session-window  | /ˈseʃn ˈwɪndoʊ/    | 会话窗口   | Session window         |
| watermark       | /ˈwɔːtərmɑːrk/     | 水印       | Event watermark        |
| checkpoint      | /ˈtʃekpɔɪnt/       | 检查点     | State checkpoint       |
| state           | /steɪt/            | 状态       | Stateful processing    |
| stateful        | /ˈsteɪtfəl/        | 有状态     | Stateful operator      |
| stateless       | /ˈsteɪtləs/        | 无状态     | Stateless operation    |
| exactly-once    | /ɪɡˈzæktli wʌns/   | 恰好一次   | Exactly-once semantics |
| at-least-once   | /ət liːst wʌns/    | 至少一次   | At-least-once delivery |

