# Shortcut Script

## Overview
Symbolic links are prevalent in Linux systems, providing easy access to files or maintaining different versions of the same library. They are similar to shortcuts in Windows. This scripting exercise will help you become familiar with various commands used to find and create symbolic links and their associated target paths. Both Bash and Python commands are available and may be used in the script.

## Script Requirements

### General
- **Script Name:** `shortcut.py`
- **Language:** Python 3
- **Target Environment:** CentOS 8 virtual machine
- **Location:** `/home/student`
- **Functions:**
  - Create a symbolic link
  - Delete a symbolic link
  - Generate a report summarizing symbolic links in the user's home directory

### Report Content
- Startup Menu
- Option 1: Create a Shortcut
- Option 2: Remove a Shortcut
- Option 3: Run Shortcut Report

### Output
The script should provide a clear and simple menu for the end-user to create, delete, and report on symbolic links.

## Installation Instructions

Before running the script, ensure that Python 3 is installed on your CentOS 8 virtual machine.

## Usage
1. Place the `shortcut.py` script in the directory `/home/student`.
2. Run the script using Python 3:
```bash
python3 /home/student/shortcut.py
```

The script will display a menu with options to create a symbolic link, delete a symbolic link, and generate a report on symbolic links in the user's home directory.