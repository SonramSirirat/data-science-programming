# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 2021

@author: sonram_sirirat
"""

# Quiz 12: Full Adder

carryIn, A, B = input("Enter three digits: ").split()
carryIn = int(carryIn)
A = int(A)
B = int(B)

def fullAdder(carryIn, A, B):
    Sum = (A or B)
    Sum = carryIn or Sum
    
    carryOut = Sum or (A or B) or (A and B)
    print("Sum = ", Sum)
    print("Carry Out = ", carryOut)

fullAdder(A, B, carryIn)
