# marketstack.com

## Fetch log
- Inbox URL: https://marketstack.com/
- Final URL: https://marketstack.com/
- Fetched: 2026-07-06
- Pages: 5
- Mode: standard

## Landing page — https://marketstack.com/

Free Stock Market Data API for Real-Time & Historical Data

Stock Data

# Real-Time, Intraday & Historical Market along with EDGAR Filings API.

## Free, easy-to-use REST API interface delivering worldwide stock market and EDGAR data in JSON format

100 Monthly Requests

Free End-of-Day stock data from 30,000+ tickers around the world.

FREE Get API Key

Real-Time & Intraday

Intraday market data & real-time updates for US tickers.

From $9.99 Pricing

- Trusted by 30,000+ Happy Customers:

**EDGAR Filings Access**
Seamlessly fetch company filings with our 6 new EDGAR endpoints. Access 10-K, 10-Q, 8-K, and other SEC documents in real-time to power financial research and compliance.

##### Every Minute, Every Day

Obtain real-time stock data for more than 30,000 tickers down to the minute, request intraday quotes for tickers from IEX, or search 15+ years of accurate EOD historical market data.

##### Stock Tickers

Easily integrate the API and make use of 30,000+ worldwide stock tickers with our Stock Price endpoint or integrate more than 500,000 tickers with our EOD endpoint collected from more global exchanges, including Nasdaq, NYSE, and more.

##### Simple, Quick & Reliable

We have built a simple, powerful and scalable REST API with an uptime of close to 100%. It will take you less than 5 minutes to get started.

##### Free Plan Available

Get up and running quickly using the Free Plan, allowing for 100 data requests per month. Instant access, no contract or payment required.

## Intuitive APIs. Effortless Integration. Limitless Opportunities.

From currencies to weather, PDFs to more, our API marketplace has it all. Start exploring today and find the perfect building blocks for your next project.

Browse All APIs

#### Covering More Global Exchanges

##### Tap into a world of market data, supporting real-time, intraday, and historical data from global stock exchanges.

- Real-Time Stock Prices for 30,000+ tickers
- Intraday Market Data from IEX
- 15+ Years EOD Historical Data
- 500,000+ Stock Tickers in EOD
- 750+ Market Indices
- Detailed Information for 2700+ stock exchanges
Search Stock Tickers

70 Stock Exchanges

#### A complete, easy-to-use JSON API for your market data needs

##### Our stock market API is powered by cutting-edge technology and highly scalable cloud infrastructure, capable of handling anything from a few hundred requests per month all the way to millions of hits per day. No matter which volume - we've got you covered!

- Lightweight JSON API — Requests are made using a simple HTTP GET structure and API response data is delivered in lightweight JSON format.
- Bank-Level Security — Each bit and byte sent to and from the marketstack API is encrypted using industry-standard 256-bit HTTPS encryption.
- Extensive Documentation — A straightforward API documentation will help you get up and running within minutes using interactive demo requests and code examples in a variety of programming languages. Explore API Documentation

#### 30,000+ companies and 80+ universities can't be wrong

##### You're in good company. Join some of the largest companies and most reputable universities out there using the marketstack stock API.

The API is free for up to 100 monthly requests. Get your API key today Get Free API Key

marketstack Logo — an APILayer product.


## Product & pricing — https://marketstack.com/product

# Market Data Subscription Plans

#### Free — $0/month
- 100 Requests / mo
- No Support
- End-of-Day Data
- 1 Year History
- Splits & Dividends
- Stock Tickers Info
- 2700+ Stock Exchanges Info
- Currencies & Timezones
- HTTPS Encryption

#### Basic — $9.99/month ($8.99 yearly)
- 10,000 Requests / mo (+ $0.003996 each)
- End-of-Day Data, 10 Years History
- IEX Intraday Data (US)
- Stock Market Index, Bonds, ETF Holding
- Standard Support, Commercial Use

#### Professional — $49.99/month ($43.99 yearly)
- 100,000 Requests / mo (+ $0.0019996 each)
- 15+ Years History
- Real-Time Updates, Real-time Stock Market Prices
- Commodity Prices, Commodities History Prices

#### Business — $149.99/month ($127.99 yearly)
- 500,000 Requests / mo (+ $0.00119992 each)
- Company Ratings, Company Statements, Company Details, Company Concepts, Company Facts

#### Enterprise — Custom pricing
- Volume Requests, Custom Solutions

Real-Time Updates: Intraday data with data frequency intervals below 15 minutes (15min), like 1min, 5min, 10min.

- 30,000+ Stock Tickers
- 70 Stock Exchanges
- 750+ Market Indices
- 30,000+ Happy Customers
- 80+ Universities

### FAQ highlights

Where is the data coming from?
Stock market data provided by the marketstack API is licensed and sourced from multiple high-authority market data providers around the world. Stock market data from United States exchanges is licensed and sourced from Tiingo, Inc. out of New York City, USA.

How scalable is this service?
The marketstack API service is built on top of apilayer cloud infrastructure and therefore comes with a significant level of scalability and performance. The API currently handles several million API requests per hour with ease.

What is the API's uptime?
The marketstack API's system status is kept track of 24/7 by the apilayer team. We keep the amount of outages or service disruptions at a minimum and are proud to have an uptime of nearly 100%, calculated based on the last 365 days. Public status page: status.marketstack.com.


## Docs — Getting Started — https://docs.apilayer.com/marketstack/docs/getting-started

### API Access Key & Authentication

For every API request you make, you will need to make sure to be authenticated with the API by passing your API access key to the API's `access_key` parameter.

Example API Request:
```
https://api.marketstack.com/v2/eod
    ? access_key = YOUR_ACCESS_KEY
    & symbols = AAPL
```

Important: Please make sure not to expose your API access key publicly. If you believe your API access key may be compromised, you can always reset in your account dashboard.

