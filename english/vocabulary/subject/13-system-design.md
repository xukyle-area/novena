# 系统设计

### 架构模式

| 英文               | 音标                   | 中文         | 例句                    |
| ------------------ | ---------------------- | ------------ | ----------------------- |
| architecture       | /ˈɑːrkɪtektʃər/        | 架构         | System architecture     |
| layered            | /ˈleɪərd/              | 分层         | Layered architecture    |
| MVC                | /ˌem viː ˈsiː/         | MVC模式      | Model-View-Controller   |
| MVP                | /ˌem viː ˈpiː/         | MVP模式      | Model-View-Presenter    |
| MVVM               | /ˌem viː viː ˈem/      | MVVM模式     | Model-View-ViewModel    |
| hexagonal          | /hekˈsæɡənl/           | 六边形       | Hexagonal architecture  |
| clean-architecture | /kliːn ˈɑːrkɪtektʃər/  | 整洁架构     | Clean architecture      |
| onion-architecture | /ˈʌnjən ˈɑːrkɪtektʃər/ | 洋葱架构     | Onion architecture      |
| CQRS               | /ˌsiː kjuː ɑːr ˈes/    | 命令查询分离 | CQRS pattern            |
| event-sourcing     | /ɪˈvent ˈsɔːrsɪŋ/      | 事件溯源     | Event sourcing          |
| serverless         | /ˈsɜːrvərləs/          | 无服务器     | Serverless architecture |
| FaaS               | /fæs/                  | 函数即服务   | Function as a Service   |
| BaaS               | /bæs/                  | 后端即服务   | Backend as a Service    |
| monolithic         | /ˌmɑːnəˈlɪθɪk/         | 单体         | Monolithic architecture |
| modular            | /ˈmɑːdʒələr/           | 模块化       | Modular monolith        |
| plugin             | /ˈplʌɡɪn/              | 插件         | Plugin architecture     |
| pipe-filter        | /paɪp ˈfɪltər/         | 管道过滤器   | Pipe and filter         |
| blackboard         | /ˈblækbɔːrd/           | 黑板         | Blackboard pattern      |
| broker             | /ˈbroʊkər/             | 代理         | Broker pattern          |
| peer-to-peer       | /pɪr tuː pɪr/          | 对等         | P2P architecture        |
| client-server      | /ˈklaɪənt ˈsɜːrvər/    | 客户端服务器 | Client-server           |
| three-tier         | /θriː tɪr/             | 三层         | Three-tier architecture |
| n-tier             | /en tɪr/               | N层          | N-tier architecture     |
| presentation       | /ˌprezənˈteɪʃn/        | 表示层       | Presentation layer      |
| business           | /ˈbɪznəs/              | 业务层       | Business layer          |
| data-access        | /ˈdeɪtə ˈækses/        | 数据访问层   | Data access layer       |
| domain             | /doʊˈmeɪn/             | 领域层       | Domain layer            |
| infrastructure     | /ˈɪnfrəstrʌktʃər/      | 基础设施层   | Infrastructure layer    |
| anti-corruption    | /ˌænti kəˈrʌpʃn/       | 防腐层       | Anti-corruption layer   |
| adapter            | /əˈdæptər/             | 适配器       | Adapter pattern         |

### 设计原则

| 英文                          | 音标                               | 中文         | 例句                          |
| ----------------------------- | ---------------------------------- | ------------ | ----------------------------- |
| SOLID                         | /ˈsɑːlɪd/                          | SOLID原则    | SOLID principles              |
| SRP                           | /ˌes ɑːr ˈpiː/                     | 单一职责     | Single Responsibility         |
| OCP                           | /ˌoʊ siː ˈpiː/                     | 开闭原则     | Open-Closed Principle         |
| LSP                           | /ˌel es ˈpiː/                      | 里氏替换     | Liskov Substitution           |
| ISP                           | /ˌaɪ es ˈpiː/                      | 接口隔离     | Interface Segregation         |
| DIP                           | /ˌdiː aɪ ˈpiː/                     | 依赖倒置     | Dependency Inversion          |
| DRY                           | /draɪ/                             | 不要重复     | Don't Repeat Yourself         |
| KISS                          | /kɪs/                              | 保持简单     | Keep It Simple Stupid         |
| YAGNI                         | /ˈjæɡni/                           | 不需要就别做 | You Aren't Gonna Need It      |
| separation-of-concerns        | /ˌsepəˈreɪʃn əv kənˈsɜːrnz/        | 关注点分离   | Separation of concerns        |
| loose-coupling                | /luːs ˈkʌplɪŋ/                     | 松耦合       | Loose coupling                |
| high-cohesion                 | /haɪ koʊˈhiːʒn/                    | 高内聚       | High cohesion                 |
| encapsulation                 | /ɪnˌkæpsjuˈleɪʃn/                  | 封装         | Encapsulation                 |
| abstraction                   | /æbˈstrækʃn/                       | 抽象         | Abstraction                   |
| composition-over-inheritance  | /ˌkɑːmpəˈzɪʃn ˈoʊvər ɪnˈherɪtəns/  | 组合优于继承 | Composition over inheritance  |
| program-to-interface          | /ˈproʊɡræm tuː ˈɪntərfeɪs/         | 面向接口编程 | Program to interface          |
| dependency-injection          | /dɪˈpendənsi ɪnˈdʒekʃn/            | 依赖注入     | Dependency injection          |
| inversion-of-control          | /ɪnˈvɜːrʒn əv kənˈtroʊl/           | 控制反转     | Inversion of control          |
| law-of-Demeter                | /lɔː əv dɪˈmiːtər/                 | 迪米特法则   | Law of Demeter                |
| tell-dont-ask                 | /tel doʊnt æsk/                    | 告诉不要问   | Tell, don't ask               |
| fail-fast                     | /feɪl fæst/                        | 快速失败     | Fail fast                     |
| defensive-programming         | /dɪˈfensɪv ˈproʊɡræmɪŋ/            | 防御式编程   | Defensive programming         |
| convention-over-configuration | /kənˈvenʃn ˈoʊvər kənˌfɪɡjəˈreɪʃn/ | 约定优于配置 | Convention over configuration |
| least-privilege               | /liːst ˈprɪvəlɪdʒ/                 | 最小权限     | Principle of least privilege  |
| defense-in-depth              | /dɪˈfens ɪn depθ/                  | 纵深防御     | Defense in depth              |
| single-source-of-truth        | /ˈsɪŋɡl sɔːrs əv truːθ/            | 单一数据源   | Single source of truth        |
| immutability                  | /ɪˌmjuːtəˈbɪləti/                  | 不可变性     | Immutability                  |
| idempotency                   | /ˌaɪdemˈpoʊtənsi/                  | 幂等性       | Idempotency                   |
| statelessness                 | /ˈsteɪtləsnəs/                     | 无状态性     | Statelessness                 |
| scalability                   | /ˌskeɪləˈbɪləti/                   | 可扩展性     | Scalability                   |

