# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 13:53:36 2021

@author: sonram_sirirat

Python
Task: Win the game
Performance: Win the game in short turn possible
Experience: Game pattern that Python can win the game
"""

# Ask number of sticks in pile
stick = int(input("How many sticks in the pile🍡: "))
print("There are", stick, "sticks in the pile.🍡")

# Ask player's name
# player_name = str(input("What is your name😃: "))

# def PlayerTake():
#     player_take = int(input(" how many stick you will take (1 or 2): "))
#     return player_take

# Stick in the pile
while stick > 0:
    player_take = int(input(" how many stick you will take (1 or 2): "))
    stick = stick - player_take
    print("Player take", player_take, "stick(s)")
    if stick == 0:
        print("No stick left")
    else:
        print(stick, "stick(s) left")
        # Python AI
        if stick
        
        