## 256-bit HTTPS Encryption

If you're subscribed to either the free or any paid plans, you will be able to access the Marketstack API using industry-standard HTTPS.

Example API Request (Available on: All Plans):
```
https://api.marketstack.com/v2
```

## API Error Codes

API errors consist of error `code` and `message` response objects. If an error occurs, the marketstack will return HTTP status codes, such as `404` for "not found" errors. If your API request succeeds, a status code `200` will be sent.

Example Error:
```
{
   "error": {
      "code": "validation_error",
      "message": "Request failed with validation error",
      "context": {
         "symbols": [
            {
               "key": "missing_symbols",
               "message": "You did not specify any symbols."
            }
         ]
      }
   }
}
```

### Common API Errors

| Code | Type | Description |
| --- | --- | --- |
| 401 | unauthorized | Authentication failed. Please verify your access key or account status. |
| 403 | function_access_restricted | This API endpoint is not available under your current subscription plan. |
| 404 | invalid_api_function | The specified API endpoint does not exist. |
| 404 | 404_not_found | The requested resource could not be found. |
| 429 | too_many_requests | The account has exceeded the allowed monthly request quota. |
| 429 | rate_limit_reached | The given user account has reached the rate limit. |
| 500 | internal_error | An internal server error has occurred. |
| 406 | data_not_available | The requested data is currently unavailable. |

Note: The API is limited to 5 requests per second.

Documentation hosted at docs.apilayer.com (redirects from marketstack.com/documentation).


## API Endpoints v1 — https://docs.apilayer.com/marketstack/docs/api-endpoints-v1

Markdown Content:
> **Note:** All the new functionalities and new endpoints listed in the pricing plans are designed for use with the new API endpoints in [**Version V2**](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0). Please refer to the [V2 API endpoints documentation page](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0) for proper usage of the service. Please be aware that **Version V1** of the API endpoints will be deprecated for use after June 30th, 2025.

Welcome to the Marketstack API documentation! In the following series of articles, you will learn how to query the Marketstack JSON API for real-time, intraday, and historical stock market data, define multiple stock symbols, retrieve extensive data about 70+ stock exchanges, 170,000+ stock tickers from more than 50 countries, as well as 750+ market indices, information about time zones, currencies, and more.

Our API is built on a RESTful, easy-to-understand request-and-response structure. API requests are always sent using a simple API request URL with a series of required and optional HTTP GET parameters, and API responses are provided in lightweight JSON format. Continue below to get started, or click the button above to jump to our 3-Step Quickstart Guide.

