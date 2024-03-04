### <p align="center"> English

# <p align="center"> Project Name : TimeFrameGenerator

## Description
TimeFrameGenerator is a Python program designed to generate custom time frames for different symbols using exchange APIs. It provides flexibility in defining specific time intervals for data retrieval from exchanges.

## Example.py File
The Example file demonstrates how to use the TimeFrameGenerator program to generate custom time frames for various symbols.

## Requirements:
**1. Python Environment:** Python must be installed on the system.
python
```
    pip install -r requirements.txt
```

**2. TF_Generator Module:** The program imports the GenerateOHLCV class from the GenerateTimeFrame module, which requires the TF_Generator package to be installed and accessible.

**3. Exchange APIs:** The program relies on the availability and accessibility of APIs provided by specified exchanges (e.g., Wallex, Nobitex, Binance, Coinbase, BingX).

**4. Symbol and Exchange Parameters:** Users need to specify the symbol (e.g., "BTCUSDT") and exchange (e.g., "BingX") for which they want to generate OHLCV data.

**5. Timeframe Interval:** The timeframe interval should be specified according to the supported intervals of the chosen exchange. For example, for "BingX", intervals like "1m", "5m", "1d" are supported.

## Usage
1. Import the GenerateOHLCV class from the GenerateTimeFrame module.
2. Create an instance of the GenerateOHLCV class with the desired parameters: symbol, timeframe, exchange, num_candles.
3. Use the instance to retrieve OHLCV data for the specified symbol, timeframe, and exchange.
4. Refer to the documentation provided with the GenerateTimeFrame module for detailed usage instructions.

## Classes

### 1. HistoryFetch
Responsible for fetching historical data from exchange APIs.

### 2. MakeTimeFrame
Generates custom time frames based on user-defined specifications.

### 3. ManagerFile
Manages file operations such as reading and writing data to files.

### 4. ManagerInputs
Handles user inputs and validates them for use in the program.

### 5. ManagerLogger
Manages logging functionality to record program events and errors.

### 6. ManagerTime
Manages time-related operations and conversions.

### 7. OrganizerDataFrame
Organizes data retrieved from APIs into structured data frames.

### 8. OrganizerTimeFrame
Organizes time frames according to specified intervals.

## Possible Problems:
**1. API Availability:** The program's functionality depends on the availability and reliability of APIs provided by the exchanges. If an exchange's API is down or inaccessible, the program may fail to retrieve data.

**2. Input Validation:** The program assumes that the user provides valid inputs for the symbol, exchange, timeframe interval, and number of candles. If invalid inputs are provided, the program may encounter errors or unexpected behavior.

**3. Timeouts:** If the program is making API requests and the connection times out or takes too long to respond, it may lead to delays or errors in data retrieval.

**4. Error Handling:** The program lacks comprehensive error handling mechanisms, which may make it challenging to diagnose and troubleshoot issues during execution.

## Disclaimer
This program is provided as-is, without any warranty or guarantee. Users are responsible for ensuring the accuracy and reliability of the data retrieved using this program. The author shall not be liable for any damages or losses arising from the use of this program.

## Contributions
Contributions to TimeFrameGenerator are welcome! Users can contribute by reporting bugs, suggesting features, or contributing code enhancements. Feel free to open issues or pull requests on the GitHub repository.

## License
This project is licensed under the GPL-3.0 License. See the [LICENSE](./LICENSE) file for details.

**Please let me know if there are any specific modifications or additions you'd like to make.**


### <p align="center"> فارسی

# <p align="center"> نام پروژه : TimeFrameGenerator

## توضیحات
برنامه پایتونی TimeFrameGenerator تایم‌فریم‌های سفارشی را برای نمادهای مختلف با استفاده از API‌های صرافی تولید می‌کند. این برنامه انعطاف‌پذیری لازم را برای ساخت تایم‌فریم‌های مختلف از صرافی‌ها فراهم می‌کند.

## فایل Example.py
فایل مثال نحوه استفاده از برنامه تولید کننده چارچوب زمانی سفارشی را برای نمادهای مختلف نشان می‌دهد.

## الزامات:
**۱. محیط پایتون:** پایتون باید روی سیستم نصب شود.
python
```
    pip install -r requirements.txt
```

**۲. ماژول TF_Generator:** برنامه کلاس GenerateOHLCV را از ماژول GenerateTimeFrame وارد می کند، که نیاز به نصب و دسترسی به بسته TF_Generator دارد.

**۳. ای‌پی‌آي‌های(API) صرافی:** این برنامه به در دسترس بودن و دسترسی به APIهای ارائه شده توسط صرافی های مشخص (مانند Wallex، Nobitex، Binance، Coinbase، BingX) متکی است.

