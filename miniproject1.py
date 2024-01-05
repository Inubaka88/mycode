#!/usr/bin/env python3

def main():
    correct_answers = 0
    incorrect_answers = 0
    systems = {
            "mario":
                {"1": "Who helps you at the end of each castle.",
                 "2": "Who is mario\'s main form of transportation",
                 "3": "Who is the main antagonist of the Mario series"},
            "street fighter":
                {"1": "Who do you fight in the bonus round",
                 "2": "What day did M. Bison destroy a village",
                 "3": "Who taught Ryu how to fight"},
            "pokemon":
                {"1": "How old do you have to be to begin your pokemon journey",
                 "2": "How many gym bades do you need to fight the elite four",
                 "3": "Which Trainer is waiting for you on top of Mt. Silver"}
                }
            
    while correct_answers <= 5 or incorrect_answers > 5:
        game = input("Please choose one game: Mario, Street fighter, Pokemon\n>").lower()
        if right_answer == correct_answers:
            print("Correct!")
            correct_answers += 1
        else :
            print("Sorry you got that answer wrong")
            incorrect_answers += 1
main()
