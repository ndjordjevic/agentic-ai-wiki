# massive.com

## Fetch log
- Inbox URL: https://massive.com/
- Final URL: https://massive.com/
- Fetched: 2026-10-15
- Pages: 10
- Mode: standard
- Notes: https://massive.com/llms.txt redirects to https://massive.com/docs/llms.txt. Landing page and mcp.massive.com captured via Jina Reader; docs pages fetched as Markdown (`.md` suffix). No github.com repo URL appears in llms.txt or the landing page, so no companion repo was fetched (docs pages reference massive-com/mcp_massive and massive-com/client-* repos).

## llms.txt — https://massive.com/docs/llms.txt
# Massive

> Massive provides financial market data for stocks, options, indices, futures, forex, and crypto through a REST API, WebSocket streams, and S3 flat files.

## Getting started

Massive needs an API key. If the user doesn't have one (or you get a 401),
give them the signup link to register themselves:
https://massive.com/dashboard/signup

Their key is at https://massive.com/dashboard/keys. Have the user put it in the
MASSIVE_API_KEY env var and read it from there; don't ask them to paste
the key into chat or hardcode it.

## AI Tools

Connect AI agents and assistants to Massive data.

- [Massive MCP server](https://mcp.massive.com/): Remote server for MCP clients. The user signs in over OAuth, with nothing to install
- [ChatGPT Setup](https://massive.com/docs/ai-tools/clients/chatgpt.md): Connect Massive to ChatGPT
- [Claude Code Setup](https://massive.com/docs/ai-tools/clients/claude-code.md): Connect Massive to Claude Code
- [Claude Desktop Setup](https://massive.com/docs/ai-tools/clients/claude-desktop.md): Connect Massive to Claude Desktop
- [Codex Setup](https://massive.com/docs/ai-tools/clients/codex.md): Connect Massive to Codex
- [Cursor Setup](https://massive.com/docs/ai-tools/clients/cursor.md): Connect Massive to Cursor
- [Gemini CLI Setup](https://massive.com/docs/ai-tools/clients/gemini-cli.md): Connect Massive to Gemini CLI
- [GitHub Copilot Setup](https://massive.com/docs/ai-tools/clients/github-copilot.md): Connect Massive to GitHub Copilot
- [Grok Setup](https://massive.com/docs/ai-tools/clients/grok.md): Connect Massive to Grok
- [AI Tools Quickstart](https://massive.com/docs/ai-tools/quickstart.md): AI Tools Quickstart Guide
- [x402 Payments](https://massive.com/docs/ai-tools/x402.md): Buy US stock data per request over the x402 protocol, with no Massive account

## Flat Files

Bulk historical market data, delivered as daily files over S3.

- [Day Aggregates](https://massive.com/docs/flat-files/crypto/day-aggregates.md): Candlesticks with open, high, low, close, and volume at per day granularity across an expansive set of crypto pairings as a daily downloadable S3 file
- [Minute Aggregates](https://massive.com/docs/flat-files/crypto/minute-aggregates.md): Candlesticks with open, high, low, close, and volume at per minute granularity across an expansive set of crypto pairings as a daily downloadable S3 file
- [Crypto Overview](https://massive.com/docs/flat-files/crypto/overview.md): Massive provides comprehensive historical cryptocurrency market data through downloadable CSV Flat Files
- [Trades](https://massive.com/docs/flat-files/crypto/trades.md): Tick-level trades with nanosecond timestamps across an expansive set of crypto pairings, made available as a daily downloadable S3 file
- [Day Aggregates](https://massive.com/docs/flat-files/forex/day-aggregates.md): Candlesticks with open, high, low, close, and volume at per day granularity for over 1,750+ currency pairs, made available as a daily downloadable S3 file
- [Minute Aggregates](https://massive.com/docs/flat-files/forex/minute-aggregates.md): Candlesticks with open, high, low, close, and volume at per minute granularity for over 1,750+ currency pairs, made available as a daily downloadable S3 file
- [Forex Overview](https://massive.com/docs/flat-files/forex/overview.md): Massive provides extensive historical forex market data via downloadable CSV Flat Files
- [Quotes](https://massive.com/docs/flat-files/forex/quotes.md): Global foreign exchange rate quotes from major institutions for over 1,750+ currency pairs, made available as a daily downloadable S3 file
- [Minute Aggregates - CBOT](https://massive.com/docs/flat-files/futures/minute-aggregates/cbot.md): Candlestick data for CBOT futures with minute-by-minute open, high, low, close, and volume aggregated from all trades
- [Minute Aggregates - CME](https://massive.com/docs/flat-files/futures/minute-aggregates/cme.md): Candlestick data for CME futures with minute-by-minute open, high, low, close, and volume aggregated from all trades
- [Minute Aggregates - COMEX](https://massive.com/docs/flat-files/futures/minute-aggregates/comex.md): Candlestick data for COMEX futures with minute-by-minute open, high, low, close, and volume aggregated from all trades
- [Minute Aggregates - NYMEX](https://massive.com/docs/flat-files/futures/minute-aggregates/nymex.md): Candlestick data for NYMEX futures with minute-by-minute open, high, low, close, and volume aggregated from all trades
- [Futures Overview](https://massive.com/docs/flat-files/futures/overview.md): Massive provides comprehensive historical U.S. futures market data through downloadable CSV Flat Files
- [Quotes Aggregates - CBOT](https://massive.com/docs/flat-files/futures/quotes/cbot.md): Top-of-book quotes with nanosecond timestamps for CBOT futures, delivered as a daily downloadable S3 file
- [Quotes Aggregates - CME](https://massive.com/docs/flat-files/futures/quotes/cme.md): Top-of-book quotes with nanosecond timestamps for CME futures, delivered as a daily downloadable S3 file
- [Quotes Aggregates - COMEX](https://massive.com/docs/flat-files/futures/quotes/comex.md): Top-of-book quotes with nanosecond timestamps for COMEX futures, delivered as a daily downloadable S3 file
- [Quotes Aggregates - NYMEX](https://massive.com/docs/flat-files/futures/quotes/nymex.md): Top-of-book quotes with nanosecond timestamps for NYMEX futures, delivered as a daily downloadable S3 file
- [Session Aggregates - CBOT](https://massive.com/docs/flat-files/futures/session-aggregates/cbot.md): Candlestick data for CBOT futures with open, high, low, close, and volume aggregated from all trades during each trading session
- [Session Aggregates - CME](https://massive.com/docs/flat-files/futures/session-aggregates/cme.md): Candlestick data for CME futures with open, high, low, close, and volume aggregated from all trades during each trading session
- [Session Aggregates - COMEX](https://massive.com/docs/flat-files/futures/session-aggregates/comex.md): Candlestick data for COMEX futures with open, high, low, close, and volume aggregated from all trades during each trading session
- [Session Aggregates - NYMEX](https://massive.com/docs/flat-files/futures/session-aggregates/nymex.md): Candlestick data for NYMEX futures with open, high, low, close, and volume aggregated from all trades during each trading session
- [Trades Aggregates - CBOT](https://massive.com/docs/flat-files/futures/trades/cbot.md): Tick-level trades with nanosecond timestamps for CBOT futures, delivered as a daily downloadable S3 file
- [Trades Aggregates - CME](https://massive.com/docs/flat-files/futures/trades/cme.md): Tick-level trades with nanosecond timestamps for CME futures, delivered as a daily downloadable S3 file
- [Trades Aggregates - COMEX](https://massive.com/docs/flat-files/futures/trades/comex.md): Tick-level trades with nanosecond timestamps for COMEX futures, delivered as a daily downloadable S3 file
- [Trades Aggregates - NYMEX](https://massive.com/docs/flat-files/futures/trades/nymex.md): Tick-level trades with nanosecond timestamps for NYMEX futures, delivered as a daily downloadable S3 file
- [Day Aggregates](https://massive.com/docs/flat-files/indices/day-aggregates.md): Candlestick data for a diverse set indices with daily open, high, low, and close values aggregated from all ticks throughout the day
- [Minute Aggregates](https://massive.com/docs/flat-files/indices/minute-aggregates.md): Candlestick data for a diverse set indices with minute-by-minute open, high, low, and close values aggregated from all ticks throughout the day
- [Indices Overview](https://massive.com/docs/flat-files/indices/overview.md): Massive provides extensive historical index market data through downloadable CSV Flat Files
- [Values](https://massive.com/docs/flat-files/indices/values.md): A daily record of tick-by-tick values for a comprehensive set of indices including S&P, Nasdaq, Dow Jones, and more as a daily downloadable S3 file
- [Day Aggregates](https://massive.com/docs/flat-files/options/day-aggregates.md): Candlesticks with open, high, low, close, and volume at per day granularity from all U.S. options markets, made available as a daily downloadable S3 file
- [Minute Aggregates](https://massive.com/docs/flat-files/options/minute-aggregates.md): Candlesticks with open, high, low, close, and volume at per minute granularity from all U.S. options markets, made available as a daily downloadable S3 file
- [Options Overview](https://massive.com/docs/flat-files/options/overview.md): Massive provides extensive historical U.S. options market data through downloadable CSV Flat Files
- [Quotes](https://massive.com/docs/flat-files/options/quotes.md): Top of book quotes with nanosecond timestamps from all U.S. options markets including CBOE, NYSE, and NASDAQ, made available as a daily downloadable S3 file
- [Trades](https://massive.com/docs/flat-files/options/trades.md): Tick-level trades with nanosecond timestamps from all U.S. options markets including CBOE, NYSE, and NASDAQ, made available as a daily downloadable S3 file
- [Flat Files Quickstart](https://massive.com/docs/flat-files/quickstart.md): Flat Files Quickstart Guide
- [Day Aggregates](https://massive.com/docs/flat-files/stocks/day-aggregates.md): Candlesticks with open, high, low, close, and volume at per-day granularity across all U.S. equities, made available as a daily downloadable S3 file
- [Minute Aggregates](https://massive.com/docs/flat-files/stocks/minute-aggregates.md): Candlesticks with open, high, low, close, and volume at per minute granularity across all U.S. equities, made available as a daily downloadable S3 file
- [Stocks Overview](https://massive.com/docs/flat-files/stocks/overview.md): Massive provides comprehensive historical U.S. stock market data through downloadable CSV flat files
- [Quotes](https://massive.com/docs/flat-files/stocks/quotes.md): Top of book quotes with nanosecond timestamps from all major U.S. exchanges and darkpools, including NYSE, Nasdaq, Cboe, Finra, and more, made available as a daily downloadable S3 file
- [Trades](https://massive.com/docs/flat-files/stocks/trades.md): Tick level nanosecond timestamped trade data from all major U.S. exchanges and darkpools including NYSE, Nasdaq, Cboe, Finra, and more, made available as a daily downloadable S3 file

## REST API

REST endpoints for market data, reference data and other financial data sets.

- [Merchant Aggregates](https://massive.com/docs/rest/alternative/consumer-spending/merchant-aggregates.md): Aggregated European consumer spending data powered by [Fable Data](https://www.fabledata.com/)
- [Merchant Hierarchy](https://massive.com/docs/rest/alternative/consumer-spending/merchant-hierarchy.md): Reference data mapping merchants to parent companies, tickers, sectors, and industries across Fable's European consumer transaction panel
- [Alternative Data Overview](https://massive.com/docs/rest/alternative/overview.md): Access alternative datasets through our REST API
- [Custom Bars (OHLC)](https://massive.com/docs/rest/crypto/aggregates/custom-bars.md): Retrieve aggregated historical OHLC (Open, High, Low, Close) and volume data for a specified cryptocurrency pair over a custom date range and time interval in Coordinated Universal Time (UTC)
- [Daily Market Summary (OHLC)](https://massive.com/docs/rest/crypto/aggregates/daily-market-summary.md): Retrieve daily OHLC (open, high, low, close), volume, and volume-weighted average price (VWAP) data for all crypto tickers on a specified trading date
- [Daily Ticker Summary (OHLC)](https://massive.com/docs/rest/crypto/aggregates/daily-ticker-summary.md): Retrieve the opening and closing trades for a specific crypto pair on a given date
- [Previous Day Bar (OHLC)](https://massive.com/docs/rest/crypto/aggregates/previous-day-bar.md): Retrieve the previous trading day's open, high, low, and close (OHLC) data for a specified cryptocurrency pair
- [Condition Codes](https://massive.com/docs/rest/crypto/market-operations/condition-codes.md): Retrieve a unified and comprehensive list of trade and quote conditions from various upstream market data providers (e.g., CTA, UTP, OPRA, FINRA)
- [Exchanges](https://massive.com/docs/rest/crypto/market-operations/exchanges.md): Retrieve a list of known exchanges, including their identifiers, names, market types, and other relevant attributes
- [Market Holidays](https://massive.com/docs/rest/crypto/market-operations/market-holidays.md): Retrieve upcoming market holidays and their corresponding open/close times
- [Market Status](https://massive.com/docs/rest/crypto/market-operations/market-status.md): Retrieve the current trading status for various exchanges and overall financial markets
- [Crypto Overview](https://massive.com/docs/rest/crypto/overview.md): At Massive, we provide a comprehensive suite of cryptocurrency market data through standardized and intuitive APIs, offering extensive coverage of the global digital asset landscape
- [Full Market Snapshot](https://massive.com/docs/rest/crypto/snapshots/full-market-snapshot.md): Retrieve a comprehensive snapshot of the crypto market in a single response
- [Single Ticker Snapshot](https://massive.com/docs/rest/crypto/snapshots/single-ticker-snapshot.md): Retrieve the most recent market data snapshot for a single ticker
- [Top Market Movers](https://massive.com/docs/rest/crypto/snapshots/top-market-movers.md): Retrieve snapshot data highlighting the top 20 gainers or losers in the crypto market
- [Unified Snapshot](https://massive.com/docs/rest/crypto/snapshots/unified-snapshot.md): Retrieve unified snapshots of market data for multiple asset classes including stocks, options, forex, and cryptocurrencies in a single request
- [Exponential Moving Average (EMA)](https://massive.com/docs/rest/crypto/technical-indicators/exponential-moving-average.md): Retrieve the Exponential Moving Average (EMA) for a specified ticker over a defined time range
- [Moving Average Convergence/Divergence (MACD)](https://massive.com/docs/rest/crypto/technical-indicators/moving-average-convergence-divergence.md): Retrieve the Moving Average Convergence/Divergence (MACD) for a specified ticker over a defined time range
- [Relative Strength Index (RSI)](https://massive.com/docs/rest/crypto/technical-indicators/relative-strength-index.md): Retrieve the Relative Strength Index (RSI) for a specified ticker over a defined time range
- [Simple Moving Average (SMA)](https://massive.com/docs/rest/crypto/technical-indicators/simple-moving-average.md): Retrieve the Simple Moving Average (SMA) for a specified ticker over a defined time range
- [All Tickers](https://massive.com/docs/rest/crypto/tickers/all-tickers.md): Retrieve a comprehensive list of ticker symbols supported by Massive across various asset classes (e.g., stocks, indices, forex, crypto)
- [Ticker Overview](https://massive.com/docs/rest/crypto/tickers/ticker-overview.md): Retrieve comprehensive details for a single ticker supported by Massive that is active as-of a given date
- [Last Trade](https://massive.com/docs/rest/crypto/trades/last-trade.md): Retrieve the most recent trade details for a specified cryptocurrency pair, including price, size, timestamp, exchange, and conditions
- [Trades](https://massive.com/docs/rest/crypto/trades/trades.md): Retrieve comprehensive, tick-level trade data for a specified crypto ticker within a defined time range
- [Funding Conditions](https://massive.com/docs/rest/economy/funding-conditions.md): Daily U.S. overnight funding snapshot — one row per day showing how cheap or tight it is for banks and dealers to borrow cash overnight
- [Inflation](https://massive.com/docs/rest/economy/inflation.md): Retrieve key indicators of realized inflation, reflecting actual changes in consumer prices and spending behavior in the U.S. economy
- [Inflation Expectations](https://massive.com/docs/rest/economy/inflation-expectations.md): Retrieve a broad view of how inflation is expected to evolve over time in the U.S. economy
- [Labor Market](https://massive.com/docs/rest/economy/labor-market.md): Retrieve key labor market indicators from the Federal Reserve, including unemployment rate, labor force participation, average hourly earnings, and job openings data
- [Economy Overview](https://massive.com/docs/rest/economy/overview.md): Access macroeconomic data from the Federal Reserve and other official sources through our REST API
- [Treasury Yields](https://massive.com/docs/rest/economy/treasury-yields.md): Retrieve historical U.S. Treasury yield data for standard timeframes ranging from 1-month to 30-years, with daily historical records back to 1962
- [Custom Bars (OHLC)](https://massive.com/docs/rest/forex/aggregates/custom-bars.md): Retrieve aggregated historical OHLC (Open, High, Low, Close) and volume data for a specified Forex currency pair over a custom date range and time interval in Coordinated Universal Time (UTC)
- [Daily Market Summary (OHLC)](https://massive.com/docs/rest/forex/aggregates/daily-market-summary.md): Retrieve daily OHLC (open, high, low, close), volume, and volume-weighted average price (VWAP) data for all forex tickers on a specified trading date
- [Previous Day Bar (OHLC)](https://massive.com/docs/rest/forex/aggregates/previous-day-bar.md): Retrieve the previous trading day's open, high, low, and close (OHLC) data for a specified forex pair
- [Currency Conversion](https://massive.com/docs/rest/forex/currency-conversion.md): Retrieve real-time currency conversion rates between any two supported currencies
- [Exchanges](https://massive.com/docs/rest/forex/market-operations/exchanges.md): Retrieve a list of known exchanges, including their identifiers, names, market types, and other relevant attributes
- [Market Holidays](https://massive.com/docs/rest/forex/market-operations/market-holidays.md): Retrieve upcoming market holidays and their corresponding open/close times
- [Market Status](https://massive.com/docs/rest/forex/market-operations/market-status.md): Retrieve the current trading status for various exchanges and overall financial markets
- [Forex Overview](https://massive.com/docs/rest/forex/overview.md): At Massive, we offer a comprehensive suite of foreign exchange (forex) market data through standardized and intuitive APIs
- [Last Quote](https://massive.com/docs/rest/forex/quotes/last-quote.md): Retrieve the most recent quote for a specified forex currency pair, including bid, ask, exchange, and timestamp
- [Quotes](https://massive.com/docs/rest/forex/quotes/quotes.md): Retrieve historical Best Bid and Offer (BBO) quotes for a specified forex currency pair over a defined time range
- [Full Market Snapshot](https://massive.com/docs/rest/forex/snapshots/full-market-snapshot.md): Retrieve a comprehensive snapshot of the forex market in a single response
- [Single Ticker Snapshot](https://massive.com/docs/rest/forex/snapshots/single-ticker-snapshot.md): Retrieve the most recent market data snapshot for a single ticker
- [Top Market Movers](https://massive.com/docs/rest/forex/snapshots/top-market-movers.md): Retrieve snapshot data highlighting the top 20 gainers or losers in the forex market
- [Unified Snapshot](https://massive.com/docs/rest/forex/snapshots/unified-snapshot.md): Retrieve unified snapshots of market data for multiple asset classes including stocks, options, forex, and cryptocurrencies in a single request
- [Exponential Moving Average (EMA)](https://massive.com/docs/rest/forex/technical-indicators/exponential-moving-average.md): Retrieve the Exponential Moving Average (EMA) for a specified ticker over a defined time range
- [Moving Average Convergence/Divergence (MACD)](https://massive.com/docs/rest/forex/technical-indicators/moving-average-convergence-divergence.md): Retrieve the Moving Average Convergence/Divergence (MACD) for a specified ticker over a defined time range
- [Relative Strength Index (RSI)](https://massive.com/docs/rest/forex/technical-indicators/relative-strength-index.md): Retrieve the Relative Strength Index (RSI) for a specified ticker over a defined time range
- [Simple Moving Average (SMA)](https://massive.com/docs/rest/forex/technical-indicators/simple-moving-average.md): Retrieve the Simple Moving Average (SMA) for a specified ticker over a defined time range
- [All Tickers](https://massive.com/docs/rest/forex/tickers/all-tickers.md): Retrieve a comprehensive list of ticker symbols supported by Massive across various asset classes (e.g., stocks, indices, forex, crypto)
- [Ticker Overview](https://massive.com/docs/rest/forex/tickers/ticker-overview.md): Retrieve comprehensive details for a single ticker supported by Massive that is active as-of a given date
- [Ticker Types](https://massive.com/docs/rest/forex/tickers/ticker-types.md): Retrieve a list of all ticker types supported by Massive
- [Aggregate Bars (OHLC)](https://massive.com/docs/rest/futures/aggregates.md): Retrieve historical OHLC (open, high, low, close) and volume bars for a futures contract over a date range
- [Contracts](https://massive.com/docs/rest/futures/contracts.md)
- [Exchanges](https://massive.com/docs/rest/futures/market-operations/exchanges.md): Retrieve a list of supported futures exchanges, including their unique exchange codes, names, and other important details
- [Market Status](https://massive.com/docs/rest/futures/market-operations/market-status.md)
- [Futures Overview](https://massive.com/docs/rest/futures/overview.md): Explore comprehensive U.S. futures market data through Massive's REST APIs.
- [Products](https://massive.com/docs/rest/futures/products.md)
- [Schedules](https://massive.com/docs/rest/futures/schedules.md): The Schedules API provides a unified way to retrieve trading schedules for futures markets, returning precise session open and close times, intraday breaks, and any adjustments for holidays or special events
- [Futures Contracts Snapshot](https://massive.com/docs/rest/futures/snapshots/contracts-snapshot.md): Retrieve real-time snapshots for a set of futures contracts, including key market data such as the latest trade, quote, session metrics (open, high, low, close, volume), and settlement prices
- [Quotes](https://massive.com/docs/rest/futures/trades-quotes/quotes.md): Retrieve quote data for a specified futures contract ticker
- [Trades](https://massive.com/docs/rest/futures/trades-quotes/trades.md): Retrieve comprehensive, tick-level trade data for a specified futures contract ticker over a defined time range
- [Custom Bars (OHLC)](https://massive.com/docs/rest/indices/aggregates/custom-bars.md): Retrieve aggregated historical OHLC (Open, High, Low, Close) and value data for a specified index over a custom date range and time interval in Eastern Time (ET)
- [Daily Ticker Summary (OHLC)](https://massive.com/docs/rest/indices/aggregates/daily-ticker-summary.md): Retrieve the opening and closing prices for a specific index on a given date, along with any pre-market and after-hours trade prices
- [Previous Day Bar (OHLC)](https://massive.com/docs/rest/indices/aggregates/previous-day-bar.md): Retrieve the previous trading day's open, high, low, and close (OHLC) data for a specified index ticker
- [Market Holidays](https://massive.com/docs/rest/indices/market-operations/market-holidays.md): Retrieve upcoming market holidays and their corresponding open/close times
- [Market Status](https://massive.com/docs/rest/indices/market-operations/market-status.md): Retrieve the current trading status for various exchanges and overall financial markets
- [Indices Overview](https://massive.com/docs/rest/indices/overview.md): At Massive, we provide a comprehensive suite of market data for over 10,000+ indices from multiple index families, including S&P, Nasdaq, Dow Jones, and more
- [Indices Snapshot](https://massive.com/docs/rest/indices/snapshots/indices-snapshot.md): Retrieve snapshot data for one or more indices, including their current value, recent performance metrics, and trading session details
- [Unified Snapshot](https://massive.com/docs/rest/indices/snapshots/unified-snapshot.md): Retrieve unified snapshots of market data for multiple asset classes including stocks, options, forex, and cryptocurrencies in a single request
- [Exponential Moving Average (EMA)](https://massive.com/docs/rest/indices/technical-indicators/exponential-moving-average.md): Retrieve the Exponential Moving Average (EMA) for a specified ticker over a defined time range
- [Moving Average Convergence/Divergence (MACD)](https://massive.com/docs/rest/indices/technical-indicators/moving-average-convergence-divergence.md): Retrieve the Moving Average Convergence/Divergence (MACD) for a specified ticker over a defined time range
- [Relative Strength Index (RSI)](https://massive.com/docs/rest/indices/technical-indicators/relative-strength-index.md): Retrieve the Relative Strength Index (RSI) for a specified ticker over a defined time range
- [Simple Moving Average (SMA)](https://massive.com/docs/rest/indices/technical-indicators/simple-moving-average.md): Retrieve the Simple Moving Average (SMA) for a specified ticker over a defined time range
- [All Tickers](https://massive.com/docs/rest/indices/tickers/all-tickers.md): Retrieve a comprehensive list of ticker symbols supported by Massive across various asset classes (e.g., stocks, indices, forex, crypto)
- [Ticker Overview](https://massive.com/docs/rest/indices/tickers/ticker-overview.md): Retrieve comprehensive details for a single ticker supported by Massive that is active as-of a given date
- [Custom Bars (OHLC)](https://massive.com/docs/rest/options/aggregates/custom-bars.md): Retrieve aggregated historical OHLC (Open, High, Low, Close) and volume data for a specified options contract over a custom date range and time interval in Eastern Time (ET)
- [Daily Ticker Summary (OHLC)](https://massive.com/docs/rest/options/aggregates/daily-ticker-summary.md): Retrieve the opening and closing prices for a specific options contract on a given date, along with any pre-market and after-hours trade prices
- [Previous Day Bar (OHLC)](https://massive.com/docs/rest/options/aggregates/previous-day-bar.md): Retrieve the previous trading day's open, high, low, and close (OHLC) data for a specified option contract
- [All Contracts](https://massive.com/docs/rest/options/contracts/all-contracts.md): Retrieve a comprehensive index of options contracts, encompassing both active and expired listings
- [Contract Overview](https://massive.com/docs/rest/options/contracts/contract-overview.md): Retrieve detailed information about a specific options contract, including its contract type (call or put), exercise style, expiration date, strike price, shares per contract, underlying ticker, and primary exchange
- [Condition Codes](https://massive.com/docs/rest/options/market-operations/condition-codes.md): Retrieve a unified and comprehensive list of trade and quote conditions from various upstream market data providers (e.g., CTA, UTP, OPRA, FINRA)
- [Exchanges](https://massive.com/docs/rest/options/market-operations/exchanges.md): Retrieve a list of known exchanges, including their identifiers, names, market types, and other relevant attributes
- [Market Holidays](https://massive.com/docs/rest/options/market-operations/market-holidays.md): Retrieve upcoming market holidays and their corresponding open/close times
- [Market Status](https://massive.com/docs/rest/options/market-operations/market-status.md): Retrieve the current trading status for various exchanges and overall financial markets
- [Options Overview](https://massive.com/docs/rest/options/overview.md): At Massive, we offer a comprehensive suite of U.S. options market data through standardized and intuitive APIs
- [Option Chain Snapshot](https://massive.com/docs/rest/options/snapshots/option-chain-snapshot.md): Retrieve a comprehensive snapshot of all options contracts associated with a specified underlying ticker
- [Option Contract Snapshot](https://massive.com/docs/rest/options/snapshots/option-contract-snapshot.md): Retrieve a comprehensive snapshot of a specified options contract, consolidating vital metrics and market data into a single response
- [Unified Snapshot](https://massive.com/docs/rest/options/snapshots/unified-snapshot.md): Retrieve unified snapshots of market data for multiple asset classes including stocks, options, forex, and cryptocurrencies in a single request
- [Exponential Moving Average (EMA)](https://massive.com/docs/rest/options/technical-indicators/exponential-moving-average.md): Retrieve the Exponential Moving Average (EMA) for a specified ticker over a defined time range
- [Moving Average Convergence/Divergence (MACD)](https://massive.com/docs/rest/options/technical-indicators/moving-average-convergence-divergence.md): Retrieve the Moving Average Convergence/Divergence (MACD) for a specified ticker over a defined time range
- [Relative Strength Index (RSI)](https://massive.com/docs/rest/options/technical-indicators/relative-strength-index.md): Retrieve the Relative Strength Index (RSI) for a specified ticker over a defined time range
- [Simple Moving Average (SMA)](https://massive.com/docs/rest/options/technical-indicators/simple-moving-average.md): Retrieve the Simple Moving Average (SMA) for a specified ticker over a defined time range
- [Last Trade](https://massive.com/docs/rest/options/trades-quotes/last-trade.md): Retrieve the latest available trade for a specified options contact, including details such as price, size, exchange, and timestamp
- [Quotes](https://massive.com/docs/rest/options/trades-quotes/quotes.md): Retrieve historical quotes for a specified options contract over a defined time range
- [Trades](https://massive.com/docs/rest/options/trades-quotes/trades.md): Retrieve comprehensive, tick-level trade data for a specified options ticker within a defined time range
- [Analyst Details](https://massive.com/docs/rest/partners/benzinga/analyst-details.md): Retrieve structured data on financial analysts, including names, affiliated firms, and historical rating activity
- [Analyst Insights](https://massive.com/docs/rest/partners/benzinga/analyst-insights.md): Retrieve insights from financial analysts, including ratings, price targets, and the rationale behind their recommendations
- [Analyst Ratings](https://massive.com/docs/rest/partners/benzinga/analyst-ratings.md): Retrieve structured historical analyst ratings, including rating actions, price target changes, and firm names for publicly traded companies
- [Bulls Bears Say](https://massive.com/docs/rest/partners/benzinga/bulls-bears-say.md): A comprehensive database of analyst bull and bear case summaries for publicly traded companies, providing concise summaries of both bullish and bearish investment arguments to help investors see both sides of the story before making investment decisions
- [Consensus Ratings](https://massive.com/docs/rest/partners/benzinga/consensus-ratings.md): Retrieve consensus ratings from financial analysts, including aggregated rating distributions and price target ranges
- [Corporate Guidance](https://massive.com/docs/rest/partners/benzinga/corporate-guidance.md): Retrieve structured earnings guidance data, including projected EPS and revenue figures, from public company disclosures
- [Earnings](https://massive.com/docs/rest/partners/benzinga/earnings.md): Retrieve structured historical and upcoming earnings announcements for publicly traded companies, including key metrics such as earnings per share (EPS), revenue, and analyst estimates
- [Firm Details](https://massive.com/docs/rest/partners/benzinga/firm-details.md): Retrieve structured data on analyst firms, including firm names and identifiers
- [Real-time Benzinga News](https://massive.com/docs/rest/partners/benzinga/news.md): Retrieve real-time structured, timestamped news articles from Benzinga, including headlines, full-text content, tickers, categories, and more
- [ETF Analytics](https://massive.com/docs/rest/partners/etf-global/analytics.md): Retrieve analytical metrics and calculated insights for U.S. listed ETFs including performance data, risk measures, and derived analytics
- [ETF Constituents](https://massive.com/docs/rest/partners/etf-global/constituents.md): Retrieve the underlying holdings and constituents of U.S. listed ETFs
- [ETF Fund Flows](https://massive.com/docs/rest/partners/etf-global/fundflows.md): Retrieve capital movement and investor activity data across U.S. listed ETFs
- [ETF Profiles & Exposure](https://massive.com/docs/rest/partners/etf-global/profiles.md): Retrieve industry classification data for U.S. listed ETFs including sector mappings and standardized categorizations across industry frameworks
- [ETF Taxonomies](https://massive.com/docs/rest/partners/etf-global/taxonomies.md): Retrieve standardized taxonomy systems used to categorize and organize U.S. listed ETFs
- [Partners Overview](https://massive.com/docs/rest/partners/overview.md): Access premium third-party data through our Partner integrations
- [Corporate Events](https://massive.com/docs/rest/partners/tmx/corporate-events.md): Retrieve structured corporate event data from Wall Street Horizon's comprehensive global events calendar, including earnings announcements, dividend dates, investor conferences, and stock splits
- [REST Quickstart](https://massive.com/docs/rest/quickstart.md): REST API Quickstart Guide
- [Custom Bars (OHLC)](https://massive.com/docs/rest/stocks/aggregates/custom-bars.md): Retrieve aggregated historical OHLC (Open, High, Low, Close) and volume data for a specified stock ticker over a custom date range and time interval in Eastern Time (ET)
- [Daily Market Summary (OHLC)](https://massive.com/docs/rest/stocks/aggregates/daily-market-summary.md): Retrieve daily OHLC (open, high, low, close), volume, and volume-weighted average price (VWAP) data for all U.S. stocks on a specified trading date
- [Daily Ticker Summary (OHLC)](https://massive.com/docs/rest/stocks/aggregates/daily-ticker-summary.md): Retrieve the opening and closing prices for a specific stock ticker on a given date, along with any pre-market and after-hours trade prices
- [Previous Day Bar (OHLC)](https://massive.com/docs/rest/stocks/aggregates/previous-day-bar.md): Retrieve the previous trading day's open, high, low, and close (OHLC) data for a specified stock ticker
- [Dividends](https://massive.com/docs/rest/stocks/corporate-actions/dividends.md): Retrieve a historical record of cash dividend distributions for a given ticker, including declaration, ex-dividend, record, and pay dates, as well as payout amounts and adjustment factors for normalizing historical data to offset the effects of dividends
- [Initial Public Offerings (IPOs)](https://massive.com/docs/rest/stocks/corporate-actions/ipos.md): Retrieve comprehensive information on Initial Public Offerings (IPOs), including upcoming and historical events, starting from the year 2008
- [Dividends (Deprecated)](https://massive.com/docs/rest/stocks/corporate-actions/reference-dividends.md): Retrieve a historical record of cash dividend distributions for a given ticker, including declaration, ex-dividend, record, and pay dates, as well as payout amounts and frequency
- [Splits (Deprecated)](https://massive.com/docs/rest/stocks/corporate-actions/reference-splits.md): Retrieve historical stock split events, including execution dates and ratio factors, to understand changes in a company’s share structure over time
- [Splits](https://massive.com/docs/rest/stocks/corporate-actions/splits.md): Retrieve historical stock split events, including execution dates and ratio factors, to understand changes in a company’s share structure over time
- [Ticker Events](https://massive.com/docs/rest/stocks/corporate-actions/ticker-events.md): Retrieve a timeline of key events associated with a given ticker, CUSIP, or Composite FIGI
- [Annual Report Sections (10-K)](https://massive.com/docs/rest/stocks/filings/10-k-sections.md): Retrieve clean plain-text extracts of key narrative sections from annual 10-K filings, including Business and Risk Factors
- [Institutional Holdings (13-F)](https://massive.com/docs/rest/stocks/filings/13-f-filings.md): Retrieve quarterly holdings data from SEC Form 13-F filings submitted by institutional investment managers with at least $100 million in assets
- [Material Event Disclosures (8-K)](https://massive.com/docs/rest/stocks/filings/8-k-disclosures.md): SEC 8-K filing disclosure categorization
- [Material Event Text (8-K)](https://massive.com/docs/rest/stocks/filings/8-k-text.md): Retrieve parsed plain-text content from the core Items sections of Form 8-K current reports
- [Disclosure Categories](https://massive.com/docs/rest/stocks/filings/disclosure-categories.md): Access the full standardized hierarchical taxonomy used to classify disclosures in SEC Form 8-K filings
- [Initial Insider Ownership (Form 3)](https://massive.com/docs/rest/stocks/filings/form-3.md): Retrieve SEC Form 3 filings that report the initial beneficial ownership of securities by corporate insiders (directors, officers, and 10%+ shareholders)
- [Insider Transactions (Form 4)](https://massive.com/docs/rest/stocks/filings/form-4.md): Retrieve SEC Form 4 filings that disclose all changes in beneficial ownership by corporate insiders
- [SEC EDGAR Index](https://massive.com/docs/rest/stocks/filings/index.md): Retrieve the master index of all SEC EDGAR filings, including form types, filing dates, CIKs, tickers, issuer names, accession numbers, and direct links to original documents on SEC.gov
- [Risk Categories](https://massive.com/docs/rest/stocks/filings/risk-categories.md): Access the full standardized hierarchical taxonomy used to classify risk factors in SEC filings
- [Risk Factors](https://massive.com/docs/rest/stocks/filings/risk-factors.md): Standardized, machine-readable risk factor disclosures from SEC filings
- [Balance Sheets](https://massive.com/docs/rest/stocks/fundamentals/balance-sheets.md): Retrieve comprehensive balance sheet data for public companies, containing quarterly and annual financial positions
- [Cash Flow Statements](https://massive.com/docs/rest/stocks/fundamentals/cash-flow-statements.md): Retrieve comprehensive cash flow statement data for public companies, including quarterly, annual, and trailing twelve-month cash flows
- [Float](https://massive.com/docs/rest/stocks/fundamentals/float.md): Retrieve the latest free float for a specified stock ticker
- [Income Statements](https://massive.com/docs/rest/stocks/fundamentals/income-statements.md): Retrieve comprehensive income statement data for public companies, including key metrics such as revenue, expenses, and net income for various reporting periods
- [Ratios](https://massive.com/docs/rest/stocks/fundamentals/ratios.md): Retrieve comprehensive financial ratios data providing key valuation, profitability, liquidity, and leverage metrics for public companies
- [Short Interest](https://massive.com/docs/rest/stocks/fundamentals/short-interest.md): Retrieve aggregated short interest data reported to FINRA by broker-dealers for a specified stock ticker on a two-week cadence
- [Short Volume](https://massive.com/docs/rest/stocks/fundamentals/short-volume.md): Retrieve daily aggregated short sale volume data reported to FINRA from off-exchange trading venues and alternative trading systems (ATS) for a specified stock ticker
- [Condition Codes](https://massive.com/docs/rest/stocks/market-operations/condition-codes.md): Retrieve a unified and comprehensive list of trade and quote conditions from various upstream market data providers (e.g., CTA, UTP, OPRA, FINRA)
- [Exchanges](https://massive.com/docs/rest/stocks/market-operations/exchanges.md): Retrieve a list of known exchanges, including their identifiers, names, market types, and other relevant attributes
- [Market Holidays](https://massive.com/docs/rest/stocks/market-operations/market-holidays.md): Retrieve upcoming market holidays and their corresponding open/close times
- [Market Status](https://massive.com/docs/rest/stocks/market-operations/market-status.md): Retrieve the current trading status for various exchanges and overall financial markets
- [News](https://massive.com/docs/rest/stocks/news.md): Retrieve the most recent news articles related to a specified ticker, along with summaries, source details, and sentiment analysis
- [Stocks Overview](https://massive.com/docs/rest/stocks/overview.md): At Massive, we provide a comprehensive suite of U.S. stock market data through a standardized and intuitive API, offering unparalleled coverage of the U.S. stock market landscape
- [Full Market Snapshot](https://massive.com/docs/rest/stocks/snapshots/full-market-snapshot.md): Retrieve a comprehensive snapshot of the entire U.S. stock market, covering over 10,000+ actively traded tickers in a single response
- [Single Ticker Snapshot](https://massive.com/docs/rest/stocks/snapshots/single-ticker-snapshot.md): Retrieve the most recent market data snapshot for a single ticker
- [Top Market Movers](https://massive.com/docs/rest/stocks/snapshots/top-market-movers.md): Retrieve snapshot data highlighting the top 20 gainers or losers in the U.S. stock market
- [Unified Snapshot](https://massive.com/docs/rest/stocks/snapshots/unified-snapshot.md): Retrieve unified snapshots of market data for multiple asset classes including stocks, options, forex, and cryptocurrencies in a single request
- [Exponential Moving Average (EMA)](https://massive.com/docs/rest/stocks/technical-indicators/exponential-moving-average.md): Retrieve the Exponential Moving Average (EMA) for a specified ticker over a defined time range
- [Moving Average Convergence/Divergence (MACD)](https://massive.com/docs/rest/stocks/technical-indicators/moving-average-convergence-divergence.md): Retrieve the Moving Average Convergence/Divergence (MACD) for a specified ticker over a defined time range
- [Relative Strength Index (RSI)](https://massive.com/docs/rest/stocks/technical-indicators/relative-strength-index.md): Retrieve the Relative Strength Index (RSI) for a specified ticker over a defined time range
- [Simple Moving Average (SMA)](https://massive.com/docs/rest/stocks/technical-indicators/simple-moving-average.md): Retrieve the Simple Moving Average (SMA) for a specified ticker over a defined time range
- [All Tickers](https://massive.com/docs/rest/stocks/tickers/all-tickers.md): Retrieve a comprehensive list of ticker symbols supported by Massive across various asset classes (e.g., stocks, indices, forex, crypto)
- [Related Tickers](https://massive.com/docs/rest/stocks/tickers/related-tickers.md): Retrieve a list of tickers related to a specified ticker, identified through an analysis of news coverage and returns data
- [Ticker Overview](https://massive.com/docs/rest/stocks/tickers/ticker-overview.md): Retrieve comprehensive details for a single ticker supported by Massive that is active as-of a given date
- [Ticker Types](https://massive.com/docs/rest/stocks/tickers/ticker-types.md): Retrieve a list of all ticker types supported by Massive
- [Last Quote](https://massive.com/docs/rest/stocks/trades-quotes/last-quote.md): Retrieve the most recent National Best Bid and Offer (NBBO) quote for a specified stock ticker, including the latest bid/ask prices, sizes, exchange details, and timestamp
- [Last Trade](https://massive.com/docs/rest/stocks/trades-quotes/last-trade.md): Retrieve the latest available trade for a specified stock ticker, including details such as price, size, exchange, and timestamp
- [Quotes](https://massive.com/docs/rest/stocks/trades-quotes/quotes.md): Retrieve National Best Bid and Offer (NBBO) quotes for a specified stock ticker over a defined time range
- [Trades](https://massive.com/docs/rest/stocks/trades-quotes/trades.md): Retrieve comprehensive, tick-level trade data for a specified stock ticker within a defined time range

## WebSocket

Streaming market data over WebSocket, pushed to the client as events arrive.

- [Aggregates (Per Minute)](https://massive.com/docs/websocket/crypto/aggregates-per-minute.md): Stream minute-by-minute aggregated OHLC (Open, High, Low, Close) and volume data for a specified cryptocurrency pair via WebSocket
- [Aggregates (Per Second)](https://massive.com/docs/websocket/crypto/aggregates-per-second.md): Stream second-by-second aggregated OHLC (Open, High, Low, Close) and volume data for a specified cryptocurrency pair via WebSocket
- [Fair Market Value](https://massive.com/docs/websocket/crypto/fair-market-value.md): Stream real-time Fair Market Value (FMV) data for a specified cryptocurrency pair via WebSocket
- [Crypto Overview](https://massive.com/docs/websocket/crypto/overview.md): At Massive, we provide real-time streaming access to the global cryptocurrency market through WebSockets
- [Quotes](https://massive.com/docs/websocket/crypto/quotes.md): Stream quote data for specified cryptocurrency pairs via WebSocket
- [Trades](https://massive.com/docs/websocket/crypto/trades.md): Stream trade data for crypto pairs via WebSocket
- [Aggregates (Per Minute)](https://massive.com/docs/websocket/forex/aggregates-per-minute.md): Stream minute-by-minute aggregated OHLC (Open, High, Low, Close) and volume data for a specified Forex currency pair via WebSocket
- [Aggregates (Per Second)](https://massive.com/docs/websocket/forex/aggregates-per-second.md): Stream second-by-second aggregated OHLC (Open, High, Low, Close) and volume data for a specified Forex currency pair via WebSocket
- [Fair Market Value](https://massive.com/docs/websocket/forex/fair-market-value.md): Stream real-time Fair Market Value (FMV) data for a specified Forex currency pair via WebSocket
- [Forex Overview](https://massive.com/docs/websocket/forex/overview.md): At Massive, we provide real-time streaming access to global foreign exchange (forex) market data through WebSockets
- [Quotes](https://massive.com/docs/websocket/forex/quotes.md): Stream real-time Best Bid and Offer (BBO) quote data for specified Forex currency pairs via WebSocket
- [Aggregates (Per Minute)](https://massive.com/docs/websocket/futures/aggregates-per-minute.md): Stream minute-by-minute aggregated OHLC (Open, High, Low, Close) and volume data for a specified futures contract ticker via WebSocket
- [Aggregates (Per Second)](https://massive.com/docs/websocket/futures/aggregates-per-second.md): Stream second-by-second aggregated OHLC (Open, High, Low, Close) and volume data for a specified futures contract ticker via WebSocket
- [Futures Overview](https://massive.com/docs/websocket/futures/overview.md): Explore comprehensive U.S. futures market data through Massive's WebSocket streams.
- [Quotes](https://massive.com/docs/websocket/futures/quotes.md): Stream BBO (Best Bid and Offer) quote data for futures tickers via WebSocket
- [Trades](https://massive.com/docs/websocket/futures/trades.md): Stream tick-level trade data for futures tickers via WebSocket
- [Aggregates (Per Minute)](https://massive.com/docs/websocket/indices/aggregates-per-minute.md): Stream minute-by-minute aggregated OHLC (Open, High, Low, Close) for a specified index via WebSocket
- [Aggregates (Per Second)](https://massive.com/docs/websocket/indices/aggregates-per-second.md): Stream second-by-second aggregated OHLC (Open, High, Low, Close) for a specified index via WebSocket
- [Indices Overview](https://massive.com/docs/websocket/indices/overview.md): At Massive, we provide real-time streaming access to index values and aggregates through WebSockets, enabling your applications to receive continuous updates directly as market conditions evolve
- [Value](https://massive.com/docs/websocket/indices/value.md): Stream real-time index value updates for specified index tickers via WebSocket
- [Aggregates (Per Minute)](https://massive.com/docs/websocket/options/aggregates-per-minute.md): Stream minute-by-minute aggregated OHLC (Open, High, Low, Close) and volume data for a specified options contract via WebSocket
- [Aggregates (Per Second)](https://massive.com/docs/websocket/options/aggregates-per-second.md): Stream second-by-second aggregated OHLC (Open, High, Low, Close) and volume data for a specified options contract via WebSocket
- [Fair Market Value](https://massive.com/docs/websocket/options/fair-market-value.md): Stream real-time Fair Market Value (FMV) data for a specified options contract via WebSocket
- [Options Overview](https://massive.com/docs/websocket/options/overview.md): At Massive, we provide real-time streaming access to U.S. options market data through WebSockets, allowing you to receive a continuous flow of updates directly into your applications
- [Quotes](https://massive.com/docs/websocket/options/quotes.md): Stream quote data for specified options contracts via WebSocket
- [Trades](https://massive.com/docs/websocket/options/trades.md): Stream tick-level trade data for option contracts via WebSocket
- [WebSocket Quickstart](https://massive.com/docs/websocket/quickstart.md): WebSocket API Quickstart Guide
- [Aggregates (Per Minute)](https://massive.com/docs/websocket/stocks/aggregates-per-minute.md): Stream minute-by-minute aggregated OHLC (Open, High, Low, Close) and volume data for specified tickers via WebSocket
- [Aggregates (Per Second)](https://massive.com/docs/websocket/stocks/aggregates-per-second.md): Stream second-by-second aggregated OHLC (Open, High, Low, Close) and volume data for specified tickers via WebSocket
- [Fair Market Value](https://massive.com/docs/websocket/stocks/fair-market-value.md): Stream real-time Fair Market Value (FMV) data for a specified stock ticker via WebSocket
- [Net Order Imbalance (NOI)](https://massive.com/docs/websocket/stocks/imbalances.md): Stream real-time Net Order Imbalance (NOI) events for specified stock tickers via WebSocket
- [Limit Up - Limit Down (LULD)](https://massive.com/docs/websocket/stocks/luld.md): Stream real-time Limit Up - Limit Down (LULD) events for specified stock tickers via WebSocket across multiple U.S. exchanges (including NYSE, Nasdaq, Cboe BZX, NYSE Arca, and NYSE American)
- [Stocks Overview](https://massive.com/docs/websocket/stocks/overview.md): At Massive, we provide real-time streaming access to U.S. stock market data through WebSockets, delivering a continuous flow of updates directly to your applications
- [Quotes](https://massive.com/docs/websocket/stocks/quotes.md): Stream NBBO (National Best Bid and Offer) quote data for stock tickers via WebSocket
- [Trades](https://massive.com/docs/websocket/stocks/trades.md): Stream tick-level trade data for stock tickers via WebSocket

## Landing page — https://massive.com/

[![Image 1: Massive Logo](https://massive.com/_next/image?url=%2Fbrands%2Flogo-massive.png&w=640&q=75)](https://massive.com/)

## Modernizing Wall St. one market at a time.

At Massive, we're on a mission to modernize the financial industry. We believe that the industry runs on old technology, and we're here to change that.

By developers for developers

## Made for builders, founders, scholars, dabblers, and dreamers

Rows of Data
0 Trillion+

Raw Data
0 Petabytes

Uptime
0%

Messages/sec
0 Million

Intuitive and easy-to-use

## Powerful data, simple access

Choose the data access method that suits your needs and get started today.

### Flat Files

Our S3 interface lets you access our flat files easily and seamlessly. With just a few clicks, you'll have the data you need to power your applications.

### API

Our Restful and WebSocket APIs provide flexible and powerful options for accessing our data. Whether you need real-time or historical data, we've got you covered.

### SQL

Our SQL Query option lets you harness the power of SQL to access our data. With this flexible and intuitive option, you can easily customize queries to fit your needs.

Market data for all

## Unblock your next innovation

We're committed to providing fair access to the financial markets for everyone, not just the big players on Wall Street. Access the same institutional-level data used by major trading firms.

Direct from the source

## No middlemen, just us

We're located in the datacenter with direct fiber cross-connects to the exchanges. We own the entire infrastructure so we can ensure quality at each step in the pipeline.

Direct connectivity means faster updates, fewer points of failure, and accurate market data you can depend on for your applications.

[About Massive →](https://massive.com/about)

Major Exchanges

![Image 2: NYSE logo](https://massive.com/_next/image?url=%2Fimages%2Flogos%2Fc38090cbc87ddab339e062c6eb76546651210c23-158x48.svg&w=256&q=75)

![Image 3: Nasdaq logo](https://massive.com/_next/image?url=%2Fimages%2Flogos%2F58db89688b8b3a2f84a5eaf673643720a8107814-158x48.svg&w=256&q=75)

![Image 4: Cboe logo](https://massive.com/_next/image?url=%2Fimages%2Flogos%2Fee7120cb00efea6aa6685d855c7af99e3d79ac1a-158x48.svg&w=256&q=75)

### Massive Infrastructure

Co-located in exchange datacenters

Direct fiber cross-connects

</>

### Your Application

Real-time market data

Use your AI tools

## Real markets. Any AI tool.

Pull market data into the AI tools you already use.  
One instruction, and your agent understands the API and handles the setup.

`I want to work with financial market data. Read massive.com/docs/llms.txt to see what Massive covers, then help me get started.`

Paste into Claude Code, Cursor, ChatGPT, Codex, Copilot, Gemini CLI, or Claude Desktop.

### Use your favorite AI tool

One instruction works in Claude Code, Cursor, ChatGPT, Codex, Copilot, Gemini, or Claude Desktop. No new workflow, no per-client setup.

### Build on live markets

Trading tools, research agents, dashboards. Your agent handles the data layer, so you go from prompt to a working idea.

### Straight from the exchanges

Depending on your plan: tick-level trades, quotes, and aggregate bars. Recency from end-of-day to real-time, up to 20+ years of history.

Setting up by hand? [Create an API key →](https://massive.com/dashboard/signup?redirect=%2Fdashboard%2Fkeys)

Built with Massive

## You're in good company

Whether you're building a trading app, a robo-advisor, or anything in between, our institutional-level data access can help you make better decisions and deliver better results.

Everything you need

## Market data platform

Our API is easy to use, fast, and reliable, so you can spend less time worrying about data and more time building your app.

API first approach

Familiar RESTful APIs and WebSockets to consume data in a language agnostic way.

Accurate, fast, and reliable

Real-time data. Complete redundancy, horizontal scalability, and built on proven technologies.

Extensive documentation

We're passionate about documentation and are always adding more tutorials, example projects, and explainers to support learners.

Financial data platform

Intuitive access to financial data in real-time and access to the world's financial history in an instant.

Institutional grade data

Directly from major exchanges. Clean, normalized data without survivorship bias.

Simple pricing

Unlimited access and simple, transparent monthly pricing across all available asset classes.

## From the blog

See what's happening at Massive

[![Image 5: x402 payments for ai agents Feature Image](https://massive.com/_next/image?url=https%3A%2F%2Fmassive.com%2Fblog%2Fcontent%2Fimages%2F2026%2F09%2Fcoinbase-massive--2-.png&w=3840&q=75)](https://massive.com/blog/x402-payments-for-ai-agents)

![Image 6: Justin Profile Photo](https://massive.com/_next/image?url=https%3A%2F%2Fmassive.com%2Fblog%2Fcontent%2Fimages%2F2026%2F06%2FIMG-0983.JPG&w=256&q=75)

[![Image 7: extended hours are coming to opra options data 2 Feature Image](https://massive.com/_next/image?url=https%3A%2F%2Fmassive.com%2Fblog%2Fcontent%2Fimages%2F2026%2F07%2FScreenshot-2026-07-10-at-10.46.25-AM.png&w=3840&q=75)](https://massive.com/blog/extended-hours-are-coming-to-opra-options-data-2)

### [Extended Hours Are Coming to OPRA Options Data](https://massive.com/blog/extended-hours-are-coming-to-opra-options-data-2)

Starting August 17, 2026, Cboe's Options Exchange is extending trading hours for select single-stock equity options with a morning GTH session (7:30–9:25 am ET) and Curb session (4:00–4:15 pm ET).

![Image 8: Cole Power Profile Photo](https://massive.com/_next/image?url=https%3A%2F%2Fmassive.com%2Fblog%2Fcontent%2Fimages%2F2026%2F02%2Fimage.jpg&w=256&q=75)

[![Image 9: tagging 8 k disclosures with ai corporate events labelled by what actually happened Feature Image](https://massive.com/_next/image?url=https%3A%2F%2Fmassive.com%2Fblog%2Fcontent%2Fimages%2F2026%2F07%2Fheader_5_2.png&w=3840&q=75)](https://massive.com/blog/tagging-8-k-disclosures-with-ai-corporate-events-labelled-by-what-actually-happened)

![Image 10: Rian Dolphin Profile Photo](https://massive.com/_next/image?url=https%3A%2F%2Fmassive.com%2Fblog%2Fcontent%2Fimages%2F2026%2F01%2FScreenshot-2026-01-22-at-16.59.40-1.png&w=256&q=75)

## Massive MCP server — https://mcp.massive.com/

Connect Massive to AI tools

Massive delivers high-quality U.S. market data that is well suited for AI agents and LLM powered applications. This guide covers the ways to connect that data to intelligent systems: our MCP server, LLM optimized documentation, direct REST integration, and Skills.

## MCP Server

The Massive MCP Server is the fastest way for AI agents to work with our data, and the right starting point for nearly everyone. It is hosted at https://mcp.massive.com/ and authenticates over OAuth, so there is nothing to install. You point your client at the URL, sign in once, and start querying.

Pick your tool for setup, verification, and troubleshooting tailored to it.

Using Cursor? Add the server in one click:

[Add to Cursor](https://cursor.com/install-mcp?name=massive&config=eyJ1cmwiOiJodHRwczovL21jcC5tYXNzaXZlLmNvbS8ifQ%3D%3D)
### How It Works

Instead of exposing dozens of individual endpoints as tools (which consumes excessive context), the server provides a small set of powerful, composable tools that let agents:

*   Discover relevant endpoints using natural language search
*   Retrieve accurate parameter documentation on demand
*   Execute any REST API call

The server dynamically indexes our documentation from llms.txt at startup, so it remains automatically up to date as we add new endpoints and features.

This design delivers dramatically lower token usage compared to traditional tool per endpoint approaches, along with better tool selection accuracy and strong support for complex, multi-step financial analysis workflows.

### Limits and Entitlements

The hosted environment currently provides 64 MB of working storage per session and supports up to 10 concurrent workspaces (roughly 10 simultaneous chats). That is ample for typical agentic analysis, but if you routinely download very large datasets the self-hosted option may be a better fit.

Access through the MCP server mirrors your Massive entitlements. You can query any asset class your plan includes. If you have Stocks access, stocks data is available through MCP. Requesting data you are not entitled to (for example, Options without an Options plan) returns an access-denied error.

### Self-Hosted MCP Server

Most users should stay on the hosted server above. If you need to work with large local datasets or prefer to run everything in your own environment, you can self-host. On top of the core tools, it adds a local data workspace that can store results as in-memory DataFrames, run SQL queries against them, and apply built-in financial functions (Greeks, returns, technical indicators, and more), which is useful for heavier local analysis. Install it via uv or pip from the official repository: [github.com/massive-com/mcp_massive](https://github.com/massive-com/mcp_massive).

## LLM Friendly Documentation

Massive's documentation is built to be AI-friendly from the ground up. Every page can be accessed as clean, structured Markdown by appending .md to the URL. Endpoint pages serve that same Markdown through two buttons in the top right corner. "View as Markdown" opens the .md URL in a new tab. "Copy for LLM" copies the Markdown to your clipboard.

We also provide an llms.txt index at any level of the documentation navigation tree. Append llms.txt to most paths, from the root down to a section or category. Each index groups pages by section, with a sentence on what each section covers, and links to the .md version of every page. An agent reads the index, then fetches only the pages it needs.

| Level | llms.txt |
| --- | --- |
| **Root** | [/docs/llms.txt](https://massive.com/docs/llms.txt) |
| **REST Section** | [/docs/rest/llms.txt](https://massive.com/docs/rest/llms.txt) |
| **Stocks Section** | [/docs/rest/stocks/llms.txt](https://massive.com/docs/rest/stocks/llms.txt) |
| **Specific Category** | [/docs/rest/stocks/tickers/llms.txt](https://massive.com/docs/rest/stocks/tickers/llms.txt) |

Start at the root for a broad view, or go lower for a smaller index scoped to one area of the API.

## Direct REST API Integration

You can also connect AI systems directly to our REST API using function calling and tool use in frameworks like OpenAI and Anthropic. Many developers now start by describing their desired workflow in natural language and letting AI generate the initial code. This approach works especially well for rapid prototyping and exploration.

We strongly recommend using our official client libraries as the foundation when building production code:

*   Python: [github.com/massive-com/client-python](https://github.com/massive-com/client-python)
*   JavaScript: [github.com/massive-com/client-js](https://github.com/massive-com/client-js)
*   Go: [github.com/massive-com/client-go](https://github.com/massive-com/client-go)
*   Kotlin / JVM: [github.com/massive-com/client-jvm](https://github.com/massive-com/client-jvm)

These libraries handle authentication, retries, pagination, error handling, and response parsing, giving you a solid, production-ready foundation, even when AI helps generate surrounding application code.

Our documentation pages include ready to use code examples for all endpoints. You can combine these examples with our llms.txt or .md files and feed them into your AI coding assistant to generate accurate, well structured integrations quickly. This combination of, strong client libraries + high-quality documentation + AI assistance, gives you the best balance of speed and reliability.

## Skills & Instructions

You can significantly improve AI performance by leveraging Skills (or equivalent project instructions and prompt libraries) in your AI tools. These act as a powerful shortcut, they teach the AI how your team specifically works with market data, rather than leaving it to guess.

A Skill encodes your internal conventions and best practices so the AI produces more consistent, accurate, and compliant outputs.

Common examples include:

*   Rules for using adjusted vs. unadjusted prices
*   Data quality checks and internal compliance guidelines
*   Handling of corporate actions, date ranges, and market hours
*   Preferred calculation methods for yields, returns, or volatility

You can implement this through Claude Skills (SKILL.md files), persistent project instructions, or reusable prompt libraries. This layer sits on top of your data access method (MCP or REST) and is one of the highest leverage ways to get reliable results from AI.

## Choosing the Right Approach

Choosing the right integration method depends on your goals, the complexity of your workflows, and how much control you need. The table below summarizes the main options and when each one tends to work best.

| Approach | Best For | Context Efficiency | Setup Effort | Recommended When |
| --- | --- | --- | --- | --- |
| Massive MCP Server | Most agentic workflows & complex analysis | Excellent | Low | You want agents to discover and use data intelligently |
| llms.txt + Markdown | Documentation-aware agents and discovery | Very Good | None | Agents need accurate, up to date API reference |
| Direct REST + Function Calling | Custom orchestration or full control | Good | Medium | Building your own agent framework or needing fine-grained control |
| Skills / Instructions | Consistent team processes & domain knowledge | Excellent | Low | You have repeatable financial workflows or compliance rules |
| x402 Pay Per Request | Agents with no Massive account or API key | Good | Medium | An agent needs to buy data on its own, paying per request from a wallet |

Quick decision guide:

1.   Building or using an agent that needs to take actions on live data? Start with the MCP Server.
2.   Need accurate, current endpoint documentation in context? Use llms.txt.
3.   Have specific internal processes or rules the AI must follow? Add Skills or project instructions.
4.   Want maximum control or custom orchestration? Use Direct REST with function calling + client libraries.
5.   Building an agent that has no Massive account behind it? Use [x402](https://mcp.massive.com/docs/ai-tools/x402) to pay per request.

## Next Steps

The fastest way to get value is usually to start with the MCP Server and llms.txt, then layer in Skills as your needs grow.

1.   Pick the client that matches your tool under [MCP Server](https://mcp.massive.com/#mcp-server) and follow its setup guide.
2.   Explore our llms.txt files so your agents can discover documentation automatically.
3.   Review the [REST Quickstart](https://mcp.massive.com/docs/rest/quickstart), [WebSocket Quickstart](https://mcp.massive.com/docs/websocket/quickstart), and [Flat Files Quickstart](https://mcp.massive.com/docs/flat-files/quickstart) for raw data access, authentication, and basic request patterns.

With these tools in place, you can move beyond manual data copying and start building reliable, production grade financial intelligence with AI.

Did you find this page helpful?

Do you still need help with something?

## AI Tools Quickstart — https://massive.com/docs/ai-tools/quickstart


AI Tools Quickstart Guide

Massive delivers high-quality U.S. market data that is well suited for AI agents and LLM powered applications. This guide covers the ways to connect that data to intelligent systems: our MCP server, LLM optimized documentation, direct REST integration, and Skills.

## MCP Server

The Massive MCP Server is the fastest way for AI agents to work with our data, and the right starting point for nearly everyone. It is hosted at `https://mcp.massive.com/` and authenticates over OAuth, so there is nothing to install. You point your client at the URL, sign in once, and start querying.

Pick your tool for setup, verification, and troubleshooting tailored to it.

- [Claude Code](https://massive.com/docs/ai-tools/clients/claude-code.md): Query market data from your terminal.
- [Claude Desktop](https://massive.com/docs/ai-tools/clients/claude-desktop.md): Chat with market data in the desktop app.
- [Cursor](https://massive.com/docs/ai-tools/clients/cursor.md): Pull market data into your editor.
- [ChatGPT](https://massive.com/docs/ai-tools/clients/chatgpt.md): Add Massive as a ChatGPT connector.
- [Grok](https://massive.com/docs/ai-tools/clients/grok.md): Add Massive as a Grok MCP tool.
- [Codex](https://massive.com/docs/ai-tools/clients/codex.md): Give Codex access to market data.
- [GitHub Copilot](https://massive.com/docs/ai-tools/clients/github-copilot.md): Use market data from Copilot in VS Code.
- [Gemini CLI](https://massive.com/docs/ai-tools/clients/gemini-cli.md): Query market data from the Gemini CLI.

Using Cursor? Add the server in one click:

[Add to Cursor](https://cursor.com/install-mcp?name=massive&config=eyJ1cmwiOiJodHRwczovL21jcC5tYXNzaXZlLmNvbS8ifQ%3D%3D)

### How It Works

Instead of exposing dozens of individual endpoints as tools (which consumes excessive context), the server provides a small set of powerful, composable tools that let agents:

- Discover relevant endpoints using natural language search
- Retrieve accurate parameter documentation on demand
- Execute any REST API call

The server dynamically indexes our documentation from `llms.txt` at startup, so it remains automatically up to date as we add new endpoints and features.

This design delivers dramatically lower token usage compared to traditional tool per endpoint approaches, along with better tool selection accuracy and strong support for complex, multi-step financial analysis workflows.

### Limits and Entitlements

The hosted environment currently provides 64 MB of working storage per session and supports up to 10 concurrent workspaces (roughly 10 simultaneous chats). That is ample for typical agentic analysis, but if you routinely download very large datasets the self-hosted option may be a better fit.

Access through the MCP server mirrors your Massive entitlements. You can query any asset class your plan includes. If you have Stocks access, stocks data is available through MCP. Requesting data you are not entitled to (for example, Options without an Options plan) returns an access-denied error.

### Self-Hosted MCP Server

Most users should stay on the hosted server above. If you need to work with large local datasets or prefer to run everything in your own environment, you can self-host. On top of the core tools, it adds a local data workspace that can store results as in-memory DataFrames, run SQL queries against them, and apply built-in financial functions (Greeks, returns, technical indicators, and more), which is useful for heavier local analysis. Install it via `uv` or `pip` from the official repository: [github.com/massive-com/mcp_massive](https://github.com/massive-com/mcp_massive).

## LLM Friendly Documentation

Massive's documentation is built to be AI-friendly from the ground up. Every page can be accessed as clean, structured Markdown by appending `.md` to the URL. Endpoint pages serve that same Markdown through two buttons in the top right corner. "View as Markdown" opens the `.md` URL in a new tab. "Copy for LLM" copies the Markdown to your clipboard.

We also provide an `llms.txt` index at any level of the documentation navigation tree. Append `llms.txt` to most paths, from the root down to a section or category. Each index groups pages by section, with a sentence on what each section covers, and links to the `.md` version of every page. An agent reads the index, then fetches only the pages it needs.

| Level                 | `llms.txt`                                                                                  |
|-----------------------|---------------------------------------------------------------------------------------------|
| **Root**              | [/docs/llms.txt](https://massive.com/docs/llms.txt)                                         |
| **REST Section**      | [/docs/rest/llms.txt](https://massive.com/docs/rest/llms.txt)                               |
| **Stocks Section**    | [/docs/rest/stocks/llms.txt](https://massive.com/docs/rest/stocks/llms.txt)                 |
| **Specific Category** | [/docs/rest/stocks/tickers/llms.txt](https://massive.com/docs/rest/stocks/tickers/llms.txt) |

Start at the root for a broad view, or go lower for a smaller index scoped to one area of the API.

## Direct REST API Integration

You can also connect AI systems directly to our REST API using function calling and tool use in frameworks like OpenAI and Anthropic. Many developers now start by describing their desired workflow in natural language and letting AI generate the initial code. This approach works especially well for rapid prototyping and exploration.

We strongly recommend using our official client libraries as the foundation when building production code:

- Python: [github.com/massive-com/client-python](https://github.com/massive-com/client-python)
- JavaScript: [github.com/massive-com/client-js](https://github.com/massive-com/client-js)
- Go: [github.com/massive-com/client-go](https://github.com/massive-com/client-go)
- Kotlin / JVM: [github.com/massive-com/client-jvm](https://github.com/massive-com/client-jvm)

These libraries handle authentication, retries, pagination, error handling, and response parsing, giving you a solid, production-ready foundation, even when AI helps generate surrounding application code.

Our documentation pages include ready to use code examples for all endpoints. You can combine these examples with our `llms.txt` or `.md` files and feed them into your AI coding assistant to generate accurate, well structured integrations quickly. This combination of, strong client libraries + high-quality documentation + AI assistance, gives you the best balance of speed and reliability.

## Skills & Instructions

You can significantly improve AI performance by leveraging Skills (or equivalent project instructions and prompt libraries) in your AI tools. These act as a powerful shortcut, they teach the AI how your team specifically works with market data, rather than leaving it to guess.

A Skill encodes your internal conventions and best practices so the AI produces more consistent, accurate, and compliant outputs.

Common examples include:
- Rules for using adjusted vs. unadjusted prices
- Data quality checks and internal compliance guidelines
- Handling of corporate actions, date ranges, and market hours
- Preferred calculation methods for yields, returns, or volatility

You can implement this through Claude Skills (`SKILL.md` files), persistent project instructions, or reusable prompt libraries. This layer sits on top of your data access method (MCP or REST) and is one of the highest leverage ways to get reliable results from AI.

## Choosing the Right Approach

Choosing the right integration method depends on your goals, the complexity of your workflows, and how much control you need. The table below summarizes the main options and when each one tends to work best.

| Approach                        | Best For                                           | Context Efficiency | Setup Effort | Recommended When |
|--------------------------------|----------------------------------------------------|--------------------|--------------|-------------------|
| Massive MCP Server         | Most agentic workflows & complex analysis          | Excellent          | Low          | You want agents to discover and use data intelligently |
| llms.txt + Markdown        | Documentation-aware agents and discovery           | Very Good          | None         | Agents need accurate, up to date API reference |
| Direct REST + Function Calling | Custom orchestration or full control           | Good               | Medium       | Building your own agent framework or needing fine-grained control |
| Skills / Instructions      | Consistent team processes & domain knowledge       | Excellent          | Low          | You have repeatable financial workflows or compliance rules |
| x402 Pay Per Request       | Agents with no Massive account or API key          | Good               | Medium       | An agent needs to buy data on its own, paying per request from a wallet |

Quick decision guide:

1. Building or using an agent that needs to take actions on live data? Start with the MCP Server.
2. Need accurate, current endpoint documentation in context? Use llms.txt.
3. Have specific internal processes or rules the AI must follow? Add Skills or project instructions.
4. Want maximum control or custom orchestration? Use Direct REST with function calling + client libraries.
5. Building an agent that has no Massive account behind it? Use [x402](https://massive.com/docs/ai-tools/x402.md) to pay per request.

## Next Steps

The fastest way to get value is usually to start with the MCP Server and `llms.txt`, then layer in Skills as your needs grow.

1. Pick the client that matches your tool under [MCP Server](#mcp-server) and follow its setup guide.
2. Explore our `llms.txt` files so your agents can discover documentation automatically.
3. Review the [REST Quickstart](https://massive.com/docs/rest/quickstart.md), [WebSocket Quickstart](https://massive.com/docs/websocket/quickstart.md), and [Flat Files Quickstart](https://massive.com/docs/flat-files/quickstart.md) for raw data access, authentication, and basic request patterns.

With these tools in place, you can move beyond manual data copying and start building reliable, production grade financial intelligence with AI.

## Claude Code Setup — https://massive.com/docs/ai-tools/clients/claude-code


Connect Massive to Claude Code

Massive's [remote MCP server](https://massive.com/docs/ai-tools/quickstart.md) connects Claude Code to live U.S. market data: dividends, trades, quotes, options chains, and the rest of our catalog. It queries our [REST API](https://massive.com/docs/rest/quickstart.md) under the hood, giving Claude Code the context to pull that data directly and write correct code against it.

This guide walks through connecting the remote MCP server, authenticating over OAuth, and verifying the integration. Setup takes about two minutes and requires Claude Code installed plus a Massive account. There is nothing else to download, and authentication happens in your browser.

## What You Can Do

Once connected, the MCP server gives Claude Code a small set of composable tools for endpoint search and live API calls, so you can ask it to:

- Pull every dividend declared this month across U.S. stocks and rank them by yield.
- Inspect the live response shape of an endpoint before writing code against it.
- Build a Python project that screens options chains, then verify it against real API responses.
- Figure out which Massive endpoint returns the data shape you need.

Because the server runs the calls itself, Claude Code can check real responses while it works, which is useful for confirming response shapes or chasing down a hallucinated field name.

## Setup

Two steps. Allow about two minutes start to finish.

### 1. Install Claude Code

If you don't have it, install [Claude Code](https://claude.ai/code) and confirm it works:

```bash
claude --version
```

### 2. Add the Massive Remote MCP Server

Register the remote server with Claude Code:

**Add the remote MCP server**

```bash
claude mcp add --transport http massive https://mcp.massive.com/
```

Then launch Claude Code and authenticate:

1. Run `claude`
2. Type `/mcp`
3. Select **massive**
4. Select **1. Authenticate** and complete the sign-in in your browser

Authentication uses OAuth against your Massive account, so there is no API key to copy or store. A free Basic account is enough to start.

Your MCP access mirrors your Massive entitlements. You can query any asset class your plan includes. If you have Stocks access, stocks data is available through MCP. Requesting data you are not entitled to (for example, Options without an Options plan) returns an access-denied error.

## Test the Integration

Now that the connection is live, put it through its paces. A few prompts to start with:

- "Show me the latest trade for AAPL." (Trades)
- "Is the U.S. market open right now?" (Market Status)
- "When is the next market holiday?" (Market Holidays)
- "What dividends has AAPL paid this year?" (Dividends)
- "Give me a snapshot of today's biggest gainers." (Snapshots)

When you're ready to go deeper, hand Claude Code a full brief and let it chain several calls together:

> Pull all dividends declared in the last 30 days, filter to U.S. stocks with a market cap over $50 billion, rank them by yield, and summarize the top five with their pay dates.

Claude Code will search for the right endpoints, make the live calls, and stitch the results into a single answer.

## Troubleshooting

**`massive` doesn't appear under `/mcp`.** Confirm the server was added with `claude mcp list`. If it's missing, run the add command from Step 2 again.

**Authentication didn't complete.** Run `/mcp`, select **massive**, and choose **Authenticate** again. Make sure you finished the browser sign-in and granted access.

**Claude responds with numbers but doesn't cite an MCP call.** It's answering from training data. Ask it explicitly to use the Massive tools, e.g. "use the Massive MCP server to check."

**Numbers look wrong or made up.** The server likely isn't connected. Confirm with `claude mcp list` and that `/mcp` shows `massive` as connected and authenticated.

## x402 Payments — https://massive.com/docs/ai-tools/x402


Buy US stock data per request over the x402 protocol, with no Massive account

An agent can buy US stock data from Massive one request at a time, paying in USDC over the x402 protocol. There is no Massive account to create and no API key to manage. All your agent needs is a wallet holding USDC on Base.

Intraday data points are based on Fair Market Value, our proprietary algorithm that generates an indication of a tradable instrument's value in real-time. Coverage is US stocks. Tick level data, streaming, and other asset classes are not available over x402. With a Massive account, the [MCP server](https://massive.com/docs/ai-tools/quickstart.md) connects an agent to the rest of the catalog, and [WebSocket](https://massive.com/docs/websocket/quickstart.md) handles streaming.

## What Is x402

x402 is an open payment standard, created by Coinbase in 2025 and since contributed to the [x402 Foundation](https://x402.org/), which operates under the Linux Foundation's governance model with members including AWS, Cloudflare, Google, Stripe, and Visa.

It uses the HTTP `402 Payment Required` status code to price a resource in the response itself. A client requests a resource, gets back machine readable payment requirements, signs a payment in USDC, and retries the request with proof of payment. Once the payment is verified, the server returns the data. The whole exchange happens over ordinary HTTP, which is what makes it usable by a program with no human in the loop.

Verification and settlement are handled by a facilitator, a service that checks the signed payment, settles it on chain, and tells the server whether it cleared, so a data provider does not have to run any crypto infrastructure of its own. We use Coinbase Developer Platform's facilitator, and it verifies every x402 payment made to our routes.

## Data Available

US stocks, priced per request:

- **Bars and aggregates.** OHLCV for one ticker over any range and interval, one day for one ticker, or one day across the whole market.
- **Snapshots.** The latest data for one ticker, every ticker, or the day's top gainers and losers.
- **Technical indicators.** SMA, EMA, RSI, and MACD, computed for you.
- **Reference data.** Ticker search and company detail.
- **News.** Recent articles for a ticker, with summaries.
- **SEC filings.** The EDGAR index, 10-K sections, 8-K text and classified disclosures, risk factors, 13-F institutional holdings, and Form 3 and Form 4 insider trades.

For the current route list, with each route's parameters and price, see the [Massive listing on Agentic.Market](https://agentic.market/services/agent-massive-com). Your agent can also read it directly from the x402 Bazaar, and every route carries its own schema and examples in its `402` response.

## Getting Started

You do not need to write any code. Ask your agent to fetch `https://agentic.market/SKILL.md` and follow the setup instructions. That skill is maintained by Coinbase and Agentic.Market, and it will:

- Set up an Agentic Wallet, which is a Coinbase wallet built for agents
- Sign you in with your email and help you add USDC
- Find the route that answers your question
- Pay for each request and hand back the data

It works in shell-capable agents like Claude Code, Codex CLI, and Gemini CLI, and in chat hosts like Claude Desktop and ChatGPT through Coinbase's payments MCP. You will not handle a private key or sign a payment yourself.

Once it is set up, ask for what you want:

> What were AAPL's daily bars for the first half of August?

Your agent finds the route, pays for the request, and answers.

## Pricing and Limits

Current prices are on the [Massive listing on Agentic.Market](https://agentic.market/services/agent-massive-com). Each route quotes its own live price in its `402` response, which is authoritative. Only successful requests are charged, a rejected or failed request costs nothing, and each page of a paginated result is charged separately.

Recency differs by route:

- **Aggregates and indicators are end of day.** The newest bar is the last completed session.
- **Snapshots cover the current session.** Snapshot data clears at 3:30 AM ET and repopulates as exchanges report, which can start as early as 4:00 AM ET.
- **Reference data is current.**

Filings return sections and classified extracts rather than whole documents. For tick level data or any asset class beyond US stocks, you need a Massive account and an API key. The [MCP server](https://massive.com/docs/ai-tools/quickstart.md) is the quickest way to give an agent access to that, and the [REST API](https://massive.com/docs/rest/quickstart.md) is there for direct integration. Streaming is not available through MCP, so use [WebSocket](https://massive.com/docs/websocket/quickstart.md) for that.

If a route you need is missing, your agent can report it for free at `POST https://agent.massive.com/feedback`. Those reports decide what we add next.

## x402 or an API Key

Most integrations still want an API key. It covers every asset class and includes real time and tick level data. If your agent runs inside an account you control, start with the [MCP server](https://massive.com/docs/ai-tools/quickstart.md), and use [WebSocket](https://massive.com/docs/websocket/quickstart.md) for streaming.

| | x402 | API key |
|---|---|---|
| Host | `agent.massive.com` | `api.massive.com` |
| Massive account required | No | Yes |
| Credential | A wallet with USDC on Base | An API key |
| Billing | Per request, in USDC | Subscription or plan |
| Data | US stocks (FMV) | Every asset class |
| Recency | End of day bars, current session snapshots | Includes real time trades and quotes |
| Streaming | No | Yes, over WebSocket |

## REST Quickstart — https://massive.com/docs/rest/quickstart


REST API Quickstart Guide

![A screenshot displaying a JSON response with stock data on one side and a graphical user interface presenting the same information, illustrating the types of applications you can build with Massive data](https://massive.com/docs/img/quickstart_rest_transparent_massive.png "Demonstration of JSON data powering a stocks data UI")

The Massive REST API delivers historical and real-time market data over HTTPS — ideal for on-demand queries and request/response integrations. For bulk historical downloads, use [Flat Files](https://massive.com/docs/flat-files/quickstart.md); for live streams, use the [WebSocket API](https://massive.com/docs/websocket/quickstart.md).

This guide walks through authenticating and making your first request manually so you understand what our [official client libraries](#explore-client-libraries) handle on your behalf.

## Browse Our Data

Select a category to see its REST endpoints, schemas, and code examples.

- [Stocks](https://massive.com/docs/rest/stocks/overview.md): Trades, quotes, fundamentals, and reference data.
- [Options](https://massive.com/docs/rest/options/overview.md): OPRA options trades, quotes, and aggregate bars.
- [Futures](https://massive.com/docs/rest/futures/overview.md): Trades, quotes, and reference across CME venues.
- [Indices](https://massive.com/docs/rest/indices/overview.md): Values and reference data for major U.S. indices.
- [Forex](https://massive.com/docs/rest/forex/overview.md): Currency pair trades, quotes, and aggregate bars.
- [Crypto](https://massive.com/docs/rest/crypto/overview.md): Global crypto trades, quotes, and aggregate bars.
- [Economy](https://massive.com/docs/rest/economy/overview.md): Macroeconomic indicators and historical time series.
- [Alternative](https://massive.com/docs/rest/alternative/overview.md): News, sentiment, and other alternative datasets.
- [Partners](https://massive.com/docs/rest/partners/overview.md): Third-party datasets accessible through Massive.

## Authenticate Your Request
Before you can access Massive data, you need your unique API key.

**Obtaining Your API Key**  
1. [Sign up](https://massive.com/dashboard/signup) or [log in](https://massive.com/dashboard/login) to your account.  
2. Visit your [Dashboard](https://massive.com/dashboard/keys) to find your API key.  
3. Keep your API key secure and do not share it publicly.

You can include your API key in two ways:

* **Query String Parameter** (e.g., `?apiKey=YOUR_API_KEY`):
  **Query String Authentication**

  ```plaintext
  https://api.massive.com/v3/reference/dividends?apiKey=YOUR_API_KEY
  ```

* **Authorization Header**:
  **Header Authentication**

  ```http
  GET /v3/reference/dividends HTTP/1.1
  Host: api.massive.com
  Authorization: Bearer YOUR_API_KEY
  ```

**Note:** Replace `YOUR_API_KEY` with your actual API key from your dashboard.

## Making Your First API Request
At your terminal, let’s make a simple request using the `curl` command, to the [Dividends](https://massive.com/docs/rest/stocks/corporate-actions/dividends.md) endpoint to list recent dividends.

**cURL**

```bash
curl "https://api.massive.com/v3/reference/dividends?apiKey=YOUR_API_KEY"
```

This command retrieves dividend records. For more parameters and advanced filtering options, see the Dividends endpoint [documentation](https://massive.com/docs/rest/stocks/corporate-actions/dividends.md).

**Pro Tip:** If you omit your API key or use an invalid one, you will receive an authorization error. Ensure you have replaced `YOUR_API_KEY` with your actual key before running the command.

## Understanding the API Response
All REST API endpoints from Massive return data in a structured JSON format. You will commonly see fields like `status`, `count`, `results`, and `request_id` at the root level. The `results` field typically contains an array of objects, each representing an individual data record (such as a dividend, trade, or ticker detail).

**JSON Response**

```json
{
  "results": [
      {
          "cash_amount": 0.25,
          "currency": "USD",
          "declaration_date": "2024-10-31",
          "dividend_type": "CD",
          "ex_dividend_date": "2024-11-08",
          "frequency": 4,
          "id": "E416a068758f85277196150c3eb73a3331d04698856c141e883ad95710dd0b189",
          "pay_date": "2024-11-14",
          "record_date": "2024-11-11",
          "ticker": "AAPL"
      }
  ],
  "status": "OK",
  "request_id": "5a8e1e551dc3a1c2c203744543b40399",
}
```

This pattern is consistent across our REST endpoints. Once you understand how to authenticate, make requests, and parse JSON responses for one endpoint -- like Dividends -- you can apply the same approach to all other endpoints. As you explore different datasets (e.g., trades, quotes, fundamentals), you will find that the process remains the same: use your API key, structure your request URL or headers appropriately, and parse the returned JSON to integrate the data into your applications.

Now that you know how to authenticate and issue requests, you have the basic skills to use any of the Massive REST endpoints.

## Explore Client Libraries
While understanding the manual workflow is valuable, integrating directly with our client libraries is the recommended approach for production use. These libraries handle:

* Authentication and secure key management
* Request formatting and retry logic
* Parsing JSON responses into easy-to-use structures

Available libraries:
* **Python**: [GitHub - Python Client](https://github.com/massive-com/client-python)
* **Go**: [GitHub - Go Client](https://github.com/massive-com/client-go)
* **Kotlin**: [GitHub - JVM Client](https://github.com/massive-com/client-jvm)
* **JavaScript**: [GitHub - JavaScript Client](https://github.com/massive-com/client-js)

## Using Massive with AI

Connecting an AI agent or assistant to Massive? Our [AI Tools](https://massive.com/docs/ai-tools/quickstart.md) area covers everything you need to give LLMs reliable access to market data: a remote MCP server for the REST API, LLM-friendly `llms.txt` files, and Markdown versions of every documentation page (just append `.md` to any URL). It includes step-by-step setup for Claude, ChatGPT, Cursor, Codex, and more.

## Next Steps
With your first successful API request and an understanding of the common patterns in our JSON responses, you are prepared to explore any of Massive’s endpoints. Check out our detailed documentation for additional parameters, data sources, and capabilities. As you progress, consider using our client libraries to greatly simplify the integration process and focus on building data-driven applications.

## WebSocket Quickstart — https://massive.com/docs/websocket/quickstart


WebSocket API Quickstart Guide

![A screenshot displaying a JSON response with options data on one side and a graphical user interface presenting the same information, illustrating the types of applications you can build with Massive data](https://massive.com/docs/img/quickstart_ws_transparent.png "Demonstration of JSON data powering a options data UI")

The Massive WebSocket API streams real-time market data over a persistent connection — ideal for event-driven dashboards, trading systems, and any application that needs live updates. For bulk historical downloads, use [Flat Files](https://massive.com/docs/flat-files/quickstart.md); for on-demand queries, use the [REST API](https://massive.com/docs/rest/quickstart.md).

This guide walks through connecting and exchanging messages manually with `wscat` so you understand what our [official client libraries](#explore-client-libraries) handle on your behalf.

## Browse Our Data

Select a category to see its WebSocket channels, message formats, and code examples.

- [Stocks](https://massive.com/docs/websocket/stocks/overview.md): Real-time stock trades, quotes, and aggregates.
- [Options](https://massive.com/docs/websocket/options/overview.md): Real-time OPRA trades, quotes, and aggregates.
- [Futures](https://massive.com/docs/websocket/futures/overview.md): Real-time futures trades and quotes across CME venues.
- [Indices](https://massive.com/docs/websocket/indices/overview.md): Real-time values and aggregates for U.S. indices.
- [Forex](https://massive.com/docs/websocket/forex/overview.md): Real-time currency pair quotes and aggregate bars.
- [Crypto](https://massive.com/docs/websocket/crypto/overview.md): Real-time global crypto trades, quotes, and aggregates.

## Requirements & Approach

In a production environment, you will likely never manually manage WebSocket connections and message flows as shown here. Instead, you would use one of our official client libraries, which encapsulate these details, handling tasks such as:

- Establishing and maintaining the WebSocket connection.
- Sending authentication messages automatically.
- Subscribing and unsubscribing to feeds.
- Efficiently parsing and handling incoming data.

By following along with the steps below using `wscat`, you'll gain insight into how our WebSocket streams operate under the hood, giving you confidence in what our client libraries are doing on your behalf.

**Preparing Your Environment:**
1. Ensure you have [Node.js](https://nodejs.org/) installed.
2. At your terminal, install `wscat`, a handy tool for interacting with WebSocket endpoints:

  **Install wscat**

  ```bash
  npm install -g wscat
  ```

## Connecting to the WebSocket
Massive offers both delayed and real-time data feeds depending on your needs.

- **15-minute Delayed Data**:

  **Connect to 15-minute delayed feed**

  ```bash
  wscat -c wss://delayed.massive.com/stocks
  ```


- **Real-Time Data**:

  **Connect to real-time feed**

  ```bash
  wscat -c wss://socket.massive.com/stocks
  ```


**Server to Client (Upon Successful Connection):**

  **Receive Successful Connection Message**

  ```json
  [{
    "ev":"status",
    "status":"connected",
    "message":"Connected Successfully"
  }]
  ```


**Note on Connections:** By default, one concurrent WebSocket connection per asset class is allowed. If you require multiple simultaneous connections for the same asset class, please [contact support](https://massive.com/contact).

## Authentication
After connecting, you must authenticate with your [API key](https://massive.com/dashboard/keys) before subscribing to data feeds.

**Client to Server (Send Your API Key):**

  **Send Authentication Request**

  ```json
  {
    "action":"auth",
    "params":"YOUR_API_KEY"
  }
  ```


**Server to Client (Successful Authentication):**

  **Receive Successful Authentication Message**

  ```json
  [{
    "ev":"status",
    "status":"auth_success",
    "message":"authenticated"
  }]
  ```

## Subscribing to Data Feeds
Once authenticated, you can subscribe to various channels. Below is an example subscribing to Stocks Aggregates (Per Minute) updates for `AAPL` and `MSFT`:

**Client to Server (Subscription Request):**

  **Send Subscription Request**

  ```json
  {
    "action":"subscribe",
    "params":"AM.AAPL,AM.MSFT"
  }
  ```


**Server to Client (Data Messages):** After subscribing, you will receive updates as they occur. For example, a real-time aggregate per minute (AM) message might look like this:

**Receive Data Messages for Your Subscription**

```json
[
  {
    "ev": "AM",
    "sym": "AAPL",
    "v": 12345,
    "o": 150.85,
    "c": 152.90,
    "h": 153.17,
    "l": 150.50,
    "a": 151.87,
    "s": 1611082800000,
    "e": 1611082860000
  }
]
```

**Field Explanations:**
- **ev**: Event type (e.g., "AM" for aggregate minute bars)
- **sym**: Symbol (e.g., "AAPL")
- **v**: Volume in the aggregate period
- **o, c, h, l**: Open, Close, High, Low prices
- **a**: VWAP (Volume Weighted Average Price)
- **s**: Start timestamp of the aggregate period (Unix ms)
- **e**: End timestamp of the aggregate period (Unix ms)

## Message Formats & Multiple Events
During high-volume periods, the server may bundle multiple events into a single JSON array.

**Example with Multiple Trade Events:**

**Server to Client (Data Messages)**

```json
[
  {
    "ev": "T",        
    "sym": "MSFT",    
    "i": "50578",     
    "x": 4,           
    "p": 215.9721,    
    "s": 100,         
    "t": 1611082428813,
    "z": 3            
  },
  {
    "ev": "T",
    "sym": "MSFT",
    "i": "12856",
    "x": 4,
    "p": 215.989,
    "s": 1,
    "c": [37],        
    "t": 1611082428814,
    "z": 3
  }
]
```

By examining the `ev` field and other attributes, you can distinguish event types and integrate the data into your application logic.

## Performance & Latency Considerations
Handling streaming market data efficiently is key:
- Process messages quickly to avoid server-side buffering.
- If you consistently receive more data than you can handle, reduce subscriptions.
- Use a wired connection and avoiding Wifi and VPNs can help reduce latency.

If the server detects slow message consumption, it may disconnect to maintain overall system performance.

## Explore Client Libraries
In practice, you’ll likely rely on our client libraries for handling these details automatically. They simplify:
- Authentication
- Subscription management
- Message parsing
- Error handling and reconnect logic

Available libraries:
- **Python**: [GitHub - Python Client](https://github.com/massive-com/client-python)
- **Go**: [GitHub - Go Client](https://github.com/massive-com/client-go)
- **Kotlin**: [GitHub - JVM Client](https://github.com/massive-com/client-jvm)
- **JavaScript**: [GitHub - JavaScript Client](https://github.com/massive-com/client-js)

## Using Massive with AI

Connecting an AI agent or assistant to Massive? Our [AI Tools](https://massive.com/docs/ai-tools/quickstart.md) area covers everything you need to give LLMs reliable access to market data: a remote MCP server for the REST API, LLM-friendly `llms.txt` files, and Markdown versions of every documentation page (just append `.md` to any URL). It includes step-by-step setup for Claude, ChatGPT, Cursor, Codex, and more.

## Next Steps
By following this guide and understanding the underlying message flow, you can appreciate what happens when you connect, authenticate, and subscribe to data feeds. While this manual approach is useful for learning, our client libraries are the recommended choice for actual development and production use. With this knowledge in hand, explore the rest of our documentation to discover more channels, event types, and advanced capabilities.

## Flat Files Quickstart — https://massive.com/docs/flat-files/quickstart


Flat Files Quickstart Guide

![A screenshot displaying CSV data and a graphical user interface powered by Flat Files, illustrating streamlined market data integration](https://massive.com/docs/img/quickstart_flatfiles_transparent.png "Example of CSV Flat File integration")

Massive's Flat Files deliver extensive historical market data as compressed CSVs over an S3-compatible endpoint — ideal when you need bulk historical data without making thousands of REST calls. For smaller on-demand queries, use the [REST API](https://massive.com/docs/rest/quickstart.md); for real-time streams, use the [WebSocket API](https://massive.com/docs/websocket/quickstart.md).

This guide walks through downloading datasets manually with popular S3 clients or our File Browser.

## Browse Our Data

Select a category to see what data is available as Flat Files.

- [Stocks](https://massive.com/docs/flat-files/stocks/overview.md): Trades, quotes, and aggregate bars for U.S. equities.
- [Options](https://massive.com/docs/flat-files/options/overview.md): OPRA options trades, quotes, and aggregate bars.
- [Futures](https://massive.com/docs/flat-files/futures/overview.md): Trades, quotes, and aggregates across CME venues.
- [Indices](https://massive.com/docs/flat-files/indices/overview.md): Values and aggregates from major index providers.
- [Forex](https://massive.com/docs/flat-files/forex/overview.md): Currency pair quotes and time-based aggregate bars.
- [Crypto](https://massive.com/docs/flat-files/crypto/overview.md): Global crypto trades, quotes, and aggregate bars.

## Exploring and Downloading Data

Flat Files are organized by asset class and data type. Available asset classes include Stocks, Options, Indices, Forex, and Crypto. Within each asset class, you'll find data types such as trades, quotes, minute aggregates, day aggregates, and more.

To quickly explore and download historical data files, use the File Browser located in the left-hand navigation of this page. Simply select the asset class you're interested in and then drill down to access specific datasets available with your subscription. Alternatively, you can use an S3 client to automate and integrate Flat Files data into your workflow, as described in the following sections.

Note: Data for each trading day is available by approximately 11:00 AM ET the following day.

### Sample Data

Here's an example of minute aggregates for the stock `AAPL`, showing the CSV structure you'll see when downloading Flat Files:

```csv
ticker,volume,open,close,high,low,window_start,transactions
AAPL,4930,200.29,200.5,200.63,200.29,1744792500000000000,129
AAPL,1815,200.39,200.34,200.61,200.34,1744792560000000000,57
AAPL,1099,200.3,200.28,200.3,200.13,1744792620000000000,40
AAPL,3672,200.39,200.61,200.64,200.39,1744792680000000000,71
AAPL,4322,200.72,200.69,200.8,200.69,1744792740000000000,88
AAPL,3675,200.7,201.5,201.5,200.7,1744792800000000000,119
AAPL,12785,201.49,202.33,202.33,201.49,1744792860000000000,329
AAPL,11473,202.39,201.81,202.46,201.81,1744792920000000000,199
AAPL,3895,202.0,201.82,202.0,201.65,1744792980000000000,116
AAPL,4322,201.76,201.36,201.76,201.17,1744793040000000000,85
AAPL,2089,201.31,201.35,201.35,201.04,1744793100000000000,48
AAPL,7317,201.31,200.88,201.31,200.71,1744793160000000000,121
```

Each CSV file you download includes a header line as the first row, clearly identifying each column. This header exists across all files within a specific dataset, making it easy for you to interpret and integrate the data into your workflows.

## Setting Up S3 Access

To download Flat Files using an S3 client, you'll first need to configure your environment with the appropriate access credentials provided by Massive:

- Ensure you have an active [Massive subscription](https://massive.com/pricing) with Flat Files access.
- Obtain your unique S3 Access Key and Secret Key from your [Dashboard](https://massive.com/dashboard/keys).

Use the following standard configuration details for all S3 clients:

- **Endpoint:** `https://files.massive.com`  
- **Bucket Name:** `flatfiles`

Massive officially supports several popular S3-compatible clients:

- **[AWS S3 CLI](#aws-s3-cli)**
- **[Rclone](#rclone)**
- **[MinIO](#minio)**
- **[Python Boto3 SDK](#python-boto3-sdk)**

Below you'll find quick setup instructions for each client.

## AWS S3 CLI
The AWS S3 CLI is an efficient command-line tool for managing S3-compatible data stores.

Here's how to get started:

* Install the AWS S3 CLI from the [official website](https://aws.amazon.com/cli/).
* Run `aws configure` in your command line and enter your Access Key ID, and Secret Access Key.
* To interact with Massive's S3 files, use aws s3 commands:

  **AWS S3 CLI**

  ```bash
  # Configure your S3 Access and Secret keys
  aws configure set aws_access_key_id YOUR_ACCESS_KEY_ID
  aws configure set aws_secret_access_key YOUR_SECRET_ACCESS_KEY

  # List
  aws s3 ls s3://flatfiles/ --endpoint-url https://files.massive.com

  # Copy
  aws s3 cp s3://flatfiles/us_stocks_sip/trades_v1/2025/11/2025-11-05.csv.gz . --endpoint-url https://files.massive.com
  ```

## Rclone
Rclone is versatile for syncing and managing S3-compatible storage directly from your command line.

Here's how to get started:

* Download and install Rclone from [here](https://rclone.org/downloads/).
* Initiate a new remote storage configuration with `rclone config`.
* Here's an example configuration is provided below for reference:

  **Rclone**

  ```bash
  # Set up your rclone configuration
  rclone config create s3massive s3 env_auth=false access_key_id=YOUR_ACCESS_KEY_ID secret_access_key=YOUR_SECRET_ACCESS_KEY endpoint=https://files.massive.com

  # List
  rclone ls s3massive:flatfiles

  # Copy
  rclone copy s3massive:flatfiles/us_stocks_sip/trades_v1/2025/11/2025-11-05.csv.gz .
  ```

## MinIO
MinIO client works seamlessly with any S3 compatible cloud storage.

Here's how to get started:

* If you haven't already, download and set up MinIO from [their documentation](https://docs.min.io/docs/minio-client-quickstart-guide).
* Here's an example configuration is provided below for reference:

  **MinIO**

  ```bash
  # Enter S3 Access and Secret keys in config file ~/.mc/config.json
  mc alias set s3massive https://files.massive.com YOUR_ACCESS_KEY_ID YOUR_SECRET_ACCESS_KEY

  # List
  mc ls s3massive/flatfiles

  # View
  mc cat s3massive/flatfiles/us_stocks_sip/trades_v1/2025/11/2025-11-05.csv.gz | gzcat | head -4

  # Copy
  mc cp s3massive/flatfiles/us_stocks_sip/trades_v1/2025/11/2025-11-05.csv.gz .
  ```

## Python Boto3 SDK
Boto3 is the Amazon Web Services (AWS) SDK for Python, which enables Python developers to write software that makes use of Amazon services like S3.

Here's how to get started:

* Install Boto3 by running `pip install boto3` if you haven't already.
* Utilize the following script to interact with Massive data:

  **Python Boto3 SDK**

  ```python
  import boto3
  from botocore.config import Config

  # Initialize a session using your credentials
  session = boto3.Session(
    aws_access_key_id='YOUR_ACCESS_KEY_ID',
    aws_secret_access_key='YOUR_SECRET_ACCESS_KEY',
  )

  # Create a client with your session and specify the endpoint
  s3 = session.client(
    's3',
    endpoint_url='https://files.massive.com',
    config=Config(signature_version='s3v4'),
  )

  # List Example
  # Initialize a paginator for listing objects
  paginator = s3.get_paginator('list_objects_v2')

  # Choose the appropriate prefix depending on the data you need:
  # - 'global_crypto' for global cryptocurrency data
  # - 'global_forex' for global forex data
  # - 'us_indices' for US indices data
  # - 'us_options_opra' for US options (OPRA) data
  # - 'us_stocks_sip' for US stocks (SIP) data
  prefix = 'us_stocks_sip'  # Example: Change this prefix to match your data need

  # List objects using the selected prefix
  for page in paginator.paginate(Bucket='flatfiles', Prefix=prefix):
    for obj in page['Contents']:
      print(obj['Key'])

  # Copy example
  # Specify the bucket name
  bucket_name = 'flatfiles'

  # Specify the S3 object key name
  object_key = 'us_stocks_sip/trades_v1/2025/11/2025-11-05.csv.gz'

  # Specify the local file name and path to save the downloaded file
  # This splits the object_key string by '/' and takes the last segment as the file name
  local_file_name = object_key.split('/')[-1]

  # This constructs the full local file path
  local_file_path = './' + local_file_name

  # Download the file
  s3.download_file(bucket_name, object_key, local_file_path)
  ```

## Using Massive with AI

Connecting an AI agent or assistant to Massive? Our [AI Tools](https://massive.com/docs/ai-tools/quickstart.md) area covers everything you need to give LLMs reliable access to market data: a remote MCP server for the REST API, LLM-friendly `llms.txt` files, and Markdown versions of every documentation page (just append `.md` to any URL). It includes step-by-step setup for Claude, ChatGPT, Cursor, Codex, and more.

## Next Steps
Now that you've successfully accessed Flat Files with your S3 client, you can easily automate data retrieval and integrate historical market data into your workflows.

## Stocks Overview — https://massive.com/docs/rest/stocks/overview


At Massive, we provide a comprehensive suite of U.S. stock market data through a standardized and intuitive API, offering unparalleled coverage of the U.S. stock market landscape. Our offerings encompass real-time prices, historical data, company information, and news from all 19 major stock exchanges, additional dark pools, FINRA trading facilities, and OTC markets. Accessible via REST APIs, WebSocket streams, and flat files, this rich dataset supports the development of sophisticated applications tailored for both retail and professional trading environments. Leveraging detailed trade data and reference information, our platform delivers a robust analytical toolset crucial for comprehensive market analysis and decision-making.

## Available Endpoints

Browse the endpoints available for Stocks. Each row links to its dedicated documentation, with a short description and the API path.

| Endpoints | Description | Path |
| --- | --- | --- |
| **Tickers** | | |
| [All Tickers](https://massive.com/docs/rest/stocks/tickers/all-tickers.md) | Retrieve a comprehensive list of ticker symbols supported by Massive across various asset classes (e.g., stocks, indices, forex, crypto). Each ticker entry provides essential details such as symbol, name, market, currency, and active status. Use Cases: Asset discovery, data integration, filtering/selection, and application development. | `GET /v3/reference/tickers` |
| [Ticker Overview](https://massive.com/docs/rest/stocks/tickers/ticker-overview.md) | Retrieve comprehensive details for a single ticker supported by Massive that is active as-of a given date. This endpoint offers a deep look into a company’s fundamental attributes, including its primary exchange, standardized identifiers (CIK, composite FIGI, share class FIGI), market capitalization, industry classification, and key dates. Users also gain access to branding assets (e.g., logos, icons), enabling them to enrich applications and analyses with visually consistent, contextually relevant information. For information on delisted tickers, use the [All Tickers](https://massive.com/docs/rest/stocks/tickers/all-tickers.md) endpoint with `active=false`. Use Cases: Company research, data integration, application enhancement, due diligence & compliance. | `GET /v3/reference/tickers/{ticker}` |
| [Ticker Types](https://massive.com/docs/rest/stocks/tickers/ticker-types.md) | Retrieve a list of all ticker types supported by Massive. This endpoint categorizes tickers across asset classes, markets, and instruments, helping users understand the different classifications and their attributes. Use Cases: Data classification, filtering mechanisms, educational reference, system integration. | `GET /v3/reference/tickers/types` |
| [Related Tickers](https://massive.com/docs/rest/stocks/tickers/related-tickers.md) | Retrieve a list of tickers related to a specified ticker, identified through an analysis of news coverage and returns data. This endpoint helps users discover peers, competitors, or thematically similar companies, aiding in comparative analysis, portfolio diversification, and market research. Use Cases: Peer identification, comparative analysis, portfolio diversification, market research. | `GET /v1/related-companies/{ticker}` |
| **Aggregate Bars (OHLC)** | | |
| [Custom Bars](https://massive.com/docs/rest/stocks/aggregates/custom-bars.md) | Retrieve aggregated historical OHLC (Open, High, Low, Close) and volume data for a specified stock ticker over a custom date range and time interval in Eastern Time (ET). Aggregates are constructed exclusively from qualifying trades that meet specific conditions. If no eligible trades occur within a given timeframe, no aggregate bar is produced, resulting in an empty interval that indicates a lack of trading activity during that period. Users can tailor their data by adjusting the multiplier and timespan parameters (e.g., a 5-minute bar), covering pre-market, regular market, and after-hours sessions. This flexibility supports a broad range of analytical and visualization needs. Use Cases: Data visualization, technical analysis, backtesting strategies, market research. | `GET /v2/aggs/ticker/{stocksTicker}/range/{multiplier}/{timespan}/{from}/{to}` |
| [Daily Market Summary](https://massive.com/docs/rest/stocks/aggregates/daily-market-summary.md) | Retrieve daily OHLC (open, high, low, close), volume, and volume-weighted average price (VWAP) data for all U.S. stocks on a specified trading date. This endpoint returns comprehensive market coverage in a single request, enabling wide-scale analysis, bulk data processing, and research into broad market performance. Use Cases: Market overview, bulk data processing, historical research, and portfolio comparison. | `GET /v2/aggs/grouped/locale/us/market/stocks/{date}` |
| [Daily Ticker Summary](https://massive.com/docs/rest/stocks/aggregates/daily-ticker-summary.md) | Retrieve the opening and closing prices for a specific stock ticker on a given date, along with any pre-market and after-hours trade prices. This endpoint provides essential daily pricing details, enabling users to evaluate performance, conduct historical analysis, and gain insights into trading activity outside regular market sessions. Use Cases: Daily performance analysis, historical data collection, after-hours insights, portfolio tracking. | `GET /v1/open-close/{stocksTicker}/{date}` |
| [Previous Day Bar](https://massive.com/docs/rest/stocks/aggregates/previous-day-bar.md) | Retrieve the previous trading day's open, high, low, and close (OHLC) data for a specified stock ticker. This endpoint provides key pricing metrics, including volume, to help users assess recent performance and inform trading strategies. Use Cases: Baseline comparison, technical analysis, market research, and daily reporting. | `GET /v2/aggs/ticker/{stocksTicker}/prev` |
| **Snapshots** | | |
| [Single Ticker Snapshot](https://massive.com/docs/rest/stocks/snapshots/single-ticker-snapshot.md) | Retrieve the most recent market data snapshot for a single ticker. This endpoint consolidates the latest trade, quote, and aggregated data (minute, day, and previous day) for the specified ticker. Snapshot data is cleared at 3:30 AM EST and begins updating as exchanges report new information, which can start as early as 4:00 AM EST. By focusing on a single ticker, users can closely monitor real-time developments and incorporate up-to-date information into trading strategies, alerts, or company-level reporting. Use Cases: Focused monitoring, real-time analysis, price alerts, investor relations. | `GET /v2/snapshot/locale/us/markets/stocks/tickers/{stocksTicker}` |
| [Full Market Snapshot](https://massive.com/docs/rest/stocks/snapshots/full-market-snapshot.md) | Retrieve a comprehensive snapshot of the entire U.S. stock market, covering over 10,000+ actively traded tickers in a single response. This endpoint consolidates key information like pricing, volume, and trade activity to provide a full-market-snapshot view, eliminating the need for multiple queries. Snapshot data is cleared daily at 3:30 AM EST and begins to repopulate as exchanges report new data, which can start as early as 4:00 AM EST. By accessing all tickers at once, users can efficiently monitor broad market conditions, perform bulk analyses, and power applications that require complete, current market information. Use Cases: Market overview, bulk data processing, heat maps/dashboards, automated monitoring. | `GET /v2/snapshot/locale/us/markets/stocks/tickers` |
| [Unified Snapshot](https://massive.com/docs/rest/stocks/snapshots/unified-snapshot.md) | Retrieve unified snapshots of market data for multiple asset classes including stocks, options, forex, and cryptocurrencies in a single request. This endpoint consolidates key metrics such as last trade, last quote, open, high, low, close, and volume for a comprehensive view of current market conditions. By aggregating data from various sources into one response, users can efficiently monitor, compare, and act on information spanning multiple markets and asset types. Use Cases: Cross-market analysis, diversified portfolio monitoring, global market insights, multi-asset trading strategies. | `GET /v3/snapshot` |
| [Top Market Movers](https://massive.com/docs/rest/stocks/snapshots/top-market-movers.md) | Retrieve snapshot data highlighting the top 20 gainers or losers in the U.S. stock market. Gainers are stocks with the largest percentage increase since the previous day’s close, and losers are those with the largest percentage decrease. To ensure meaningful insights, only tickers with a minimum trading volume of 10,000 are included. Snapshot data is cleared daily at 3:30 AM EST and begins repopulating as exchanges report new information, typically starting around 4:00 AM EST. By focusing on these market movers, users can quickly identify significant price shifts and monitor evolving market dynamics. Use Cases: Market movers identification, trading strategies, market sentiment analysis, portfolio adjustments. | `GET /v2/snapshot/locale/us/markets/stocks/{direction}` |
| **Trades & Quotes** | | |
| [Trades](https://massive.com/docs/rest/stocks/trades-quotes/trades.md) | Retrieve comprehensive, tick-level trade data for a specified stock ticker within a defined time range. Each record includes price, size, exchange, trade conditions, and precise timestamp information. This granular data is foundational for constructing aggregated bars and performing in-depth analyses, as it captures every eligible trade that contributes to calculations of open, high, low, and close (OHLC) values. By leveraging these trades, users can refine their understanding of intraday price movements, test and optimize algorithmic strategies, and ensure compliance by maintaining an auditable record of market activity. Use Cases: Intraday analysis, algorithmic trading, market microstructure research, data integrity and compliance. | `GET /v3/trades/{stockTicker}` |
| [Last Trade](https://massive.com/docs/rest/stocks/trades-quotes/last-trade.md) | Retrieve the latest available trade for a specified stock ticker, including details such as price, size, exchange, and timestamp. This endpoint supports monitoring recent trading activity and updating dashboards or applications with the most current trade information, providing timely insights into ongoing market conditions. Use Cases: Trade monitoring, price updates, market snapshot. | `GET /v2/last/trade/{stocksTicker}` |
| [Quotes](https://massive.com/docs/rest/stocks/trades-quotes/quotes.md) | Retrieve National Best Bid and Offer (NBBO) quotes for a specified stock ticker over a defined time range. Each record includes the prevailing best bid/ask prices, sizes, exchanges, and timestamps, reflecting the top-of-book quote environment at each moment. By examining this historical quote data, users can analyze price movements, evaluate liquidity at the NBBO level, and enhance trading strategies or research efforts. Use Cases: Historical quote analysis, liquidity evaluation, algorithmic backtesting, trading strategy refinement. | `GET /v3/quotes/{stockTicker}` |
| [Last Quote](https://massive.com/docs/rest/stocks/trades-quotes/last-quote.md) | Retrieve the most recent National Best Bid and Offer (NBBO) quote for a specified stock ticker, including the latest bid/ask prices, sizes, exchange details, and timestamp. This endpoint supports monitoring current market conditions and updating platforms or applications with near-term quote information, allowing users to evaluate liquidity, track spreads, and make more informed decisions. Use Cases: Price display, spread analysis, market monitoring. | `GET /v2/last/nbbo/{stocksTicker}` |
| **Technical Indicators** | | |
| [SMA](https://massive.com/docs/rest/stocks/technical-indicators/simple-moving-average.md) | Retrieve the Simple Moving Average (SMA) for a specified ticker over a defined time range. The SMA calculates the average price across a set number of periods, smoothing price fluctuations to reveal underlying trends and potential signals. Use Cases: Trend analysis, trading signal generation (e.g., SMA crossovers), identifying support/resistance, and refining entry/exit timing. | `GET /v1/indicators/sma/{stockTicker}` |
| [EMA](https://massive.com/docs/rest/stocks/technical-indicators/exponential-moving-average.md) | Retrieve the Exponential Moving Average (EMA) for a specified ticker over a defined time range. The EMA places greater weight on recent prices, enabling quicker trend detection and more responsive signals. Use Cases: Trend identification, EMA crossover signals, dynamic support/resistance levels, and adjusting strategies based on recent market volatility. | `GET /v1/indicators/ema/{stockTicker}` |
| [MACD](https://massive.com/docs/rest/stocks/technical-indicators/moving-average-convergence-divergence.md) | Retrieve the Moving Average Convergence/Divergence (MACD) for a specified ticker over a defined time range. MACD is a momentum indicator derived from two moving averages, helping to identify trend strength, direction, and potential trading signals. Use Cases: Momentum analysis, signal generation (crossover events), spotting overbought/oversold conditions, and confirming trend directions. | `GET /v1/indicators/macd/{stockTicker}` |
| [RSI](https://massive.com/docs/rest/stocks/technical-indicators/relative-strength-index.md) | Retrieve the Relative Strength Index (RSI) for a specified ticker over a defined time range. The RSI measures the speed and magnitude of price changes, oscillating between 0 and 100 to help identify overbought or oversold conditions. Use Cases: Overbought/oversold detection, divergence analysis, trend confirmation, and refining market entry/exit strategies. | `GET /v1/indicators/rsi/{stockTicker}` |
| **Market Operations** | | |
| [Exchanges](https://massive.com/docs/rest/stocks/market-operations/exchanges.md) | Retrieve a list of known exchanges, including their identifiers, names, market types, and other relevant attributes. This information helps map exchange codes, understand market coverage, and integrate exchange details into applications. Use Cases: Data mapping, market coverage analysis, application development (e.g., display exchange options), and ensuring regulatory compliance. | `GET /v3/reference/exchanges` |
| [Market Holidays](https://massive.com/docs/rest/stocks/market-operations/market-holidays.md) | Retrieve upcoming market holidays and their corresponding open/close times. This endpoint is forward-looking only, listing future holidays that affect market hours. Use this data to plan ahead for trading activities and system operations. Use Cases: Trading schedule adjustments, integrated holiday calendars, operational planning (e.g., system maintenance), and notifying users about upcoming market closures. | `GET /v1/marketstatus/upcoming` |
| [Market Status](https://massive.com/docs/rest/stocks/market-operations/market-status.md) | Retrieve the current trading status for various exchanges and overall financial markets. This endpoint provides real-time indicators of whether markets are open, closed, or operating in pre-market/after-hours sessions, along with timing details for the current or upcoming trading periods. Use Cases: Real-time monitoring, algorithm scheduling, UI updates, and operational planning. | `GET /v1/marketstatus/now` |
| [Condition Codes](https://massive.com/docs/rest/stocks/market-operations/condition-codes.md) | Retrieve a unified and comprehensive list of trade and quote conditions from various upstream market data providers (e.g., CTA, UTP, OPRA, FINRA). Each condition identifies special circumstances associated with market data, such as trades occurring outside regular sessions or at averaged prices, and outlines how these conditions affect metrics like high, low, open, close, and volume. By examining these mapped conditions, users can accurately interpret the context of trades and quotes, apply appropriate filtering, and ensure that aggregated data correctly reflects eligible trading activity. Use Cases: Data interpretation, unified condition mapping, filtering and analysis, algorithmic adjustments, compliance and reporting. | `GET /v3/reference/conditions` |
| **Corporate Actions** | | |
| [IPOs](https://massive.com/docs/rest/stocks/corporate-actions/ipos.md) | Retrieve comprehensive information on Initial Public Offerings (IPOs), including upcoming and historical events, starting from the year 2008. This endpoint provides key details such as issuer name, ticker symbol, security type, IPO date, number of shares offered, expected price ranges, final issue prices, and offering sizes. Users can filter results by IPO status (e.g., pending, new, rumors, historical) to target their research and inform investment decisions. Use Cases: IPO research, market trend analysis, investment screening, historical event comparison. | `GET /vX/reference/ipos` |
| [Splits (Deprecated)](https://massive.com/docs/rest/stocks/corporate-actions/reference-splits.md) | Retrieve historical stock split events, including execution dates and ratio factors, to understand changes in a company’s share structure over time. Massive leverages this data for accurate price adjustments in other endpoints, such as the Aggregates API, ensuring that users can access both adjusted and unadjusted views of historical prices for more informed analysis. Use Cases: Historical analysis, price adjustments, data consistency, modeling. | `GET /v3/reference/splits` |
| [Splits](https://massive.com/docs/rest/stocks/corporate-actions/splits.md) | Retrieve historical stock split events, including execution dates and ratio factors, to understand changes in a company’s share structure over time. Also find adjustment factors that can be used to normalize historical prices to today's share basis. Use Cases: Historical analysis, price adjustments, data consistency, modeling. | `GET /stocks/v1/splits` |
| [Dividends (Deprecated)](https://massive.com/docs/rest/stocks/corporate-actions/reference-dividends.md) | Retrieve a historical record of cash dividend distributions for a given ticker, including declaration, ex-dividend, record, and pay dates, as well as payout amounts and frequency. This endpoint consolidates key dividend information, enabling users to account for dividend income in returns, develop dividend-focused strategies, and support tax reporting needs. Use Cases: Income analysis, total return calculations, dividend strategies, tax planning. | `GET /v3/reference/dividends` |
| [Dividends](https://massive.com/docs/rest/stocks/corporate-actions/dividends.md) | Retrieve a historical record of cash dividend distributions for a given ticker, including declaration, ex-dividend, record, and pay dates, as well as payout amounts and adjustment factors for normalizing historical data to offset the effects of dividends. This endpoint consolidates key dividend information, enabling users to account for dividend income in returns, develop dividend-focused strategies, and support tax reporting needs. Use Cases: Income analysis, total return calculations, dividend strategies, tax planning. | `GET /stocks/v1/dividends` |
| [Ticker Events](https://massive.com/docs/rest/stocks/corporate-actions/ticker-events.md) | Retrieve a timeline of key events associated with a given ticker, CUSIP, or Composite FIGI. This endpoint is experimental and highlights ticker changes, such as symbol renaming or rebranding, helping users maintain continuity in their records and analyses. Use Cases: Historical reference for ticker symbol changes, data continuity, and record-keeping. | `GET /vX/reference/tickers/{id}/events` |
| **Fundamentals** | | |
| [Balance Sheets](https://massive.com/docs/rest/stocks/fundamentals/balance-sheets.md) | Retrieve comprehensive balance sheet data for public companies, containing quarterly and annual financial positions. This dataset includes detailed asset, liability, and equity positions representing the company's financial position at specific points in time. Balance sheet data represents point-in-time snapshots rather than cumulative flows, showing what the company owns, owes, and shareholders' equity as of each period end date. Use Cases: Financial analysis, company valuation, asset assessment, debt analysis, equity research. | `GET /stocks/financials/v1/balance-sheets` |
| [Cash Flow Statements](https://massive.com/docs/rest/stocks/fundamentals/cash-flow-statements.md) | Retrieve comprehensive cash flow statement data for public companies, including quarterly, annual, and trailing twelve-month cash flows. This dataset includes detailed operating, investing, and financing cash flows with TTM calculations that sum all cash flow components over four quarters. Use Cases: Cash flow analysis, liquidity assessment, operational efficiency evaluation, investment activity tracking. | `GET /stocks/financials/v1/cash-flow-statements` |
| [Income Statements](https://massive.com/docs/rest/stocks/fundamentals/income-statements.md) | Retrieve comprehensive income statement data for public companies, including key metrics such as revenue, expenses, and net income for various reporting periods. This dataset provides detailed financial performance data including revenue breakdowns, operating expenses, and profitability metrics across quarterly, annual, and trailing twelve-month periods. Use Cases: Profitability analysis, revenue trend analysis, expense management evaluation, earnings assessment. | `GET /stocks/financials/v1/income-statements` |
| [Ratios](https://massive.com/docs/rest/stocks/fundamentals/ratios.md) | Retrieve comprehensive financial ratios data providing key valuation, profitability, liquidity, and leverage metrics for public companies. This dataset combines data from income statements, balance sheets, and cash flow statements with daily stock prices to calculate ratios for the most recent trading day using trailing twelve months (TTM) financials. Use Cases: Company valuation, comparative analysis, financial health assessment, investment screening. | `GET /stocks/financials/v1/ratios` |
| [Short Interest](https://massive.com/docs/rest/stocks/fundamentals/short-interest.md) | Retrieve aggregated short interest data reported to FINRA by broker-dealers for a specified stock ticker on a two-week cadence. Short interest represents the total number of shares sold short but not yet covered or closed out, serving as an indicator of market sentiment and potential price movements. High short interest can signal bearish sentiment or highlight opportunities such as potential short squeezes. This endpoint provides essential insights for investors monitoring market positioning and sentiment. Use Cases: Market sentiment analysis, short-squeeze prediction, risk management, trading strategy refinement. | `GET /stocks/v1/short-interest` |
| [Short Volume](https://massive.com/docs/rest/stocks/fundamentals/short-volume.md) | Retrieve daily aggregated short sale volume data reported to FINRA from off-exchange trading venues and alternative trading systems (ATS) for a specified stock ticker. Unlike short interest, which measures outstanding short positions at specific reporting intervals, short volume captures the daily trading activity of short sales. Monitoring short volume helps users detect immediate market sentiment shifts, analyze trading behavior, and identify trends in short-selling activity that may signal upcoming price movements. Use Cases: Intraday sentiment analysis, short-sale trend identification, liquidity analysis, trading strategy optimization. | `GET /stocks/v1/short-volume` |
| [Float](https://massive.com/docs/rest/stocks/fundamentals/float.md) | Retrieve the latest free float for a specified stock ticker. Free float represents the shares outstanding that are considered available for public trading, after accounting for shares held by strategic or long-term holders. Shares held by founders, officers and directors, employees, controlling shareholders, affiliated companies, private equity and venture capital firms, sovereign wealth funds, government entities, employee plans, trusts, restricted or locked-up holdings, and any shareholder owning 5% or more of total issued shares are not treated as part of the tradable supply. Shares held by pension funds, mutual funds, ETFs, hedge funds without board representation, depositary banks, and other broadly diversified investors are generally treated as part of the public free float. Free float reflects a stock’s effective tradable supply and is a key input for assessing liquidity, volatility, market impact, and ownership structure. Figures may reflect ownership changes with a reporting lag, since they are based on publicly available disclosures and ownership information rather than real-time trading activity. Use cases: liquidity analysis, volatility modeling, position sizing, market impact estimation, and ownership structure analysis. | `GET /stocks/vX/float` |
| **Filings & Disclosures** | | |
| [EDGAR Index](https://massive.com/docs/rest/stocks/filings/index.md) | Retrieve the master index of all SEC EDGAR filings, including form types, filing dates, CIKs, tickers, issuer names, accession numbers, and direct links to original documents on SEC.gov. This serves as the central discovery layer for the entire EDGAR database, allowing powerful filtering and sorting without manual website searches. Use Cases: Automated filing discovery and monitoring, regulatory compliance alerts, due diligence pipelines, competitive intelligence, and historical disclosure research. | `GET /stocks/filings/vX/index` |
| [Annual Report Sections (10-K)](https://massive.com/docs/rest/stocks/filings/10-k-sections.md) | Retrieve clean plain-text extracts of key narrative sections from annual 10-K filings, including Business and Risk Factors. These provide detailed insights into company operations, strategy, markets, and material risks in structured AI-ready format. Use Cases: NLP and text analysis, automated risk profiling, competitive benchmarking, topic modeling, summarization, and LLM knowledge base construction. | `GET /stocks/filings/10-K/vX/sections` |
| [Material Event Text (8-K)](https://massive.com/docs/rest/stocks/filings/8-k-text.md) | Retrieve parsed plain-text content from the core Items sections of Form 8-K current reports. These disclose major material events such as acquisitions, leadership changes, material contracts, and other significant developments in AI-ready format. Use Cases: Real-time event detection and alerts, event-driven trading strategies, automated news digestion, M&A tracking, and corporate action timelines. | `GET /stocks/filings/8-K/vX/text` |
| [Event Disclosures (8-K)](https://massive.com/docs/rest/stocks/filings/8-k-disclosures.md) | SEC 8-K filing disclosure categorization. Each material event in a filing (leadership changes, acquisitions, material agreements, regulatory actions, etc.) is classified into a consistent three-tier taxonomy (primary, secondary, tertiary) with a supporting text excerpt directly from the filing. A single filing can produce multiple records when it contains multiple disclosures. Each record represents one tagged disclosure within the filing. The full taxonomy is available at `/stocks/taxonomies/vX/disclosures`. Use Cases: Event detection and alerts, event-driven trading strategies, M&A tracking, leadership-change monitoring, and corporate-action timelines. | `GET /stocks/filings/8-K/vX/disclosures` |
| [Disclosure Categories](https://massive.com/docs/rest/stocks/filings/disclosure-categories.md) | Access the full standardized hierarchical taxonomy used to classify disclosures in SEC Form 8-K filings. It includes primary, secondary, and tertiary categories with detailed descriptions, providing the controlled vocabulary that powers the 8-K disclosures endpoint. Use Cases: Event-classification models, category-level analytics and dashboards, cross-company comparisons, building category-aware filters, and thematic monitoring of corporate disclosures. | `GET /stocks/taxonomies/vX/disclosures` |
| [Institutional Holdings (13-F)](https://massive.com/docs/rest/stocks/filings/13-f-filings.md) | Retrieve quarterly holdings data from SEC Form 13-F filings submitted by institutional investment managers with at least $100 million in assets. Reports show equity positions, share counts, market values, investment discretion, and voting authority as of quarter-end. Use Cases: Tracking institutional ownership trends, replicating hedge fund strategies, portfolio overlap analysis, activist monitoring, and idea generation from smart-money flows. | `GET /stocks/filings/vX/13-F` |
| [Risk Factors](https://massive.com/docs/rest/stocks/filings/risk-factors.md) | Standardized, machine-readable risk factor disclosures from SEC filings. Each risk factor is categorized using a consistent taxonomy, enabling direct comparison across time periods or between different companies. For details on the methodology used, see our [research paper](https://arxiv.org/pdf/2601.15247). Use Cases: Risk trend analysis, cross-company comparisons, compliance tools, classification models, investment research. | `GET /stocks/filings/vX/risk-factors` |
| [Risk Categories](https://massive.com/docs/rest/stocks/filings/risk-categories.md) | Access the full standardized hierarchical taxonomy used to classify risk factors in SEC filings. It includes primary, secondary, and tertiary categories with detailed descriptions and examples for consistent analysis across companies and time periods. Use Cases: Risk classification models, category-level analytics and dashboards, cross-company comparisons, quantitative risk scoring, and thematic monitoring. | `GET /stocks/taxonomies/vX/risk-factors` |
| [Insider Ownership (Form 3)](https://massive.com/docs/rest/stocks/filings/form-3.md) | Retrieve SEC Form 3 filings that report the initial beneficial ownership of securities by corporate insiders (directors, officers, and 10%+ shareholders). These filings establish the baseline ownership position when an insider first becomes subject to Section 16 reporting requirements. Use Cases: Tracking new insider positions, monitoring executive and director ownership, due diligence on large shareholders, building ownership databases, and regulatory compliance checks. | `GET /stocks/filings/vX/form-3` |
| [Insider Transactions (Form 4)](https://massive.com/docs/rest/stocks/filings/form-4.md) | Retrieve SEC Form 4 filings that disclose all changes in beneficial ownership by corporate insiders. These must be filed within two business days of any transaction (purchases, sales, option exercises, grants, gifts, etc.) and include detailed transaction data such as dates, prices, share amounts, and transaction codes. Use Cases: Real-time insider trading monitoring, management confidence analysis, large trade detection, regulatory and Section 16 compliance tracking, and historical insider behavior studies. | `GET /stocks/filings/vX/form-4` |
| [News](https://massive.com/docs/rest/stocks/news.md) | Retrieve the most recent news articles related to a specified ticker, along with summaries, source details, and sentiment analysis. This endpoint consolidates relevant financial news in one place, extracting associated tickers, assigning sentiment, and providing direct links to the original sources. By incorporating publisher information, article metadata, and sentiment reasoning, users can quickly gauge market sentiment, stay informed on company developments, and integrate news insights into their trading or research workflows. Use Cases: Market sentiment analysis, investment research, automated monitoring, and portfolio strategy refinement. | `GET /v2/reference/news` |

## Market Hours and Timezone
Data is available for all U.S. market sessions, which are segmented into pre-market, regular market, and after-hours:

![U.S. stock market trading hours in Eastern Time (ET): Pre-market from 4:00 AM to 9:30 AM, regular hours from 9:30 AM to 4:00 PM, and after-hours from 4:00 PM to 8:00 PM.](https://massive.com/docs/img/graphic-timezone-light.svg)

- Pre-Market Trading Hours: From 4:00 AM to 9:30 AM Eastern Time (ET).
- Regular Market Hours: From 9:30 AM to 4:00 PM ET.
- After-Hours Trading: From 4:00 PM to 8:00 PM ET.

All timestamps in the datasets are provided as Unix timestamps (seconds since epoch, UTC). When converting these timestamps into human-readable form (e.g., market open at 9:30 AM), remember they represent UTC time, not Eastern Time (ET). To correctly align data with market hours or dates, you'll need to explicitly convert timestamps from UTC to ET during your analysis.

## Infrastructure and Reliability
Our platform's robustness begins with our primary data facility at the Equinix Data Center in New Jersey, strategically co-located with the exchanges. This setup allows us to receive data through direct physical connections, significantly reducing latency and enhancing the reliability of the data. Initially established in New Jersey, our infrastructure has expanded to include full redundancy at the ORD11 data center in Chicago. This expansion ensures uninterrupted service and data availability, even under adverse conditions, across multiple geographic locations.

Our data is sourced directly from proprietary exchange feeds and government-regulated consolidators known as Securities Information Processors (SIPs). By combining direct exchange access with regulated data consolidation, we ensure the provision of the most accurate and timely market data available. This infrastructure supports a wide range of financial data services and applications, offering our clients resilience, speed, and compliance with the highest industry standards.

## Data Flow: From Exchanges to You
Our stock market data journey begins at the numerous trading venues across the U.S., encompassing all 19 major stock exchanges and additional dark pools. We maintain direct relationships with each exchange and comply with all licensing requirements, ensuring our data includes every trade, quote, and market event as it occurs.

![The flow of U.S. stock market data from major exchanges (e.g., NYSE, Nasdaq, Cboe) and dark pools through direct connections to Massive's co-located data facilities.](https://massive.com/docs/img/graphic-stocks-dataflow-light.svg)

Our data facility, co-located with the exchanges in the Equinix Data Center in New Jersey, receives this data through direct physical connections. This setup not only guarantees the fastest possible data transmission due to our proximity to the source but also enhances the reliability and integrity of the data we deliver.

This extensive coverage includes major platforms such as:

- New York Stock Exchange (NYSE, NYSE American, NYSE Arca, NYSE Chicago, NYSE National)
- Nasdaq (OMX, BX, PSX, Philadelphia)
- Cboe Global Markets (BZX, BYX, EDGX, EDGA)
- MIAX Exchange Group (Pearl, Emerald, Equities)
- Members Exchange (MEMX)
- Investors Exchange (IEX)
- Long-Term Stock Exchange (LTSE)

Additionally, our dataset is enriched with trade data from:

- FINRA Trading Facilities: including FINRA NYSE TRF, FINRA Nasdaq TRF Carteret, and FINRA Nasdaq TRF Chicago, which provide comprehensive trade reporting but not quotes.
- OTC Reporting Facility: captures trades from over-the-counter markets but not quotes.

While our core data includes every trade and quote from the major stock exchanges, it's important to note that for the FINRA and OTC platforms, we exclusively capture trade information. This distinction is crucial for users relying on our data for accurate market analysis and decision-making.

From these diverse sources, the raw data is channeled to Securities Information Processors (SIPs). Our broad coverage across these platforms allows us to offer a complete view of the U.S. stock market landscape, making our data essential for those requiring comprehensive market insights. By integrating and processing this data, we ensure that all market participants have access to the full spectrum of market activities, empowering them with the data needed to make informed decisions.

## What are Securities Information Processors (SIPs)?

Securities Information Processors (SIPs) are integral to the U.S. market data system, consolidating trade and quote data from all exchanges into a single feed, which includes the official National Best Bid and Offer (NBBO) and last sale data. We receive this consolidated data directly from SIPs such as the Consolidated Tape Association (CTA) for NYSE-listed and regional exchange securities (Tapes A and B), and the Unlisted Trading Privileges (UTP), managed by Nasdaq, for all Nasdaq-listed securities (Tape C). Additionally, our platform includes data from Alternative Trading Systems (ATSs), which are required to report executed trades to FINRA within 10 seconds. We access these trades directly from the FINRA feed, enriching our dataset with comprehensive on-exchange and off-exchange trading activity.

SIPs are vital infrastructure in the U.S. financial markets, designed to consolidate and standardize the torrent of information from various exchanges. Their primary function is to ensure all market participants have equal access to trade and quote data, which is essential for maintaining a transparent and fair trading environment. SIPs compile this data into a consolidated stream that includes the National Best Bid and Offer (NBBO) and trade information, thus providing the official record of stock prices and transactions.

After processing by the SIPs, this consolidated data is delivered to Massive, where we further refine and distribute it to our users through our REST APIs, WebSocket streams, and Flat Files. This structured data flow ensures that you receive comprehensive, accurate, and timely market data to power your applications and analyses.

## Regulatory Compliance
U.S. stock market data regulations allow us to provide the full U.S. feed, covering all exchanges, to non-industry professionals for personal use. We closely monitor compliance to ensure these data feeds are used appropriately. For business clients, we offer tailored plans that may include specific exchange licensing requirements, providing a flexible approach to meet diverse professional needs. This ensures that our platform can serve a broad spectrum of users from casual individual traders to large institutional clients.

## Next Steps
Explore our REST API endpoints to fully harness the capabilities of our extensive market data. Our detailed documentation will guide you through integrating real-time and historical data into your applications, helping you make informed decisions backed by comprehensive and timely market insights.
