# Documentation & Guide (GenerateTimeFrame)

### Overview (GenerateOHLCV Class)
The `GenerateOHLCV` class is designed to facilitate the generation and manipulation of OHLCV (Open, High, Low, Close, Volume) data for cryptocurrency markets. It offers methods for fetching market data from external APIs, creating new OHLCV data, updating existing data, and managing timeframes. This documentation provides a comprehensive guide on how to use the class effectively.

## Methods

### `__init__(symbol: str, timeframe: str, exchange: str, num_candles: int, data_directory: str, enable_logging: bool)`
- **Description:** Initializes a `GenerateOHLCV` instance.
- **Parameters:**
  - `symbol` (str): Market symbol.
  - `timeframe` (str): Timeframe for the OHLCV data.
  - `exchange` (str): Exchange name.
  - `num_candles` (int): Number of candles to fetch.
  - `data_directory` (str): Directory path to store the OHLCV DataFrame files.
  - `enable_logging` (bool): Flag to enable or disable logging.

### `__enter__()`
- **Description:** Enter method for context management.

### `__exit__(exc_type, exc_value, traceback)`
- **Description:** Exit method for context management.

### `__del__()`
- **Description:** Destructor method, logs a message when the instance is deleted.

### `_fetch_market_history(symbol: str, interval: int, startTime: int, endTime: int) -> pd.DataFrame`
- **Description:** Fetches market data from an external API.
- **Parameters:**
  - `symbol` (str): Market symbol.
  - `interval` (int): Time interval for fetching data.
  - `startTime` (int): Start timestamp for data fetching.
  - `endTime` (int): End timestamp for data fetching.
- **Returns:**
  - `pd.DataFrame`: Market data in DataFrame format.

### `_create_new_data(start_timestamp: int = None, end_timestamp: int = None) -> pd.DataFrame`
- **Description:** Creates new OHLCV data.
- **Parameters:**
  - `start_timestamp` (int): Start timestamp for data creation (optional).
  - `end_timestamp` (int): End timestamp for data creation (optional).
- **Returns:**
  - `pd.DataFrame`: New OHLCV data in DataFrame format.

### `_update_existing_data(existing_ohlcv_df: pd.DataFrame) -> pd.DataFrame`
- **Description:** Updates existing OHLCV data.
- **Parameters:**
  - `existing_ohlcv_df` (pd.DataFrame): Existing OHLCV DataFrame.
- **Returns:**
  - `pd.DataFrame`: Updated OHLCV data in DataFrame format.

### `dataframe_release(existing_ohlcv_df: pd.DataFrame = None) -> pd.DataFrame`
- **Description:** Releases OHLCV DataFrame, either by updating or creating new data.
- **Parameters:**
  - `existing_ohlcv_df` (pd.DataFrame): Existing OHLCV DataFrame (optional).
- **Returns:**
  - `pd.DataFrame`: Released OHLCV DataFrame.

### `timeframe_release(ohlcv_dataframe: pd.DataFrame = None, new_timeframe: str = None) -> pd.DataFrame`
- **Description:** Releases OHLCV DataFrame with a specified timeframe.
- **Parameters:**
  - `ohlcv_dataframe` (pd.DataFrame): OHLCV DataFrame (optional).
  - `new_timeframe` (str): New timeframe for the released DataFrame (optional).
- **Returns:**
  - `pd.DataFrame`: Released OHLCV DataFrame with the specified timeframe.

## Example Usage

```python
import time
from GenerateOHLCV import GenerateOHLCV

symbol = "BTC-USDT"
exchange = "BingX"
timeframe = "1min"
num_candles = 1000

with GenerateOHLCV(
    symbol=symbol,
    timeframe=timeframe,
    exchange=exchange,
    num_candles=num_candles
) as ohlcv_object:
    cycles = 2
    for i in range(cycles):
        print("Exchange:", exchange, "\n")
        print("Number of Cycle:", i + 1)
        print(ohlcv_object.timeframe_release())
        print("------------ end ------------\n")
        if i + 1 < cycles:
            time.sleep(5)
```

This example demonstrates how to use the `GenerateOHLCV` class to fetch market data from the BingX exchange for the BTC-USDT pair with a 1-minute timeframe. The program runs for two cycles, printing the released OHLCV DataFrame for each cycle.
