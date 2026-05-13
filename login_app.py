"""
ICTPRG302 - Python Project
Name: Julio Cesar Da Silva Filho
Date: 24/09/2024
Purpose: Login Application
"""
import sys


# import packages
def newRegistration():
    # ask user to enter new username and password
    # write this to accounts.txt

    username = input("Please enter new username:")
    password = input("Please enter password minimum length 10:")
    # also check meets minimum length 10 of password
    if len(password) < 10:
        print("Please enter password minimum length of 10")
        newRegistration()
    else:
        # open the file and add new username and new password
        myfile = open("accounts.txt", "a")
        # add the username and password in the next line
        myfile.write(f"{username},{password}\n")
        myfile.close()
        print("Username and password saved")

def displayUsers():
    # reading accounts.txt file and displaying username
    myfile = open("accounts.txt", "r")
    # read line by line
    lines = myfile.read().splitlines()
    # close the file
    myfile.close()
    # print the usernames
    print("Displaying Usernames: ")
    print()
    count = 0
    for line in lines:
        words = line.split(",")
        print(words[0])
        # count how many users we have in file
        count = count+1
    print("---------------------")
    print(f"Total users {count}.")


def login():
    # ask user to enter username and password
    # open file and compare with existing username and password
    username = input("Please enter your username:")
    password = input("Please enter your password:")
    print()
    # open the file and read
    myfile = open("accounts.txt", "r")
    lines = myfile.read().splitlines()
    myfile.close()

    for line in lines:
        words = line.split(",")
        # compare the typed username and password with the username and password inside the file
        if words[0] == username and password == words[1]:
            print("Correctly Username and Password!!")
            displayUsers()
            return
    print("Incorrectly Username and/or Password!!")

def main_menu():
    # Provides the options to user

    # Display choices
    print("--Main Menu--")
    print()
    print("Type 1 for New Registration")
    print("Type 2 for Login")
    print("Type 3 for Exit")
    print("-----------------------------------------------------------")

    # ask for user choices
    userChoice = input("Please type your choice as 1 or 2 or 3:")
    print()

    #process user choice
    if userChoice == "1":
        newRegistration()
    elif userChoice == "2":
        login()
    elif userChoice == "3":
        sys.exit("Thank you for using the application")
    else:
        print("Invalid option, please select again")
        main_menu()

# main menu of application
main_menu()
