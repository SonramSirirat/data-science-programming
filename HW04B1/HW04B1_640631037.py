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
# num_list = [50, 2, 1, 9]
# n = str(num_list[0])
# print(type(n))
    
# user_input = [int(x) for x in input('User Input: ').split()]
user_input = [50, 2, 1, 9]
for x in range(len(user_input)):
    # print(user_input[x])
    print(user_input)
    
    
# user_input2 = str(user_input[1])
# user_input3 = str(user_input[2])
# user_input4 = str(user_input[3])
# output = user_input1 + user_input2 + user_input3 + user_input4
# print(output)
# i = 0
# print('Key', 'Value')
# while i < len(user_input):
#     print(i, user_input[i])
#     i += 1
# print(user_input.sort(10))