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

# Create number dict to compare
num_dict = {
    'zero'  : 0,
    'one'   : 1,
    'two'   : 2,
    'three' : 3,
    'four'  : 4,
    'five'  : 5,
    'six'   : 6,
    'seven' : 7,
    'eight' : 8,
    'nine'  : 9
    }

# Get user input
# user_input = list(input("Type here: "))
user_input = list(str(19))
print('Input:', user_input)

# Convert user input to list
# user_input = list(user_input)

# # Convert to integer
# for i in range(0, len(user_input)):
#     # i = 9, 0 to 2
#     user_input[i] = int(user_input[i])
#     # str(9) = int(9)
#     if user_input[i] == 9:
#         # int(9) == 9
#         print(user_input[i])
#         for n in range(len(user_input)):
#             result = user_input[i]
#     else:
#         print(result)
print('len:', len(user_input))
i = 0
while i < len(user_input):
    if user_input[i] == 1:
        print(user_input[i])
    else:
        print(user_input[i])
    i += 1