#!/bin/python3

"""
Owen Joslin
NSSA.221.02 - Systems Administration I
ScriptAssignment01
Sunday, 18 September 2022
"""

import os
import subprocess
import time

GATEWAY = subprocess.getoutput("ip route show default | awk \'/default/ {print $3}\'")	# retrieves the gateway from the computer when the program starts
REMOTEIPADDRESS = "129.21.3.17" # RIT's DNS
DNS = "www.google.com" # 8.8.8.8

class COL:	# colors used for formating
    GREEN = "\033[92m"	
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    NORM = "\033[0m"

def startup():	# main menu greeting and options 
	os.system("clear")
	print("      **************************************      ")
	print("      ****** " + COL.GREEN + "Ping Test Troubleshooter " + COL.NORM + "******      ")
	print("      **************************************      \n")
	print("Enter Selection:\n")
	print("      1 - Test connectivity to your gateway.")
	print("      2 - Test for remote connectivity.")
	print("      3 - Test for DNS resolution.")
	print("      4 - Display gateway IP Address.\n")

def gateway():	# ping tester for the gateway
	os.system("clear")
	print("Testing connectivity to your gateway...\n")
	print("Running test, please wait.\n")
	time.sleep(4)
	if(subprocess.call("ping -c 1 " + GATEWAY, shell=True) == 0):	# if the connection is sucessful
		print("\nPlease infrom your system administrator that the test was " + COL.GREEN + "SUCCESSFUL" + COL.NORM + "!\n")	# tell the user
	else:
		print("\nPlease infrom your system administrator that the test has " + COL.FAIL + "FAILED" + COL.NORM + "!\n")	# or tell them otherwise
	input("Press \"ENTER\" to continue\n")

def remoteIPAddress():	# ping tester for the remote ip address
	os.system("clear")
	print("Testing for remote connectivity... trying IP address " + REMOTEIPADDRESS + "\n")
	print("Running test, please wait.\n")
	time.sleep(4)
	if(subprocess.call("ping -c 1 " + REMOTEIPADDRESS, shell=True) == 0):	# if the connection is sucessful	
		print("\nPlease infrom your system administrator that the test was " + COL.GREEN + "SUCCESSFUL" + COL.NORM + "!\n")	# tell the user
	else:
		print("\nPlease infrom your system administrator that the test has " + COL.FAIL + "FAILED" + COL.NORM + "!\n")	# or tell them otherwise
	input("Press \"ENTER\" to continue\n")

def dns():	# ping tester for the dns
	os.system("clear")
	print("Resolving DNS: trying URL... " + DNS + ".\n")
	print("Running test, please wait.\n")
	time.sleep(4)
	if(subprocess.call("ping -c 1 " + DNS, shell=True) == 0):	# if the connection is sucessful
		print("\nPlease infrom your system administrator that the test was " + COL.GREEN + "SUCCESSFUL" + COL.NORM + "!\n")	# tell the user
	else:
		print("\nPlease infrom your system administrator that the test has " + COL.FAIL + "FAILED" + COL.NORM + "!\n")	# or tell them otherwise
	input("Press \"ENTER\" to continue\n")

def main():
	sentinal = True
	while(sentinal == True):	# continuously run the program
		startup()	# print main menu
		command = input("Please enter a number " + COL.GREEN + "1 - 4" + COL.NORM + " or " + COL.GREEN + "\"Q/q\" " + COL.NORM + "to quit the program.      ")	# then prompt user for an option
		if(command == "1"):	# if the command is 1
			gateway()
		elif (command == "2"):	# if the command is 2
			remoteIPAddress()
		elif (command == "3"):	# if the command is 3
			dns()
		elif (command == "4"):	# if the command is 4
			os.system("clear")	
			print("Your gateway IP address is " + COL.WARNING + GATEWAY + COL.NORM +  ".\n")	# print the GATEWAY 
			input("Press \"ENTER\" to continue\n")
		elif(command.upper() == "Q"):	# if the user wants to quit
			sentinal = False	# set sentinal to false
		else:	# if the command was incorrect
			print("\nYou enetered an " + COL.WARNING + "invalid option" + COL.NORM + "!\n")	# tell the user
			print("Please select a number between 1 through 4\n")	# and ask for a proper command
			time.sleep(5)

if __name__ == "__main__":
	main()