"""
Created on Wed Jul 28 15:30:08 2021

@author: sonram_sirirat 640631037
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
user_input = [50, 2, 1, 9]
# user_input = [2, 1, 3, 4, 5, 6, 7, 8, 9, 0]
# user_input = [20, 2]
print('List of positive integers:', user_input)

# Find the largest integer in the list
largest_int = max(user_input)
print('Largest integer:', largest_int)

# Count lenght of largest integer
larg_len_int = len(str(largest_int))
print('Lenght of largest integer:', larg_len_int)

# Create a dictionary contain a integer to compare each others
dict_int = {}
for i in user_input:
    # Count lenght i in user_input list
    length_int = len(str(i))
    
    if length_int == 1:
        dict_int[i] = (i + 1) * 10 ** (larg_len_int - length_int) - 1
    else:
        dict_int[i] = i * 10 ** (larg_len_int - length_int)
print('Dictionary:', dict_int)

# Sort dictionary value and rearrage new integers
sorted_dict_int = sorted(dict_int, key=dict_int.__getitem__, reverse=True)
print('Rearrage integer:', sorted_dict_int)

# Convert dictionary to string
output = ''.join(str(o) for o in sorted_dict_int)
print('The largest formed number is', output)
