#!/bin/python3

"""
Owen Joslin
NSSA.221.02 - Systems Administration I
ScriptAssignment03
Friday, 21 October 2022
"""

import os
import subprocess
import time

HOME_DIR = subprocess.getoutput("cd ~; pwd")    # gets the home directory of the user

class COL:	# colors used for formating
    GREEN = "\033[92m"	
    YELLOW = "\033[93m"
    RED = "\033[91m"
    UNDER = "\033[4m"
    NORM = "\033[0m"

def startup():  # main menu options
    os.system("clear")
    print("      **************************************      ")
    print("      ********** " + COL.GREEN + "Shortcut Creator " + COL.NORM + "**********      ")
    print("      **************************************      \n")
    print("Enter Selection:\n")
    print("      1 - Create a shortcut in your home directory.")
    print("      2 - Remove a shortcut from your home directory.")
    print("      3 - Run shortcut report.\n")

def progress(): # prints out the progress bar
    progress = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", ""]
    print()
    for i in range(21):
        str1 = ""
        str1 = str1.join(progress)
        os.system("echo -ne '[" + str1 + "]  (" + str(i*5) + "%)\r'")
        os.system("sleep .075")
        progress[i] = "="
    print()

def createShortcut():   # creates a shortcut
    sentinal = 1
    while(sentinal == 1):
        file = input("Please enter the file of the name to create a shortcut:       ")  # prompts user for file
        if(file != ""):
            sentinal = 0
    find = subprocess.getoutput("cd ~; find ~+ -type f -name " + file)  # finds file location
    if(find != ""): # if a file was found
        confirm = input("Found " + COL.GREEN + find + COL.NORM + ". Create shortcut? (Y/N)        ")    # prompt user if they want to create a shortcut
        if(confirm.upper() == "Y"):
            progress()
            os.system("ln  -s " + find + " " + HOME_DIR + "/" + file)   # and create the shortcut
            input("\nPress" + COL.YELLOW + " Enter" + COL.NORM + " to return to" + COL.YELLOW + " main menu" + COL.NORM + ".       ")
        else:
            return
    else:
        input("File not found: " + COL.RED + file + COL.NORM +  ". Press" + COL.YELLOW + " Enter" + COL.NORM + " to return to" + COL.YELLOW + " main menu" + COL.NORM + ".       ") # if no file was found, say so and prompt to exit
    
def removeShortcut():   # remove a shortcut
    sentinal = 1
    while(sentinal == 1):
        file = input("Please enter the shortcut/link to remove:       ")    # prompts user for file
        if(file != ""):
            sentinal = 0
    confirm = input("Are you sure you want to remove " + COL.GREEN + file + COL.NORM + "? (Y/N)       ")    # prompt user if they want to remove a shortcut
    if(confirm.upper() == "Y"): # if yes
        print("Removing link, please wait...")
        progress()
        os.system("cd ~; rm " + file)   # remove the shortcut
        input("\nPress" + COL.YELLOW + " Enter" + COL.NORM + " to return to" + COL.YELLOW + " main menu" + COL.NORM + ".       ")   # and prompt to exit

def getLinks(): # gets the symbolic links and target parths, and prints them
    sym_link = subprocess.getoutput("cd ~; find . -maxdepth 1 -type l -ls | awk '{print $11}'") # gets the symbolic links
    tar_path = subprocess.getoutput("cd ~; find . -maxdepth 1 -type l -ls | awk '{print $13}'") # gets the target parths
    sym_link_str1 = ""; tar_path_str1 = ""
    sym_link_list = sym_link_str1.join(sym_link).split()    # converts output of system commands to strings
    tar_path_list = tar_path_str1.join(tar_path).split()
    
    table_data = []
    for i in range(len(sym_link_list)): # adds strings to 2d list so we can format output
        col = []
        col.append(sym_link_list[i]); col.append(tar_path_list[i])
        table_data.append(col)
    
    print("The number of links is: " + COL.YELLOW + str(len(sym_link_list)) + COL.NORM + ".\n") # prints the symbolic links and target parths
    print(COL.UNDER + COL.YELLOW + "Symbolic Link" + COL.NORM + "             " + COL.UNDER + COL.YELLOW +"Target Path" + COL.NORM)
    for row in table_data:
        print("{: <25} {: <25}".format(*row))

def report():   # prints CLI for shortcut report
    print("      **************************************      ")
    print("      ********** " + COL.GREEN + "Shortcut  Report " + COL.NORM + "**********      ")
    print("      **************************************      \n")
    print("User Home Directory: " + COL.YELLOW + HOME_DIR + COL.NORM + ".\n")
    getLinks()
    command = input("\nTo return to the" + COL.YELLOW + " main menu" + COL.NORM + ", press" + COL.YELLOW + " Enter" + COL.NORM + ". Or select" + COL.YELLOW + " \"R\"" + COL.NORM + " to remove a link.")
    if(command.upper() == "R"):
        os.system("clear")
        removeShortcut()

def main():
    sentinal = True
    while(sentinal == True):	# continuously run the program
        startup()	# print main menu
        command = input("Please enter a number " + COL.GREEN + "1 - 3" + COL.NORM + " or " + COL.GREEN + "\"quit\" " + COL.NORM + "to quit the program.      ")	# then prompt user for an option
        if(command == "1"):	# if the command is 1
            os.system("clear")	
            createShortcut()
        elif (command == "2"):	# if the command is 2
            os.system("clear")	
            removeShortcut()
        elif (command == "3"):	# if the command is 3
            os.system("clear")	
            report()
        elif(command.upper() == "QUIT"):	# if the user wants to quit
            sentinal = False	# set sentinal to false
        else:	# if the command was incorrect
            print("\nYou enetered an " + COL.RED + "invalid option" + COL.NORM + "!\n")	# tell the user
            print("Please select a number between 1 through 3\n")	# and ask for a proper command
            time.sleep(5)

if __name__ == "__main__":
	main()