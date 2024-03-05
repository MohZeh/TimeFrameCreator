# راهنما و مستندات (ManagerLogger)

### مقدمه:
کلاس LoggerManager قابلیت‌های مورد نیاز برای مدیریت عملیات ثبت وقایع در برنامه‌های پایتون را فراهم می‌کند. این کلاس شامل متدهایی برای شروع تنظیمات ثبت وقایع، ثبت پیام‌های خطا و پیام‌های دیباگ است.

## متدها:

**۱. متد init__(log_directory: str = LOG_DIRECTORY, log_file_name: str = LOG_FILE_NAME, log_level: int = logging.DEBUG)__:**

  این متد نمونه LoggerManager را با پارامترهای اختیاری برای دایرکتوری ثبت، نام فایل ثبت و سطح ثبت اولیه مقداردهی می‌کند.
  
  **مثال استفاده:**
  ```python
      logger = LoggerManager(log_directory="/path/to/logs", log_file_name="app.log", log_level=logging.INFO)
  ```

**۲. متد _()setup_logger:**

  این متد لاگر را برای پردازش فایل راه‌اندازی می‌کند و تنظیمات لاگر را پیکربندی می‌کند.
  
  **مثال استفاده:**
    این متد به طور داخلی در هنگام شروع نمونه LoggerManager فراخوانی می‌شود.


**۳. متد log_error(message: str):**

  یک پیام خطا را ثبت می‌کند.
  
  **پارامترها:**
  - (message (str): Error message to be logged)
  
  **مثال استفاده:**
  ```python
      logger.log_error("An error occurred while processing the data.")
  ```

**۴. متد log_debug(message: str, *args, \**\*kwargs):**

یک پیام دیباگ را ثبت می‌کند.

  **پارامترها:**
  - message (str): Debug message to be logged.
  - *args: Additional positional arguments.
  - **kwargs: Additional keyword arguments.
    
**مثال استفاده:**
  ```python
      logger.log_debug("Received data:", data, timestamp="2023-01-01")
  ```

**نتیجه:**

با استفاده از این راهنما و مستندات، کاربران می‌توانند به طور موثر از کلاس LoggerManager برای مدیریت عملیات ثبت وقایع در برنامه‌های پایتون خود استفاده کنند. مثال‌های ارائه شده نحوه استفاده از هر متد برای ثبت پیام‌های خطا و دیباگ را نشان می‌دهند.
