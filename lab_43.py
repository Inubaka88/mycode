#!/usr/bin/env python3
number = int(input("How many bottles of beer are on the wall? "))
singular = 1
zero = 0
for num in range(int(number), 0, -1):
    if number <= 100 and number >= 2:
        print(f"{num} bottles of beer on the wall!")
        print(f"{num} bottles of beer on the wall! {num} bottles of beer! You take one down, pass it around!")
    elif number == singular:
        print(f"{num} bottle of beer on the wall!")
        print(f"{num} bottle of beer on the wall! {num} bottle of beer! You wake one down, pass it around!")
    elif number == zero:
        print(f"{num} bottles of beer on the wall!")
        print(f"{num} bottles of beer on the wall! {num} bottles of beer! You got no more {num} bottles of beer")
    elif number >= 101:   
        print("Sorry this wall can only hold 100 bottles of beer\n")
        break