[**Quickstart Guide**](https://docs.apilayer.com/marketstack/docs/quickstart-guide)
## Supported Endpoint

## End-of-Day Data

You can use the API's `eod` endpoint to obtain end-of-day data for one or multiple stock tickers. A single or multiple comma-separated ticker symbols are passed to the API using the `symbols` parameter.

> **Note:** To request end-of-day data for single ticker symbols, you can also use the API's [Tickers Endpoint](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/Tickers/get_tickers__symbol_ "Tickers Endpoint").

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/eod
    ? access_key = YOUR_ACCESS_KEY
    & symbols = AAPL
```

**Endpoint Features:**

| **Object** | **Description** |
| --- | --- |
| `/eod/[date]` | **Specify a date in YYYY-MM-DD format. You can also specify an exact time in ISO-8601 date format, e.g. 2020-05-21T00:00:00+0000. Example: /eod/2020-01-01** |
| `/eod/latest` | **Obtain the latest available end-of-day data for one or multiple stock tickers.** |

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required] Specify your API access key, available in your**[**account dashboard**](https://marketstack.com/login?utm_source=DocumentationPage&utm_medium=Referral)**.** |
| `symbols` | **[Required] Specify one or multiple comma-separated stock symbols (tickers) for your request, e.g. AAPL or AAPL,MSFT. Each symbol consumes one API request. Maximum: 100 symbols** |
| `exchange` | **[Optional] Filter your results based on a specific stock exchange by specifying the MIC identification of a stock exchange. Example: XNAS** |
| `sort` | **[Optional] By default, results are sorted by date/time descending. Use this parameter to specify a sorting order. Available values: DESC (Default), ASC.** |
| `date_from` | **[Optional] Filter results based on a specific timeframe by passing a from-date in YYYY-MM-DD format. You can also specify an exact time in ISO-8601 date format, e.g. 2020-05-21T00:00:00+0000.** |
| `date_to` | **[Optional] Filter results based on a specific timeframe by passing an end-date in YYYY-MM-DD format. You can also specify an exact time in ISO-8601 date format, e.g. 2020-05-21T00:00:00+0000.** |
| `limit` | **[Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is 100, maximum allowed limit value is 1000.** |
| `offset` | **[Optional] Specify a pagination offset value for your API request. Example: An offset value of 100 combined with a limit value of 10 would show results 100-110. Default value is 0, starting with the first available result.** |

**Example API Response:**If your API request was successful, the Marketstack API will return both `pagination` information as well as a `data` object, which contains a separate sub-object for each requested date/time and symbol. All response objects are explained below.

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 9944
    },
    "data": [
        {
            "open": 129.8,
            "high": 133.04,
            "low": 129.47,
            "close": 132.995,
            "volume": 106686703.0,
            "adj_high": 133.04,
            "adj_low": 129.47,
            "adj_close": 132.995,
            "adj_open": 129.8,
            "adj_volume": 106686703.0,
            "split_factor": 1.0,
            "dividend": 0.0,
            "symbol": "AAPL",
            "exchange": "XNAS",
            "date": "2021-04-09T00:00:00+0000"
            },
            [...]
    ]
}
```

**API Response Objects:**

| Response Object | Description |
| --- | --- |
| `pagination > limit` | Returns your pagination limit value. |
| `pagination > offset` | Returns your pagination offset value. |
| `pagination > count` | Returns the results count on the current page. |
| `pagination > total` | Returns the total count of results available. |
| `date` | Returns the exact UTC date/time the given data was collected in ISO-8601 format. |
| `symbol` | Returns the stock ticker symbol of the current data object. |
| `exchange` | Returns the exchange MIC identification associated with the current data object. |
| `split_factor` | Returns the split factor, which is used to adjust prices when a company splits, reverse splits, or pays a distribution. |
| `dividend` | Returns the dividend, which are the distribution of earnings to shareholders. |
| `open` | Returns the raw opening price of the given stock ticker. |
| `high` | Returns the raw high price of the given stock ticker. |
| `low` | Returns the raw low price of the given stock ticker. |
| `close` | Returns the raw closing price of the given stock ticker. |
| `volume` | Returns the raw volume of the given stock ticker. |
| `adj_open` | Returns the adjusted opening price of the given stock ticker. |
| `adj_high` | Returns the adjusted high price of the given stock ticker. |
| `adj_low` | Returns the adjusted low price of the given stock ticker. |
| `adj_close` | Returns the adjusted closing price of the given stock ticker. |
| `adj_volume` | Returns the adjusted volume of given stock ticker. |

> **Adjusted Prices:** "Adjusted" prices are stock price values that were amended to accurately reflect the given stock's value after accounting for any corporate actions, such as splits or dividends. Adjustments are made in accordance with the "CRSP Calculations" methodology set forth by the Center for Research in Security Prices (CRSP).

**End-of-Day Data:**You can use the API's eod endpoint in order to obtain end-of-day data for one or multiple stock tickers. A single or multiple comma-separated ticker symbols are passed to the API using the symbols parameter.

**JavaScript Fetch**

```
const url = "https://api.marketstack.com/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL";
const options = {
    method: "GET",
};

try {
    const response = await fetch(url, options);
    const result = await response.text();
    console.log(result);
} catch (error) {
    console.error(error);
}
```

**JavaScript Axios**

```
import axios from "axios";
const options = {
   method: "GET",
   url: "https://api.marketstack.com/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}",
   params: {
       symbols: "AAPL",
   },
};
try {
   const response = await axios.request(options);
   console.log(response.data);
} catch (error) {
   console.error(error);
}
```

**Python Request**

```
import requests
url = "https://api.marketstack.com/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}"
querystring = {"symbols":"AAPL"}
response = requests.get(url, params=querystring)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Market Indices

The API is also capable of delivering end-of-day for 750+ of the world's major indices, including the S&P 500 Index, the Dow Jones Industrial Average Index as well as the NASDAQ Composite Index. Index data is available both on a "`latest`" basis as well as historically.

To list or access index data, simply pass `INDX` as your stock exchange MIC identification, as seen in the examples below. The example API request below illustrates how to obtain end-of-day data for the `DJI` market index.

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/eod
    ? access_key = YOUR_ACCESS_KEY
    & symbols = DJI.INDX
```

**Parameters:**For more information about request parameters, please refer to the [End-of-day Data](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/End-of-day/get_eod "EOD endpoint") section of this documentation.

**API Response:**

```
{
    "pagination": {
        "limit": 1,
        "offset": 0,
        "count": 1,
        "total": 7561
    },
    "data": [
        {
            "date": "2020-08-21T00:00:00+0000",
            "symbol": "DJI.INDX",
            "exchange": "INDX",
            "open": 27758.1309,
            "high": 27959.4805,
            "low": 27686.7793,
            "close": 27930.3301,
            "volume": 374339179,
            "adj_high": null,
            "adj_low": null,
            "adj_close": 27930.3301,
            "adj_open": null,
            "adj_volume": null
        }
    ]
}
```

**API Response Objects:**For more information about response objects, please refer to the [End-of-day Data](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/End-of-day/get_eod "EOD endpoint") section of this documentation.

**Market Indices in Other API Endpoints:**

| **Object** | **Description** |
| --- | --- |
| `/exchanges/INDX/tickers` | Obtain all available market indices by passing `INDX` as the exchange MIC identification. |
| `/tickers/[symbol].INDX` | Obtain meta information for a specific market index. |
| `/tickers/[symbol].INDX/eod` | Obtain end-of-day data for a specific market index. |

## Historical Data

Historical stock prices are available both from the end-of-day (`eod`) and intraday (`intraday`) API endpoints. To obtain historical data, simply use the `date_from` and `date_to` parameters as shown in the example request below.

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/eod
    ? access_key = YOUR_ACCESS_KEY
    & symbols = AAPL
    & date_from = 2026-02-27
    & date_to = 2026-03-09
```

**Parameters:**For details on request parameters on the `eod` data endpoint, please jump to the [End-of-Day Data](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/End-of-day/get_eod "End-of-Day Stock Data") section.

**Example API Response:**

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 22,
        "total": 22
    },
    "data": [
        {
            "date": "2019-02-01T00:00:00+0000",
            "symbol": "AAPL",
            "exchange": "XNAS",
            "open": 166.96,
            "high": 168.98,
            "low": 165.93,
            "close": 166.52,
            "volume": 32668138.0,
            "adj_open": 164.0861621594,
            "adj_high": 166.0713924395,
            "adj_low": 163.073891274,
            "adj_close": 163.6537357617,
            "adj_volume": 32668138.0
        },
        {
            "date": "2019-01-31T00:00:00+0000",
            "symbol": "AAPL",
            "exchange": "XNAS",
            "open": 166.11,
            "high": 169.0,
            "low": 164.56,
            "close": 166.44,
            "volume": 40739649.0,
            "adj_open": 163.2507929821,
            "adj_high": 166.0910481848,
            "adj_low": 161.7274727177,
            "adj_close": 163.5751127804,
            "adj_volume": 40739649.0
        }
        [...]
    ]
}
```

**API Response Objects:**For details on API response objects, please jump to the [End-of-Day Data](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/End-of-day/get_eod "End-of-Day Stock Data") section.

> **Note:** Historical end-of-day data (`eod`) is available for up to 30 years back, while intraday data (`intraday`) always only offers the last 10,000 entries for each of the intervals available. Example: For a 1-minute interval, historical intraday data is available for up to 10,000 minutes back.

**Historial Data:**Historical stock prices are available both from the `end-of-day (eod)` and`intraday (intraday)`API endpoints. To obtain historical data, simply use the `date_from`and `date_to`parameters as shown in the example request below.

**JavaScript Fetch**

```
const url =
    "https://api.marketstack.com/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL&date_from=2024-02-26&date_to=2024-03-07";
const options = {
    method: "GET",
};

try {
    const response = await fetch(url, options);
    const result = await response.text();
    console.log(result);
} catch (error) {
    console.error(error);
}
```

**JavaScript Axios**

```
import axios from "axios";
const options = {
   method: "GET",
   url: "https://api.marketstack.com/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}",
   params: {
       symbols: "AAPL",
       date_from: "2024-02-26",
       date_to: "2024-03-07",
   },
};
try {
   const response = await axios.request(options);
   console.log(response.data);
} catch (error) {
   console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}"
querystring = {"symbols":"AAPL","date_from":"2024-02-26", "date_to":"2024-03-07"}
response = requests.get(url, params=querystring)
print(response.json())
```

**Python Http.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/eod?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL&date_from=2024-02-26&date_to=2024-03-07")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Intraday Data

In additional to daily end-of-day stock prices, the marketstack API also supports intraday data with data intervals as short as one minute. Intraday prices are available for all US stock tickers included in the IEX (Investors Exchange) stock exchange.

To obtain intraday data, you can use the API's `intraday` endpoint and specify your preferred stock ticker symbols.

> **Note:** To request intraday data for single ticker symbols, you can also use the API's [Tickers Endpoint](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/Tickers/get_tickers__symbol_ "Tickers Endpoint").

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/intraday
    ? access_key = YOUR_ACCESS_KEY
    & symbols = AAPL
```

**Endpoint Features:**

| **Object** | **Description** |
| --- | --- |
| `/intraday/[date]` | Specify a date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. Example: `/intraday/2020-01-01` |
| `/intraday/latest` | Obtain the latest available intraday data for one or multiple stock tickers. |

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required]** Specify your API access key, available in your [account dashboard](https://marketstack.com/login/?utm_source=DocumentationPage&utm_medium=Referral "API Access K Key"). |
| `symbols` | **[Required]** Specify one or multiple comma-separated stock symbols (tickers) for your request, e.g. `AAPL` or `AAPL,MSFT`. Each symbol consumes one API request. Maximum: 100 symbols |
| `exchange` | [Optional] Filter your results based on a specific stock exchange by specifying the MIC identification of a stock exchange. Example: `IEXG` |
| `interval` | [Optional] Specify your preferred data interval. Available values: `1min`, `5min`, `10min`, `15min`, `30min`, `1hour` (Default), `3hour`, `6hour`, `12hour` and `24hour`. |
| `sort` | [Optional] By default, results are sorted by date/time descending. Use this parameter to specify a sorting order. Available values: `DESC` (Default), `ASC`. |
| `date_from` | [Optional] Filter results based on a specific timeframe by passing a from-date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. |
| `date_to` | [Optional] Filter results based on a specific timeframe by passing an end-date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. |
| `limit` | [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is `100`, maximum allowed limit value is `1000`. |
| `offset` | [Optional] Specify a pagination offset value for your API request. Example: An offset value of `100` combined with a limit value of 10 would show results 100-110. Default value is `0`, starting with the first available result. |

**Real-Time Updates:** Please note that data frequency intervals below 15 minutes (`15min`) are only supported if you are subscribed to the Professional Plan or higher. If you are the Free or Basic Plan, please [upgrade your account](https://marketstack.com/login/?utm_source=DocumentationPage&utm_medium=Referral "Pricing Plans").

**Example API Response:**If your API request was successful, the marketstack API will return both `pagination` information as well as a `data` object, which contains a separate sub-object for each requested date/time and symbol. All response objects are explained below.

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 5000
    },
    "data": [
        {
            "date": "2020-06-02T00:00:00+0000"
            "symbol": "AAPL",
            "exchange": "IEXG",
            "open": 317.75,
            "high": 322.35,
            "low": 317.21,
            "close": 317.94,
            "last": 318.91,
            "volume": 41551000
        },
        [...]
    ]
}
```

**API Response Objects:**

| **Response Object** | **Description** |
| --- | --- |
| `pagination`>`limit` | Returns your pagination limit value. |
| `pagination`>`offset` | Returns your pagination offset value. |
| `pagination`>`count` | Returns the results count on the current page. |
| `pagination`>`total` | Returns the total count of results available. |
| `date` | Returns the exact UTC date/time the given data was collected in ISO-8601 format. |
| `symbol` | Returns the stock ticker symbol of the current data object. |
| `exchange` | Returns the exchange MIC identification associated with the current data object. |
| `open` | Returns the raw opening price of the given stock ticker. |
| `high` | Returns the raw high price of the given stock ticker. |
| `low` | Returns the raw low price of the given stock ticker. |
| `close` | Returns the raw closing price of the given stock ticker. |
| `last` | Returns the last executed trade of the given symbol on its exchange. |
| `volume` | Returns the volume of the given stock ticker. |

**Intraday Data:**

**JavaScript Fetch**

```
const url = "https://api.marketstack.com/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL";
const options = {
    method: "GET",
};

try {
    const response = await fetch(url, options);
    const result = await response.text();
    console.log(result);
} catch (error) {
    console.error(error);
}
```

**JavaScript Axios**

```
import axios from "axios";
const options = {
   method: "GET",
   url: "https://api.marketstack.com/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}",
   params: {
       symbols: "AAPL",
   },
};
try {
   const response = await axios.request(options);
   console.log(response.data);
} catch (error) {
   console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}"
querystring = {"symbols":"AAPL"}
response = requests.get(url, params=querystring)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

**Real-Time Updates**

For customers with an active subscription to the Professional Plan, the marketstack API's `intraday` endpoint is also capable of providing real-time market data, updated every minute, every 5 minutes or every 10 minutes.

To obtain real-time data using this endpoint, simply append the API's `interval` parameter and set it to `1min`, `5min` or `10min`.

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/intraday
    ? access_key = YOUR_ACCESS_KEY
    & symbols = AAPL
    & interval = 1min
```

**Endpoint Features, Parameters & API Response:**To learn about endpoint features, request parameters and API response objects, please navigate to the [Intraday Data](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/Intraday/get_intraday "Intraday Data") section.

**Real-Time-Updates:**Specify the interval parameter and set it to 1min, 5min or 10min to obtain real-time data using this endpoint.

**JavaScript Fetch**

```
const url = "https://api.marketstack.com/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL&interval=1min";
const options = {
    method: "GET",
};

try {
    const response = await fetch(url, options);
    const result = await response.text();
    console.log(result);
} catch (error) {
    console.error(error);
}
```

**JavaScript Axios**

```
import axios from "axios";
const options = {
   method: "GET",
   url: "https://api.marketstack.com/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}",
   params: {
       symbols: "AAPL",
       interval: "1min",
   },
};
try {
   const response = await axios.request(options);
   console.log(response.data);
} catch (error) {
   console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}"
querystring = {"symbols":"AAPL","interval":"1min"}
response = requests.get(url, params=querystring)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/intraday?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL&interval=1min")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Splits Data

Using the APIs `splits`endpoint you will be able to look up information about the stock splits factor for different symbols. You will be able to find and try out an example API request below.

To obtain splits data, you can use the API's `splits` endpoint and specify your preferred stock ticker symbols.

> **Note:** To request splits data for single ticker symbols, you can also use the API's [Tickers Endpoint](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/Tickers/get_tickers__symbol_ "Tickers Endpoint").

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/splits
    ? access_key = YOUR_ACCESS_KEY
    & symbols = AAPL
```

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required]** Specify your API access key, available in your [account dashboard](https://marketstack.com/login/?utm_source=DocumentationPage&utm_medium=Referral "API Access K Key"). |
| `symbols` | **[Required]** Specify one or multiple comma-separated stock symbols (tickers) for your request, e.g. `AAPL` or `AAPL,MSFT`. Each symbol consumes one API request. Maximum: 100 symbols |
| `sort` | [Optional] By default, results are sorted by date/time descending. Use this parameter to specify a sorting order. Available values: `DESC` (Default), `ASC`. |
| `date_from` | [Optional] Filter results based on a specific timeframe by passing a from-date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. |
| `date_to` | [Optional] Filter results based on a specific timeframe by passing an end-date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. |
| `limit` | [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is `100`, maximum allowed limit value is `1000`. |
| `offset` | [Optional] Specify a pagination offset value for your API request. Example: An offset value of `100` combined with a limit value of 10 would show results 100-110. Default value is `0`, starting with the first available result. |

**Example API Response:**If your API request was successful, the marketstack API will return both `pagination` information as well as a `data` object, which contains a separate sub-object for each requested date/time and symbol. All response objects are explained below.

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 50765
    },
    "data": [
        {
            "date": "2021-05-24",
            "split_factor": 0.5,
            "symbol": "IAU"
        },
        [...]
    ]
}
```

**API Response Objects:**

| **Response Object** | **Description** |
| --- | --- |
| `pagination`>`limit` | Returns your pagination limit value. |
| `pagination`>`offset` | Returns your pagination offset value. |
| `pagination`>`count` | Returns the results count on the current page. |
| `pagination`>`total` | Returns the total count of results available. |
| `date` | Returns the exact UTC date/time the given data was collected in ISO-8601 format. |
| `symbol` | Returns the stock ticker symbol of the current data object. |
| `volume` | Returns the split factor for that symbol on the date. |

**Splits Data:**

**JavaScript Fetch**

```
const url = 'https://api.marketstack.com/v1/splits?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL';
const options = {
	method: 'GET'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}
