# System Architecture

## Core Positioning

This is a real-time market data processing system built around Kafka and Flink as its core components. The system supports multiple market data source ingestion, real-time push delivery, historical data queries, and is completely decoupled from the matching engine. The architecture focuses on three primary objectives that drive all technical decisions:

- The first objective is achieving low-latency real-time market data push delivery to end users.
- The second objective ensures that market data can be replayed and recalculated when needed for analysis or recovery scenarios.
- The third objective provides unified processing for both internal matching engine data and external market data sources.

## System Components

### Component 1: External Market Data Sources

The outer market component consists of various external data source connectors including Binance WebSocket connections, Binance REST API integrations, and other exchange data sources. This component is responsible for ingesting external exchange market data through multiple channels.

WebSocket connections provide real-time tick data, trade executions, and order book depth updates. The REST API integration serves two critical purposes: filling historical data gaps and recovering from connection interruptions. This dual-channel approach ensures we maintain continuous data coverage even when WebSocket connections experience temporary failures.

The design intentionally separates external market data because external sources are inherently unreliable and unstable. We cannot trust external data with the same confidence as internally generated data. Therefore, external market data must be completely decoupled from our internal matching engine output and must flow through the same internal processing pipeline to ensure consistency.

### Component 2: Internal Trade Service Group

The internal trade service group centers around the matching engine, which is the authoritative source for all internal trade execution data. The matching engine's primary responsibility is executing order matching logic and producing authoritative trade events and order book mutation events.

One critical architectural decision is that the matching engine never directly faces client connections. Its sole responsibility is calculating trade executions based on order matching rules. This separation of concerns allows the matching engine to focus exclusively on deterministic order matching without being burdened by concerns about data distribution or client connectivity.

### Component 3: Event Decoupling (Kafka)

Kafka serves as the event backbone connecting the matching engine to downstream processing systems. The architecture uses Kafka at two critical junctions in the data flow pipeline.

The first junction receives events directly from the matching engine and writes them to Kafka topics. The second junction receives processed events from Flink jobs and writes them to different Kafka topics for consumption by various downstream services.

Kafka fulfills four essential roles in this architecture. First, it provides complete decoupling between the matching engine and market data processing systems, allowing them to evolve independently. Second, it provides buffering capacity to handle traffic spikes and smooth out processing loads. Third, it enables event replay capability, which is crucial for debugging, backtesting, and disaster recovery scenarios. Fourth, it serves as the natural input source for Flink streaming jobs, providing reliable event consumption with exactly-once semantics.

### Component 4: Stream Processing Core (Flink)

Flink jobs represent the computational heart of the system, sitting at the center of the architecture diagram. These jobs consume events from Kafka topics and perform real-time stream processing to generate various market data products.

The Flink processing component consumes several types of events from Kafka including trade execution events and order book mutation events. Based on these raw event streams, Flink jobs compute various market data artifacts such as order books at different price resolutions, real-time ticker data with 24-hour statistics, and candlestick charts at multiple time resolutions.

Flink was chosen specifically because it provides stateful stream processing capabilities with exactly-once guarantees. The system uses RocksDB as the state backend, which allows maintaining large state datasets that exceed available memory. Checkpointing is configured at 60-second intervals to ensure we can recover quickly from failures without losing significant processing progress.

One critical architectural decision is how we partition processing across Flink's parallel execution slots. Different types of market data require different parallelization strategies. Order book processing must be strictly serialized per trading symbol because order book updates are inherently stateful and order-dependent. However, ticker and candlestick calculations can be parallelized much more aggressively because they involve stateless aggregations over event streams.

### Component 5: Data Storage and Distribution

After Flink jobs complete their stream processing, processed market data artifacts are written to Redis for low-latency access by client-facing services. Redis was selected because it provides microsecond-level read latency and supports pub/sub patterns for real-time notification of data updates.

The system stores several types of market data in Redis with carefully designed key schemas. Order book data is stored with keys formatted as `orderbook:{resolution}:{contractId}` where resolution indicates the price grouping level. Ticker data uses keys formatted as `ticker:{contractId}` containing 24-hour rolling statistics. Candlestick data uses keys formatted as `candle:{period}:{contractId}` where period indicates the time resolution such as 1m, 5m, or 1h.

## Data Flow Pipeline

