# TimeManager Class Documentation & Guide (ManagerTime)

## Overview
The `TimeManager` class is designed to facilitate time-related calculations based on the provided timeframe and number of candles. It offers methods to initialize the class, configure time-related parameters, and perform various time-related computations.

## General Explanation
The `TimeManager` class manages time-related calculations for financial data analysis, particularly in the context of trading. It allows users to work with different timeframes and candlestick intervals efficiently.

## Methods

### `__init__(timeframe: str, exchange: str, num_candles: int, logger=None)`
Initializes the `TimeManager` instance.

Parameters:
- `timeframe` (str): Input timeframe string.
- `exchange` (str): Name of the exchange for which the input is being standardized.
- `num_candles` (int): Number of candles.
- `logger` (optional): LoggerManager instance.

### `_setup_time_manager()`
Sets up `TimeManager` using `InputsManager`.

### `_seconds_time_unit(time_unit: str = None) -> int`
Gets the seconds for the specified time unit.

Parameters:
- `time_unit` (str): Time unit.

Returns:
- `int`: Seconds for the specified time unit.

### `_totaltime_seconds(actual_candles: int) -> int`
Calculates the total time in seconds.

Parameters:
- `actual_candles` (int): Actual number of candles.

Returns:
- `int`: Total time in seconds.

### `_end_time_now() -> int`
Gets the current end time in timestamp format.

Returns:
- `int`: End time in timestamp format.

### `_start_time_new() -> int`
Calculates the new start time in timestamp format.

Returns:
- `int`: New start time in timestamp format.

### `_start_time_exists(existing_ohlcv_df: pd.DataFrame) -> int`
Calculates the existing start time after the last timestamp in the provided DataFrame.

Parameters:
- `existing_ohlcv_df` (pd.DataFrame): Existing OHLCV DataFrame.

Returns:
- `int`: Existing start time in timestamp format.

### `_time_exists_info(existing_ohlcv_df: pd.DataFrame) -> Tuple[int, int]`
Gets the first and last timestamps from the existing DataFrame.

Parameters:
- `existing_ohlcv_df` (pd.DataFrame): Existing OHLCV DataFrame.

Returns:
- `Tuple[int, int]`: First and last timestamps in timestamp format.

## Usage Guide

1. **Initializing TimeManager:**
```python
from TimeManager import TimeManager

timeframe = "1H"  # Example timeframe
exchange = "Binance"  # Example exchange
num_candles = 100  # Example number of candles

time_manager = TimeManager(timeframe, exchange, num_candles)
```

2. **Getting Total Time in Seconds:**
```python
total_seconds = time_manager._totaltime_seconds(num_candles)
print("Total Time in Seconds:", total_seconds)
```

3. **Getting Current End Time:**
```python
end_time = time_manager._end_time_now()
print("Current End Time (Timestamp):", end_time)
```

4. **Calculating New Start Time:**
```python
start_time = time_manager._start_time_new()
print("New Start Time (Timestamp):", start_time)
```

5. **Calculating Existing Start Time:**
```python
existing_ohlcv_df = pd.DataFrame(...)  # Example OHLCV DataFrame
start_time_exists = time_manager._start_time_exists(existing_ohlcv_df)
print("Existing Start Time (Timestamp):", start_time_exists)
```

6. **Getting First and Last Timestamps from Existing DataFrame:**
```python
first_timestamp, last_timestamp = time_manager._time_exists_info(existing_ohlcv_df)
print("First Timestamp:", first_timestamp)
print("Last Timestamp:", last_timestamp)
```

## Note
- Ensure that the necessary dependencies are installed before using the `TimeManager` class.
- Provide appropriate inputs to the methods for accurate results.
