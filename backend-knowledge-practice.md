# Java & Backend Knowledge Practice Guide

## 目标
在练习英语的同时，系统复习Java和后端核心知识点，能够用英文清晰解释技术概念。

---

## 练习方法：用英文解释技术概念

### 核心原则
❌ **不要只背定义**  
✅ **要能像给同事讲解一样，用自己的话说出来**

### 每天练习流程（20-30分钟）

#### 1. 选择2-3个知识点（5分钟）
从下面的列表中选择，或结合当天的词汇主题

#### 2. 用英文解释（15分钟）
对每个知识点，大声说出：
- **What it is**: 这是什么（定义）
- **Why we use it**: 为什么用它（目的/好处）
- **When to use it**: 什么时候用（场景）
- **How it works**: 怎么工作的（原理）
- **Example from my project**: 我项目中的例子

#### 3. 录音或写下来（5-10分钟）
用手机录音或写在 `daily-practice-log.md` 中

---

## Java 核心知识点清单

### Week 1: Java 基础 (配合词汇 Days 1-7)

#### Day 1-2: OOP 核心概念
- [ ] **Encapsulation** - 封装
  - "Encapsulation means bundling data and methods together..."
  - "In my project, I encapsulated user authentication logic in a UserService class..."

- [ ] **Inheritance** - 继承
  - "Inheritance allows a class to inherit properties from a parent class..."
  - "We used inheritance for different types of payment processors..."

- [ ] **Polymorphism** - 多态
  - "Polymorphism enables objects to take multiple forms..."
  - "I implemented polymorphism using interfaces for notification handlers..."

- [ ] **Abstraction** - 抽象
  - "Abstraction hides complex implementation details..."

#### Day 3-4: Java 集合框架
- [ ] **HashMap vs ConcurrentHashMap**
  - "HashMap is not thread-safe, while ConcurrentHashMap..."
  - "In our multi-threaded environment, we chose ConcurrentHashMap because..."

- [ ] **ArrayList vs LinkedList**
  - "ArrayList uses a dynamic array internally..."
  - "We use ArrayList when we need fast random access..."

- [ ] **HashSet vs TreeSet**

#### Day 5-6: 并发基础
- [ ] **Thread vs Runnable**
  - "There are two ways to create threads in Java..."

- [ ] **synchronized keyword**
  - "The synchronized keyword ensures thread safety by..."
  - "I used synchronized blocks to protect shared resources..."

- [ ] **volatile keyword**
  - "Volatile ensures visibility across threads..."

#### Day 7: JVM 基础
- [ ] **Heap vs Stack memory**
  - "The heap stores objects, while the stack stores method calls and local variables..."

- [ ] **Garbage Collection basics**
  - "Garbage collection automatically frees up memory..."
  - "We tuned GC parameters to reduce pause times..."

---

### Week 2: Spring & 数据库 (配合词汇 Days 8-14)

#### Day 8-9: Spring Core
- [ ] **Dependency Injection**
  - "DI is a design pattern where objects receive their dependencies from external sources..."
  - "Spring uses DI to manage beans and reduce coupling..."

- [ ] **IoC Container**
  - "The IoC container manages the lifecycle of beans..."

- [ ] **Bean Scopes** (singleton, prototype, request, session)

- [ ] **@Autowired vs @Resource vs @Inject**

#### Day 10-11: Spring Boot & Web
- [ ] **@RestController vs @Controller**
  - "RestController is used for RESTful APIs..."
  - "In my microservices, all endpoints use RestController..."

- [ ] **@RequestMapping, @GetMapping, @PostMapping**

- [ ] **Spring Boot Auto-configuration**
  - "Auto-configuration automatically configures Spring application based on dependencies..."

- [ ] **Application.properties vs Application.yml**

#### Day 12-13: 数据库 & ORM
- [ ] **JPA vs Hibernate**
  - "JPA is a specification, Hibernate is an implementation..."

- [ ] **@Entity, @Table, @Column annotations**

- [ ] **Lazy Loading vs Eager Loading**
  - "Lazy loading fetches related entities only when accessed..."
  - "We use lazy loading to avoid the N+1 query problem..."

- [ ] **Transaction Management (@Transactional)**
  - "The @Transactional annotation ensures database operations are atomic..."

- [ ] **ACID properties**
  - "ACID stands for Atomicity, Consistency, Isolation, Durability..."

#### Day 14: SQL 优化
- [ ] **Index types** (B-tree, Hash, Full-text)
  - "B-tree indexes are best for range queries..."
  - "We added an index on user_id column to speed up lookups..."

- [ ] **Query optimization techniques**
  - "To optimize slow queries, I first used EXPLAIN to analyze the execution plan..."

- [ ] **N+1 query problem**

---

### Week 3: 系统设计 & 高级主题 (配合词汇 Days 15-20)

#### Day 15-16: 缓存 & 消息队列
- [ ] **Cache strategies** (Cache-aside, Write-through, Write-behind)
  - "We use cache-aside pattern where the application checks cache first..."

- [ ] **Redis data structures**
  - "Redis supports strings, lists, sets, sorted sets, and hashes..."
  - "I used Redis sorted sets to implement a leaderboard..."

- [ ] **Cache invalidation strategies**
  - "There are only two hard things in computer science: cache invalidation and naming things..."

- [ ] **Message Queue use cases**
  - "We use Kafka for asynchronous processing and event streaming..."
  - "Message queues help decouple services and improve scalability..."

#### Day 17-18: 微服务 & 分布式
- [ ] **Microservices vs Monolith**
  - "Microservices architecture breaks down applications into small, independent services..."
  - "Each service can be deployed independently..."

