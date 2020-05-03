#!/bin/env python3


"""User specifies a file name and a person name,
the program then finds the address of the person named"""


# Displays all names and addresses in the file
def All():
    f = open('doc/AddressBook.txt', "r")
    for line in f:
        print(line)
    f.close

# Adds name and address to file
def Add(N, A):
    f = open('doc/AddressBook.txt', 'a')
    f.write('\n')
    f.write(N + ":" + A)
    f.close
    print("Wrote to 'AddressBook.txt'")

#Enter name to delete
def Delete():
    pass

# Returns the name provided the address
def OnePerson(A):
    for key, value in Dict.items():
        if A == value:
            return("The address you entered belongs to: " + key)
    else: return "Name not found"


# Returns the address provided the name
def OneAddress(N):
    for key, value in Dict.items():
        if N == key:
            return(N + "'s address is " + value)
    return "Not found"


# First create the dictionary and then use the other functions to search
def CreateDict():
    Dict = {}
    f = open('doc/AddressBook.txt', 'r')
    for line in f:
        nline = line.strip('\n')
        if nline not in Dict:
            strip = nline.split(':', 1)
            Dict[strip[0]] = strip[1]
    f.close
    return Dict


def Menu():
    print()
    print("Choose one: All, Add, OnePerson, OneAddress, or Delete")
    print("To exit enter X")
    print()
    option = input(">? ")
    print()
    if option.lower() == 'x':
        quit()
    elif option.lower() == 'all':
        print()
        All()
    elif option.lower() == 'add':
        name = input("Enter name: ") 
        address = input("Enter address: ")
        print()
        Add(name, address)
    elif option.lower() == 'oneperson':
        address = input("Enter address: ")
        print()
        print(OnePerson(address))
    elif option.lower() == 'oneaddress':
        name = input("Enter name: ")
        print()
        print(OneAddress(name))
    elif option.lower() == 'delete':
        name = input("Enter Name to delete: ")
        print()
        print(Delete)
    else:
        print("Not valid command, try again")

        
    Menu()
    
if __name__ == "__main__":
    Dict = CreateDict()
    Menu()