#!/usr/bin/env python3

import html

trivia = {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
def main():
    game_night = trivia.get('question')
    correct_choice = trivia.get('correct_answer')
    wrong1 = trivia['incorrect_answers'][0]
    wrong2 = trivia['incorrect_answers'][1]
    wrong3 = trivia['incorrect_answers'][2]
    print(game_night)
    print(f"A: {html.unescape(correct_choice)}")
    print(f"B: {html.unescape(wrong1)}")
    print(f"C: {html.unescape(wrong2)}")
    print(f"D: {html.unescape(wrong3)}")
    print("Make your choice: ")
    user_choice = input().lower()
    correct_choice = 'a'
    if user_choice == correct_choice: 
        print("Correct!")
    else :
        print ("Wrong answer.")
main()
