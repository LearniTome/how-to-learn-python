# 010 - Concatenation And Training

# -------------------
# -- Concatenation  --
# -------------------

# Concatenation (Joining Strings Together) Using + Operator

msg = "I Love" # String
lang = "Python" # String
print(msg + " " + lang) # I Love Python # Concatenation (Joining Strings Together)

full = msg + " " + lang # I Love Python # Concatenation (Joining Strings Together)
print(full) # I Love Python

# Concatenation With Escape Sequences Characters

a = "First \
Second \
Third" # Using \ to continue the line without creating a new line in the output

# a = "First\nSecond\nThird" # Using \n to create a new line in the output

b = "A \
B \
C" # Using \ to continue the line without creating a new line in the output

# b = "A\nB\nC" # Using \n to create a new line in the output

print(a + "\n" + b) # First Second Third \n A B C # Concatenation (Joining Strings Together) With New Line Between a and b

#  print("Hello " + 1)  # Error # TypeError: can only concatenate str (not "int") to str
print("Hello " + str(1))  # Hello 1 # Convert 1 to string for concatenation

print("="*50)
# Concatenation (Joining Strings Together)
a = "Hello" + " " + "World" + " " + "I" + " " + "Love" + " " + "Python" + " " + "Programming"
print(a) # Hello World I Love Python Programming

b = "Hello"
c = "World"
d = b + " " + c
print(d) # Hello World

# Concatenation With Numbers (Need To Convert Numbers To Strings)

age = 25 # Integer
print("My Age Is " + str(age)) # My Age Is 25 # Convert age to string for concatenation
print("My Age Is " + str(age) + " Years") # My Age Is 25 Years # Convert age to string for concatenation

# Training Examples (Concatenation)

print("="*50)

print("Hello" + " " + "Elzero") # Hello Elzero
print("Hello" + " " + "Web") # Hello Web

print("="*50)

print("I Love " + "Programming") # I Love Programming
print("I Love " + "Elzero") # I Love Elzero

print("="*50)

print("I Love " + "Python " + "And " + "Programming") # I Love Python And Programming
print("I Love " + "Python " + "And " + "Elzero") # I Love Python And Elzero


print("="*50)