### 高可用与扩展

| 英文                 | 音标                     | 中文     | 例句                    |
| -------------------- | ------------------------ | -------- | ----------------------- |
| high-availability    | /haɪ əˌveɪləˈbɪləti/     | 高可用   | High availability       |
| HA                   | /ˌeɪtʃ ˈeɪ/              | 高可用   | HA architecture         |
| redundancy           | /rɪˈdʌndənsi/            | 冗余     | System redundancy       |
| fault-tolerance      | /fɔːlt ˈtɑːlərəns/       | 容错     | Fault tolerance         |
| resilience           | /rɪˈzɪliəns/             | 弹性     | System resilience       |
| disaster-recovery    | /dɪˈzæstər rɪˈkʌvəri/    | 灾难恢复 | Disaster recovery       |
| backup               | /ˈbækʌp/                 | 备份     | Data backup             |
| restore              | /rɪˈstɔːr/               | 恢复     | System restore          |
| replication          | /ˌreplɪˈkeɪʃn/           | 复制     | Data replication        |
| failover             | /ˈfeɪloʊvər/             | 故障转移 | Automatic failover      |
| failback             | /ˈfeɪlbæk/               | 故障恢复 | Failback process        |
| hot-standby          | /hɑːt ˈstændbaɪ/         | 热备份   | Hot standby             |
| cold-standby         | /koʊld ˈstændbaɪ/        | 冷备份   | Cold standby            |
| warm-standby         | /wɔːrm ˈstændbaɪ/        | 温备份   | Warm standby            |
| active-active        | /ˈæktɪv ˈæktɪv/          | 双活     | Active-active           |
| active-passive       | /ˈæktɪv ˈpæsɪv/          | 主备     | Active-passive          |
| multi-region         | /ˈmʌlti ˈriːdʒən/        | 多区域   | Multi-region deployment |
| geo-redundancy       | /ˈdʒiːoʊ rɪˈdʌndənsi/    | 地理冗余 | Geo-redundancy          |
| scalability          | /ˌskeɪləˈbɪləti/         | 可扩展性 | System scalability      |
| horizontal-scaling   | /ˌhɔːrɪˈzɑːntl ˈskeɪlɪŋ/ | 水平扩展 | Scale out               |
| vertical-scaling     | /ˈvɜːrtɪkl ˈskeɪlɪŋ/     | 垂直扩展 | Scale up                |
| elasticity           | /ɪˌlæsˈtɪsəti/           | 弹性     | Cloud elasticity        |
| auto-scaling         | /ˈɔːtoʊ ˈskeɪlɪŋ/        | 自动扩展 | Auto-scaling            |
| scale-out            | /skeɪl aʊt/              | 横向扩展 | Scale-out architecture  |
| scale-up             | /skeɪl ʌp/               | 纵向扩展 | Scale-up resources      |
| bottleneck           | /ˈbɑːtlnek/              | 瓶颈     | Performance bottleneck  |
| capacity-planning    | /kəˈpæsəti ˈplænɪŋ/      | 容量规划 | Capacity planning       |
| load-shedding        | /loʊd ˈʃedɪŋ/            | 负载削减 | Load shedding           |
| graceful-degradation | /ˈɡreɪsfl ˌdeɡrəˈdeɪʃn/  | 优雅降级 | Graceful degradation    |
| circuit-breaker      | /ˈsɜːrkɪt ˈbreɪkər/      | 熔断器   | Circuit breaker         |
| bulkhead             | /ˈbʌlkhed/               | 舱壁     | Bulkhead pattern        |
| throttling           | /ˈθrɑːtlɪŋ/              | 节流     | Request throttling      |
| rate-limiting        | /reɪt ˈlɪmɪtɪŋ/          | 速率限制 | Rate limiting           |
| backpressure         | /ˈbækpreʃər/             | 背压     | Backpressure handling   |
| idempotent           | /aɪˈdempətənt/           | 幂等     | Idempotent operation    |
| retry                | /ˌriːˈtraɪ/              | 重试     | Retry mechanism         |
| timeout              | /ˈtaɪmaʊt/               | 超时     | Timeout configuration   |
| jitter               | /ˈdʒɪtər/                | 抖动     | Retry jitter            |
| exponential-backoff  | /ˌekspəˈnenʃl ˈbækɔːf/   | 指数退避 | Exponential backoff     |
| health-check         | /helθ tʃek/              | 健康检查 | Health check            |