```

**JavaScript Axios**

```
import axios from 'axios';
const options = {
 method: 'GET',
 url: 'https://api.marketstack.com/v1/splits?access_key={PASTE_YOUR_API_KEY_HERE}',
 params: {
   symbols: "AAPL",
 }
};
try {
    const response = await axios.request(options);
    console.log(response.data);
} catch (error) {
    console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/splits?access_key={PASTE_YOUR_API_KEY_HERE}"
querystring = {"symbols":"AAPL"}
response = requests.get(url, params=querystring)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/splits?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Dividends Data

Using the APIs `dividends`endpoint you will be able to look up information about the stock dividend for different symbols. You will be able to find and try out an example API request below.

To obtain dividends data, you can use the API's `dividends` endpoint and specify your preferred stock ticker symbols.

> **Note:** To request dividends data for single ticker symbols, you can also use the API's [Tickers Endpoint](https://docs.apilayer.com/marketstack/docs/marketstack-api-v2-v-2-0-0#/Tickers/get_tickers__symbol_ "Tickers Endpoint").

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/dividends
    ? access_key = YOUR_ACCESS_KEY
    & symbols = AAPL
```

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required]** Specify your API access key, available in your [account dashboard](https://marketstack.com/dashboard "API Access K Key"). |
| `symbols` | **[Required]** Specify one or multiple comma-separated stock symbols (tickers) for your request, e.g. `AAPL` or `AAPL,MSFT`. Each symbol consumes one API request. Maximum: 100 symbols |
| `sort` | [Optional] By default, results are sorted by date/time descending. Use this parameter to specify a sorting order. Available values: `DESC` (Default), `ASC`. |
| `date_from` | [Optional] Filter results based on a specific timeframe by passing a from-date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. |
| `date_to` | [Optional] Filter results based on a specific timeframe by passing an end-date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. |
| `limit` | [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is `100`, maximum allowed limit value is `1000`. |
| `offset` | [Optional] Specify a pagination offset value for your API request. Example: An offset value of `100` combined with a limit value of 10 would show results 100-110. Default value is `0`, starting with the first available result. |

**Example API Response:**If your API request was successful, the marketstack API will return both `pagination` information as well as a `data` object, which contains a separate sub-object for each requested date/time and symbol. All response objects are explained below.

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 50765
    },
    "data": [
        {
            "date": "2021-05-24",
            "dividend": 0.5,
            "symbol": "IAU"
        },
        [...]
    ]
}
```

**API Response Objects:**

| **Response Object** | **Description** |
| --- | --- |
| `pagination`>`limit` | Returns your pagination limit value. |
| `pagination`>`offset` | Returns your pagination offset value. |
| `pagination`>`count` | Returns the results count on the current page. |
| `pagination`>`total` | Returns the total count of results available. |
| `date` | Returns the exact UTC date/time the given data was collected in ISO-8601 format. |
| `symbol` | Returns the stock ticker symbol of the current data object. |
| `volume` | Returns the dividend for that symbol on the date. |

**Dividends Data:**

**JavaScript Fetch**

```
const url = 'https://api.marketstack.com/v1/dividends?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL';
const options = {
	method: 'GET'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}
```

**JavaScript Axios**

```
import axios from 'axios';
const options = {
 method: 'GET',
 url: 'https://api.marketstack.com/v1/dividends?access_key={PASTE_YOUR_API_KEY_HERE}',
 params: {
   symbols: "AAPL",
 }
};
try {
    const response = await axios.request(options);
    console.log(response.data);
} catch (error) {
    console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/dividends?access_key={PASTE_YOUR_API_KEY_HERE}"
querystring = {"symbols":"AAPL"}
response = requests.get(url, params=querystring)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/dividends?access_key={PASTE_YOUR_API_KEY_HERE}&symbols=AAPL")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Tickers

Using the API's `tickers` endpoint you will be able to look up information about one or multiple stock ticker symbols as well as obtain end-of-day, real-time and intraday market data for single tickers. You will be able to find and try out an example API request below.

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/tickers
    ? access_key = YOUR_ACCESS_KEY
```

**Endpoint Features:**

| **Object** | **Description** |
| --- | --- |
| `/tickers/[symbol]` | Obtain information about a specific ticker symbol by attach it to your API request URL, e.g. `/tickers/AAPL`. |
| `/tickers/[symbol]/eod` | Obtain end-of-day data for a specific stock ticker by attaching `/eod` to your URL, e.g. `/tickers/AAPL/eod`. This route supports parameters of the [End-of-day Data](https://marketstack.com/documentation#eod_data "End-of-day Data Endpoint") endpoint. |
| `/tickers/[symbol]/splits` | Obtain end-of-day data for a specific stock ticker by attaching `/splits` to your URL, e.g. `/tickers/AAPL/splits`. This route supports parameters like date period `date_from` and `date_to` and also you can `sort the results DESC or ASC.` |
| `/tickers/[symbol]/dividends` | Obtain end-of-day data for a specific stock ticker by attaching `/dividends` to your URL, e.g. `/tickers/AAPL/dividends`. This route supports parameters like date period `date_from` and `date_to` and also you can `sort the results DESC or ASC.` |
| `/tickers/[symbol]/intraday` | Obtain real-time & intraday data for a specific stock ticker by attaching `/intraday` to your URL, e.g. `/tickers/AAPL/intraday`. This route supports parameters of the [Intraday Data](https://marketstack.com/documentation#intraday_data "Intraday Data Endpoint") endpoint. |
| `/tickers/[symbol]/eod/[date]` | Specify a date in `YYYY-MM-DD` format. You can also specify an exact time in ISO-8601 date format, e.g. `2020-05-21T00:00:00+0000`. Example: `/eod/2020-01-01` or `/intraday/2020-01-01` |
| `/tickers/[symbol]/eod/latest` | Obtain the latest end-of-day data for a given stock symbol. Example: `/tickers/AAPL/eod/latest` |
| `/tickers/[symbol]/intraday/latest` | Obtain the latest intraday data for a given stock symbol. Example: `/tickers/AAPL/intraday/latest` |

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required]** Specify your API access key, available in your [account dashboard](https://marketstack.com/dashboard "API Access K Key"). |
| `exchange` | [Optional] To filter your results based on a specific stock exchange, use this parameter to specify the MIC identification of a stock exchange. Example: `XNAS` |
| `search` | [Optional] Use this parameter to search stock tickers by name or ticker symbol. |
| `limit` | [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is `100`, maximum allowed limit value is `1000`. |
| `offset` | [Optional] Specify a pagination offset value for your API request. Example: An offset value of `100` combined with a limit value of 10 would show results 100-110. Default value is `0`, starting with the first available result. |

**API Response:**

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 136785
    },
    "data": [
        {
            "name": "MICROSOFT CORP",
            "symbol": "MSFT",
            "stock_exchange": {
                "name": "NASDAQ Stock Exchange",
                "acronym": "NASDAQ",
                "mic": "XNAS",
                "country": "USA",
                "country_code": "US",
                "city": "New York",
                "website": "www.nasdaq.com",
            }
        },
        [...]
    ]
}
```

**API Response Objects:**

| **Response Object** | **Description** |
| --- | --- |
| `pagination`>`limit` | Returns your pagination limit value. |
| `pagination`>`offset` | Returns your pagination offset value. |
| `pagination`>`count` | Returns the results count on the current page. |
| `pagination`>`total` | Returns the total count of results available. |
| `name` | Returns the name of the given stock ticker. |
| `symbol` | Returns the symbol of the given stock ticker. |
| `stock_exchange`>`name` | Returns the name of the stock exchange associated with the given stock ticker. |
| `stock_exchange`>`acronym` | Returns the acronym of the stock exchange associated with the given stock ticker. |
| `stock_exchange`>`mic` | Returns the MIC identification of the stock exchange associated with the given stock ticker. |
| `stock_exchange`>`country` | Returns the country of the stock exchange associated with the given stock ticker. |
| `stock_exchange`>`country_code` | Returns the 3-letter country code of the stock exchange associated with the given stock ticker. |
| `stock_exchange`>`city` | Returns the city of the stock exchange associated with the given stock ticker. |
| `stock_exchange`>`website` | Returns the website URL of the stock exchange associated with the given stock ticker. |

**Tickers:**

**JavaScript Fetch**

```
const url = 'https://api.marketstack.com/v1/tickers?access_key={PASTE_YOUR_API_KEY_HERE}';
const options = {
	method: 'GET'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}
```

**JavaScript Axios**

```
import axios from 'axios';
const options = {
 method: 'GET',
 url: 'https://api.marketstack.com/v1/tickers?access_key={PASTE_YOUR_API_KEY_HERE}'
};
try {
    const response = await axios.request(options);
    console.log(response.data);
} catch (error) {
    console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/tickers?access_key={PASTE_YOUR_API_KEY_HERE}"
response = requests.get(url)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/tickers?access_key={PASTE_YOUR_API_KEY_HERE}")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Exchanges

Using the `exchanges` API endpoint you will be able to look up information any of the 2700+ stock exchanges supported by this endpoint. This endpoint provides general information about several stock exchanges. Not all stock exchanges found here are supported by other Marketstack endpoints. For the supported stock exchanges supported by each endpoint, please verify each endpoint documentation. You will be able to find and try out an example API request below.

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/exchanges
    ? access_key = YOUR_ACCESS_KEY
```

**Endpoint Features:**

| **Object** | **Description** |
| --- | --- |
| `/exchanges/[mic]` | Obtain information about a specific stock exchange by attaching its MIC identification to your API request URL, e.g. `/exchanges/XNAS`. |
| `/exchanges/[mic]/tickers` | Obtain all available tickers for a specific exchange by attaching the exchange MIC as well as `/tickers`, e.g. `/exchanges/XNAS/tickers`. |
| `/exchanges/[mic]/eod` | Obtain end-of-day data for all available tickers from a specific exchange, e.g. `/exchanges/XNAS/eod`. For parameters, refer to [End-of-day Data](https://marketstack.com/documentation#eod_data "End-of-day Data Endpoint") endpoint. |
| `/exchanges/[mic]/intraday` | Obtain intraday data for tickers from a specific exchange, e.g. `/exchanges/XNAS/intraday`. For parameters, refer to [Intraday Data](https://marketstack.com/documentation#intraday_data "Intraday Data Endpoint") endpoint. |
| `/exchanges/[mic]/eod/[date]` | Obtain end-of-day data for a specific date in `YYYY-MM-DD` or ISO-8601 format. Example: `/exchanges/XNAS/eod/2020-01-01`. |
| `/exchanges/[mic]/intraday/[date]` | Obtain intraday data for a specific date and time in `YYYY-MM-DD` or ISO-8601 format. Example: `/exchanges/IEXG/intraday/2020-05-21T00:00:00+0000`. |
| `/exchanges/[mic]/eod/latest` | Obtain the latest end-of-day data for tickers of the given exchange. Example: `/exchanges/XNAS/eod/latest` |
| `/exchanges/[mic]/intraday/latest` | Obtain the latest intraday data for tickers of the given exchange. Example: `/exchanges/IEXG/intraday/latest` |

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required]** Specify your API access key, available in your [account dashboard](https://marketstack.com/dashboard "API Access K Key"). |
| `search` | [Optional] Use this parameter to search stock exchanges by name or MIC. |
| `limit` | [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is `100`, maximum allowed limit value is `1000`. |
| `offset` | [Optional] Specify a pagination offset value for your API request. Example: An offset value of `100` combined with a limit value of 10 would show results 100-110. Default value is `0`, starting with the first available result. |

**API Response:**

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 71,
        "total": 71
    },
    "data": [
        {
            "name": "NASDAQ Stock Exchange",
            "acronym": "NASDAQ",
            "mic": "XNAS",
            "country": "USA",
            "country_code": "US",
            "city": "New York",
            "website": "www.nasdaq.com",
            "timezone": {
                "timezone": "America/New_York",
                "abbr": "EST",
                "abbr_dst": "EDT"
            }
        },
        [...]
    ]
}
```

**API Response Objects:**

| **Response Object** | **Description** |
| --- | --- |
| `pagination`>`limit` | Returns your pagination limit value. |
| `pagination`>`offset` | Returns your pagination offset value. |
| `pagination`>`count` | Returns the results count on the current page. |
| `pagination`>`total` | Returns the total count of results available. |
| `name` | Returns the name of the given stock exchange. |
| `acronym` | Returns the acronym of the given stock exchange. |
| `mic` | Returns the MIC identification of the given stock exchange. |
| `country` | Returns the country of the given stock exchange. |
| `country_code` | Returns the 3-letter country code of the given stock exchange. |
| `city` | Returns the given city of the stock exchange. |
| `website` | Returns the website URL of the given stock exchange. |
| `timezone`>`timezone` | Returns the timezone name of the given stock exchange. |
| `timezone`>`abbr` | Returns the timezone abbreviation of the given stock exchange. |
| `timezone`>`abbr_dst` | Returns the Summer time timezone abbreviation of the given stock exchange. |

**Exchanges:**

**JavaScript Fetch**

```
const url = 'https://api.marketstack.com/v1/exchanges?access_key={PASTE_YOUR_API_KEY_HERE}';
const options = {
	method: 'GET'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}
```

**JavaScript Axios**

```
import axios from 'axios';
const options = {
 method: 'GET',
 url: 'https://api.marketstack.com/v1/exchanges?access_key={PASTE_YOUR_API_KEY_HERE}'
};
try {
    const response = await axios.request(options);
    console.log(response.data);
} catch (error) {
    console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/exchanges?access_key={PASTE_YOUR_API_KEY_HERE}"
response = requests.get(url)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/exchanges?access_key={PASTE_YOUR_API_KEY_HERE}")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Currencies

Using the `currencies` API endpoint you will be able to look up all currencies supported by the marketstack API. You will be able to find and try out an example API request below.

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/currencies
    ? access_key = YOUR_ACCESS_KEY
```

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required]** Specify your API access key, available in your [account dashboard](https://marketstack.com/dashboard "API Access K Key"). |
| `limit` | [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is `100`, maximum allowed limit value is `1000`. |
| `offset` | [Optional] Specify a pagination offset value for your API request. Example: An offset value of `100` combined with a limit value of 10 would show results 100-110. Default value is `0`, starting with the first available result. |

**API Response:**

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 40,
        "total": 40
    },
    "data": [
        {
            "code": "USD",
            "name": "US Dollar",
            "symbol": "$",
            "symbol_native": "$",
        },
        [...]
    ]
}
```

**API Response Objects:**

| **Response Object** | **Description** |
| --- | --- |
| `pagination`>`limit` | Returns your pagination limit value. |
| `pagination`>`offset` | Returns your pagination offset value. |
| `pagination`>`count` | Returns the results count on the current page. |
| `pagination`>`total` | Returns the total count of results available. |
| `code` | Returns the 3-letter code of the given currency. |
| `name` | Returns the name of the given currency. |
| `symbol` | Returns the text symbol of the given currency. |
| `symbol_native` | Returns the native text symbol of the given currency. |

**Currencies:**

**JavaScript Fetch**

```
const url = 'https://api.marketstack.com/v1/currencies?access_key={PASTE_YOUR_API_KEY_HERE}';
const options = {
	method: 'GET'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}
```

**JavaScript Axios**

```
import axios from 'axios';
const options = {
 method: 'GET',
 url: 'https://api.marketstack.com/v1/currencies?access_key={PASTE_YOUR_API_KEY_HERE}'
};
try {
    const response = await axios.request(options);
    console.log(response.data);
} catch (error) {
    console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/currencies?access_key={PASTE_YOUR_API_KEY_HERE}"
response = requests.get(url)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/currencies?access_key={PASTE_YOUR_API_KEY_HERE}")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```

## Timezones

Using the `timezones` API endpoint you will be able to look up information about all supported timezones. You will be able to find and try out an example API request below.

**Example API Request:**

[**Sign Up to Run API Request**](https://marketstack.com/signup/free/?utm_source=DocumentationPage&utm_medium=Referral)
```
https://api.marketstack.com/v1/timezones
    ? access_key = YOUR_ACCESS_KEY
```

**Parameters:**

| **Object** | **Description** |
| --- | --- |
| `access_key` | **[Required]** Specify your API access key, available in your [account dashboard](https://marketstack.com/dashboard "API Access K Key"). |
| `limit` | [Optional] Specify a pagination limit (number of results per page) for your API request. Default limit value is `100`, maximum allowed limit value is `1000`. |
| `offset` | [Optional] Specify a pagination offset value for your API request. Example: An offset value of `100` combined with a limit value of 10 would show results 100-110. Default value is `0`, starting with the first available result. |

**API Response:**

```
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 57,
        "total": 57
    },
    "data": [
        {
            "timezone": "America/New_York",
            "abbr": "EST",
            "abbr_dst": "EDT"
        },
        [...]
    ]
}
```

**API Response Objects:**

| **Response Object** | **Description** |
| --- | --- |
| `pagination`>`limit` | Returns your pagination limit value. |
| `pagination`>`offset` | Returns your pagination offset value. |
| `pagination`>`count` | Returns the results count on the current page. |
| `pagination`>`total` | Returns the total count of results available. |
| `timezone` | Returns the name of the given timezone. |
| `abbr` | Returns the abbreviation of the given timezone. |
| `abbr_dst` | Returns the Summer time abbreviation of the given timezone. |

**Timezones:**

**JavaScript Fetch**

```
const url = 'https://api.marketstack.com/v1/timezones?access_key={PASTE_YOUR_API_KEY_HERE}';
const options = {
	method: 'GET'
};

try {
	const response = await fetch(url, options);
	const result = await response.text();
	console.log(result);
} catch (error) {
	console.error(error);
}
```

**JavaScript Axios**

```
import axios from 'axios';
const options = {
 method: 'GET',
 url: 'https://api.marketstack.com/v1/timezones?access_key={PASTE_YOUR_API_KEY_HERE}'
};
try {
    const response = await axios.request(options);
    console.log(response.data);
} catch (error) {
    console.error(error);
}
```

**Python Requests**

```
import requests
url = "https://api.marketstack.com/v1/timezones?access_key={PASTE_YOUR_API_KEY_HERE}"
response = requests.get(url)
print(response.json())
```

**Python HTTP.client**

```
import http.client
conn = http.client.HTTPSConnection("api.marketstack.com")
conn.request("GET", "/v1/timezones?access_key={PASTE_YOUR_API_KEY_HERE}")
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
```