**۴. پارامترهای نماد و تبادل:** کاربران باید نماد (مانند "BTCUSDT") و مبادله (مانند "BingX") را که می خواهند برای آن داده های OHLCV تولید کنند، مشخص کنند.

**۵. فاصله زمانی:** فاصله بازه زمانی باید با توجه به فواصل پشتیبانی شده صرافی انتخاب شده مشخص شود. به عنوان مثال، برای "BingX"، فواصل مانند "1m"، "5m"، "1d" پشتیبانی می‌شود.


## استفاده
۱. کلاس GenerateOHLCV را از ماژول GenerateTimeFrame وارد کنید.

۲. یک نمونه از کلاس GenerateOHLCV با پارامترهای مورد نظر ایجاد کنید: نماد، تایم فریم، تبادل، num_candles.

۳. از نمونه برای بازیابی داده های OHLCV برای نماد، بازه زمانی و تبادل مشخص شده استفاده کنید.

۴. برای دستورالعمل های استفاده دقیق به مستندات ارائه شده با ماژول GenerateTimeFrame مراجعه کنید.


## کلاس‌ها

### ۱. کلاس HistoryFetch
مسئول بارگیری داده‌های تاریخی از API‌های صرافی است.

### ۲. کلاس MakeTimeFrame
چارچوب‌های زمانی سفارشی را بر اساس مشخصات تعریف شده توسط کاربر ایجاد می‌کند.

### ۳. کلاس ManagerFile
عملیات فایل مانند خواندن و نوشتن داده به فایل‌ها را مدیریت می‌کند.

### ۴. کلاس ManagerInputs
ورودی‌های کاربر را مدیریت کرده و آن‌ها را برای استفاده در برنامه اعتبارسنجی می‌کند.

### ۵. کلاس ManagerLogger
قابلیت ثبت رویدادها و خطاهای برنامه را مدیریت می‌کند.

### ۶. کلاس ManagerTime
عملیات مربوط به زمان و تبدیل‌ها را مدیریت می‌کند.

### ۷. کلاس OrganizerDataFrame
داده‌های دریافت شده از API‌ها را به فریم‌های داده ساختارمند ترتیب می‌دهد.

### ۸. کلاس OrganizerTimeFrame
چارچوب‌های زمانی را بر اساس فواصل زمانی مشخص مرتب می‌کند.

## مشکلات احتمالی:
**۱. در دسترس بودن API:** عملکرد برنامه به در دسترس بودن و قابلیت اطمینان API های ارائه شده توسط صرافی ها بستگی دارد. اگر API یک صرافی خراب یا غیر قابل دسترسی باشد، ممکن است برنامه نتواند داده ها را بازیابی کند.

**۲. اعتبار ورودی‌ها (Input Validation):** برنامه فرض می کند که کاربر ورودی های معتبری را برای نماد، تبادل، بازه زمانی و تعداد شمع ها ارائه می دهد. اگر ورودی های نامعتبر ارائه شود، برنامه ممکن است با خطاها یا رفتار غیرمنتظره ای مواجه شود.

**۳. وقفه‌ها:** اگر برنامه درخواست‌های API را ارسال می‌کند و زمان اتصال به پایان می‌رسد یا پاسخگویی بیش از حد طول می‌کشد، ممکن است منجر به تأخیر یا خطا در بازیابی داده شود.

**۴. مدیریت خطا:** برنامه فاقد مکانیسم های جامع رسیدگی به خطا است، که ممکن است تشخیص و عیب یابی مشکلات را در حین اجرا چالش برانگیز کند.


## سلب مسئولیت
این برنامه به صورت "چگونه هست" ارائه شده است، بدون هیچ گونه گارانتی یا تضمینی. کاربران مسئول اطمینان از دقت و قابلیت اعتماد داده‌های به دست آمده با استفاده از این برنامه هستند. نویسنده این برنامه در قبال هر گونه آسیب یا ضرر ناشی از استفاده از این برنامه مسئولیتی ندارد.

## مشارکت‌ها
مشارکت‌ها در تولید کننده چارچوب زمانی سفارشی مورد استقبال قرار می‌گیرند! کاربران می‌توانند با گزارش باگ‌ها، پیشنهاد ویژگی‌ها یا ارائه افزودنی‌های کدی، به این پروژه کمک کنند. احساس راحتی کنید که مشکلات یا درخواست‌های پیشنهادی را در مخزن GitHub باز کنید.

## مجوز
این پروژه تحت مجوز GPL-3.0 است. برای جزئیات، فایل [LICENSE](./LICENSE) را مشاهده کنید.

**اگر نیاز به اصلاح یا حذف و اضافه شدن موارد دیتگری هست، لطفاً به من اطلاع دهید!**