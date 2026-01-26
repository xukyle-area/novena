# Java生态

### JVM相关

| 英文               | 音标                  | 中文             | 例句                      |
| ------------------ | --------------------- | ---------------- | ------------------------- |
| JVM                | /ˌdʒeɪ viː ˈem/       | Java虚拟机       | Java Virtual Machine      |
| bytecode           | /ˈbaɪtkoʊd/           | 字节码           | Java bytecode             |
| JIT                | /ˌdʒeɪ aɪ ˈtiː/       | 即时编译         | Just-in-time compiler     |
| AOT                | /ˌeɪ oʊ ˈtiː/         | 提前编译         | Ahead-of-time compilation |
| classloader        | /klæs ˈloʊdər/        | 类加载器         | Class loader              |
| bootstrap-loader   | /ˈbuːtstræp ˈloʊdər/  | 引导类加载器     | Bootstrap class loader    |
| extension-loader   | /ɪkˈstenʃn ˈloʊdər/   | 扩展类加载器     | Extension class loader    |
| application-loader | /ˌæplɪˈkeɪʃn ˈloʊdər/ | 应用类加载器     | Application class loader  |
| parent-delegation  | /ˈperənt ˌdelɪˈɡeɪʃn/ | 双亲委派         | Parent delegation model   |
| heap               | /hiːp/                | 堆               | Java heap                 |
| stack              | /stæk/                | 栈               | Thread stack              |
| metaspace          | /ˈmetəspeɪs/          | 元空间           | Metaspace                 |
| PermGen            | /pɜːrm dʒen/          | 永久代           | Permanent generation      |
| young-generation   | /jʌŋ ˌdʒenəˈreɪʃn/    | 年轻代           | Young generation          |
| old-generation     | /oʊld ˌdʒenəˈreɪʃn/   | 老年代           | Old generation            |
| Eden               | /ˈiːdn/               | 伊甸园           | Eden space                |
| Survivor           | /sərˈvaɪvər/          | 幸存者           | Survivor space            |
| garbage-collection | /ˈɡɑːrbɪdʒ kəˈlekʃn/  | 垃圾回收         | Garbage collection        |
| GC                 | /ˌdʒiː ˈsiː/          | 垃圾回收         | GC pause                  |
| minor-GC           | /ˈmaɪnər dʒiː siː/    | 小GC             | Minor GC                  |
| major-GC           | /ˈmeɪdʒər dʒiː siː/   | 大GC             | Major GC                  |
| full-GC            | /fʊl dʒiː siː/        | 完全GC           | Full GC                   |
| STW                | /ˌes tiː ˈdʌbljuː/    | 停顿世界         | Stop-the-world            |
| generational       | /ˌdʒenəˈreɪʃənl/      | 分代             | Generational GC           |
| reachability       | /ˌriːtʃəˈbɪləti/      | 可达性           | Object reachability       |
| root               | /ruːt/                | 根               | GC root                   |
| mark-sweep         | /mɑːrk swiːp/         | 标记清除         | Mark-sweep algorithm      |
| mark-compact       | /mɑːrk ˈkɑːmpækt/     | 标记整理         | Mark-compact              |
| copying            | /ˈkɑːpiɪŋ/            | 复制             | Copying algorithm         |
| reference-counting | /ˈrefrəns ˈkaʊntɪŋ/   | 引用计数         | Reference counting        |
| weak-reference     | /wiːk ˈrefrəns/       | 弱引用           | Weak reference            |
| soft-reference     | /sɔːft ˈrefrəns/      | 软引用           | Soft reference            |
| phantom-reference  | /ˈfæntəm ˈrefrəns/    | 虚引用           | Phantom reference         |
| strong-reference   | /strɔːŋ ˈrefrəns/     | 强引用           | Strong reference          |
| finalization       | /ˌfaɪnəlaɪˈzeɪʃn/     | 终结             | Object finalization       |
| finalize           | /ˈfaɪnəlaɪz/          | 终结方法         | Finalize method           |
| G1                 | /dʒiː wʌn/            | G1收集器         | G1 garbage collector      |
| ZGC                | /ziː dʒiː siː/        | ZGC收集器        | Z garbage collector       |
| Shenandoah         | /ˌʃenənˈdoʊə/         | Shenandoah收集器 | Shenandoah GC             |
| concurrent-mark    | /kənˈkɜːrənt mɑːrk/   | 并发标记         | Concurrent marking        |

