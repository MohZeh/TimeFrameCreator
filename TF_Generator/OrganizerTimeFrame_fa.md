
## راهنما و مستندات (OrganizerTimeFrame)

### مرور
کلاس `TimeFrameOrg` قابلیت‌هایی را برای سازماندهی و تبدیل داده‌های OHLCV (Open, High, Low, Close, Volume) به یک مقیاس زمانی جدید ارائه می‌دهد. این کلاس دارای متدهایی برای محاسبه واحد زمانی، بررسی امکان تبدیل و انجام تبدیل واقعی است.

## متدها

**`__init__(exchange: str, ohlcv_dataframe: pd.DataFrame = None, new_timeframe: str = None, logger=None)`**

یک نمونه از کلاس `TimeFrameOrg` را مقداردهی اولیه می‌کند.

**پارامترها:**
- `exchange` (str): نام صرافی.
- `ohlcv_dataframe` (pd.DataFrame): DataFrame OHLCV با مقیاس زمانی اولیه.
- `new_timeframe` (str): مقیاس زمانی مورد نظر برای تبدیل.
- `logger`: نمونه LoggerManager.

**`_calculate_time_unit(ohlcv_dataframe: pd.DataFrame) -> str`**

واحد زمانی را بر اساس تفاوت زمانی بین برچسب‌های زمانی متوالی در DataFrame محاسبه می‌کند.

**پارامترها:**
- `ohlcv_dataframe` (pd.DataFrame): DataFrame با برچسب‌های زمانی.

**بازگرداندن:**
- `str`: واحد زمانی محاسبه شده ('min'، 'H' یا 'D').

**`_can_converted(ohlcv_dataframe: pd.DataFrame, new_timeframe: str) -> bool`**

بررسی می‌کند که آیا تبدیل میان مقیاس‌های زمانی اولیه و جدید ممکن است یا خیر.

**پارامترها:**
- `ohlcv_dataframe` (pd.DataFrame): DataFrame OHLCV اولیه.
- `new_timeframe` (str): مقیاس زمانی جدید برای تبدیل.

**بازگرداندن:**
- `bool`: درستی اگر تبدیل ممکن باشد و در غیر این صورت نادرست.

**`convert_timeframe(ohlcv_dataframe: pd.DataFrame = None, new_timeframe: str = None) -> pd.DataFrame`**

DataFrame OHLCV را به مقیاس زمانی مورد نظر تبدیل می‌کند.

**پارامترها:**
- `ohlcv_dataframe` (pd.DataFrame): DataFrame OHLCV با مقیاس زمانی اولیه.
- `new_timeframe` (str): مقیاس زمانی مورد نظر برای تبدیل.

**بازگرداندن:**
- `pd.DataFrame`: DataFrame OHLCV با داده‌های تجمعی برای مقیاس زمانی مورد نظر.

**`__del__()`**

متد مخرب، پیامی را ثبت می‌کند هنگامی که نمونه حذف می‌شود.

## مثال‌های استفاده

```python
import pandas as pd
import os
import sys
from TF_Generator.ManagerInputs import InputsManager
from TimeFrameOrg import TimeFrameOrg

# مقداردهی اولیه نمونه TimeFrameOrg
logger = LoggerManager()
exchange = "Binance"
ohlcv_df = pd.read_csv("ohlcv_data.csv")
new_timeframe = "H"  # تبدیل به مقیاس زمانی ساعتی
tf_org = TimeFrameOrg(exchange, ohlcv_df, new_timeframe, logger)

# محاسبه واحد زمانی
time_unit = tf_org._calculate_time_unit(ohlcv_df)

# بررسی امکان تبدیل
feasible = tf_org._can_converted(ohlcv_df, new_timeframe)

# تبدیل مقیاس زمانی
converted_df = tf_org.convert_timeframe()

# خروجی DataFrame تبدیل شده
print(converted_df)
```

این راهنما درک روشنی از نحوه استفاده از هر متد از کلاس TimeFrameOrg را فراهم می‌کند و کاربران را قادر می‌سازد داده‌های OHLCV را به مقیاس زمانی مورد نظر خود به طور کارآمد تبدیل کنند.
