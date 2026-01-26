# 并发与多线程

### 线程基础

| 英文               | 音标                     | 中文         | 例句                      |
| ------------------ | ------------------------ | ------------ | ------------------------- |
| thread             | /θred/                   | 线程         | Worker thread             |
| process            | /ˈprɑːses/               | 进程         | Operating system process  |
| concurrency        | /kənˈkɜːrənsi/           | 并发         | Concurrent execution      |
| parallelism        | /ˈpærəlelɪzəm/           | 并行         | True parallelism          |
| multithreading     | /ˌmʌltiˈθredɪŋ/          | 多线程       | Multithreaded application |
| multiprocessing    | /ˌmʌltiˈprɑːsesɪŋ/       | 多进程       | Multiprocessing           |
| context-switch     | /ˈkɑːntekst swɪtʃ/       | 上下文切换   | Context switching         |
| thread-pool        | /θred puːl/              | 线程池       | Thread pool executor      |
| worker             | /ˈwɜːrkər/               | 工作线程     | Worker thread             |
| daemon             | /ˈdiːmən/                | 守护线程     | Daemon thread             |
| runnable           | /ˈrʌnəbl/                | 可运行       | Runnable interface        |
| callable           | /ˈkɔːləbl/               | 可调用       | Callable task             |
| future             | /ˈfjuːtʃər/              | Future       | Future result             |
| completable-future | /kəmˈpliːtəbl ˈfjuːtʃər/ | 可完成Future | CompletableFuture         |
| executor           | /ɪɡˈzekjətər/            | 执行器       | Executor service          |
| fork-join          | /fɔːrk dʒɔɪn/            | 分叉合并     | Fork-join pool            |
| work-stealing      | /wɜːrk ˈstiːlɪŋ/         | 工作窃取     | Work-stealing algorithm   |
| lifecycle          | /ˈlaɪfsaɪkl/             | 生命周期     | Thread lifecycle          |
| NEW                | /nuː/                    | 新建         | NEW state                 |
| RUNNABLE           | /ˈrʌnəbl/                | 可运行       | RUNNABLE state            |
| BLOCKED            | /blɑːkt/                 | 阻塞         | BLOCKED state             |
| WAITING            | /ˈweɪtɪŋ/                | 等待         | WAITING state             |
| TIMED_WAITING      | /taɪmd ˈweɪtɪŋ/          | 超时等待     | TIMED_WAITING state       |
| TERMINATED         | /ˈtɜːrmɪneɪtɪd/          | 终止         | TERMINATED state          |
| start              | /stɑːrt/                 | 启动         | Start thread              |
| run                | /rʌn/                    | 运行         | Run method                |
| join               | /dʒɔɪn/                  | 加入         | Join thread               |
| sleep              | /sliːp/                  | 睡眠         | Thread sleep              |
| yield              | /jiːld/                  | 让步         | Thread yield              |
| interrupt          | /ˌɪntəˈrʌpt/             | 中断         | Interrupt thread          |
| interrupted        | /ˌɪntəˈrʌptɪd/           | 中断状态     | Interrupted flag          |
| priority           | /praɪˈɔːrəti/            | 优先级       | Thread priority           |
| scheduling         | /ˈskedʒuːlɪŋ/            | 调度         | Thread scheduling         |
| preemptive         | /priˈemptɪv/             | 抢占式       | Preemptive scheduling     |
| cooperative        | /koʊˈɑːpərətɪv/          | 协作式       | Cooperative scheduling    |
| time-slice         | /taɪm slaɪs/             | 时间片       | CPU time slice            |
| CPU-bound          | /ˌsiː piː ˈjuː baʊnd/    | CPU密集      | CPU-bound task            |
| I/O-bound          | /ˌaɪ oʊ baʊnd/           | I/O密集      | I/O-bound task            |
| thread-local       | /θred ˈloʊkl/            | 线程本地     | ThreadLocal variable      |
| inheritable        | /ɪnˈherɪtəbl/            | 可继承       | InheritableThreadLocal    |

### 同步机制

