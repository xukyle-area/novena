# Handling Large Price Deviations Between External and Internal Markets

When external prices diverge significantly from internal prices, safety must be prioritized.
The system should protect funds and prevent arbitrage abuse before worrying about continuity.
A practical approach uses quantified thresholds and staged mitigation actions.

## Define deviation with measurable rules
Deviation should be calculated as a percentage difference between internal and external reference prices.
A time condition is needed to avoid reacting to momentary spikes.
External references should be aggregated across multiple sources to reduce single-source errors.

## Response levels
A mild deviation can trigger tighter limit price checks to reject outlier orders.
A moderate deviation can disable market orders and restrict large trades.
A severe deviation can pause matching and rebuild the order book using a trusted anchor price.
In extreme cases, trading can be halted to prevent losses and systemic risk.

## Derivatives considerations
Risk calculations should use a mark price derived from external indices rather than last trade price.
Forced liquidations should be suppressed when prices are clearly abnormal.
This prevents unfair liquidations caused by short-lived price manipulation.

## Operational requirements
Every mitigation action should be logged and replayable for auditability.
Operators should have the ability to override or restore trading states when conditions stabilize.
Clear user communication is required when trading is limited or paused.

---

## Interview Q&A Practice

### Q1: What happens when your internal market price diverges significantly from external exchange prices?
**A:** When we detect significant price divergence, we implement staged mitigation controls based on the severity. We continuously compare our internal last trade price against a weighted median from multiple external exchanges. If the deviation exceeds a threshold, such as 0.5 percent for more than five seconds, we first tighten price limits to reject orders that are clearly outliers. If the deviation grows beyond 1 percent, we disable market orders and only allow limit orders within a narrower band. In severe cases above 2 percent deviation, we pause trading entirely until the situation stabilizes. The goal is to protect users from unfair execution prices and prevent arbitrage exploitation while maintaining service where it is safe to do so.

### Q2: Why is it important to intervene rather than letting the market self-correct?
**A:** Market self-correction assumes that arbitrageurs will quickly close price gaps, but in practice, automated trading bots can exploit deviations in milliseconds before any correction occurs. If we do not intervene, users could place orders at severely disadvantageous prices, either buying too high or selling too low relative to the broader market. For derivatives and margin trading, this is even more critical because price deviations can trigger liquidations or allow manipulation. Our internal market might have lower liquidity than major exchanges, so a few large orders could create artificial price swings. By intervening, we protect user funds and maintain market integrity. The cost of intervention is temporary trading disruption, which is far preferable to systematic losses.

### Q3: How do you calculate the deviation threshold to avoid false triggers?
**A:** We use multiple criteria to avoid reacting to noise. First, we aggregate external prices from at least three major exchanges and use a weighted median to filter outliers. Second, we require the deviation to persist for a time window, typically five to ten seconds, rather than triggering on instantaneous spikes. Third, we set different thresholds for different asset classes because volatility characteristics vary. For liquid spot pairs, a 0.5 percent deviation is significant, whereas for smaller cap tokens, we might tolerate 1 to 2 percent. Fourth, we monitor external data feed health and only trigger controls if we have high confidence in the external reference. Fifth, we log all near-threshold events for post-analysis to tune the thresholds based on false positive and false negative rates.

### Q4: In derivatives trading, why do you use mark price instead of last trade price for risk calculations?
**A:** Using last trade price for margin and liquidation calculations would create a severe manipulation risk. A trader could place a single large order on our exchange to move the last price significantly, which would trigger liquidations or allow them to manipulate their own margin requirements. Mark price is derived from external spot index prices plus a funding rate adjustment, making it much harder to manipulate because it reflects the broader market. Even if someone moves our internal price, their positions are still margined against the external reference. This protects both the exchange and users from artificial liquidations caused by low-liquidity price spikes. It also ensures that our risk calculations remain aligned with the underlying asset's true value.

### Q5: What are the operational challenges of implementing price deviation controls?
**A:** The biggest challenge is balancing safety with continuity. If controls trigger too aggressively, users experience frequent trading interruptions, which damages trust and usability. If controls are too loose, we fail to prevent the problems we are trying to avoid. We need comprehensive logging and auditability because any intervention that affects trading must be explainable and defensible to users and regulators. We also need operator override capabilities because automated systems cannot anticipate every scenario, such as a legitimate price movement that looks like an anomaly. Communication is critical because users need to understand why trading is paused or limited. Finally, we need to test these controls regularly in simulation to ensure they work correctly when a real event occurs.
