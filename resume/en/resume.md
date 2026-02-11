
# Kyle Xu (Zhongjian Xu)

Senior Backend Engineer – Distributed Systems & Real-Time Infrastructure
Beijing, China
Email: [zjxu97@gmail.com](mailto:zjxu97@gmail.com)
LinkedIn: [https://linkedin.com/in/xu-kyle](https://linkedin.com/in/xu-kyle)

---

## Summary

Backend engineer with 6 years of experience in distributed systems and real-time processing. Specialized in market data infrastructure, trading systems, and streaming architectures using Flink and Kafka. Strong background in high-concurrency system design and financial system modeling.

---

## Experience

### Tiger Brokers – Crypto Exchange

**Senior Software Engineer** | May 2023 – Present

Hong Kong licensed cryptocurrency exchange. Core contributor to market data, OTC trading, and real-time rule engine infrastructure.

#### Market Data Infrastructure

* Consumed trade-level events from matching engine and computed real-time ticker and candlestick data (1s–1d) using Flink
* Integrated external exchange feeds (e.g., Binance) for redundancy and price validation
* Designed tiered architecture: MQTT real-time push (<50ms), Redis hot cache, DynamoDB historical storage
* Implemented real-time volatility and liquidity monitoring for automated risk alerts

#### Real-Time Rule Engine Platform

* Built configurable Flink-based rule engine enabling hot rule deployment without service release
* Implemented dynamic job lifecycle management with savepoint recovery and state persistence
* Reduced rule rollout time from 1 day to 1 hour
* Designed multi-source adapter framework (Kafka, MySQL, WebSocket) for extensible data integration

#### OTC Trading System

* Designed OTC trading platform supporting fiat–crypto large-volume transactions
* Implemented proprietary order book aggregation across multiple LPs for optimal pricing
* Modeled full order lifecycle using state machine (Quote → Lock → Trade → Settlement)
* Optimized net settlement process, improving capital turnover by 70%

---

### Meituan – Hotel & Travel Group

**Software Engineer** | May 2021 – Mar 2023

* Built merchant-level rate limiting system using Redis + Lua, improving system stability under high QPS
* Implemented signature verification with multi-level cache (Guava + Redis), increasing throughput by 3×
* Designed distributor lifecycle state machine to prevent invalid state transitions

---

### Xiaomi

**Software Engineer** | Oct 2019 – Apr 2021

* Contributed to retail management system, focusing on order and inventory modules
* Optimized inventory synchronization and transaction consistency under high concurrency

---

## Technical Skills

**Languages:** Java (Primary), Python, SQL
**Streaming & Messaging:** Flink, Kafka
**Storage:** Redis, MySQL, DynamoDB
**Architecture:** Distributed systems, high-concurrency design, state machine modeling
**DevOps:** Docker, Kubernetes, Prometheus