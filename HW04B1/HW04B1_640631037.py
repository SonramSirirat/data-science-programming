"""
Created on Wed Jul 28 15:30:08 2021

@author: sonram_sirirat
"""

# =============================================================================
# Write a program that accepts a list of four non negative integers,
# arranges them such that they form a largest possible number.
# 
# For example (50,2,1,9) the largest formed number is 95021
# 
# Be carefull if [10,1] the answer is 110 not 101
# =============================================================================

# Get user input
# user_input = list(input("Type here: "))
user_input = [50, 2, 1, 9]
print('List of positive integers:', user_input)

# Find the greater integer in the list
greater_int = max(user_input)
print('Greater number of digits:', greater_int)

# Count digits of greater interger in the list
digits_count = len(str(greater_int))
print('Leght number of greater number:', digits_count)