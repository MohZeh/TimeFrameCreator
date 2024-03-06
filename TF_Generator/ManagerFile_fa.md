## مستندات و راهنما (ManagerFile)

### مرور
کلاس `FileManager` کمک می‌کند تا مدیریت فایل‌های DataFrame OHLCV (Open, High, Low, Close, Volume) انجام شود که شامل عملیات ذخیره و خواندن است. این کلاس دارای متدهایی برای ذخیره کردن DataFrame‌های OHLCV به فایل‌های CSV و خواندن DataFrame‌های OHLCV موجود از فایل‌های CSV است.

## متدها

**`__init__(data_directory: str, logger=None)`**

یک نمونه از کلاس FileManager را مقداردهی اولیه می‌کند.

**پارامترها:**
- `data_directory` (str): مسیر دایرکتوری که فایل‌های DataFrame OHLCV در آن ذخیره می‌شوند.
- `logger`: نمونه اختیاری برای نمایش پیام‌ها.

**`_setup_file_manager()`**

FileManager را با مقداردهی اولیه نمونه‌های لازم راه‌اندازی می‌کند.

**`_save_df_ohlcv(file_name: str, ohlcv_dataframe: pd.DataFrame) -> None`**

DataFrame OHLCV را به یک فایل CSV ذخیره می‌کند.

**پارامترها:**
- `file_name` (str): نام فایل برای ذخیره‌سازی.
- `ohlcv_dataframe` (pd.DataFrame): DataFrame OHLCV برای ذخیره‌سازی.

**`_read_df_ohlcv(file_name: str) -> pd.DataFrame | None`**

DataFrame OHLCV موجود را از یک فایل CSV خوانده و بازمی‌گرداند.

**پارامترها:**
- `file_name` (str): نام فایل برای خواندن.

**بازگشت:**
- `pd.DataFrame | None`: DataFrame OHLCV خوانده شده یا `None` اگر فایل وجود نداشته باشد.

**`__del__()`**

متد نابودکننده، وقتی نمونه حذف می‌شود، وظایف پاک‌سازی را انجام می‌دهد.

## مثال استفاده

```python
import pandas as pd
import os
import sys
from TF_Generator.OrganizerDataFrame import DataFrameOrg
from FileManager import FileManager

# Initialize FileManager instance
logger = LoggerManager()
data_directory = "data"
file_manager = FileManager(data_directory, logger)

# Create a sample OHLCV DataFrame
ohlcv_df = pd.DataFrame({
    'timestamp': ['2024-01-01 00:00:00', '2024-01-01 01:00:00', '2024-01-01 02:00:00'],
    'open': [100, 110, 105],
    'high': [120, 115, 110],
    'low': [95, 105, 100],
    'close': [110, 105, 105],
    'volume': [1000, 1200, 1500]
})

# Save the OHLCV DataFrame to a CSV file
file_manager._save_df_ohlcv("ohlcv_data", ohlcv_df)

# Read the existing OHLCV DataFrame from the CSV file
existing_ohlcv_df = file_manager._read_df_ohlcv("ohlcv_data")

# Output the read DataFrame
print(existing_ohlcv_df)
```

این راهنما درک روش استفاده از هر متد از کلاس FileManager را برای کاربران فراهم می‌کند و امکان مدیریت بهینه‌ی فایل‌های DataFrame OHLCV را برای آن‌ها فراهم می‌کند.
