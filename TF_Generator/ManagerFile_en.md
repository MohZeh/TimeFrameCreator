## Documentation & Guide (ManagerFile)

### Overview
The `FileManager` class facilitates the management of OHLCV (Open, High, Low, Close, Volume) DataFrame files, including saving and reading operations. It provides methods to save OHLCV DataFrames to CSV files and read existing OHLCV DataFrames from CSV files.

## Methods

**`__init__(data_directory: str, logger=None)`**

Initializes a FileManager instance.

**Parameters:**
- `data_directory` (str): The directory path where OHLCV DataFrame files will be stored.
- `logger`: Optional logger instance for logging messages.

**`_setup_file_manager()`**

Sets up the FileManager by initializing necessary instances.

**`_save_df_ohlcv(file_name: str, ohlcv_dataframe: pd.DataFrame) -> None`**

Saves the OHLCV DataFrame to a CSV file.

**Parameters:**
- `file_name` (str): The name of the file to be saved.
- `ohlcv_dataframe` (pd.DataFrame): The OHLCV DataFrame to be saved.

**`_read_df_ohlcv(file_name: str) -> pd.DataFrame | None`**

Reads the existing OHLCV DataFrame from a CSV file.

**Parameters:**
- `file_name` (str): The name of the file to be read.

**Returns:**
- `pd.DataFrame | None`: The read OHLCV DataFrame or None if the file does not exist.

**`__del__()`**

Destructor method, performs cleanup tasks when the instance is deleted.

## Example Usage

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

This guide provides a clear understanding of how to use each method of the FileManager class, enabling users to efficiently manage OHLCV DataFrame files.
