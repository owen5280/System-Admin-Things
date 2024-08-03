# Attacker Report Script

## Overview
The security team has observed an increase in failed login attempts on one of its remote servers. To identify if other servers are also affected, this script generates a report analyzing the system log file for attack patterns. The report includes the IP address, the number of failed login attempts (if the attempts are ten or more), the country of origin, and the report date.

## Script Requirements

### General
- **Script Name:** `attacker_report.py`
- **Language:** Python 3
- **Target Environment:** CentOS 8 virtual machine
- **Location:** `/home/student`
- **System Log File:** `syslog.log` (provided, to be placed in the same directory as the script)

### Report Content
- IP address
- Number of failed login attempts (if ≥ 10)
- Country of origin
- Date of the report

### Output
The report should be organized and readable. Refer to Figure 1 for sample output. The format does not need to match precisely but should display information clearly.

## Installation Instructions
Before running the script, ensure the following Python packages are installed:
```bash
python3 -m pip install python-geoip-python3
python3 -m pip install python-geoip-geolite2
```

Additionally, import the following module in your script:
```python
from geoip import geolite2
```

## Usage
1. Download the `syslog.log` file and place it in the same directory as the script.
2. Run the script using Python 3:
```bash
python3 attacker_report.py
```

The script will analyze the `syslog.log` file and generate a report displaying the specified details. The report helps the security team monitor remote login attempts and identify potential attack sources.