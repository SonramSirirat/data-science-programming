# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 2021

author: sonram sirirat
Exercises
"""
# Quiz 10
# Ex.1 Check whether x = 2.3 is a zero of the function:
# f(x) = x ** 2 + 0.25 * x - 5
x = float(input("f(x): "))
def f(x):
    print (0 == x ** 2 + 0.25 * x - 5)

f(x)