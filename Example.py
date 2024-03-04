### --- Example.py is sample to use TimeFrameGenerator class.
"""
This program demonstrates the usage of the GenerateOHLCV class from the GenerateTimeFrame module.
It allows users to generate OHLCV (Open, High, Low, Close, Volume) data for a specified symbol, timeframe, exchange, and number of candles.

Requirements:
1. Python Environment: Python must be installed on the system.
2. TF_Generator Module: The program imports the GenerateOHLCV class from the GenerateTimeFrame module, which requires the TF_Generator package to be installed and accessible.
3. Exchange APIs: The program relies on the availability and accessibility of APIs provided by specified exchanges (e.g., Wallex, Nobitex, Binance, Coinbase, BingX).
4. Symbol and Exchange Parameters: Users need to specify the symbol (e.g., "BTCUSDT") and exchange (e.g., "BingX") for which they want to generate OHLCV data.
5. Timeframe Interval: The timeframe interval should be specified according to the supported intervals of the chosen exchange. For example, for "BingX", intervals like "1m", "5m", "1d" are supported.

Possible Problems:
1. API Availability: The program's functionality depends on the availability and reliability of APIs provided by the exchanges. If an exchange's API is down or inaccessible, the program may fail to retrieve data.
2. Input Validation: The program assumes that the user provides valid inputs for the symbol, exchange, timeframe interval, and number of candles. If invalid inputs are provided, the program may encounter errors or unexpected behavior.
3. Timeouts: If the program is making API requests and the connection times out or takes too long to respond, it may lead to delays or errors in data retrieval.
4. Error Handling: The program lacks comprehensive error handling mechanisms, which may make it challenging to diagnose and troubleshoot issues during execution.

Usage:
1. Import the GenerateOHLCV class from the GenerateTimeFrame module.
2. Create an instance of the GenerateOHLCV class with the desired parameters: symbol, timeframe, exchange, num_candles.
3. Use the instance to retrieve OHLCV data for the specified symbol, timeframe, and exchange.
4. Refer to the documentation provided with the GenerateTimeFrame module for detailed usage instructions.

Example Usage:
from TF_Generator.GenerateTimeFrame import GenerateOHLCV

symbol = "BTC-USDT"
timeframe = "1min"
exchange = "BingX"
num_candles = 10000

with GenerateOHLCV(
    symbol=symbol, timeframe=timeframe, exchange=exchange, num_candles=num_candles
) as ohlcv_object:
    print("Symbol:", symbol, "--> Exchange:", exchange, "\n")
    print(ohlcv_object.timeframe_release())

    print("------------ end ------------\n")
"""
from TF_Generator.GenerateTimeFrame import GenerateOHLCV
import time

symbol_13 = "BTCUSDT"
symbol_45 = "BTC-USDT"
symbol = symbol_45

### interval "BingX": (min), (H), (D), (W), (M)
interval = "1min"

### Exchanges: "Wallex", "Nobitex", "Binance", "Coinbase", "BingX"
exchange1 = "Wallex"
exchange2 = "Nobitex"
exchange3 = "Binance"
exchange4 = "Coinbase"
exchange5 = "BingX"
exchange = exchange5

num_candles = 10000

with GenerateOHLCV(
    symbol=symbol, timeframe=interval, exchange=exchange, num_candles=num_candles
) as ohlcv_object:
    print("Symbol:", symbol, "--> Exchange:", exchange, "\n")
    print(ohlcv_object.timeframe_release())

    print("------------ end ------------\n")

    # cycle = 3
    # for i in range(x):
    #     print("Exchange:", exchange, "\n")
    #     print("Number of Cycle: ", i + 1)
    #     print(ohlcv_object.timeframe_release())

    #     print("------------ end ------------\n")
    #     if i + 1 < cycle:
    #         time.sleep(5)
