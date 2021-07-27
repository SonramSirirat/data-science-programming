# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 13:53:36 2021

@author: sonram_sirirat

Python
Task: Win the game
Performance: Win the game in short turn possible
Experience: Game pattern that Python can win the game
"""
# Import Random
import random as rd

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
    player_take = int(input("How many stick you will take (1 or 2): "))
    stick = stick - player_take
    print("Player take", player_take, "stick", stick, "stick left")
    if stick == 0:
        print("You take the last stick you lose!")
    elif stick == 1:
        stick -= 1
        print("Bot take the last stick bot lose!")
    else:
        # target acquired ready to engage!
        if stick % 3 == 0:
            stick -= 2
            print("Bot take 2 - ", stick, "stick left")
        elif stick < 18:
            stick -= 1
            print("Bot take 1 - ", stick, "stick left")
        else:
            bot_take = rd.randint(1, 2)
            stick -= bot_take
            print("Bot take",bot_take , stick, "stick left")