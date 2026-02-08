# 性能优化

### 性能指标

| 英文               | 音标                           | 中文           | 例句                       |
| ------------------ | ------------------------------ | -------------- | -------------------------- |
| performance        | /pərˈfɔːrməns/                 | 性能           | System performance         |
| throughput         | /ˈθruːpʊt/                     | 吞吐量         | Request throughput         |
| latency            | /ˈleɪtənsi/                    | 延迟           | Response latency           |
| response-time      | /rɪˈspɑːns taɪm/               | 响应时间       | Average response time      |
| QPS                | /ˌkjuː piː ˈes/                | 每秒查询数     | Queries per second         |
| TPS                | /ˌtiː piː ˈes/                 | 每秒事务数     | Transactions per second    |
| RPS                | /ˌɑːr piː ˈes/                 | 每秒请求数     | Requests per second        |
| concurrency        | /kənˈkɜːrənsi/                 | 并发数         | Concurrent users           |
| CPU-utilization    | /ˌsiː piː ˈjuː ˌjuːtələˈzeɪʃn/ | CPU利用率      | CPU utilization            |
| memory-usage       | /ˈmeməri ˈjuːsɪdʒ/             | 内存使用       | Memory usage               |
| disk-I/O           | /dɪsk ˌaɪ ˈoʊ/                 | 磁盘I/O        | Disk I/O                   |
| network-bandwidth  | /ˈnetwɜːrk ˈbændwɪdθ/          | 网络带宽       | Network bandwidth          |
| IOPS               | /ˌaɪ oʊ piː ˈes/               | 每秒I/O操作数  | I/O operations per second  |
| percentile         | /pərˈsentaɪl/                  | 百分位         | 95th percentile            |
| p50                | /piː ˈfɪfti/                   | 50分位         | P50 latency                |
| p95                | /piː ˈnaɪnti faɪv/             | 95分位         | P95 latency                |
| p99                | /piː ˈnaɪnti naɪn/             | 99分位         | P99 latency                |
| p999               | /piː naɪn naɪn naɪn/           | 99.9分位       | P999 latency               |
| average            | /ˈævərɪdʒ/                     | 平均值         | Average latency            |
| median             | /ˈmiːdiən/                     | 中位数         | Median response time       |
| variance           | /ˈveriəns/                     | 方差           | Response time variance     |
| standard-deviation | /ˈstændərd ˌdiːviˈeɪʃn/        | 标准差         | Standard deviation         |
| jitter             | /ˈdʒɪtər/                      | 抖动           | Latency jitter             |
| bottleneck         | /ˈbɑːtlnek/                    | 瓶颈           | Performance bottleneck     |
| saturation         | /ˌsætʃəˈreɪʃn/                 | 饱和           | Resource saturation        |
| degradation        | /ˌdeɡrəˈdeɪʃn/                 | 降级           | Performance degradation    |
| SLA                | /ˌes el ˈeɪ/                   | 服务级别协议   | Service Level Agreement    |
| SLO                | /ˌes el ˈoʊ/                   | 服务级别目标   | Service Level Objective    |
| SLI                | /ˌes el ˈaɪ/                   | 服务级别指标   | Service Level Indicator    |
| uptime             | /ˈʌptaɪm/                      | 正常运行时间   | System uptime              |
| downtime           | /ˈdaʊntaɪm/                    | 停机时间       | Planned downtime           |
| availability       | /əˌveɪləˈbɪləti/               | 可用性         | 99.99% availability        |
| reliability        | /rɪˌlaɪəˈbɪləti/               | 可靠性         | System reliability         |
| MTBF               | /ˌem tiː biː ˈef/              | 平均无故障时间 | Mean Time Between Failures |
| MTTR               | /ˌem tiː tiː ˈɑːr/             | 平均修复时间   | Mean Time To Repair        |
| error-rate         | /ˈerər reɪt/                   | 错误率         | Request error rate         |
| success-rate       | /səkˈses reɪt/                 | 成功率         | Transaction success rate   |
| retry-rate         | /ˌriːˈtraɪ reɪt/               | 重试率         | Retry rate                 |
| timeout-rate       | /ˈtaɪmaʊt reɪt/                | 超时率         | Timeout rate               |
| connection-pool    | /kəˈnekʃn puːl/                | 连接池         | Connection pool size       |