| 英文              | 音标                  | 中文     | 例句                   |
| ----------------- | --------------------- | -------- | ---------------------- |
| synchronization   | /ˌsɪŋkrənaɪˈzeɪʃn/    | 同步     | Thread synchronization |
| synchronized      | /ˈsɪŋkrənaɪzd/        | 同步的   | Synchronized method    |
| lock              | /lɑːk/                | 锁       | Lock object            |
| unlock            | /ʌnˈlɑːk/             | 解锁     | Unlock operation       |
| mutex             | /ˈmjuːteks/           | 互斥锁   | Mutex lock             |
| monitor           | /ˈmɑːnɪtər/           | 监视器   | Object monitor         |
| intrinsic-lock    | /ɪnˈtrɪnsɪk lɑːk/     | 内置锁   | Intrinsic lock         |
| reentrant         | /riːˈentrənt/         | 可重入   | Reentrant lock         |
| non-reentrant     | /nɑːn riːˈentrənt/    | 不可重入 | Non-reentrant lock     |
| fair-lock         | /fer lɑːk/            | 公平锁   | Fair lock              |
| unfair-lock       | /ʌnˈfer lɑːk/         | 非公平锁 | Unfair lock            |
| exclusive-lock    | /ɪkˈskluːsɪv lɑːk/    | 独占锁   | Exclusive lock         |
| shared-lock       | /ʃerd lɑːk/           | 共享锁   | Shared lock            |
| read-lock         | /riːd lɑːk/           | 读锁     | Read lock              |
| write-lock        | /raɪt lɑːk/           | 写锁     | Write lock             |
| read-write-lock   | /riːd raɪt lɑːk/      | 读写锁   | ReadWriteLock          |
| optimistic-lock   | /ˌɑːptɪˈmɪstɪk lɑːk/  | 乐观锁   | Optimistic locking     |
| pessimistic-lock  | /ˌpesɪˈmɪstɪk lɑːk/   | 悲观锁   | Pessimistic locking    |
| spinlock          | /ˈspɪnlɑːk/           | 自旋锁   | Spin lock              |
| tryLock           | /traɪ lɑːk/           | 尝试锁   | Try lock operation     |
| lockInterruptibly | /lɑːk ˌɪntəˈrʌptəbli/ | 可中断锁 | Interruptible lock     |
| condition         | /kənˈdɪʃn/            | 条件     | Condition variable     |
| wait              | /weɪt/                | 等待     | Wait method            |
| notify            | /ˈnoʊtɪfaɪ/           | 通知     | Notify method          |
| notifyAll         | /ˈnoʊtɪfaɪ ɔːl/       | 通知全部 | NotifyAll method       |
| await             | /əˈweɪt/              | 等待     | Await condition        |
| signal            | /ˈsɪɡnl/              | 信号     | Signal method          |
| signalAll         | /ˈsɪɡnl ɔːl/          | 信号全部 | SignalAll method       |
| semaphore         | /ˈseməfɔːr/           | 信号量   | Semaphore              |
| permit            | /pərˈmɪt/             | 许可     | Semaphore permit       |
| acquire           | /əˈkwaɪər/            | 获取     | Acquire lock           |
| release           | /rɪˈliːs/             | 释放     | Release lock           |
| barrier           | /ˈbæriər/             | 屏障     | CyclicBarrier          |
| latch             | /lætʃ/                | 闩锁     | CountDownLatch         |
| countdown         | /ˈkaʊntdaʊn/          | 倒计数   | Count down             |
| phaser            | /ˈfeɪzər/             | 阶段器   | Phaser                 |
| exchanger         | /ɪksˈtʃeɪndʒər/       | 交换器   | Exchanger              |
| LockSupport       | /lɑːk səˈpɔːrt/       | 锁支持   | LockSupport class      |
| park              | /pɑːrk/               | 停靠     | Park thread            |
| unpark            | /ʌnˈpɑːrk/            | 唤醒     | Unpark thread          |

### 并发问题

