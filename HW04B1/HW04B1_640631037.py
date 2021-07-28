"""
Created on Wed Jul 28 15:30:08 2021

@author: sonram_sirirat
"""

# =============================================================================
# Write a program that accepts a list of four non negative integers,
# arranges them such that they form a largest possible number.
# 
# For example (50,2,1,9), the largest formed number is 95021
# 
# Be carefull if [10,1] the answer is 110 not 101 
# =============================================================================

f = [50, 2, 1, 9]

for i in range(f):
    if f[i] > f[0]:
        print(int(f))