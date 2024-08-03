#!/bin/python3

"""
Owen Joslin
NSSA.221.02 - Systems Administration I
ScriptAssignment02
Friday, 30 September 2022
"""

import os
import subprocess

# global vars for all sys infor
HOSTNAME = None; DOMAIN = None; IPADDR = None; GATEWAY = None; NETWORK_MASK = None; DNS = None; OS = None; OS_VER = None; KERNEL = None; HD_CAPACITY = None; HD_AVALABLE = None; CPU = None; CPU_PROCESSORS = None; CPU_CORES = None; RAM = None; RAM_AVALABLE = None; FILEAPTH = None

class TEXT: # colors used for formating
    GREEN = "\033[92m\033[1m"	
    YELLOW = "\033[93m\033[1m"
    RED = "\033[91m\033[1m"
    BOLD = "\033[1m"
    NORMAL = "\033[0m\033[0m"

def getSystemInfo():    # collects the system information
    global HOSTNAME, DOMAIN, IPADDR, GATEWAY, NETWORK_MASK, DNS, OS, OS_VER, KERNEL, HD_CAPACITY, HD_AVALABLE, CPU, CPU_PROCESSORS, CPU_CORES, RAM, RAM_AVALABLE, FILEAPTH
    HOSTNAME = subprocess.getoutput("hostname | cut -d\".\" -f1")   # gets hostmname
    whoami = subprocess.getoutput("whoami") # gets the username
    FILEAPTH = "/home/" + whoami + "/" + HOSTNAME  + "_system_report.log"   # gets creates the filepath for the log file
    os.system("touch " + FILEAPTH) # creates the file
    DOMAIN = subprocess.getoutput("hostname | cut -d\".\" -f2-")    # gets the domain
    IPADDR = subprocess.getoutput("hostname -I | awk '{print $1}'") # gets teh ip addr
    netdev = subprocess.getoutput("ip route | grep \"default\" | awk '{print $5}'") # gets the main network device
    GATEWAY = subprocess.getoutput("ip route show default | awk '/default/ {print $3}'")    # gets the gateway
    NETWORK_MASK = subprocess.getoutput("ifconfig " + netdev + " | awk '/netmask/ {print $4}'") # gets the netmask
    DNS = subprocess.getoutput("cat /etc/resolv.conf | awk '/nameserver/ {print $2}'")  # gets the dns information
    OS = subprocess.getoutput("cat /etc/os-release | awk '/NAME/' | grep -oP '\"\K[^\"]+' | head -1")   # gets the os name
    OS_VER = subprocess.getoutput("cat /etc/os-release | awk '/VERSION_ID/' | grep -oP '\"\K[^\"]+'")   # gets the os version
    KERNEL = subprocess.getoutput("uname -r")   # gets the kernel version
    drive = subprocess.getoutput("findmnt / | awk '/\//{print $2}'")    # gets the main drive mounted on /
    HD_CAPACITY = subprocess.getoutput("df -h | grep " + drive + " | awk '{print $2}'") # gets the total hd capasity
    HD_AVALABLE = subprocess.getoutput("df -h | grep " + drive + " | awk '{print $4}'") # gets the avalable hd capasity
    CPU = subprocess.getoutput("cat /proc/cpuinfo | awk '/model name/' | cut -d' ' -f4- | tail -1") # gets the system information
    CPU_PROCESSORS = subprocess.getoutput("nproc")  # gets the number of processors
    CPU_CORES = subprocess.getoutput("cat /proc/cpuinfo | awk '/cpu cores/' | cut -d' ' -f3- | tail -1")    # gets the number of cores in a processor
    RAM = subprocess.getoutput("free -g -h -t | awk '/Mem/ {print $2}'")    # gets the total ram
    RAM_AVALABLE = subprocess.getoutput("free -g -h -t | awk '/Mem/ {print $4}'")   # gets the avalable ram

def printToFile():  # prints the system information to a file
    file = open(FILEAPTH, 'w')  # opens the log file for writing
    file.write(TEXT.RED + "           System Report - " + subprocess.getoutput("date") + TEXT.NORMAL + "\n")    # writes system info to the log file
    file.write(TEXT.GREEN + "\nDevice Information" + TEXT.NORMAL + "\n")
    file.write(TEXT.BOLD + "Hostname:                   " + TEXT.NORMAL + HOSTNAME + "\n")
    file.write(TEXT.BOLD + "Domain:                     " + TEXT.NORMAL + DOMAIN + "\n")
    file.write(TEXT.GREEN + "\nNetwork Information" + TEXT.NORMAL + "\n")
    file.write(TEXT.BOLD + "IP Address:                 " + TEXT.NORMAL + IPADDR + "\n")
    file.write(TEXT.BOLD + "Gateway:                    " + TEXT.NORMAL + GATEWAY + "\n")
    file.write(TEXT.BOLD + "Network Mask:               " + TEXT.NORMAL + NETWORK_MASK + "\n")
    record = ""; index = 1
    for x in DNS:   # prints each dns server to the log file
        if(x == "\n"): 
            file.write(TEXT.BOLD + "DNS" + str(index) + TEXT.NORMAL + ":                       " + record + "\n")
            record = ""
            index+=1
        else:
            record = record + str(x)
    file.write(TEXT.BOLD + "DNS" + str(index) + TEXT.NORMAL + ":                       " + record + "\n")   # writes the remaining system info to the log file
    file.write(TEXT.GREEN + "\nOS Information" + TEXT.NORMAL + "\n")
    file.write(TEXT.BOLD + "Operating System:           " + TEXT.NORMAL + OS + "\n")
    file.write(TEXT.BOLD + "Operating Version:          " + TEXT.NORMAL + OS_VER + "\n")
    file.write(TEXT.BOLD + "Kernel:                     " + TEXT.NORMAL + KERNEL + "\n")
    file.write(TEXT.GREEN + "\nStorage Information" + TEXT.NORMAL + "\n")
    file.write(TEXT.BOLD + "Hard Drive Capacity:        " + TEXT.NORMAL + HD_CAPACITY + "\n")
    file.write(TEXT.BOLD + "Avalable Space:             " + TEXT.NORMAL + HD_AVALABLE + "\n")
    file.write(TEXT.GREEN + "\nProcessor Information" + TEXT.NORMAL + "\n")
    file.write(TEXT.BOLD + "CPU Model:                  " + TEXT.NORMAL + CPU + "\n")
    file.write(TEXT.BOLD + "Number of Processors:       " + TEXT.NORMAL + CPU_PROCESSORS + "\n")
    file.write(TEXT.BOLD + "Cores per Processor:        " + TEXT.NORMAL + CPU_CORES + "\n")
    file.write(TEXT.GREEN + "\nMemory Information" + TEXT.NORMAL + "\n")
    file.write(TEXT.BOLD + "Total RAM:                  " + TEXT.NORMAL + RAM + "\n")
    file.write(TEXT.BOLD + "Available RAM:              " + TEXT.NORMAL + RAM_AVALABLE + "\n")
    file.close()

def main(): # main funciton to compile and print system information
    os.system("clear")
    print("Collecting system information... please wait.\n")
    getSystemInfo()
    printToFile()
    print("Done! System information can be found in: " + FILEAPTH + "\n")

if __name__ == "__main__":
    main()
