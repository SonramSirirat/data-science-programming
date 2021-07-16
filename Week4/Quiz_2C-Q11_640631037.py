# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 2021

@author: sonram_sirirat
"""

# Quiz 11: HalfAdder

A, B = input("Enter two digits: ").split()
A = int(A)
B = int(B)
def HalfAdder(A, B):    
    Sum = A or B
    Carry = A and B
    
    print("Sum ", Sum)
    print("Carry", Carry)
    
    return(Sum, Carry)

HalfAdder(A, B)