### Java工具

| 英文         | 音标                | 中文         | 例句                  |
| ------------ | ------------------- | ------------ | --------------------- |
| Maven        | /ˈmeɪvn/            | Maven        | Maven build tool      |
| Gradle       | /ˈɡreɪdl/           | Gradle       | Gradle build          |
| POM          | /ˌpiː oʊ ˈem/       | 项目对象模型 | POM file              |
| dependency   | /dɪˈpendənsi/       | 依赖         | Project dependency    |
| artifact     | /ˈɑːrtɪfækt/        | 构件         | Maven artifact        |
| repository   | /rɪˈpɑːzətɔːri/     | 仓库         | Maven repository      |
| central      | /ˈsentrəl/          | 中央仓库     | Maven Central         |
| scope        | /skoʊp/             | 作用域       | Dependency scope      |
| compile      | /kəmˈpaɪl/          | 编译         | Compile scope         |
| runtime      | /ˈrʌntaɪm/          | 运行时       | Runtime scope         |
| provided     | /prəˈvaɪdɪd/        | 已提供       | Provided scope        |
| test         | /test/              | 测试         | Test scope            |
| transitive   | /ˈtrænsətɪv/        | 传递         | Transitive dependency |
| exclusion    | /ɪkˈskluːʒn/        | 排除         | Dependency exclusion  |
| plugin       | /ˈplʌɡɪn/           | 插件         | Maven plugin          |
| goal         | /ɡoʊl/              | 目标         | Plugin goal           |
| phase        | /feɪz/              | 阶段         | Build phase           |
| lifecycle    | /ˈlaɪfsaɪkl/        | 生命周期     | Build lifecycle       |
| clean        | /kliːn/             | 清理         | Clean phase           |
| validate     | /ˈvælɪdeɪt/         | 验证         | Validate phase        |
| package      | /ˈpækɪdʒ/           | 打包         | Package phase         |
| install      | /ɪnˈstɔːl/          | 安装         | Install phase         |
| deploy       | /dɪˈplɔɪ/           | 部署         | Deploy phase          |
| JAR          | /dʒɑːr/             | JAR包        | JAR file              |
| WAR          | /wɔːr/              | WAR包        | WAR file              |
| EAR          | /ɪr/                | EAR包        | EAR file              |
| classpath    | /ˈklæspæθ/          | 类路径       | Java classpath        |
| manifest     | /ˈmænɪfest/         | 清单         | JAR manifest          |
| shade        | /ʃeɪd/              | 遮蔽         | Shade plugin          |
| assembly     | /əˈsembli/          | 组装         | Assembly plugin       |
| profile      | /ˈproʊfaɪl/         | 配置文件     | Maven profile         |
| property     | /ˈprɑːpərti/        | 属性         | Maven property        |
| variable     | /ˈveriəbl/          | 变量         | Environment variable  |
| multi-module | /ˈmʌlti ˈmɑːdʒuːl/  | 多模块       | Multi-module project  |
| parent-POM   | /ˈperənt piː oʊ em/ | 父POM        | Parent POM            |
| aggregation  | /ˌæɡrɪˈɡeɪʃn/       | 聚合         | Module aggregation    |
| inheritance  | /ɪnˈherɪtəns/       | 继承         | POM inheritance       |
| snapshot     | /ˈsnæpʃɑːt/         | 快照         | Snapshot version      |
| release      | /rɪˈliːs/           | 发布         | Release version       |
| version      | /ˈvɜːrʒn/           | 版本         | Artifact version      |

