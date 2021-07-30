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
user_input = [int(x) for x in input('User Input: ').split()]

i = 0
print('Key', 'Value')
while i < len(user_input):
    # 0 < 4, 0 < 3, 0 < 2, 0 < 1
    print(i, user_input[i])
    # if user_input[i] >:
    #     # [0]50 > 
    i += 1