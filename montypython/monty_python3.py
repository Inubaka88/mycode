#!/usr/bin/python3

round = 0
answer = " "

while round < 3 and answer != "Brian":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ').capitalize()
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    elif answer == "Shrubbery":
        print("You gave the super secret answer!")
        break
    else:                 # if answer was wrong
        print("Sorry. Try again!")
