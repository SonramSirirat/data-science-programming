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

losing_position = stick - 1
print("Losing position is", losing_position)
# Stick in the pile
while stick > 0:
    # 7 > 0
    player_take = int(input("How many stick you will take (1 or 2): "))
    # 2
    stick = stick - player_take
    # 5 = 7 - 2
    print("Player take", player_take, "stick(s)")
    if stick == 0:
        print("No stick left")
    else:
        print(stick, "stick(s) left")
        # target acquired ready to engage!
        if stick == losing_position:        
            if stick == 2:
                stick = stick - 1
                print("Python take 1 stick")
                print(stick, "stick(s) left")
            else:
                stick = losing_position - 2
                print("Python take 2 sticks")
                print(stick, "stick(s) left")
        elif stick != losing_position:
            # 5 != 6
            if stick == 2:
                stick = stick - 1
                print("Python take 1 stick")
                print(stick, "stick(s) left")
            elif stick == 1:
                stick = stick - 1
                print("Python take the last stick you win!")
            elif stick < losing_position:
                # 5 < 6
                stick = stick - 1
                # 4 = 5 - 1
                print("Python take 1 stick")
                print(stick, "stick(s) left")