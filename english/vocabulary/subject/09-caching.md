# 缓存技术

### Redis核心

| 英文             | 音标                   | 中文         | 例句                     |
| ---------------- | ---------------------- | ------------ | ------------------------ |
| Redis            | /ˈredɪs/               | Redis        | Redis cache              |
| in-memory        | /ɪn ˈmeməri/           | 内存         | In-memory database       |
| key-value        | /kiː ˈvæljuː/          | 键值         | Key-value store          |
| string           | /strɪŋ/                | 字符串       | String type              |
| list             | /lɪst/                 | 列表         | List data structure      |
| set              | /set/                  | 集合         | Set type                 |
| sorted-set       | /ˈsɔːrtɪd set/         | 有序集合     | Sorted set (zset)        |
| hash             | /hæʃ/                  | 哈希         | Hash type                |
| bitmap           | /ˈbɪtmæp/              | 位图         | Bitmap operations        |
| hyperloglog      | /ˈhaɪpərˌlɔːɡlɔːɡ/     | HyperLogLog  | HyperLogLog counter      |
| geospatial       | /ˌdʒiːoʊˈspeɪʃl/       | 地理空间     | Geospatial index         |
| stream           | /striːm/               | 流           | Redis Stream             |
| pub-sub          | /pʌb sʌb/              | 发布订阅     | Pub/Sub messaging        |
| transaction      | /trænˈzækʃn/           | 事务         | Redis transaction        |
| pipeline         | /ˈpaɪplaɪn/            | 管道         | Command pipeline         |
| Lua-script       | /ˈluːə skrɪpt/         | Lua脚本      | Lua scripting            |
| persistence      | /pərˈsɪstəns/          | 持久化       | Data persistence         |
| RDB              | /ˌɑːr diː ˈbiː/        | RDB快照      | RDB snapshot             |
| AOF              | /ˌeɪ oʊ ˈef/           | 追加文件     | Append-only file         |
| rewrite          | /ˌriːˈraɪt/            | 重写         | AOF rewrite              |
| replication      | /ˌreplɪˈkeɪʃn/         | 复制         | Master-slave replication |
| sentinel         | /ˈsentɪnl/             | 哨兵         | Redis Sentinel           |
| cluster          | /ˈklʌstər/             | 集群         | Redis Cluster            |
| slot             | /slɑːt/                | 槽           | Hash slot                |
| resharding       | /riːˈʃɑːrdɪŋ/          | 重分片       | Cluster resharding       |
| failover         | /ˈfeɪloʊvər/           | 故障转移     | Automatic failover       |
| TTL              | /ˌtiː tiː ˈel/         | 生存时间     | Key TTL                  |
| expiration       | /ˌekspəˈreɪʃn/         | 过期         | Key expiration           |
| eviction         | /ɪˈvɪkʃn/              | 驱逐         | Key eviction             |
| LRU              | /ˌel ɑːr ˈjuː/         | 最近最少使用 | LRU algorithm            |
| LFU              | /ˌel ef ˈjuː/          | 最不经常使用 | LFU algorithm            |
| maxmemory        | /mæks ˈmeməri/         | 最大内存     | Maxmemory policy         |
| distributed-lock | /dɪˈstrɪbjuːtɪd lɑːk/  | 分布式锁     | Distributed lock         |
| Redlock          | /ˈredlɑːk/             | Redlock算法  | Redlock algorithm        |
| atomic           | /əˈtɑːmɪk/             | 原子         | Atomic operation         |
| INCR             | /ˈɪŋkrəmənt/           | 自增         | INCR command             |
| DECR             | /ˈdekrəmənt/           | 自减         | DECR command             |
| SETNX            | /set ɪf nɑːt ɪɡˈzɪsts/ | 不存在则设置 | SETNX command            |
| GETSET           | /ɡet set/              | 获取并设置   | GETSET command           |
| WATCH            | /wɑːtʃ/                | 监视         | WATCH command            |

### 缓存策略

