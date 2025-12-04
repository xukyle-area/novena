# 消息队列

### 消息队列核心

| 英文           | 音标              | 中文     | 例句                    |
| -------------- | ----------------- | -------- | ----------------------- |
| message-queue  | /ˈmesɪdʒ kjuː/    | 消息队列 | Message queue system    |
| producer       | /prəˈduːsər/      | 生产者   | Message producer        |
| consumer       | /kənˈsuːmər/      | 消费者   | Message consumer        |
| broker         | /ˈbroʊkər/        | 代理     | Message broker          |
| topic          | /ˈtɑːpɪk/         | 主题     | Kafka topic             |
| partition      | /pɑːrˈtɪʃn/       | 分区     | Topic partition         |
| queue          | /kjuː/            | 队列     | Message queue           |
| exchange       | /ɪksˈtʃeɪndʒ/     | 交换机   | RabbitMQ exchange       |
| routing-key    | /ˈruːtɪŋ kiː/     | 路由键   | Message routing key     |
| binding        | /ˈbaɪndɪŋ/        | 绑定     | Queue binding           |
| publish        | /ˈpʌblɪʃ/         | 发布     | Publish message         |
| subscribe      | /səbˈskraɪb/      | 订阅     | Subscribe to topic      |
| push           | /pʊʃ/             | 推送     | Push model              |
| pull           | /pʊl/             | 拉取     | Pull model              |
| offset         | /ˈɔːfset/         | 偏移量   | Message offset          |
| commit         | /kəˈmɪt/          | 提交     | Commit offset           |
| auto-commit    | /ˈɔːtoʊ kəˈmɪt/   | 自动提交 | Auto-commit offset      |
| manual-commit  | /ˈmænjuəl kəˈmɪt/ | 手动提交 | Manual commit           |
| acknowledgment | /əkˈnɑːlɪdʒmənt/  | 确认     | Message ack             |
| positive-ack   | /ˈpɑːzətɪv æk/    | 正向确认 | Positive acknowledgment |
| negative-ack   | /ˈneɡətɪv æk/     | 负向确认 | Negative acknowledgment |
| requeue        | /riːˈkjuː/        | 重新入队 | Requeue message         |
| dead-letter    | /ded ˈletər/      | 死信     | Dead letter exchange    |
| retry          | /ˌriːˈtraɪ/       | 重试     | Message retry           |
| backoff        | /ˈbækɔːf/         | 退避     | Retry backoff           |
| poison-message | /ˈpɔɪzn ˈmesɪdʒ/  | 毒药消息 | Poison message          |
| at-most-once   | /ət moʊst wʌns/   | 至多一次 | At-most-once delivery   |
| at-least-once  | /ət liːst wʌns/   | 至少一次 | At-least-once delivery  |
| exactly-once   | /ɪɡˈzæktli wʌns/  | 恰好一次 | Exactly-once semantics  |
| idempotent     | /aɪˈdempətənt/    | 幂等     | Idempotent consumer     |
| ordering       | /ˈɔːrdərɪŋ/       | 顺序     | Message ordering        |
| FIFO           | /ˈfaɪfoʊ/         | 先进先出 | FIFO queue              |
| priority       | /praɪˈɔːrəti/     | 优先级   | Priority queue          |
| delay          | /dɪˈleɪ/          | 延迟     | Delayed message         |
| scheduled      | /ˈskedʒuːld/      | 定时     | Scheduled message       |
| batch          | /bætʃ/            | 批处理   | Batch processing        |
| streaming      | /ˈstriːmɪŋ/       | 流式     | Stream processing       |
| compaction     | /kəmˈpækʃn/       | 压缩     | Log compaction          |
| retention      | /rɪˈtenʃn/        | 保留     | Message retention       |
| expiration     | /ˌekspəˈreɪʃn/    | 过期     | Message expiration      |

### Kafka特有

