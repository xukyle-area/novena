# 微服务架构

### 微服务核心概念

| 英文                   | 音标                       | 中文        | 例句                      |
| ---------------------- | -------------------------- | ----------- | ------------------------- |
| microservice           | /ˈmaɪkroʊsɜːrvɪs/          | 微服务      | Microservice architecture |
| monolith               | /ˈmɑːnəlɪθ/                | 单体        | Monolithic application    |
| service                | /ˈsɜːrvɪs/                 | 服务        | Business service          |
| domain                 | /doʊˈmeɪn/                 | 领域        | Business domain           |
| bounded-context        | /ˈbaʊndɪd ˈkɑːntekst/      | 限界上下文  | Bounded context           |
| domain-driven          | /doʊˈmeɪn ˈdrɪvn/          | 领域驱动    | Domain-driven design      |
| aggregate              | /ˈæɡrɪɡət/                 | 聚合        | Aggregate root            |
| entity                 | /ˈentəti/                  | 实体        | Domain entity             |
| value-object           | /ˈvæljuː ˈɑːbdʒekt/        | 值对象      | Value object              |
| repository             | /rɪˈpɑːzətɔːri/            | 仓储        | Repository pattern        |
| API-gateway            | /ˌeɪ piː ˈaɪ ˈɡeɪtweɪ/     | API网关     | API gateway               |
| service-mesh           | /ˈsɜːrvɪs meʃ/             | 服务网格    | Service mesh              |
| sidecar                | /ˈsaɪdkɑːr/                | 边车        | Sidecar proxy             |
| service-discovery      | /ˈsɜːrvɪs dɪˈskʌvəri/      | 服务发现    | Service discovery         |
| service-registry       | /ˈsɜːrvɪs ˈredʒɪstri/      | 服务注册    | Service registry          |
| health-check           | /helθ tʃek/                | 健康检查    | Health check endpoint     |
| heartbeat              | /ˈhɑːrtbiːt/               | 心跳        | Heartbeat signal          |
| load-balancing         | /loʊd ˈbælənsɪŋ/           | 负载均衡    | Load balancing            |
| round-robin            | /raʊnd ˈrɑːbɪn/            | 轮询        | Round-robin algorithm     |
| least-connections      | /liːst kəˈnekʃnz/          | 最少连接    | Least connections         |
| weighted               | /ˈweɪtɪd/                  | 加权        | Weighted load balancing   |
| sticky-session         | /ˈstɪki ˈseʃn/             | 粘性会话    | Sticky session            |
| circuit-breaker        | /ˈsɜːrkɪt ˈbreɪkər/        | 熔断器      | Circuit breaker           |
| rate-limiting          | /reɪt ˈlɪmɪtɪŋ/            | 限流        | Rate limiting             |
| throttling             | /ˈθrɑːtlɪŋ/                | 节流        | Request throttling        |
| bulkhead               | /ˈbʌlkhed/                 | 舱壁隔离    | Bulkhead pattern          |
| retry                  | /ˌriːˈtraɪ/                | 重试        | Retry policy              |
| timeout                | /ˈtaɪmaʊt/                 | 超时        | Timeout configuration     |
| fallback               | /ˈfɔːlbæk/                 | 降级        | Fallback mechanism        |
| graceful-degradation   | /ˈɡreɪsfl ˌdeɡrəˈdeɪʃn/    | 优雅降级    | Graceful degradation      |
| API-versioning         | /ˌeɪ piː ˈaɪ ˈvɜːrʒnɪŋ/    | API版本控制 | API versioning            |
| backward-compatibility | /ˈbækwərd kəmˌpætəˈbɪləti/ | 向后兼容    | Backward compatibility    |
| contract               | /ˈkɑːntrækt/               | 契约        | Service contract          |
| consumer-driven        | /kənˈsuːmər ˈdrɪvn/        | 消费者驱动  | Consumer-driven contract  |
| stub                   | /stʌb/                     | 存根        | Service stub              |
| mock                   | /mɑːk/                     | 模拟        | Mock service              |
| canary-deployment      | /kəˈneri dɪˈplɔɪmənt/      | 金丝雀部署  | Canary deployment         |
| blue-green             | /bluː ɡriːn/               | 蓝绿部署    | Blue-green deployment     |
| rolling-update         | /ˈroʊlɪŋ ʌpˈdeɪt/          | 滚动更新    | Rolling update            |
| feature-flag           | /ˈfiːtʃər flæɡ/            | 特性开关    | Feature flag              |

### 服务间通信

