# Parallel vs Serial Processing in Flink Market Jobs

Some market data computations require strict ordering, while others can run in parallel.
The key distinction is whether the state is order-sensitive or can be derived through aggregation.

## Order book processing
An order book is a strict state machine where event order matters.
Operations like add, modify, match, and cancel must be applied in sequence.
The correct model is to process events serially per symbol, while allowing different symbols to run in parallel.
This is typically implemented with `keyBy(symbol)` and a stateful process function.

## Ticker computation
Ticker values such as last price and 24h stats are aggregate results over trade streams.
The exact event order inside the window does not change the final result as long as the window is correct.
This makes ticker computation safe to parallelize per symbol using windows and aggregations.

## Candle computation
Candles are windowed aggregates that depend on timestamps rather than arrival order.
As long as watermarks are configured correctly, late data can be handled safely.
Candles can be parallelized by symbol and resolution, and even separated into dedicated jobs.

## Recommended job structure
A common structure keeps order book processing in a dedicated serial-per-symbol operator.
Trade analytics such as ticker and candles can be in parallel branches or separate jobs.
This balances low latency with operational scalability and simplifies recomputation.

## Reliability notes
Order book state typically requires exact-once guarantees and frequent checkpoints.
Ticker and candle outputs can often tolerate at-least-once delivery with idempotent sinks.
The design should always follow the rule that state safety determines parallelism, not the other way around.

---

## Interview Q&A Practice

### Q1: Why must order book processing be serial, and how do you implement it in Flink?
**A:** Order book processing must be serial because it is a state machine where the order of events fundamentally matters. If you receive an add order event followed by a cancel order event, reversing that sequence would produce incorrect results or even errors. Each operation modifies the state based on the current state, so concurrent modifications would lead to race conditions. In Flink, we implement this by using keyBy to partition events by symbol. This ensures that all events for BTCUSDT go to the same parallel instance and are processed in order, while ETHUSDT events go to a different instance and can be processed in parallel. Within each keyed stream, we use a ProcessFunction with MapState to maintain the bid and ask levels and apply each event sequentially.

### Q2: If order books must be serial, does that limit your system's scalability?
**A:** Serial processing per symbol does not limit overall scalability because we have hundreds or thousands of trading symbols. Each symbol's order book is independent, so they can all be processed in parallel. If we set parallelism to 32, we can process 32 different symbols simultaneously. The limitation only applies within a single symbol, where events must be processed one after another. In practice, this is not a bottleneck because individual order book updates are very fast, usually completing in microseconds. The real scalability limit comes from per-symbol throughput, which is constrained by the trading activity of that symbol. For extremely high-frequency symbols, we can optimize the processing logic itself rather than trying to parallelize it incorrectly.

### Q3: Why can ticker and candle computation be parallelized when order books cannot?
**A:** Ticker and candle computations are aggregations rather than state machines. For ticker calculation, we are computing statistics like 24-hour volume, high, low, and price change over a sliding window of trades. The order in which trades arrive within that window does not change the final result because we are summing volumes and taking min/max of prices. These operations are commutative and associative. Similarly, candles aggregate OHLCV data over fixed time windows. As long as we use event time and configure watermarks correctly, late-arriving events can be merged into the correct window. Flink's windowing operators are designed to handle this safely. The key difference is that aggregations combine multiple inputs into a summary, whereas order book operations depend on precise sequential state transitions.

### Q4: How do you structure your Flink jobs to handle both serial and parallel operations?
**A:** We typically use separate jobs for different concerns, which gives us better operational flexibility. The order book job consumes order and cancel events from Kafka, uses keyBy on symbol, and runs a stateful ProcessFunction that emits depth snapshots. This job has parallelism set based on the number of active symbols. The ticker and candle jobs consume trade events, also key by symbol, but use window operations and aggregation functions that can safely run in parallel. We might even split candles by resolution, running separate jobs for one-minute and one-hour candles. This separation allows us to tune checkpointing, parallelism, and resources independently. If ticker computation falls behind, it does not affect order book updates. If we need to reprocess candles, we can do so without touching order book state.

### Q5: What would happen if you tried to parallelize order book processing incorrectly?
**A:** If we tried to process order book events in parallel without proper keying, we would see data corruption and race conditions. For example, two threads might both read the current quantity at a price level as 100, then one adds 50 and the other adds 30, and both write back their results. Depending on timing, the final quantity might be 150 or 130 instead of the correct 180. In a distributed system like Flink, the problem is worse because you could have partial order book views on different machines that never converge. You might also see events processed out of order, like a cancel arriving before the original add, which would cause exceptions or invalid state. The only safe way is to ensure per-symbol serialization through keying and let Flink's stream partitioning guarantee that all events for one symbol flow through the same task.