| 英文               | 音标                   | 中文        | 例句                   |
| ------------------ | ---------------------- | ----------- | ---------------------- |
| Kafka              | /ˈkæfkə/               | Kafka       | Apache Kafka           |
| cluster            | /ˈklʌstər/             | 集群        | Kafka cluster          |
| Zookeeper          | /ˈzuːkiːpər/           | Zookeeper   | Zookeeper coordination |
| leader             | /ˈliːdər/              | 领导者      | Partition leader       |
| follower           | /ˈfɑːloʊər/            | 跟随者      | Partition follower     |
| replica            | /ˈreplɪkə/             | 副本        | Partition replica      |
| ISR                | /ˌaɪ es ˈɑːr/          | 同步副本集  | In-sync replica        |
| replication-factor | /ˌreplɪˈkeɪʃn ˈfæktər/ | 复制因子    | Replication factor     |
| log-segment        | /lɔːɡ ˈseɡmənt/        | 日志段      | Log segment file       |
| consumer-group     | /kənˈsuːmər ɡruːp/     | 消费者组    | Consumer group         |
| rebalance          | /ˌriːˈbæləns/          | 重平衡      | Consumer rebalance     |
| coordinator        | /koʊˈɔːrdɪneɪtər/      | 协调器      | Group coordinator      |
| partition-key      | /pɑːrˈtɪʃn kiː/        | 分区键      | Partition key          |
| Kafka-Connect      | /ˈkæfkə kəˈnekt/       | Kafka连接器 | Kafka Connect          |
| Kafka-Streams      | /ˈkæfkə striːmz/       | Kafka流     | Kafka Streams API      |
| KTable             | /keɪ ˈteɪbl/           | KTable      | KTable abstraction     |
| KStream            | /keɪ striːm/           | KStream     | KStream abstraction    |
| changelog          | /ˈtʃeɪndʒlɔːɡ/         | 变更日志    | Changelog topic        |
| state-store        | /steɪt stɔːr/          | 状态存储    | State store            |
| windowing          | /ˈwɪndoʊɪŋ/            | 窗口化      | Stream windowing       |

### RabbitMQ特有

| 英文               | 音标                     | 中文             | 例句                |
| ------------------ | ------------------------ | ---------------- | ------------------- |
| RabbitMQ           | /ˈræbɪt em kjuː/         | RabbitMQ         | RabbitMQ broker     |
| AMQP               | /ˌeɪ em kjuː ˈpiː/       | 高级消息队列协议 | AMQP protocol       |
| vhost              | /viː hoʊst/              | 虚拟主机         | Virtual host        |
| direct-exchange    | /dəˈrekt ɪksˈtʃeɪndʒ/    | 直连交换机       | Direct exchange     |
| fanout-exchange    | /ˈfænaʊt ɪksˈtʃeɪndʒ/    | 扇出交换机       | Fanout exchange     |
| topic-exchange     | /ˈtɑːpɪk ɪksˈtʃeɪndʒ/    | 主题交换机       | Topic exchange      |
| headers-exchange   | /ˈhedərz ɪksˈtʃeɪndʒ/    | 头部交换机       | Headers exchange    |
| durable            | /ˈdʊrəbl/                | 持久化           | Durable queue       |
| transient          | /ˈtrænziənt/             | 非持久           | Transient message   |
| exclusive          | /ɪkˈskluːsɪv/            | 独占             | Exclusive queue     |
| auto-delete        | /ˈɔːtoʊ dɪˈliːt/         | 自动删除         | Auto-delete queue   |
| TTL                | /ˌtiː tiː ˈel/           | 生存时间         | Message TTL         |
| prefetch           | /ˈpriːfetʃ/              | 预取             | Prefetch count      |
| QoS                | /ˌkjuː oʊ ˈes/           | 服务质量         | Quality of Service  |
| publisher-confirm  | /ˈpʌblɪʃər kənˈfɜːrm/    | 发布者确认       | Publisher confirms  |
| mandatory          | /ˈmændətɔːri/            | 强制             | Mandatory flag      |
| immediate          | /ɪˈmiːdiət/              | 立即             | Immediate flag      |
| alternate-exchange | /ˈɔːltərnət ɪksˈtʃeɪndʒ/ | 备用交换机       | Alternate exchange  |
| shovel             | /ˈʃʌvl/                  | 铲子插件         | Shovel plugin       |
| federation         | /ˌfedəˈreɪʃn/            | 联邦             | RabbitMQ federation |