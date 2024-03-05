# Documentation & Guide (ManagerLogger):

### Introduction:
The LoggerManager class provides functionalities to manage logging operations within Python applications. It offers methods to initialize logging settings, log error messages, and debug messages.

## Methods:

**1. __init__(log_directory: str = LOG_DIRECTORY, log_file_name: str = LOG_FILE_NAME, log_level: int = logging.DEBUG):**

  Initializes the LoggerManager instance with optional parameters for log directory, log file name, and log level.
  
  **Usage Example:**
  ```python
      logger = LoggerManager(log_directory="/path/to/logs", log_file_name="app.log", log_level=logging.INFO)
  ```

**2. _setup_logger():**

  Sets up the logger with a file handler, configuring the logging settings.
  
  **Usage Example:**
    This method is called internally during the initialization of the LoggerManager instance.


**3. log_error(message: str):**

  Logs an error message.
  
  **Parameters:**
  - message (str): Error message to be logged.
  
  **Usage Example:**
  ```python
      logger.log_error("An error occurred while processing the data.")
  ```

**4. log_debug(message: str, *args, \**\*kwargs):**

Logs a debug message.

**Parameters:**
  - message (str): Debug message to be logged.
  - *args: Additional positional arguments.
  - **kwargs: Additional keyword arguments.

**Usage Example:**
  ```python
      logger.log_debug("Received data:", data, timestamp="2023-01-01")
  ```

**Conclusion:**

With this guide and documentation, users can effectively utilize the LoggerManager class to manage logging operations in their Python applications. The provided examples demonstrate the usage of each method for logging error and debug messages.
