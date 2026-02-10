# Price Deviation Handling in Exchange Systems

## Core Principle

When external market prices diverge significantly from our exchange's internal prices, the priority order for system response is clear: protecting system and financial safety comes first, fairness to users comes second, and maintaining continuous trading experience comes third.

Many engineers worry that implementing price protection mechanisms appears unprofessional or suggests the exchange has technical problems. However, the consequences of not having proper safeguards are far worse. Without protection, the exchange risks margin calls cascading into bankruptcy, malicious users manipulating prices to execute favorable trades against trapped counterparties, and arbitrageurs systematically draining capital through price discrepancies.

Professional exchanges implement multiple layers of price protection because the alternative is existential risk. It is far better to temporarily restrict trading when something appears wrong than to allow systematic capital extraction or create situations where users lose confidence in the platform's reliability.

## Defining "Excessive Deviation"

Price protection mechanisms cannot rely on intuition or manual intervention. Every protection rule must be quantified with clear thresholds that can be monitored and evaluated objectively. I will walk through the standard approach to defining when price deviation becomes actionable.

### Price Difference Threshold

The most basic metric compares internal and external prices using percentage difference calculated as the absolute value of internal price minus external price, divided by external price. When this percentage exceeds a defined threshold, it triggers protection mechanisms.

For spot trading, thresholds typically range from 0.5% to 1% depending on the asset's normal volatility characteristics. More volatile assets tolerate larger percentage deviations before protection activates. For perpetual futures and contracts, thresholds are usually tighter, ranging from 0.3% to 0.8%, because derivative pricing should closely track spot markets and significant deviation suggests dysfunction.

These thresholds are not arbitrary but are derived from empirical analysis of normal price movements. Analyzing historical price data allows determining what percentage deviation represents abnormal conditions versus normal market volatility.

### Duration Requirement

A single instantaneous price spike should not trigger protection mechanisms because order book crossing can create momentary price discrepancies that resolve within seconds. Protection mechanisms should only activate when price deviation persists for a meaningful duration, typically 3, 5, or 10 seconds depending on market characteristics.

This duration filter prevents false positives from transient order book states while still responding quickly enough to protect against sustained mispricing. If price deviation exceeds the threshold but returns to normal within the duration window, no protection activates.

### External Price Reliability

A critical consideration is that no single external exchange represents the true market price. Using a single external source creates vulnerability where that exchange's technical issues or manipulation could trigger inappropriate responses in our system.

The robust approach is computing external reference price as a weighted median across multiple highly liquid exchanges. This calculation should exclude outliers that deviate significantly from the median before computing the final reference price. Exchanges with insufficient liquidity should be weighted lower or excluded entirely from the calculation.

By requiring consensus across multiple external sources, we avoid reacting to issues that are specific to one external exchange. If our internal price deviates from the median of multiple major exchanges, that represents a genuine issue requiring response.

## Response Levels

Price protection operates through escalating levels of intervention, starting with minimal restrictions and increasing to aggressive measures if deviation persists or worsens. This graduated approach balances protecting the exchange against unnecessarily disrupting legitimate trading activity.

### Level 1: Price Limit Tightening

The most conservative intervention is dynamically restricting the allowed price range for new orders without stopping trading entirely. This approach is appropriate for mild price deviations where the market is still functioning but prices show unusual characteristics.

The mechanism works by applying dynamic price limits on incoming orders. Buy orders above external reference price times 1.01 are rejected. Sell orders below external reference price times 0.99 are rejected. These limits prevent users from submitting orders at obviously wrong prices that would result in unfavorable executions.

This level of intervention allows trading to continue normally for users placing reasonable limit orders while blocking clearly anomalous orders. It is nearly invisible to users during normal market conditions but provides automatic protection against basic errors or manipulation attempts.

### Level 2: Trading Mode Degradation

When price deviation is more significant but the market is still functioning, the exchange can degrade trading capabilities rather than completely halting trading. This level is appropriate when price deviation is clear but not severe enough to justify stopping all activity.

Common restrictions include disabling market orders since they execute at whatever price is available and could result in extremely unfavorable fills for users. Large order submission can be blocked on the premise that significant positions should not be established during abnormal pricing conditions. Opening new positions can be prohibited while allowing users to close existing positions, which is particularly relevant for futures and perpetual contracts.

Many major exchanges use these restrictions in production. During times of market stress or unusual price action, they automatically restrict the types of trading activity allowed. This pragmatic approach acknowledges that sometimes markets need constraints to prevent worse outcomes.

### Level 3: Price Reset and Order Book Reconstruction

When price deviation indicates clear system malfunction or manipulation, aggressive intervention is necessary despite the disruption it causes. This level includes temporarily suspending matching entirely, re-anchoring the internal price to external reference prices, and potentially reconstructing the order book with current orders re-evaluated at correct prices.

This intervention is dangerous because it disrupts active trading and may invalidate existing orders. However, when internal prices have clearly diverged from reality due to technical issues or manipulation, continuing to operate the dysfunctional market causes greater harm than resetting to a correct state.

The key is having clear criteria for when this level of intervention is justified and transparent communication to users about what happened and why the intervention was necessary.

### Level 4: Trading Halt with Manual Review

The most aggressive intervention is completely halting trading and requiring manual review before resuming. This is appropriate when the system cannot automatically determine the correct response or when multiple indicators suggest serious system-wide issues.

During a trading halt, all new orders are rejected, existing orders may be canceled, and positions are frozen at their current state. Operations teams investigate the root cause, determine whether the issue stems from internal system problems versus external market conditions, and implement corrections before allowing trading to resume.

Trading halts should be rare because they represent acknowledgment that the automated systems cannot safely manage the situation. However, having this capability is essential for handling truly aberrant situations.

## Implementation Approach

Implementing price protection requires careful monitoring infrastructure and decision logic. The system must continuously track external reference prices from multiple sources, compute median prices with outlier filtering, and calculate deviation metrics comparing internal execution prices to external references.

When deviation thresholds are exceeded, the system must automatically enact the appropriate response level. This automation is critical because requiring manual intervention introduces dangerous delays. Markets can move rapidly and delayed response can turn a small problem into a large one.

However, automation requires sophisticated monitoring and alerting. Operations teams must be immediately notified when any protection mechanism activates. They need clear dashboards showing current deviation metrics, which protection levels are active, and historical patterns. Post-incident analysis is essential to tune thresholds and ensure protection mechanisms balance safety against trading disruption.

## Real-World Considerations

In practice, price protection mechanisms occasionally trigger false positives that create user complaints. A legitimate rapid price movement might trigger protection as deviation increases before external reference prices update. Building user trust requires transparency about why protection mechanisms exist and clear communication when they activate.

I recommend including price protection policies in user documentation explaining the thresholds, what protections may activate during abnormal conditions, and why these protections exist to safeguard user interests. When protection activates, immediate notification through the user interface and client notifications explains what happened and when normal trading is expected to resume.

The goal is creating a trading environment where users trust that the exchange will protect them from abnormal situations rather than allowing system issues or manipulation to cause losses. Well-designed and clearly communicated price protection mechanisms enhance rather than damage user confidence.
