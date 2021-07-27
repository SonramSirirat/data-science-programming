# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 13:53:36 2021

@author: sonram_sirirat

"""
# Import Random
import random as rd

# Ask number of sticks in pile
stick = int(input("How many sticks in the pile🍡: "))
print("There are", stick, "sticks in the pile.🍡")

# Ask player's name
player_name = str(input("What is your name😃: "))

# While the stick is greater than zero
while stick > 0:
    
    # Ask player to take the stick
    player_take = int(input(player_name +", How many stick you will take (1 or 2): "))
    
    # Rules
    if player_take <= 0:
        print(player_name,", No you cannot take less than 1 stick❗")
    elif player_take >= 3:
        print(player_name,", No you cannot take more than 2 sticks❗")
    elif stick < player_take:
        print(player_name,", There are no enough sticks to take❗")
    
    # If correctly
    else:
        stick = stick - player_take
        if stick == 0:
            print(player_name,"takes the last stick😥 Python Win!!!🎊")
        elif stick == 1:
            stick -= 1
            print("Python take the last stick😥", player_name, "Win!!!🎊")
        else:
            print("There are", stick, "sticks in the pile.🍡")
            if stick % 3 == 0:
                stick -= 2
                print("Python take 2 sticks, There are", stick, "sticks in the pile.🍡")
            elif stick < 18:
                stick -= 1
                print("Python take 1 stick, There are", stick, "sticks in the pile.🍡")
            else:
                bot_take = rd.randint(1, 2)
                stick -= bot_take
                print("Python take", bot_take, "sticks, There are", stick, "sticks in the pile.🍡")