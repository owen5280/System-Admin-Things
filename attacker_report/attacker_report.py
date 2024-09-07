#!/bin/python3

"""
Owen Joslin
NSSA.221.02 - Systems Administration I
ScriptAssignment04
Friday, 04 November 2022
"""

from datetime import date
import re
import requests
import os

class COL:	# colors used for formating
    GREEN = "\033[92m"	
    RED = "\033[91m"
    NORM = "\033[0m"

def getIpAddresses():
    ipaddrs = {}    # dicionary for ips

    log = open('syslog.log', 'r')   # opens the log file for reading
    reader = log.read() # reads the log
    allipaddrs = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", reader)  # and pulls out ALL ips and puts them in allipaddrs

    for ip in allipaddrs:   # puts the ips into a dictioary, incrementing the number of each ip each time
        try:
            ipaddrs[ip] += 1
        except KeyError:
            ipaddrs[ip] = 1

    return dict(sorted(ipaddrs.items(), key = lambda kv: kv[1]))  # sorts the dictionary in accending order

def main():
    sorted_ips = getIpAddresses()

    os.system("clear")  # clears the terminal
    todaysdate = date.today().strftime("%B %d, %Y") # gets todays current date
   
    table_data = [] # creates a table for formating output
    for x in sorted_ips.keys(): # adds strings to 2d list so we can format output
        if sorted_ips.get(x) >= 10: # any with more than 10 ips gets added to output
            data = requests.get(f'https://api.ipdata.co/{x}?api-key={"KEY"}').json()   # uses an api for country code, couldnt get geolite2 to work
            country_code = data["country_code"] # gets country code for the ip
            col = []
            col.append(sorted_ips.get(x)); col.append(x); col.append(country_code)  # and appends all three fields to teh table (Count, IP Address, and Country)
            table_data.append(col)  # then adds each ip to the table

    print(COL.GREEN + "Attacker Report" + COL.NORM + " - " + todaysdate + "\n") # prints todays date
    
    print(COL.RED + "Count" + COL.NORM + "      " + COL.RED + "IP ADDRESS" + COL.NORM + "           " + COL.RED + "COUNTRY" + COL.NORM) # and the column headers
    for row in table_data:  # then the data in the table 
        print("{: <10} {: <20} {: <20}".format(*row))
    
if __name__ == "__main__":
	main()