### 优化技术

| 英文                | 音标                  | 中文         | 例句                     |
| ------------------- | --------------------- | ------------ | ------------------------ |
| optimization        | /ˌɑːptɪməˈzeɪʃn/      | 优化         | Performance optimization |
| profiling           | /ˈproʊfaɪlɪŋ/         | 性能分析     | Code profiling           |
| benchmarking        | /ˈbentʃmɑːrkɪŋ/       | 基准测试     | Performance benchmarking |
| caching             | /ˈkæʃɪŋ/              | 缓存         | Data caching             |
| memoization         | /ˌmeməˈzeɪʃn/         | 记忆化       | Function memoization     |
| lazy-loading        | /ˈleɪzi ˈloʊdɪŋ/      | 懒加载       | Lazy loading             |
| eager-loading       | /ˈiːɡər ˈloʊdɪŋ/      | 饿加载       | Eager loading            |
| prefetching         | /priːˈfetʃɪŋ/         | 预取         | Data prefetching         |
| preloading          | /priːˈloʊdɪŋ/         | 预加载       | Resource preloading      |
| compression         | /kəmˈpreʃn/           | 压缩         | Data compression         |
| minification        | /ˌmɪnɪfɪˈkeɪʃn/       | 最小化       | Code minification        |
| bundling            | /ˈbʌndlɪŋ/            | 打包         | Asset bundling           |
| pagination          | /ˌpædʒɪˈneɪʃn/        | 分页         | Result pagination        |
| batching            | /ˈbætʃɪŋ/             | 批处理       | Request batching         |
| debouncing          | /dɪˈbaʊnsɪŋ/          | 防抖         | Input debouncing         |
| throttling          | /ˈθrɑːtlɪŋ/           | 节流         | Event throttling         |
| pooling             | /ˈpuːlɪŋ/             | 池化         | Resource pooling         |
| connection-reuse    | /kəˈnekʃn ˌriːˈjuːz/  | 连接复用     | Connection reuse         |
| keep-alive          | /kiːp əˈlaɪv/         | 保持连接     | HTTP keep-alive          |
| multiplexing        | /ˈmʌltɪpleksɪŋ/       | 多路复用     | HTTP/2 multiplexing      |
| pipelining          | /ˈpaɪplaɪnɪŋ/         | 流水线       | Request pipelining       |
| asynchronous        | /eɪˈsɪŋkrənəs/        | 异步         | Asynchronous processing  |
| non-blocking        | /nɑːn ˈblɑːkɪŋ/       | 非阻塞       | Non-blocking I/O         |
| parallel-processing | /ˈpærəlel ˈprɑːsesɪŋ/ | 并行处理     | Parallel processing      |
| sharding            | /ˈʃɑːrdɪŋ/            | 分片         | Database sharding        |
| partitioning        | /pɑːrˈtɪʃnɪŋ/         | 分区         | Table partitioning       |
| indexing            | /ˈɪndeksɪŋ/           | 索引         | Database indexing        |
| denormalization     | /diːˌnɔːrməlaɪˈzeɪʃn/ | 反规范化     | Data denormalization     |
| materialized-view   | /məˈtɪriəlaɪzd vjuː/  | 物化视图     | Materialized view        |
| read-replica        | /riːd ˈreplɪkə/       | 读副本       | Read replica             |
| write-buffer        | /raɪt ˈbʌfər/         | 写缓冲       | Write buffer             |
| memory-mapping      | /ˈmeməri ˈmæpɪŋ/      | 内存映射     | Memory-mapped file       |
| zero-copy           | /ˈzɪroʊ ˈkɑːpi/       | 零拷贝       | Zero-copy transfer       |
| CDN                 | /ˌsiː diː ˈen/        | 内容分发网络 | Content Delivery Network |
| edge-caching        | /edʒ ˈkæʃɪŋ/          | 边缘缓存     | Edge caching             |
| static-content      | /ˈstætɪk ˈkɑːntent/   | 静态内容     | Static content           |
| dynamic-content     | /daɪˈnæmɪk ˈkɑːntent/ | 动态内容     | Dynamic content          |
| resource-pooling    | /ˈriːsɔːrs ˈpuːlɪŋ/   | 资源池化     | Resource pooling         |
| object-pooling      | /ˈɑːbdʒekt ˈpuːlɪŋ/   | 对象池       | Object pooling           |
| vertical-scaling    | /ˈvɜːrtɪkl ˈskeɪlɪŋ/  | 垂直扩展     | Vertical scaling         |

