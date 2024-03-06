
# راهنما و مستندات (HistoryFetch):

## کلاس ExchangeAPI

### مرور
کلاس `ExchangeAPI` برای تعامل با رابط‌های برنامه‌نویسی (API) صرافی‌ها برای بازیابی داده‌های تاریخچه بازار طراحی شده است. این کلاس رابطی راحت برای ارسال درخواست‌های HTTP به رابط‌های برنامه‌نویسی صرافی‌ها فراهم می‌کند و داده‌های تاریخچه بازار را بازیابی می‌کند.

### متدها

**`make_request(url: str, params: dict = None) -> dict`**

یک درخواست HTTP GET به آدرس مشخص شده ارسال می‌کند و پاسخ JSON را از API بازمی‌گرداند.

- `url` (str): The URL of the API endpoint.
- `params` (dict, optional): Query parameters to include in the request. Defaults to None.
  
**Returns:**
- `dict`: The JSON response from the API.

**Raises:**
- `requests.exceptions.RequestException`: If a network-related error occurs.
- `requests.exceptions.HTTPError`: If an HTTP error (4xx or 5xx) occurs.
## کلاس HistoryOHLCV

### مرور
کلاس `HistoryOHLCV` از کلاس `ExchangeAPI` ارث‌بری می‌کند و متدهایی را برای بازیابی داده‌های تاریخچه بازار از رابط‌های برنامه‌نویسی صرافی‌ها ارائه می‌دهد.

### متدها

**`get_ohlcv_history(exchange: str, symbol: str, interval: str, startTime: int, endTime: int) -> dict`**

داده‌های تاریخچه بازار برای یک نماد خاص و محدوده زمانی مشخص از رابط API صرافی مشخص را بازیابی می‌کند.

- `exchange` (str):

نام صرافی که می‌خواهید از آن داده را دریافت کنید. صرافی‌های پشتیبانی شده: "Wallex"، "Nobitex"، "Binance"، "Coinbase"، "BingX".
- `symbol` (str): نمادی که می‌خواهید داده‌های تاریخچه بازار آن را دریافت کنید.
- `interval` (str): فاصله زمانی برای داده. قالب فاصله زمانی برای صرافی‌های مختلف متفاوت است.
- `startTime` (int): زمان شروع برای بازیابی داده‌ها (زمان یونیکس به ثانیه).
- `endTime` (int): زمان پایان برای بازیابی داده‌ها (زمان یونیکس به ثانیه).

**Returns:**
- `dict`: یک دیکشنری شامل داده‌های تاریخچه بازار.

## مثال استفاده

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
