# راهنما و مستندات (ManagerInputs):

### مقدمه:
کلاس InputsManager امکان مرتب‌سازی مقادیر ورودی مانند تایم‌فریم‌های مختلف را برای صرافی‌های مختلف فراهم می‌کند.

## متدها:

**۱. متد __init__**
**__init__(timeframe: str, exchange: str, num_candles: int = None, logger=None):**

  این متد یک نمونه از کلاس InputsManager را مقداردهی اولیه می‌کند.

  **پارامترها:**
  - timeframe (str): Input timeframe string (e.g., '1min', '2H', '1D').
  - exchange (str): Name of the exchange for which the input is being standardized.
  - num_candles (int): Number of candles (optional).
  - logger: LoggerManager instance (optional).

  **مثال برای استفاده:**
  ```python
      inputs_manager = InputsManager(timeframe="1H", exchange="Wallex", num_candles=100, logger=my_logger)
  ```

**۲. متد ()setup_regularize_inputs_values:**

  این متد با فراخوانی متدهای راه‌اندازی مورد نیاز، نمونه InputsManager را مقداردهی اولیه می‌کند.

**۳. متد parse_timeframe(timeframe: str) -> None_:**

  این متد رشته فریم زمانی ورودی را پردازش می‌کند تا مقدار عددی و واحد زمانی آن را استخراج کند.

  **پارامترها:**
  - timeframe (str): Input timeframe string.

  **نوع بازگشت:**
  - None

**۴. متد time_unit() -> str_:**

  این متد واحد زمانی استاندارد برای صرافی داده شده را برمی‌گرداند.

  **نوع بازگشت:**
  - str: Time unit.

**۵. متد numeric_value() -> int_:**

  این متد مقدار عددی استخراج شده از فریم زمانی را برمی‌گرداند.

  **نوع بازگشت:**
  - int: Numeric value.

**۶. متد time_interval() -> str_:**

  این متد تایم‌فریم متناظر با فریم زمانی را به صورت رشته برمی‌گرداند.

  **نوع بازگشت:**
  - str: Time interval.

**۷. متد actual_candles(num_candles: int = None) -> int_:**

  این متد بر اساس فریم زمانی ورودی، تعداد واقعی کندل‌ها را محاسبه می‌کند.

  **پارامترها:**
  - num_candles (int): Number of candles (optional).

  **نوع بازگشت:**
  - int: Actual number of candles.
