# Interview Technical Points for the Market Data Project

This project is a real-time market data processing system built on Kafka, Flink, and Redis.
It focuses on order book maintenance, ticker and candle calculation, and low-latency delivery.
The system is designed for millisecond-level latency and scalable parallelism in production.

## Architecture summary
The outer layer ingests exchange data through WebSocket and pushes normalized events into Kafka.
Flink jobs consume Kafka topics and compute order book snapshots, tickers, and candles.
Redis stores the latest snapshots and rolling statistics for low-latency reads.
Downstream services expose data through APIs or push channels.

## Key Flink jobs
The order book job maintains per-symbol state and emits depth snapshots on a timer.
The ticker job uses sliding event-time windows to compute 24-hour statistics.
The candle job computes OHLCV over multiple resolutions using windowed aggregation.

## State management
Order book data uses `MapState` to track bid and ask levels efficiently.
State size is controlled by price grouping and removal of zero-quantity levels.
RocksDB is used for large state and to reduce memory pressure.

## Checkpoint and consistency
Checkpoint barriers snapshot operator state and Kafka offsets for recovery.
Exact-once semantics are required for order book correctness.
Ticker and candle outputs can use idempotent writes to tolerate at-least-once delivery.

## Performance optimization
Parallelism is tuned per operator to balance throughput and CPU usage.
State backend configuration and incremental checkpoints reduce IO pressure.
Network buffer tuning and operator chaining are adjusted to control latency.
Data skew is mitigated with custom partitioning or two-stage aggregation where needed.

## Troubleshooting practices
When the order book stops updating, check the Flink job status and Kafka consumption first.
Kafka consumer group lag indicates backpressure or downstream delays.
Redis connectivity issues often surface as missing or stale snapshots.
Monitoring of checkpoint duration and backpressure metrics helps detect early degradation.

## Typical interview questions
Explain why Flink is chosen for this system and how it ensures low latency.
Describe how you keep order book state consistent under high throughput.
Discuss the trade-offs between exact-once and at-least-once for different outputs.
Explain how you handle late or out-of-order events for candle computation.

---

## Interview Q&A Practice

### Q1: Can you give me an overview of your market data project?
**A:** I worked on a real-time market data processing system that handles order book maintenance, ticker calculations, and candle generation for a cryptocurrency exchange. The system is built on Kafka for message streaming, Flink for stateful computation, and Redis for low-latency data access. We ingest market data through WebSocket connections and publish normalized events to Kafka. Flink jobs consume these events to maintain live order books using MapState, compute rolling 24-hour statistics in sliding windows, and generate OHLCV candles at multiple time resolutions. The processed data is written to Redis so downstream services can access the latest market snapshots with sub-millisecond latency. We also persist historical data for analytics and regulatory compliance.

### Q2: How do you maintain order book state in Flink?
**A:** We use a KeyedProcessFunction with MapState to maintain the order book for each trading symbol. The MapState holds price levels as keys and quantities as values, with separate map states for bids and asks. When an order event arrives, we parse the operation type, which could be insert, update, or delete. For inserts, we add the quantity to the existing quantity at that price level, creating a new level if needed. For deletes, we subtract the quantity and remove the level entirely if it reaches zero. To reduce state size, we implement price grouping, where we round prices to discrete buckets based on tick size. We also register a timer to periodically emit order book snapshots rather than emitting on every event, which reduces downstream message volume.

### Q3: How does your system achieve exactly-once semantics?
**A:** We achieve exactly-once semantics through Flink's checkpoint mechanism combined with transactional Kafka sources and idempotent sinks. Flink periodically triggers checkpoints, which snapshot the state of all operators and record Kafka offsets. When a checkpoint completes, it represents a consistent global state across all parallel tasks. If a failure occurs, Flink restarts from the last successful checkpoint, restoring both the operator state and Kafka read positions. This ensures no events are processed twice or skipped. For the order book job, exact-once is critical because duplicate or missed events would corrupt the book. For sinks, we either use idempotent operations like Redis SET, or we use transactional writes that only commit after checkpoint completion.

### Q4: What performance optimizations have you implemented?
**A:** We have optimized performance at multiple levels. First, we tune parallelism per operator based on its workload, rather than using a global parallelism. Order book processing has parallelism matching the number of symbols, while heavier aggregations might have higher parallelism. Second, we use RocksDB as the state backend for large state that does not fit in memory, and we enable incremental checkpoints to reduce IO during snapshotting. Third, we implement price grouping to limit the number of state entries per order book. Fourth, we tune network buffer settings to reduce latency for small messages. Fifth, we monitor for data skew and rebalance partition keys if certain symbols become hot. Finally, we separate jobs by concern so that one job's checkpoint duration does not block others.

### Q5: How do you troubleshoot when the order book stops updating?
**A:** I follow a systematic debugging process starting from the data source and working downstream. First, I check if the Flink job is running by looking at the web UI and verifying that all tasks are in the running state. Second, I check Kafka consumer lag to see if the job is consuming events. If lag is growing, it indicates backpressure or processing delays. Third, I examine Flink task logs for exceptions or warnings. Fourth, I verify that the WebSocket feed is still connected and producing events, which could be checked through the ingestion service logs. Fifth, I check Redis connectivity and confirm that the sink is writing successfully. Finally, I look at checkpoint metrics because failed checkpoints can sometimes cause state loss. Once I identify the layer where the failure occurred, I can dig into specific logs or metrics for that component.

### Q6: What are the challenges of computing candles from streaming trade data?
**A:** The main challenges are handling late arrivals, dealing with sparse data, and ensuring window alignment. Trades can arrive out of order due to network delays or source system issues, so we must use event time processing with watermarks. The watermark tells Flink how far behind the latest event time it should wait before closing a window. If the watermark is too tight, we might close candles prematurely and miss late trades. If it is too loose, we add unnecessary latency. For sparse symbols that trade infrequently, we might have windows with no trades at all, which requires special handling to either carry forward the last candle or mark the period as inactive. We also need to ensure that candles at different resolutions align correctly, so a one-hour candle contains exactly 60 one-minute candles.
