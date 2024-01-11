#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    print(pokeapi["sprites"]["front_default"])
    games= 0
    for x in pokeapi["moves"]:
        print(x["move"]["name"])
    for x in pokeapi["game_indices"]:
        games+= 1
        print(x["version"]["name"])
        print(f"This one has shown up in {games} games!")

main()