- [ ] **Service Discovery** (Eureka, Consul)
  - "Service discovery allows services to find each other dynamically..."

- [ ] **API Gateway pattern**
  - "API Gateway acts as a single entry point for all client requests..."

- [ ] **Circuit Breaker pattern** (Hystrix, Resilience4j)
  - "Circuit breaker prevents cascading failures..."

- [ ] **Distributed Transaction** (2PC, Saga)
  - "In distributed systems, we can't use traditional ACID transactions..."

#### Day 19-20: 性能 & 安全
- [ ] **Load Balancing algorithms**
  - "Round-robin distributes requests evenly across servers..."
  - "We use Nginx as a load balancer..."

- [ ] **Horizontal vs Vertical Scaling**
  - "Horizontal scaling adds more machines, vertical scaling upgrades existing ones..."

- [ ] **JWT authentication**
  - "JWT is a stateless authentication mechanism..."
  - "The token contains user claims and is signed with a secret..."

- [ ] **SQL Injection prevention**
  - "Always use prepared statements to prevent SQL injection..."

- [ ] **Rate Limiting**
  - "Rate limiting protects APIs from abuse by limiting request frequency..."

---

## Backend 系统设计常见主题

### 每周练习一个完整的系统设计（Week 2-3）

#### Week 2: 设计一个 URL Shortener
**用英文说出来：**
1. **Requirements**
   - "We need to generate short URLs that redirect to original URLs..."
   - "The system should handle 1000 writes per second..."

2. **API Design**
   - "POST /api/shorten - creates a short URL"
   - "GET /{shortUrl} - redirects to original URL"

3. **Database Schema**
   - "We need a table with columns: id, short_url, original_url, created_at..."

4. **Key Generation Strategy**
   - "We can use base62 encoding to generate short URLs..."

5. **Scalability**
   - "We can use Redis for caching frequently accessed URLs..."
   - "Partition the database by hash of short_url..."

#### Week 3: 设计一个 Rate Limiter
**练习点：**
- Token Bucket vs Sliding Window
- Distributed rate limiting with Redis
- Handling edge cases

---

## 实战练习题库

### 每周做3-5道，用英文回答

#### 基础题（Week 1）
1. "What's the difference between == and equals() in Java?"
2. "Explain how HashMap works internally"
3. "What is the difference between List and Set?"
4. "What are the differences between String, StringBuilder, and StringBuffer?"
5. "Explain the concept of immutability in Java"

#### 中级题（Week 2）
1. "How does Spring Boot's auto-configuration work?"
2. "Explain the @Transactional annotation and its propagation levels"
3. "What's the difference between @Component, @Service, and @Repository?"
4. "How do you handle database connection pooling?"
5. "What are the differences between SQL and NoSQL databases?"

#### 高级题（Week 3）
1. "How would you design a distributed lock?"
2. "Explain the CAP theorem"
3. "How do you ensure data consistency in microservices?"
4. "What's your approach to monitoring and alerting in production?"
5. "How do you handle database migration in a zero-downtime deployment?"

---

## 练习模板（复制到 daily-practice-log.md）

### Day X - [Knowledge Topic]

#### 今天练习的知识点
1. [知识点名称]

#### 我的英文解释（大声说出来）

**What it is:**


**Why we use it:**


**When to use it:**


**How it works:**


**Example from my project:**


#### 遇到的表达困难


#### 改进方向


---

## 推荐的学习资源

### 面试准备
- LeetCode: 用英文写comments解释solution
- System Design Primer (GitHub)
- Grokking the System Design Interview

### 技术博客（英文阅读练习）
- Martin Fowler's Blog
- Baeldung (Java & Spring)
- Netflix Tech Blog
- High Scalability

---

## 检查清单

### Week 1 结束时，你应该能够：
- [ ] 用英文解释Java OOP核心概念
- [ ] 说出HashMap和ConcurrentHashMap的区别
- [ ] 解释Java线程基础
- [ ] 描述JVM内存模型

### Week 2 结束时，你应该能够：
- [ ] 解释Spring依赖注入
- [ ] 说明Spring Boot注解的用途
- [ ] 讨论数据库事务管理
- [ ] 描述缓存策略

### Week 3 结束时，你应该能够：
- [ ] 设计一个简单的分布式系统
- [ ] 讨论微服务架构
- [ ] 解释常见的设计模式
- [ ] 回答性能优化问题

---

## 与词汇学习的结合

| 词汇文件                     | 对应技术知识点    | 练习重点               |
| ---------------------------- | ----------------- | ---------------------- |
| Day 1-2: Basic + Programming | Java OOP          | 用专业术语描述面向对象 |
| Day 3: Data Structures       | 集合框架          | 解释数据结构的选择     |
| Day 4: OS & Network          | 线程、网络协议    | 描述并发和网络问题     |
| Day 5: Database              | SQL、事务         | 讨论数据库设计         |
| Day 6: Distributed Systems   | 分布式概念        | 解释CAP、一致性        |
| Day 7: Microservices         | Spring Boot微服务 | 描述微服务架构         |
| Day 8: Message Queue         | Kafka使用         | 说明异步处理           |
| Day 9: Caching               | Redis策略         | 讨论缓存方案           |
| Day 10: Concurrency          | Java并发工具      | 解释线程安全           |
| Day 11: Java Ecosystem       | Maven、工具链     | 描述开发流程           |
| Day 12: Spring Framework     | Spring核心        | 说明框架优势           |
| Day 13: System Design        | 完整设计          | 设计一个系统           |

