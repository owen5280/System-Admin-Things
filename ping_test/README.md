# Ping Test Script

## Overview
The end-user will run this script to test network connectivity. This facilitates troubleshooting by allowing the end-user to communicate the success or failure of each test to the system administrator. From a CentOS 8 virtual machine, the script will test connectivity to the gateway, a remote IP address, and a URL to validate DNS resolution. The output must be direct and unambiguous to ensure accurate information is provided by the end-user.

## Script Requirements

### General
- **Script Name:** `ping_test.py`
- **Language:** Python 3
- **Target Environment:** CentOS 8 virtual machine
- **Location:** `/home/student`
- **Tests Conducted:**
  - Connectivity to the gateway (pfSense LAN interface)
  - Connectivity to a remote IP address (RIT’s DNS: 129.21.3.17)
  - DNS resolution using the URL `www.google.com`

### Report Content
- Title: "Attacker Report" with today's date.
- Column Headers: "Count", "IP ADDRESS", and "COUNTRY" with color formatting.
- Rows: Each row contains the count of failed attempts, the IP address, and the corresponding country code for IPs with 10 or more failed attempts.

### Output
The script output should be clear and direct, indicating the success or failure of each test.

## Installation Instructions

Before running the script, ensure that Python 3 is installed on your CentOS 8 virtual machine.

## Usage
1. Place the `ping_test.py` script in the directory `/home/student`.
2. Run the script using Python 3:
```bash
python3 /home/student/ping_test.py
```

The script will test network connectivity to the gateway, a remote IP address, and a URL for DNS resolution. The results will be displayed in an easy-to-understand format for end-users to report back to system administrators.

