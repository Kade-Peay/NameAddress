#!/bin/env python3

import sys, re

"""User specifies a file name and a person name,
the program then finds the address of the person named"""


# Displays all names and addresses in the file
def All():
    f = open('doc/AddressBook.txt', "r")
    for line in f:
        print(line, end='')
    f.close

# Adds name and address to file
def Add(N, A):
    f = open('doc/AddressBook.txt', 'a')
    f.write('\n')
    f.write(N + ": " + A)
    f.close
    print("Wrote to 'AddressBook.txt'")

# Returns the address of one person
def OnePerson():
    Dict = {}
    f = open('doc/AddressBook.txt', 'r')
    for line in f:
        re.split(r'[,:]', line)
        if line not in Dict:
            dict[line] = name
    f.close

def CreateDict():
    Dict = {}
    f = open('doc/AddressBook.txt', 'r')
    for line in f:
        re.split(r'[,:]', line)
        if line not in Dict:
            dict[line] = line
    f.close

# Returns the name of one address
def OneAddress():
    pass

# Deletes one person and their address
def Delete():
    pass

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Choose one: All, Add, OnePerson, OneAddress, Delete")
    else:
        if sys.argv[1].lower() == 'all':
            print()
            All()
        elif sys.argv[1].lower() == 'add':
            name = input("Enter name: ") 
            address = input("Enter address: ")
            print()
            Add(name, address)
        elif sys.argv[1].lower() == 'dict':
            CreateDict()