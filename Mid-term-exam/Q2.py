# Q2
# Q2: Problem Solving (6 pts)
# Make the shortest Palindrome word from the input text.
# Wiki: What is Palindrome ?

# 1. Get input from user
word = input("Input:")
# print(word)
# 2. Create valriable to contian a palindrome result
pd = ""
# 3. Count length of the word and minus by 1 for loop to create a new word
length = len(word) - 1
# print(length)

# 4. Create the new word last letter come first
for i in range(length, -1, -1): 
    rd = word[i]
    print(rd)
    pd = pd + rd
# 5. Check if new word and the word from start are equal that mean is a palindrome
if pd == word:
    print("Output:",pd)

# 6. If not then create a new palindrome word
else:
    rd = word[:: -1]
    pd = word[:length] + rd
    print("Output", pd)