# Documentation & Guide (HistoryFetch):

## ExchangeAPI Class

### Overview
The `ExchangeAPI` class is designed to interact with various Exchange APIs for retrieving market history data. This class provides a convenient interface to make HTTP requests to Exchange APIs and retrieve historical market data.

### Methods

**`make_request(url: str, params: dict = None) -> dict`**

Sends an HTTP GET request to the specified endpoint and returns the JSON response from the API.

- `url` (str): The URL of the API endpoint.
- `params` (dict, optional): Query parameters to include in the request. Defaults to None.
  
**Returns:**
- `dict`: The JSON response from the API.

**Raises:**
- `requests.exceptions.RequestException`: If a network-related error occurs.
- `requests.exceptions.HTTPError`: If an HTTP error (4xx or 5xx) occurs.

## HistoryOHLCV Class

### Overview
The `HistoryOHLCV` class extends the `ExchangeAPI` class and provides methods specifically for retrieving market history data from Exchange APIs.

### Methods

**`get_ohlcv_history(exchange: str, symbol: str, interval: str, startTime: int, endTime: int) -> dict`**

Retrieves market history data for a specific symbol and time range from the specified exchange API.

- `exchange` (str): The name of the exchange from which to retrieve data. Supported exchanges: "Wallex", "Nobitex", "Binance", "Coinbase", "BingX".
- `symbol` (str): The symbol for which to retrieve market history data.
- `interval` (str): The time interval for data. The interval format varies for different exchanges.
- `startTime` (int): The start time for data retrieval (Unix timestamp in seconds).
- `endTime` (int): The end time for data retrieval (Unix timestamp in seconds).

**Returns:**
- `dict`: A dictionary containing market history data.

## Example Usage

```python
from exchange_api import HistoryOHLCV
import pandas as pd
import time

# Initialize HistoryOHLCV class
api = HistoryOHLCV()

# Retrieve market history data for a specific symbol and time range
start_time = int(time.time()) - 60 * 60 * 15
end_time = int(time.time())
exchange = "BingX"
symbol = "BTC-USDT"
interval = "1m"

market_history = api.get_ohlcv_history(
    exchange=exchange,
    symbol=symbol,
    interval=interval,
    startTime=start_time,
    endTime=end_time,
)

# Convert market history data to DataFrame
market_history_df = pd.DataFrame(market_history)
print("Market History Result:")
print(market_history_df)
```