The complete end-to-end data flow follows this sequence: external exchanges send data through WebSocket and REST API connections, which is received by the market-outer module. This module publishes raw events to Kafka topics. Flink jobs continuously consume from these Kafka topics, perform stream processing to compute market data products, and write results to Redis. Finally, client-facing APIs and frontend applications query Redis to retrieve market data for display to end users.

This architecture achieves several important properties. It provides clear separation of concerns with each component having a well-defined responsibility. It enables horizontal scalability by adding more Flink task slots or Redis nodes as load increases. It ensures data consistency through Kafka's ordering guarantees and Flink's state management. It supports disaster recovery through Kafka's persistent event log and Flink's checkpoint mechanism.

## Design Rationale

The decision to build around Kafka and Flink was driven by specific technical requirements that these technologies address particularly well. Kafka provides the reliable event backbone with ordering guarantees, persistence, and replay capability that are essential for financial data processing. Flink provides the stateful stream processing engine with exactly-once semantics and flexible windowing operations needed for complex market data calculations.

The complete decoupling of the matching engine from market data distribution means we can scale and modify the market data system without impacting trade execution reliability. The matching engine can focus purely on its core responsibility of deterministic order matching while market data concerns are handled by a separate, specialized subsystem.

This architecture has proven capable of handling high-frequency trading scenarios with acceptable latency characteristics, typically delivering market data updates to clients within 100 milliseconds of the underlying event occurrence under normal load conditions.

## Interview Q&A Practice

### Q1: Can you explain the overall architecture of your market data system?
**A:** Our market data system is built around Kafka and Flink as the core components. External market data comes in through WebSocket connections for real-time feeds and REST APIs for historical backfill. We treat external sources as untrusted, so we normalize and validate everything before it enters our processing pipeline. The matching engine produces authoritative internal trade events, which also flow into Kafka. Flink jobs then consume from Kafka to compute real-time metrics like order book snapshots, candles, and ticker statistics. The computed data goes to Redis for low-latency access and to persistent storage for historical queries. Finally, we have a push system that delivers real-time updates to clients over MQTT or WebSocket.

### Q2: Why did you choose Kafka and Flink for this architecture?
**A:** Kafka provides several critical benefits for our use case. First, it decouples the matching engine from downstream consumers, which means matching can run at full speed without being slowed down by client delivery. Second, it handles traffic spikes by buffering messages. Third, it enables event replay, so we can recompute historical metrics when we need to fix bugs or add new features. Flink was chosen because it is purpose-built for stateful stream processing with exactly-once semantics. The MapState feature makes order book maintenance natural and efficient. Flink also gives us fine-grained control over parallelism and checkpointing, which are critical for both performance and correctness.

### Q3: How do you handle the separation between real-time and historical data?
**A:** We maintain two separate data paths because they have different requirements. For real-time data, clients subscribe through MQTT or WebSocket to get the lowest possible latency. This path prioritizes speed and can tolerate occasional message loss since the next update will arrive shortly. For historical data, clients use REST APIs to query specific time ranges or symbol data. This path prioritizes consistency and completeness over latency. By separating these concerns, we avoid using Kafka for random access queries, which it is not designed for, and we do not let historical queries impact real-time delivery performance.

### Q4: What are the main challenges in maintaining this architecture?
**A:** The biggest challenges are around state management and failure recovery. Flink checkpoint configuration must be tuned carefully to balance between recovery time and checkpoint overhead. If checkpoints take too long, they can impact throughput, but if the interval is too long, recovery takes longer after failures. Another challenge is managing backpressure from slow clients. We need to ensure that slow subscribers do not cause memory buildup in the push layer, which is why we use brokers or rate limiting. Kafka topic design is also critical because poor partitioning can lead to hot spots and uneven load distribution across Flink tasks.

### Q5: How does the system handle external market data that might be unreliable?
**A:** We treat all external data as untrusted input that must be validated and normalized. First, we aggregate prices from multiple exchanges to create a reference price, rather than relying on a single source. We set deviation thresholds and time windows to filter out obvious anomalies or flash crashes. When external data stops arriving or appears corrupted, we have fallback logic to either use cached values or mark the data as stale. This isolation is why external sources feed into Kafka first rather than directly into client-facing services. This gives us a point where we can apply validation rules and decide whether to propagate the data forward.