| 英文                 | 音标                      | 中文       | 例句                  |
| -------------------- | ------------------------- | ---------- | --------------------- |
| cache-aside          | /kæʃ əˈsaɪd/              | 旁路缓存   | Cache-aside pattern   |
| read-through         | /riːd θruː/               | 读穿       | Read-through cache    |
| write-through        | /raɪt θruː/               | 写穿       | Write-through cache   |
| write-behind         | /raɪt bɪˈhaɪnd/           | 写回       | Write-behind cache    |
| write-around         | /raɪt əˈraʊnd/            | 绕写       | Write-around pattern  |
| cache-warming        | /kæʃ ˈwɔːrmɪŋ/            | 缓存预热   | Cache warming         |
| lazy-loading         | /ˈleɪzi ˈloʊdɪŋ/          | 懒加载     | Lazy loading          |
| eager-loading        | /ˈiːɡər ˈloʊdɪŋ/          | 饿加载     | Eager loading         |
| cache-hit            | /kæʃ hɪt/                 | 缓存命中   | Cache hit rate        |
| cache-miss           | /kæʃ mɪs/                 | 缓存未命中 | Cache miss            |
| hit-rate             | /hɪt reɪt/                | 命中率     | Cache hit rate        |
| miss-rate            | /mɪs reɪt/                | 未命中率   | Miss rate             |
| cold-start           | /koʊld stɑːrt/            | 冷启动     | Cold start problem    |
| cache-penetration    | /kæʃ ˌpenɪˈtreɪʃn/        | 缓存穿透   | Cache penetration     |
| cache-breakdown      | /kæʃ ˈbreɪkdaʊn/          | 缓存击穿   | Cache breakdown       |
| cache-avalanche      | /kæʃ ˈævəlæntʃ/           | 缓存雪崩   | Cache avalanche       |
| bloom-filter         | /bluːm ˈfɪltər/           | 布隆过滤器 | Bloom filter          |
| null-cache           | /nʌl kæʃ/                 | 空值缓存   | Cache null values     |
| hotspot              | /ˈhɑːtspɑːt/              | 热点       | Hot key               |
| hotkey               | /hɑːt kiː/                | 热点键     | Hot key problem       |
| big-key              | /bɪɡ kiː/                 | 大键       | Big key issue         |
| invalidation         | /ɪnˌvælɪˈdeɪʃn/           | 失效       | Cache invalidation    |
| refresh              | /rɪˈfreʃ/                 | 刷新       | Cache refresh         |
| update               | /ʌpˈdeɪt/                 | 更新       | Cache update          |
| delete               | /dɪˈliːt/                 | 删除       | Cache delete          |
| consistency          | /kənˈsɪstənsi/            | 一致性     | Cache consistency     |
| staleness            | /steɪlnəs/                | 过时性     | Data staleness        |
| freshness            | /ˈfreʃnəs/                | 新鲜度     | Data freshness        |
| coherence            | /koʊˈhɪrəns/              | 一致性     | Cache coherence       |
| synchronization      | /ˌsɪŋkrənaɪˈzeɪʃn/        | 同步       | Data synchronization  |
| eventual-consistency | /ɪˈventʃuəl kənˈsɪstənsi/ | 最终一致性 | Eventual consistency  |
| strong-consistency   | /strɔːŋ kənˈsɪstənsi/     | 强一致性   | Strong consistency    |
| weak-consistency     | /wiːk kənˈsɪstənsi/       | 弱一致性   | Weak consistency      |
| double-delete        | /ˈdʌbl dɪˈliːt/           | 双删       | Double delete pattern |
| delayed-delete       | /dɪˈleɪd dɪˈliːt/         | 延迟删除   | Delayed deletion      |
| multi-level          | /ˈmʌlti ˈlevl/            | 多级       | Multi-level cache     |
| local-cache          | /ˈloʊkl kæʃ/              | 本地缓存   | Local cache           |
| distributed-cache    | /dɪˈstrɪbjuːtɪd kæʃ/      | 分布式缓存 | Distributed cache     |
| cache-hierarchy      | /kæʃ ˈhaɪərɑːrki/         | 缓存层次   | Cache hierarchy       |
| tiered-cache         | /tɪrd kæʃ/                | 分层缓存   | Tiered caching        |

