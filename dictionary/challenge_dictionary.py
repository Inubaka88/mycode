#!/usr/bin/env python3

char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n>").capitalize()

char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n>").lower()

marvelchars= {
        "Starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

        "Mystique":
        {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

        "Hulk":
        {"real name": "bruce banner",
        "powers": "temper tantrum",
        "archenemy": "peace"}

        }
print(f"{char_name}'s {char_stat} is: {marvelchars[char_name][char_stat].title()}")
