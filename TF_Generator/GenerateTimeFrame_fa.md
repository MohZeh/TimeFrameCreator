# راهنما و مستندات (GenerateTimeFrame) 

### مرور (کلاس GenerateOHLCV)
کلاس `GenerateOHLCV` برای تسهیل تولید و مدیریت داده‌های OHLCV (باز شدن، بالاترین، پایین‌ترین، بسته شدن و حجم) برای بازارهای رمزارز طراحی شده است. این کلاس دارای متدهایی برای دریافت داده‌های بازار از API‌های خارجی، ایجاد داده‌های OHLCV جدید، به‌روزرسانی داده‌های موجود و مدیریت بازه‌های زمانی است. این مستند به عنوان راهنمای جامعی برای استفاده موثر از این کلاس ارائه شده است.

## متدها

### `__init__(symbol: str, timeframe: str, exchange: str, num_candles: int, data_directory: str, enable_logging: bool)`
**توضیحات:** یک نمونه از کلاس `GenerateOHLCV` را مقداردهی اولیه می‌کند.

**پارامترها:**
  - `symbol` (str): نماد بازار.
  - `timeframe` (str): بازه زمانی برای دریافت داده‌ها.
  - `exchange` (str): نام صرافی.
  - `num_candles` (int): تعداد شمع‌ها برای دریافت.
  - `data_directory` (str): مسیر دایرکتوری برای ذخیره داده‌های دیتافریم.
  - `enable_logging` (bool): تعیین فعال یا غیرفعال کردن ثبت اطلاعات برنامه.

### `__enter__()`
**توضیحات:** متد ورود برای مدیریت محیط.

### `__exit__(exc_type, exc_value, traceback)`
**توضیحات:** متد خروج برای مدیریت محیط.

### `__del__()`
**توضیحات:** متد نابودگر، یک پیام را ثبت می‌کند زمانی که نمونه حذف می‌شود.

### `_fetch_market_history(symbol: str, interval: int, startTime: int, endTime: int) -> pd.DataFrame`
**توضیحات:** داده‌های بازار را از یک API خارجی دریافت می‌کند.

**پارامترها:**
  - `symbol` (str): نماد بازار.
  - `interval` (int): فاصله زمانی برای دریافت داده‌ها.
  - `startTime` (int): زمان شروع برای دریافت داده.
  - `endTime` (int): زمان پایان برای دریافت داده.

**برگرداندن:**
  - `pd.DataFrame`: داده‌های بازار به فرم دیتافریم.

### `_create_new_data(start_timestamp: int = None, end_timestamp: int = None) -> pd.DataFrame`
**توضیحات:** داده‌های OHLCV جدید ایجاد می‌کند.

**پارامترها:**
  - `start_timestamp` (int): زمان شروع برای ایجاد داده (اختیاری).
  - `end_timestamp` (int): زمان پایان برای ایجاد داده (اختیاری).

**برگرداندن:**
  - `pd.DataFrame`: داده‌های جدید به فرم دیتافریم.

### `_update_existing_data(existing_ohlcv_df: pd.DataFrame) -> pd.DataFrame`
**توضیحات:** داده‌های OHLCV موجود را به‌روز می‌کند.

**پارامترها:**
  - `existing_ohlcv_df` (pd.DataFrame): دیتافریم موجود.

**برگرداندن:**
  - `pd.DataFrame`: داده‌های به‌روز شده به فرم دیتافریم.

### `dataframe_release(existing_ohlcv_df: pd.DataFrame = None) -> pd.DataFrame`
**توضیحات:** DataFrame OHLCV را ارائه می‌دهد، ساخت داده‌های جدید یا به‌روزرسانی داده‌ها.

**پارامترها:**
  - `existing_ohlcv_df` (pd.DataFrame): دیتافریم موجود (اختیاری).

**برگرداندن:**
  - `pd.DataFrame`: دیتافریم ارائه‌شده.

### `timeframe_release(ohlcv_dataframe: pd.DataFrame = None, new_timeframe: str = None) -> pd.DataFrame`
**توضیحات:** DataFrame OHLCV را با یک بازه زمانی خاص ارائه می‌دهد.

**پارامترها:**
  - `ohlcv_dataframe` (pd.DataFrame): دیتافریم (اختیاری).
  - `new_timeframe` (str): بازه زمانی جدید برای دیتافریم ارائه‌شده (اختیاری).


**برگرداندن:**
  - `pd.DataFrame`: دیتافریم ارائه‌شده با بازه زمانی مشخص شده.

## مثال‌ استفاده

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
این مثال نحوه استفاده از کلاس `GenerateOHLCV` را برای واکشی داده های بازار از صرافی BingX برای جفت BTC-USDT با بازه زمانی 1 دقیقه‌ای نشان می‌دهد. این برنامه برای دو چرخه اجرا می‌شود و برای هر چرخه OHLCV DataFrame منتشر شده را چاپ می‌کند.
