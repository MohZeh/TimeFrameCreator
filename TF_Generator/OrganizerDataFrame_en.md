# Documentation & Guide (OrganizerDataFrame)

### Overview
The `DataFrameOrg` class provides functionalities for organizing and processing OHLCV (Open, High, Low, Close, Volume) DataFrame from various exchanges. It offers methods to regularize, index, concatenate, and process the OHLCV data efficiently.

## Methods

**`__init__(logger=None)`**

Initializes a DataFrameOrg instance.

**Parameters:**
- `logger`: Optional parameter for LoggerManager instance.

**`_regularize_dataframe(exchange: str, ohlcv_dataframe: pd.DataFrame) -> pd.DataFrame`**

Regularizes the OHLCV DataFrame based on the specified exchange.

**Parameters:**
- `exchange` (str): The name of the exchange from which the data originates (e.g., "Wallex", "Binance", "Coinbase").
- `ohlcv_dataframe` (pd.DataFrame): The input OHLCV DataFrame containing columns 't' (timestamp), 'o' (open), 'h' (high), 'l' (low), 'c' (close), and 'v' (volume).

**Returns:**
- `pd.DataFrame`: The regularized OHLCV DataFrame with standardized column names.

**Raises:**
- `ValueError`: If the specified exchange is not supported.

**`_index_dataframe(ohlcv_dataframe: pd.DataFrame) -> pd.DataFrame`**

Indexes the OHLCV DataFrame based on the timestamp column.

**Parameters:**
- `ohlcv_dataframe` (pd.DataFrame): The input OHLCV DataFrame.

**Returns:**
- `pd.DataFrame`: The indexed OHLCV DataFrame with the timestamp converted to datetime and set as the index.

**`_concatenate_dataframe(existing_ohlcv_df: pd.DataFrame, new_ohlcv_data: pd.DataFrame, actual_candles: int) -> pd.DataFrame`**

Concatenates existing and new OHLCV DataFrames, drops duplicates, and trims the DataFrame to the specified number of actual candles.

**Parameters:**
- `existing_ohlcv_df` (pd.DataFrame): The existing OHLCV DataFrame.
- `new_ohlcv_data` (pd.DataFrame): The new OHLCV DataFrame to be concatenated.
- `actual_candles` (int): The number of actual candles to trim the concatenated DataFrame.

**Returns:**
- `pd.DataFrame`: The concatenated and trimmed OHLCV DataFrame.

**`__del__()`**

Destructor method, logs a message when the instance is deleted.

## Example Usage

```python
from dataframe_org import DataFrameOrg
import pandas as pd

# Initialize DataFrameOrg instance
logger = LoggerManager()
df_org = DataFrameOrg(logger)

# Regularize OHLCV DataFrame for Wallex exchange
exchange = "Wallex"
ohlcv_df = pd.read_csv("wallex_ohlcv_data.csv")
regularized_df = df_org._regularize_dataframe(exchange, ohlcv_df)

# Index the OHLCV DataFrame
indexed_df = df_org._index_dataframe(regularized_df)

# Concatenate and trim existing and new OHLCV DataFrames
existing_df = pd.read_csv("existing_ohlcv_data.csv")
new_df = pd.read_csv("new_ohlcv_data.csv")
actual_candles = 1000
concatenated_df = df_org._concatenate_dataframe(existing_df, new_df, actual_candles)
```