| 英文                   | 音标                     | 中文       | 例句                        |
| ---------------------- | ------------------------ | ---------- | --------------------------- |
| race-condition         | /reɪs kənˈdɪʃn/          | 竞态条件   | Race condition bug          |
| data-race              | /ˈdeɪtə reɪs/            | 数据竞争   | Data race                   |
| deadlock               | /ˈdedlɑːk/               | 死锁       | Deadlock situation          |
| livelock               | /ˈlaɪvlɑːk/              | 活锁       | Livelock problem            |
| starvation             | /stɑːrˈveɪʃn/            | 饥饿       | Thread starvation           |
| priority-inversion     | /praɪˈɔːrəti ɪnˈvɜːrʒn/  | 优先级反转 | Priority inversion          |
| contention             | /kənˈtenʃn/              | 争用       | Lock contention             |
| mutual-exclusion       | /ˈmjuːtʃuəl ɪkˈskluːʒn/  | 互斥       | Mutual exclusion            |
| critical-section       | /ˈkrɪtɪkl ˈsekʃn/        | 临界区     | Critical section            |
| atomic-operation       | /əˈtɑːmɪk ˌɑːpəˈreɪʃn/   | 原子操作   | Atomic operation            |
| atomicity              | /ˌætəˈmɪsəti/            | 原子性     | Operation atomicity         |
| visibility             | /ˌvɪzəˈbɪləti/           | 可见性     | Memory visibility           |
| ordering               | /ˈɔːrdərɪŋ/              | 顺序性     | Operation ordering          |
| reordering             | /riːˈɔːrdərɪŋ/           | 重排序     | Instruction reordering      |
| happens-before         | /ˈhæpənz bɪˈfɔːr/        | 先行发生   | Happens-before relationship |
| memory-barrier         | /ˈmeməri ˈbæriər/        | 内存屏障   | Memory barrier              |
| fence                  | /fens/                   | 栅栏       | Memory fence                |
| volatile               | /ˈvɑːlətl/               | 易失的     | Volatile keyword            |
| volatile-read          | /ˈvɑːlətl riːd/          | 易失读     | Volatile read               |
| volatile-write         | /ˈvɑːlətl raɪt/          | 易失写     | Volatile write              |
| final-field            | /ˈfaɪnl fiːld/           | Final字段  | Final field semantics       |
| safe-publication       | /seɪf ˌpʌblɪˈkeɪʃn/      | 安全发布   | Safe publication            |
| immutability           | /ɪˌmjuːtəˈbɪləti/        | 不可变性   | Object immutability         |
| thread-safe            | /θred seɪf/              | 线程安全   | Thread-safe class           |
| thread-unsafe          | /θred ʌnˈseɪf/           | 线程不安全 | Thread-unsafe code          |
| lock-free              | /lɑːk friː/              | 无锁       | Lock-free algorithm         |
| wait-free              | /weɪt friː/              | 无等待     | Wait-free algorithm         |
| CAS                    | /ˌsiː eɪ ˈes/            | 比较交换   | Compare-and-swap            |
| ABA-problem            | /ˌeɪ biː ˈeɪ ˈprɑːbləm/  | ABA问题    | ABA problem                 |
| atomic-variable        | /əˈtɑːmɪk ˈveriəbl/      | 原子变量   | AtomicInteger               |
| atomic-reference       | /əˈtɑːmɪk ˈrefrəns/      | 原子引用   | AtomicReference             |
| atomic-array           | /əˈtɑːmɪk əˈreɪ/         | 原子数组   | AtomicIntegerArray          |
| field-updater          | /fiːld ʌpˈdeɪtər/        | 字段更新器 | AtomicFieldUpdater          |
| lazy-initialization    | /ˈleɪzi ɪˌnɪʃəlaɪˈzeɪʃn/ | 懒初始化   | Lazy initialization         |
| double-checked-locking | /ˈdʌbl tʃekt ˈlɑːkɪŋ/    | 双重检查锁 | Double-checked locking      |
| singleton              | /ˈsɪŋɡltən/              | 单例       | Singleton pattern           |
| thread-confinement     | /θred kənˈfaɪnmənt/      | 线程限制   | Thread confinement          |
| stack-confinement      | /stæk kənˈfaɪnmənt/      | 栈限制     | Stack confinement           |
| thread-safety          | /θred ˈseɪfti/           | 线程安全性 | Thread safety               |
| composability          | /kəmˌpoʊzəˈbɪləti/       | 可组合性   | Composability               |

