# راهنما و مستندات کلاس TimeManager (ManagerTime)

### مرور
کلاس `TimeManager` برای تسهیل محاسبات مربوط به زمان براساس بازه زمانی وارد شده و تعداد کندل‌ها، طراحی شده است. این کلاس امکان مدیریت بازه‌های زمانی مختلف و فاصله زمانی بین کندل‌ها را به کاربر می‌دهد.


## متدها

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

## راهنمای استفاده

۱. **مقداردهی اولیه TimeManager:**
```python
from TimeManager import TimeManager

timeframe = "1H"  # یک نمونه بازه زمانی
exchange = "Binance"  # نام یک صرافی
num_candles = 100  # تعداد کندل‌ها

time_manager = TimeManager(timeframe, exchange, num_candles)
```

۲. **دریافت زمان کل به صورت ثانیه:**
```python
total_seconds = time_manager._totaltime_seconds(num_candles)
print("Total Time in Seconds:", total_seconds)
```

۳. **دریافت زمان پایانی فعلی:**
```python
end_time = time_manager._end_time_now()
print("Current End Time (Timestamp):", end_time)
```

۴. **محاسبه زمان شروع جدید:**
```python
start_time = time_manager._start_time_new()
print("New Start Time (Timestamp):", start_time)
```

۵. **محاسبه زمان شروع موجود:**
```python
existing_ohlcv_df = pd.DataFrame(...)  # یک نمونه از جدول داده‌های موجود
start_time_exists = time_manager._start_time_exists(existing_ohlcv_df)
print("Existing Start Time (Timestamp):", start_time_exists)


```

۶. **دریافت اولین و آخرین زمان از دیتافریم موجود (درصورت وجود):**
```python
first_timestamp, last_timestamp = time_manager._time_exists_info(existing_ohlcv_df)
print("First Timestamp:", first_timestamp)
print("Last Timestamp:", last_timestamp)
```

## توجه
- قبل از استفاده از کلاس `TimeManager` اطمینان حاصل کنید که وابستگی‌های مورد نیاز نصب شده باشد.
- ورودی‌های مناسب را به متدها ارائه دهید تا نتایج دقیق و صحیحی بدست آورید.
