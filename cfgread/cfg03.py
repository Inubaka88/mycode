#!/usr/bin/env python3
## create file object in "r"ead mode

with open(input("What file do you want to open? "), "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    configlist = [line.strip() for line in configlist]
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print("Number of lines: ", len(configlist))