### JVM优化

| 英文               | 音标                         | 中文       | 例句                    |
| ------------------ | ---------------------------- | ---------- | ----------------------- |
| JVM-tuning         | /ˌdʒeɪ viː em ˈtuːnɪŋ/       | JVM调优    | JVM tuning              |
| heap-size          | /hiːp saɪz/                  | 堆大小     | Heap size configuration |
| Xms                | /eks em es/                  | 初始堆     | Initial heap size       |
| Xmx                | /eks em eks/                 | 最大堆     | Maximum heap size       |
| Xmn                | /eks em en/                  | 年轻代     | Young generation size   |
| Xss                | /eks es es/                  | 栈大小     | Thread stack size       |
| MetaspaceSize      | /ˈmetəspeɪs saɪz/            | 元空间大小 | Metaspace size          |
| MaxMetaspaceSize   | /mæks ˈmetəspeɪs saɪz/       | 最大元空间 | Max metaspace size      |
| GC-tuning          | /dʒiː siː ˈtuːnɪŋ/           | GC调优     | GC tuning               |
| GC-algorithm       | /dʒiː siː ˈælɡərɪðəm/        | GC算法     | GC algorithm            |
| Serial-GC          | /ˈsɪriəl dʒiː siː/           | 串行GC     | Serial GC               |
| Parallel-GC        | /ˈpærəlel dʒiː siː/          | 并行GC     | Parallel GC             |
| CMS                | /ˌsiː em ˈes/                | CMS收集器  | CMS GC                  |
| G1-GC              | /dʒiː wʌn dʒiː siː/          | G1收集器   | G1 GC                   |
| ZGC                | /ziː dʒiː siː/               | ZGC收集器  | ZGC                     |
| pause-time         | /pɔːz taɪm/                  | 暂停时间   | GC pause time           |
| throughput         | /ˈθruːpʊt/                   | 吞吐量     | GC throughput           |
| footprint          | /ˈfʊtprɪnt/                  | 内存占用   | Memory footprint        |
| compaction         | /kəmˈpækʃn/                  | 压缩       | Heap compaction         |
| survivor-ratio     | /sərˈvaɪvər ˈreɪʃioʊ/        | 幸存区比例 | Survivor ratio          |
| tenuring-threshold | /ˈtenjərɪŋ ˈθreʃhoʊld/       | 晋升阈值   | Tenuring threshold      |
| parallel-threads   | /ˈpærəlel θredz/             | 并行线程数 | Parallel GC threads     |
| concurrent-threads | /kənˈkɜːrənt θredz/          | 并发线程数 | Concurrent GC threads   |
| GC-log             | /dʒiː siː lɔːɡ/              | GC日志     | GC log file             |
| verbose-GC         | /vɜːrˈboʊs dʒiː siː/         | 详细GC     | Verbose GC              |
| PrintGCDetails     | /prɪnt dʒiː siː dɪˈteɪlz/    | 打印GC详情 | Print GC details        |
| heap-dump          | /hiːp dʌmp/                  | 堆转储     | Heap dump               |
| thread-dump        | /θred dʌmp/                  | 线程转储   | Thread dump             |
| JIT-compilation    | /ˌdʒeɪ aɪ tiː ˌkɑːmpɪˈleɪʃn/ | JIT编译    | JIT compilation         |
| code-cache         | /koʊd kæʃ/                   | 代码缓存   | Code cache              |

