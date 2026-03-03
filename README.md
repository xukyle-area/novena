# Novena - 个人技术知识库

系统化整理的技术知识库，涵盖项目经验总结、核心技术栈深度分析以及英文面试准备资料。

> 📖 **在线阅读**：[https://kyleexu.github.io/novena](https://kyleexu.github.io/novena)

## 📁 项目结构

```
novena/
├── project/          # 实际项目经验总结
│   ├── market/       # 行情系统
│   ├── otc/          # OTC 交易系统
│   ├── rate-limit/   # 分布式限流
│   └── rule-engine/  # 规则引擎
├── repository/       # 技术栈知识库
│   ├── flink/        # Flink 流计算
│   ├── java/         # Java 核心
│   ├── kafka/        # Kafka 消息队列
│   ├── mysql/        # MySQL 数据库
│   ├── redis/        # Redis 缓存
│   └── others/       # 其他技术
├── english/          # 英文技术文档与面试准备
│   ├── market/       # 行情系统英文表达
│   ├── rule-engine/  # 规则引擎英文表达
│   └── vocabulary/   # 技术词汇表
├── interview/        # 面试总结
└── resume/           # 个人简历
```

---

## 🚀 项目经验 (project/)

### 行情系统 (market/)

交易所实时行情推送系统 —— 基于 Kafka + Flink 构建流式计算链路，通过 MQTT 实现毫秒级推送。

| 文档 | 内容 |
|------|------|
| [系统结构](project/market/01.%20系统结构.md) | 整体架构设计，数据流拆解 |
| [Flink 任务](project/market/02.%20Flink%20任务.md) | TickerJob、CandleJob、OrderbookJob 详解 |
| [推送技术选型](project/market/03.%20推送技术选型.md) | MQTT vs WebSocket 对比分析 |
| [价格偏差处理](project/market/04.%20价格偏差处理.md) | 价格计算与偏差控制策略 |
| [K 线补偿](project/market/05.%20K%20线补偿.md) | 数据缺失场景的补偿机制 |
| [MQTT 耗时分析](project/market/06.%20MQTT%20耗时分析.md) | 端到端延迟分析与优化 |

**核心技术**：Kafka · Flink · MQTT · Redis · WebSocket

### OTC 系统 (otc/)

场外交易系统的订单生命周期管理。

- [订单状态](project/otc/01.%20订单状态.md) - 订单状态机设计
- [OTC 结算](project/otc/02.%20OTC%20结算.md) - 结算流程设计

**核心技术**：状态机 · 分布式事务

### 限流系统 (rate-limit/)

分布式限流方案设计与实现。

- [概况](project/rate-limit/01.%20概况.md) - 限流方案概述
- [同一毫秒多次请求](project/rate-limit/02.%20同一毫秒多次请求.md) - 高并发场景处理
- [与单机限流对比](project/rate-limit/03.%20与单机限流比.md) - 分布式 vs 单机方案

**核心技术**：Redis · Lua · 滑动窗口

### 规则引擎 (rule-engine/)

业务规则引擎架构设计。

- [概述](project/rule-engine/01.%20概述.md) - 规则引擎架构

---

## 📚 技术知识库 (repository/)

### Flink
- [Flink 架构](repository/flink/01.%20flink-architecture.md) - 架构原理与核心概念

### Java
- [CMS 垃圾收集器](repository/java/01.%20concurrent%20mark%20sweep.md) - CMS 工作原理
- [G1 垃圾收集器](repository/java/02.%20G1.md) - G1 算法与调优
- [HashMap](repository/java/03.%20hashmap.md) - 底层实现与扩容机制
- [ConcurrentHashMap](repository/java/04.%20concurrenthashmap.md) - 并发容器原理
- [Lock & Synchronized](repository/java/05.%20lock%20&%20synchornized.md) - 锁机制对比

### Kafka
- [结构](repository/kafka/01.%20结构.md) - Broker、Topic、Partition
- [丢失、重复与有序](repository/kafka/02.%20丢失、重复与有序.md) - 消息可靠性保证

### MySQL
- [并发修改](repository/mysql/01.%20并发修改.md) - 乐观锁与悲观锁
- [死锁](repository/mysql/02.%20死锁.md) - 死锁场景分析与解决
- [MVCC](repository/mysql/03.%20mvcc.md) - 多版本并发控制

### Redis
- [数据结构](repository/redis/01.%20数据结构.md) - 五大数据类型底层实现
- [分布式锁](repository/redis/02.%20分布式锁.md) - Redisson 实现方案

### 其他
- [Nonce 与时间戳](repository/others/01.%20nonce%20与时间戳.md) - 防重放攻击
- [状态机](repository/others/02.%20状态机.md) - 状态机设计模式
- [事件驱动](repository/others/03.%20事件驱动.md) - 事件驱动架构
- [高性能架构](repository/others/04.%20高性能的架构.md) - 高并发系统设计
- [零拷贝](repository/others/05.%20零拷贝.md) - 零拷贝技术原理

---

## 🌍 英文面试准备 (english/)

### 自我介绍
- [Self Introduction](english/self-introduction.md) - 英文自我介绍模板

### 行情系统 (Market System)
| 文档 | 内容 |
|------|------|
| [System Architecture](english/market/01-system-architecture.md) | 系统架构英文表达 |
| [MQTT vs WebSocket](english/market/02-mqtt-vs-websocket.md) | 技术选型讨论 |
| [Parallel vs Serial](english/market/03-parallel-vs-serial.md) | 并行与串行处理 |
| [Technical Points](english/market/04-technical-points.md) | 核心技术点 |
| [Price Deviation](english/market/05-price-deviation-controls.md) | 价格偏差控制 |
| [Latency Analysis](english/market/06-latency-analysis.md) | 延迟分析 |

### 规则引擎 (Rule Engine)
- [Summary](english/rule-engine/01.%20summary.md) - 规则引擎概述

### 技术词汇表 (vocabulary/)

系统化整理的技术英语词汇，按主题分类：

| 编号 | 主题 |
|------|------|
| 01 | [基础计算机词汇](english/vocabulary/subject/01-basic-computer-vocabulary.md) |
| 02 | [编程语言核心](english/vocabulary/subject/02-programming-language-core.md) |
| 03 | [数据结构与算法](english/vocabulary/subject/03-data-structures-algorithms.md) |
| 04 | [操作系统与网络](english/vocabulary/subject/04-operating-system-network.md) |
| 05 | [数据库](english/vocabulary/subject/05-database.md) |
| 06 | [分布式系统](english/vocabulary/subject/06-distributed-systems.md) |
| 07 | [微服务](english/vocabulary/subject/07-microservices.md) |
| 08 | [消息队列](english/vocabulary/subject/08-message-queue.md) |
| 09 | [缓存](english/vocabulary/subject/09-caching.md) |
| 10 | [并发与多线程](english/vocabulary/subject/10-concurrency-multithreading.md) |
| 11 | [Java 生态](english/vocabulary/subject/11-java-ecosystem.md) |
| 12 | [Spring 框架](english/vocabulary/subject/12-spring-framework.md) |
| 13 | [系统设计](english/vocabulary/subject/13-system-design.md) |
| 14 | [性能优化](english/vocabulary/subject/14-performance-optimization.md) |
| 15 | [DevOps](english/vocabulary/subject/15-devops-deployment.md) |
| 16 | [软件工程](english/vocabulary/subject/16-software-engineering-practices.md) |
| 17 | [测试](english/vocabulary/subject/17-testing.md) |
| 18 | [安全](english/vocabulary/subject/18-security.md) |
| 19 | [面试表达](english/vocabulary/subject/19-interview-expressions.md) |

---

## 📝 简历 (resume/)

- [Markdown 简历](resume/markdown-resume.md)
- [LaTeX 简历（中文）](resume/zh/kyle_resume_zh.tex)
- [LaTeX 简历（英文）](resume/en/kyle_resume_en.tex)

---

## 🎯 技术栈

| 分类 | 技术 |
|------|------|
| **语言** | Java |
| **框架** | Spring Boot, Spring Cloud |
| **消息队列** | Kafka, MQTT |
| **流计算** | Flink |
| **数据库** | MySQL |
| **缓存** | Redis |
| **协议** | WebSocket, MQTT |

---

## 🔧 本地预览

```bash
# 安装 docsify-cli
npm i docsify-cli -g

# 启动本地服务
docsify serve

# 访问 http://localhost:3000
```

---

## 📜 License

本项目仅用于个人学习和技术分享。

---

**Last Updated:** March 2026