### Java框架

| 英文          | 音标                 | 中文               | 例句                  |
| ------------- | -------------------- | ------------------ | --------------------- |
| Hibernate     | /ˈhaɪbərneɪt/        | Hibernate          | Hibernate ORM         |
| MyBatis       | /maɪ ˈbeɪtɪs/        | MyBatis            | MyBatis framework     |
| ORM           | /ˌoʊ ɑːr ˈem/        | 对象关系映射       | ORM framework         |
| entity        | /ˈentəti/            | 实体               | JPA entity            |
| persistence   | /pərˈsɪstəns/        | 持久化             | Data persistence      |
| JPA           | /ˌdʒeɪ piː ˈeɪ/      | Java持久化API      | JPA specification     |
| session       | /ˈseʃn/              | 会话               | Hibernate session     |
| transaction   | /trænˈzækʃn/         | 事务               | Database transaction  |
| mapping       | /ˈmæpɪŋ/             | 映射               | Object mapping        |
| annotation    | /ˌænəˈteɪʃn/         | 注解               | JPA annotation        |
| XML           | /ˌeks em ˈel/        | XML                | XML configuration     |
| lazy-loading  | /ˈleɪzi ˈloʊdɪŋ/     | 懒加载             | Lazy loading          |
| eager-loading | /ˈiːɡər ˈloʊdɪŋ/     | 饿加载             | Eager loading         |
| cascade       | /kæsˈkeɪd/           | 级联               | Cascade operation     |
| fetch         | /fetʃ/               | 抓取               | Fetch strategy        |
| join          | /dʒɔɪn/              | 连接               | Join fetch            |
| criteria      | /kraɪˈtɪriə/         | 条件               | Criteria query        |
| HQL           | /ˌeɪtʃ kjuː ˈel/     | Hibernate查询语言  | HQL query             |
| JPQL          | /ˌdʒeɪ piː kjuː ˈel/ | Java持久化查询语言 | JPQL                  |
| native-query  | /ˈneɪtɪv ˈkwɪri/     | 原生查询           | Native SQL query      |
| named-query   | /neɪmd ˈkwɪri/       | 命名查询           | Named query           |
| projection    | /prəˈdʒekʃn/         | 投影               | Query projection      |
| cache         | /kæʃ/                | 缓存               | Second-level cache    |
| first-level   | /fɜːrst ˈlevl/       | 一级               | First-level cache     |
| second-level  | /ˈsekənd ˈlevl/      | 二级               | Second-level cache    |
| query-cache   | /ˈkwɪri kæʃ/         | 查询缓存           | Query cache           |
| dirty-check   | /ˈdɜːrti tʃek/       | 脏检查             | Dirty checking        |
| flush         | /flʌʃ/               | 刷新               | Flush session         |
| detached      | /dɪˈtætʃt/           | 分离               | Detached entity       |
| merge         | /mɜːrdʒ/             | 合并               | Merge entity          |
| persist       | /pərˈsɪst/           | 持久化             | Persist entity        |
| remove        | /rɪˈmuːv/            | 移除               | Remove entity         |
| find          | /faɪnd/              | 查找               | Find entity           |
| refresh       | /rɪˈfreʃ/            | 刷新               | Refresh entity        |
| lock          | /lɑːk/               | 锁                 | Pessimistic lock      |
| versioning    | /ˈvɜːrʒnɪŋ/          | 版本控制           | Optimistic locking    |
| interceptor   | /ˌɪntərˈseptər/      | 拦截器             | Hibernate interceptor |
| listener      | /ˈlɪsənər/           | 监听器             | Entity listener       |
| validator     | /ˈvælɪdeɪtər/        | 验证器             | Bean validator        |
| constraint    | /kənˈstreɪnt/        | 约束               | Validation constraint |