| 英文            | 音标                   | 中文         | 例句                      |
| --------------- | ---------------------- | ------------ | ------------------------- |
| RPC             | /ˌɑːr piː ˈsiː/        | 远程过程调用 | RPC framework             |
| REST            | /rest/                 | REST         | RESTful service           |
| GraphQL         | /ɡræf kjuː ˈel/        | GraphQL      | GraphQL API               |
| gRPC            | /ɡriːˌɑːr piː ˈsiː/    | gRPC         | gRPC service              |
| protocol-buffer | /ˈproʊtəkɑːl ˈbʌfər/   | 协议缓冲     | Protocol buffer           |
| Thrift          | /θrɪft/                | Thrift       | Apache Thrift             |
| message-queue   | /ˈmesɪdʒ kjuː/         | 消息队列     | Message queue             |
| event-driven    | /ɪˈvent ˈdrɪvn/        | 事件驱动     | Event-driven architecture |
| pub-sub         | /pʌb sʌb/              | 发布订阅     | Pub-sub pattern           |
| point-to-point  | /pɔɪnt tuː pɔɪnt/      | 点对点       | Point-to-point messaging  |
| request-reply   | /rɪˈkwest rɪˈplaɪ/     | 请求响应     | Request-reply pattern     |
| fire-and-forget | /ˈfaɪər ənd fərˈɡet/   | 即发即弃     | Fire-and-forget           |
| acknowledgment  | /əkˈnɑːlɪdʒmənt/       | 确认         | Message acknowledgment    |
| idempotency     | /ˌaɪdemˈpoʊtənsi/      | 幂等性       | Idempotent operation      |
| at-most-once    | /ət moʊst wʌns/        | 至多一次     | At-most-once delivery     |
| at-least-once   | /ət liːst wʌns/        | 至少一次     | At-least-once delivery    |
| exactly-once    | /ɪɡˈzæktli wʌns/       | 恰好一次     | Exactly-once delivery     |
| dead-letter     | /ded ˈletər/           | 死信         | Dead letter queue         |
| poison-message  | /ˈpɔɪzn ˈmesɪdʒ/       | 毒药消息     | Poison message            |
| backpressure    | /ˈbækpreʃər/           | 背压         | Backpressure handling     |
| flow-control    | /floʊ kənˈtroʊl/       | 流量控制     | Flow control              |
| correlation-id  | /ˌkɔːrəˈleɪʃn aɪ ˈdiː/ | 关联ID       | Correlation ID            |
| tracing         | /ˈtreɪsɪŋ/             | 追踪         | Distributed tracing       |
| span            | /spæn/                 | 跨度         | Trace span                |
| baggage         | /ˈbæɡɪdʒ/              | 行李         | Trace baggage             |
| sampling        | /ˈsæmplɪŋ/             | 采样         | Trace sampling            |
| instrumentation | /ˌɪnstrəmenˈteɪʃn/     | 埋点         | Code instrumentation      |
| observability   | /əbˌzɜːrvəˈbɪləti/     | 可观测性     | System observability      |
| telemetry       | /təˈlemətri/           | 遥测         | Telemetry data            |
| metrics         | /ˈmetrɪks/             | 指标         | System metrics            |

### 数据管理

| 英文                     | 音标                        | 中文         | 例句                     |
| ------------------------ | --------------------------- | ------------ | ------------------------ |
| database-per-service     | /ˈdeɪtəbeɪs pɜːr ˈsɜːrvɪs/  | 每服务一库   | Database per service     |
| shared-database          | /ʃerd ˈdeɪtəbeɪs/           | 共享数据库   | Shared database          |
| data-ownership           | /ˈdeɪtə ˈoʊnərʃɪp/          | 数据所有权   | Data ownership           |
| eventual-consistency     | /ɪˈventʃuəl kənˈsɪstənsi/   | 最终一致性   | Eventual consistency     |
| SAGA                     | /ˈsɑːɡə/                    | Saga模式     | SAGA pattern             |
| orchestration            | /ˌɔːrkɪˈstreɪʃn/            | 编排         | SAGA orchestration       |
| choreography             | /ˌkɔːriˈɑːɡrəfi/            | 协同         | SAGA choreography        |
| compensating-transaction | /ˈkɑːmpenseɪtɪŋ trænˈzækʃn/ | 补偿事务     | Compensating transaction |
| event-sourcing           | /ɪˈvent ˈsɔːrsɪŋ/           | 事件溯源     | Event sourcing           |
| event-store              | /ɪˈvent stɔːr/              | 事件存储     | Event store              |
| snapshot                 | /ˈsnæpʃɑːt/                 | 快照         | State snapshot           |
| projection               | /prəˈdʒekʃn/                | 投影         | Read projection          |
| CQRS                     | /ˌsiː kjuː ɑːr ˈes/         | 命令查询分离 | CQRS pattern             |
| command                  | /kəˈmænd/                   | 命令         | Command handler          |
| query                    | /ˈkwɪri/                    | 查询         | Query handler            |
| read-model               | /riːd ˈmɑːdl/               | 读模型       | Read model               |
| write-model              | /raɪt ˈmɑːdl/               | 写模型       | Write model              |
| materialized-view        | /məˈtɪriəlaɪzd vjuː/        | 物化视图     | Materialized view        |
| denormalization          | /diːˌnɔːrməlaɪˈzeɪʃn/       | 反规范化     | Data denormalization     |
| change-data-capture      | /tʃeɪndʒ ˈdeɪtə ˈkæptʃər/   | 变更数据捕获 | CDC                      |
| outbox-pattern           | /ˈaʊtbɑːks ˈpætərn/         | 发件箱模式   | Outbox pattern           |
| inbox-pattern            | /ˈɪnbɑːks ˈpætərn/          | 收件箱模式   | Inbox pattern            |
| dual-write               | /ˈduːəl raɪt/               | 双写         | Dual write problem       |
| data-replication         | /ˈdeɪtə ˌreplɪˈkeɪʃn/       | 数据复制     | Data replication         |
| cache-aside              | /kæʃ əˈsaɪd/                | 旁路缓存     | Cache-aside pattern      |
| write-through            | /raɪt θruː/                 | 写穿         | Write-through cache      |
| write-behind             | /raɪt bɪˈhaɪnd/             | 写回         | Write-behind cache       |
| cache-stampede           | /kæʃ stæmˈpiːd/             | 缓存击穿     | Cache stampede           |
| cache-penetration        | /kæʃ ˌpenɪˈtreɪʃn/          | 缓存穿透     | Cache penetration        |
| cache-avalanche          | /kæʃ ˈævəlæntʃ/             | 缓存雪崩     | Cache avalanche          |

