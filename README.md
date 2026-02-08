# Novena - 个人技术知识库

这是一个系统化整理的技术知识库，涵盖实际项目经验、核心技术栈深度总结以及技术英语学习资料。

## 📁 项目结构

```
novena/
├── project/           # 实际项目经验总结
├── repository/        # 技术栈知识库
├── english/          # 英文技术文档
├── resume/           # 个人简历
└── vocabulary/       # 技术词汇表
```

---

## 🚀 项目经验 (project/)

### 行情系统 (market/)
交易所实时行情推送系统的架构设计与技术实现

- [系统结构](project/market/01.%20系统结构.md) - 整体架构设计
- [MQTT vs WebSocket](project/market/02.%20mqtt对比websocket.md) - 推送协议技术选型
- [技术点](project/market/04.%20技术点.md) - 核心技术点总结
- [价格偏差分析](project/market/05.%20价格偏差.md) - 价格计算与偏差处理
- [耗时分析](project/market/06.%20耗时分析.md) - 性能优化与瓶颈分析

**核心技术：** Kafka、MQTT、WebSocket、Flink、Redis

### OTC 系统 (otc/)
场外交易系统的订单状态管理

- [订单状态](project/otc/01.%20订单状态.md) - 订单状态机设计

**核心技术：** 状态机、分布式事务

### 限流系统 (rate-limit/)
分布式限流方案设计与实现

- [概况](project/rate-limit/01.%20概况.md) - 限流方案概述
- [同一毫秒多次请求](project/rate-limit/02.%20同一毫秒多次请求.md) - 高并发场景处理
- [与单机限流对比](project/rate-limit/03.%20与单机限流比.md) - 分布式 vs 单机

**核心技术：** Redis、Lua、分布式限流

### 规则引擎 (rule-engine/)
业务规则引擎的设计与应用

- [概述](project/rule-engine/01.%20概述.md) - 规则引擎架构

---

## 📚 技术知识库 (repository/)

### Flink
- [指南](repository/flink/00.%20guide.md)
- [Flink 架构](repository/flink/01.%20flink-architecture.md)

### Java
- [垃圾回收](repository/java/01.%20垃圾回收.md)

### Kafka
- [结构](repository/kafka/01.%20结构.md)
- [丢失、重复与有序](repository/kafka/02.%20丢失、重复与有序.md)

### MySQL
- [并发修改](repository/mysql/01.%20并发修改.md)
- [死锁](repository/mysql/02.%20死锁.md)

### Redis
- [数据结构](repository/redis/01.%20数据结构.md)
- [分布式锁](repository/redis/02.%20分布式锁.md)

### 其他
- [Nonce 与时间戳](repository/others/01.%20nonce%20与时间戳.md)
- [状态机](repository/others/02.%20状态机.md)

---

## 🌍 英文技术文档 (english/)

### Market System
- [Structure](english/market/01.%20structure.md)
- [Core Code](english/market/02.%20core_code.md)
- [Questions](english/market/03.%20questions.md)
- [Tech Points](english/market/04.%20tech_point.md)

### Rule Engine
- [Summary](english/rule-engine/01.%20summary.md)

---

## 📖 技术词汇表 (vocabulary/)

系统化整理的技术英语词汇，按主题分类：

### 词汇主题

1. [基础计算机词汇](vocabulary/subject/01-basic-computer-vocabulary.md)
2. [编程语言核心](vocabulary/subject/02-programming-language-core.md)
3. [数据结构与算法](vocabulary/subject/03-data-structures-algorithms.md)
4. [操作系统与网络](vocabulary/subject/04-operating-system-network.md)
5. [数据库](vocabulary/subject/05-database.md)
6. [分布式系统](vocabulary/subject/06-distributed-systems.md)
7. [微服务](vocabulary/subject/07-microservices.md)
8. [消息队列](vocabulary/subject/08-message-queue.md)
9. [缓存](vocabulary/subject/09-caching.md)
10. [并发与多线程](vocabulary/subject/10-concurrency-multithreading.md)
11. [Java 生态系统](vocabulary/subject/11-java-ecosystem.md)
12. [Spring 框架](vocabulary/subject/12-spring-framework.md)
13. [系统设计](vocabulary/subject/13-system-design.md)
14. [性能优化](vocabulary/subject/14-performance-optimization.md)
15. [DevOps 部署](vocabulary/subject/15-devops-deployment.md)
16. [软件工程实践](vocabulary/subject/16-software-engineering-practices.md)
17. [测试](vocabulary/subject/17-testing.md)
18. [安全](vocabulary/subject/18-security.md)
19. [面试表达](vocabulary/subject/19-interview-expressions.md)

### 工具脚本

- [extract_vocabulary.py](vocabulary/extract_vocabulary.py) - 词汇提取工具
- [remove_duplicates.py](vocabulary/remove_duplicates.py) - 去重工具

---

## 📝 简历 (resume/)

- [Markdown 简历](resume/markdown-resume.md)
- [LaTeX 简历（中文）](resume/zh/kyle_resume.tex)
- [LaTeX 简历（英文）](resume/en/kyle_resume.tex)

---

## 🎯 核心技能栈

### 后端技术
- **语言：** Java
- **框架：** Spring Boot, Spring Cloud
- **消息队列：** Kafka, MQTT
- **数据库：** MySQL, Redis
- **流计算：** Flink
- **通信协议：** WebSocket, MQTT

### 架构能力
- 分布式系统设计
- 高并发系统架构
- 微服务架构
- 实时数据处理
- 性能优化

### 领域经验
- 交易所系统
- 实时行情推送
- 限流与风控
- 规则引擎
- OTC 交易

---

## 📈 项目特色

### 1. 实战经验导向
所有项目文档都来自真实的业务场景，包含架构设计、技术选型、问题解决等完整过程。

### 2. 技术深度总结
不仅记录"是什么"，更关注"为什么"和"怎么做"，深入技术原理和最佳实践。

### 3. 双语文档
中英文双语技术文档，提升技术英语能力。

### 4. 系统化组织
按技术栈和项目维度系统化整理，便于检索和学习。

---

## 🔧 使用说明

### 快速导航

- **学习某个技术栈？** → 查看 `repository/` 对应目录
- **了解项目经验？** → 查看 `project/` 对应系统
- **准备英文面试？** → 查看 `english/` 和 `vocabulary/`
- **制作简历？** → 参考 `resume/` 模板

### 文档阅读建议

1. **项目文档：** 建议按序号顺序阅读，从整体架构到细节实现
2. **技术知识库：** 可独立查阅，每篇文档都是完整的知识点
3. **词汇表：** 建议结合实际技术文档使用，边学边查

---

## 🌟 亮点文档推荐

### 必读文档

1. **[MQTT vs WebSocket 技术选型](project/market/02.%20mqtt对比websocket.md)**  
   深入对比两种协议在行情推送场景的优劣，展现系统边界感和工程思维

2. **[Kafka 丢失、重复与有序](repository/kafka/02.%20丢失、重复与有序.md)**  
   消息队列核心问题的系统性解决方案

3. **[Redis 分布式锁](repository/redis/02.%20分布式锁.md)**  
   分布式系统的经典问题及实现方案

4. **[MySQL 死锁](repository/mysql/02.%20死锁.md)**  
   数据库并发问题的深入分析

---

## 📮 联系方式

如有问题或建议，欢迎交流讨论。

---

## 📜 License

本项目仅用于个人学习和技术分享。

---

**Last Updated:** February 2026
