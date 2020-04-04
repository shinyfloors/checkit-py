# Checkit

Checkit is a simple Python script to find and validate [BagIt](http://purl.org/net/bagit)-style packages using the @LibraryOfCongress [bagit-python](https://github.com/LibraryOfCongress/) project.

## Installation

Install [@LibraryOfCongress/bagit-python](https://github.com/LibraryOfCongress/) (or, at least, clone the repository).

Update the `checkit.py` script to specify the path to your bagit-python installation, the parent directory where your bags are located, and your log output directory. See below for more details.

```python
path_to_bagit = "/users/example/bagit-python"
path_to_parent_directory = "/users/example/bags/"
path_to_log_directory = "/users/example/checkit-logs"
```

## Usage

From your command line, use Python to run the `checkit.py` script.
```bash
python checkit.py
```

## Logging
The script will create log files in your specified directory. If this directory does not exist, the script will attempt to create it.

Log files follow the naming pattern of YYYY-MM-DD-hhmmss.txt (for example, 2020-04-01-123000.txt for 12:30:00 on 01 April 2020). Each time you run the script, a new log file will be generated.

## Disclaimer
I am not proud of this script. Feel free to contact me with requests/issues/concerns/whatever.