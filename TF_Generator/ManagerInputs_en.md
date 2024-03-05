# Documentation Guide (ManagerInputs):

### Introduction:
The InputsManager class is designed to standardize input values, such as timeframes, for different exchanges.

## Methods:

**1. __init__(timeframe: str, exchange: str, num_candles: int = None, logger=None):**

  Initializes the InputsManager instance with the given parameters.
  
  **Parameters:**
  - timeframe (str): Input timeframe string (e.g., '1min', '2H', '1D').
  - exchange (str): Name of the exchange for which the input is being standardized.
  - num_candles (int): Number of candles (optional).
  - logger: LoggerManager instance (optional).

  **Usage Example:**
  ```python
      inputs_manager = InputsManager(timeframe="1H", exchange="Wallex", num_candles=100, logger=my_logger)
  ```

**2. setup_regularize_inputs_values():**

  Sets up the InputsManager instance by calling necessary setup methods.

**3. _parse_timeframe(timeframe: str) -> None:**

  Parses the input timeframe string to extract the numeric value and time unit.

  **Parameters:**
  - timeframe (str): Input timeframe string.

  **Returns:**
  - None

**4. _time_unit() -> str:**

  Returns the standardized time unit for the given exchange.

  **Returns:**
  - str: Time unit.

**5. _numeric_value() -> int:**

  Returns the numeric value extracted from the timeframe.

  **Returns:**
  - int: Numeric value.

**6. _time_interval() -> str:**

  Returns the interval string corresponding to the timeframe.

  **Returns:**
  - str: Time interval.

**7. _actual_candles(num_candles: int = None) -> int:**

  Calculates the actual number of candles based on the input timeframe.

  **Parameters:**
  - num_candles (int): Number of candles (optional).

  **Returns:**
  - int: Actual number of candles.

