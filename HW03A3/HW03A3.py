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
losing_position = stick - 1
print("There are", stick, "sticks in the pile.🍡")

# Ask player's name
# player_name = str(input("What is your name😃: "))

# def PlayerTake():
#     player_take = int(input(" how many stick you will take (1 or 2): "))
#     return player_take

# Stick in the pile
while stick > 0:
    player_take = int(input("How many stick you will take (1 or 2): "))
    # stick = stick - player_take
    print("Player take", player_take, "stick(s)")
    if stick == 0:
        print("No stick left")
    else:
        # print(stick, "stick(s) left")
        # If player take 1 stick
        if player_take == 1:
            stick = stick - player_take
            print(stick, "stick(s) left")
            # Python do
            if stick > 0:
                stick = stick - 2
                print("Python take 2 sticks")
                print(stick, "stick(s) left")
        
        # If player take 2 sticks      
        if player_take == 2:
            stick = stick - player_take
            print(stick, "stick(s) left")
            # Python do
            if stick > 0:
                stick = stick - 1
                print("Python take 1 stick")
                print(stick, "stick(s) left")