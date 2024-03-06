# Documentation & Guide (TimeFrameOrg)

### Overview
The `TimeFrameOrg` class provides functionalities for organizing and converting OHLCV (Open, High, Low, Close, Volume) DataFrame to a new timeframe. It offers methods to calculate time unit, check conversion feasibility, and perform the actual conversion.

## Methods

**`__init__(exchange: str, ohlcv_dataframe: pd.DataFrame = None, new_timeframe: str = None, logger=None)`**

Initializes a TimeFrameOrg instance.

**Parameters:**
- `exchange` (str): Name of the exchange.
- `ohlcv_dataframe` (pd.DataFrame): OHLCV DataFrame with the initial time frame.
- `new_timeframe` (str): Desired time frame for conversion.
- `logger`: LoggerManager instance.

**`_calculate_time_unit(ohlcv_dataframe: pd.DataFrame) -> str`**

Calculates the time unit based on the time difference between consecutive timestamps in the DataFrame.

**Parameters:**
- `ohlcv_dataframe` (pd.DataFrame): DataFrame with timestamps.

**Returns:**
- `str`: Calculated time unit ('min', 'H', or 'D').

**`_can_converted(ohlcv_dataframe: pd.DataFrame, new_timeframe: str) -> bool`**

Checks if conversion is possible between the initial and new timeframes.

**Parameters:**
- `ohlcv_dataframe` (pd.DataFrame): Initial OHLCV DataFrame.
- `new_timeframe` (str): New timeframe for conversion.

**Returns:**
- `bool`: True if conversion is possible, False otherwise.

**`convert_timeframe(ohlcv_dataframe: pd.DataFrame = None, new_timeframe: str = None) -> pd.DataFrame`**

Converts the OHLCV DataFrame to the desired time frame.

**Parameters:**
- `ohlcv_dataframe` (pd.DataFrame): OHLCV dataframe with the initial time frame.
- `new_timeframe` (str): Desired time frame for conversion.

**Returns:**
- `pd.DataFrame`: OHLCV dataframe with aggregated data for the desired time frame.

**`__del__()`**

Destructor method, logs a message when the instance is deleted.

## Example Usage

```python
import pandas as pd
import os
import sys
from TF_Generator.ManagerInputs import InputsManager
from TimeFrameOrg import TimeFrameOrg

# Initialize TimeFrameOrg instance
logger = LoggerManager()
exchange = "Binance"
ohlcv_df = pd.read_csv("ohlcv_data.csv")
new_timeframe = "H"  # Convert to hourly timeframe
tf_org = TimeFrameOrg(exchange, ohlcv_df, new_timeframe, logger)

# Calculate time unit
time_unit = tf_org._calculate_time_unit(ohlcv_df)

# Check conversion feasibility
feasible = tf_org._can_converted(ohlcv_df, new_timeframe)

# Convert timeframe
converted_df = tf_org.convert_timeframe()

# Output the converted dataframe
print(converted_df)
```

This guide provides a clear understanding of how to use each method of the TimeFrameOrg class, enabling users to efficiently organize and convert OHLCV data to their desired timeframe.
