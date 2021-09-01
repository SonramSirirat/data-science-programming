# Q1
# Write the Python code for that it will
# 1) accept the size of the matrix m and n, when m represents row and n 
# represents column of the matrix
import numpy as np
R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))  

print("Enter the entries in a single line (separated by space): ")

entries = list(map(int, input().split()))
  
# For printing the matrix
matrix = np.array(entries).reshape(R, C)
print(matrix)

# 2) Writing the Python code to generate the Matrix m x n.
