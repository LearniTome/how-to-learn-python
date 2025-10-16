# ------------------------
# -- Strings Formatting --
# ------------------------

# starting Course 017 - Strings Formatting in Python (Old Way)
print(f"{'Starting Course 017- Strings Formatting in Python (Old Way)'}")


name = "Osama" # String to test the old way of formatting method in Python
age = 36 # Integer to test the old way of formatting method in Python
rank = 10 # Float to test the old way of formatting method in Python

# Old Way of Formatting Method in Python (Using % Operator) to format strings
# It is not recommended to use this method because it is not very flexible and hard to read

print("My Name is: " + name) # Concatenation using + operator

# print("My Name is: " + name + " and My Age is: " + age)  # Type Error - You cannot concatenate string and integer directly

print("My Name is: %s" % "Osama") # Using %s as a placeholder for string
print("My Name is: %s" % name) # Using %s as a placeholder for string with variable
print("My Name is: %s and My Age is: %d" % (name, age)) # Using %s and %d as placeholders for string and integer with variables
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, rank)) # Using %s, %d and %f as placeholders for string, integer and float with variables

# %s => String (Also works with numbers)
# %d => Number (Integer)
# %f => Float (Decimal Number)

n = "Osama" # String to test the old way of formatting method in Python
l = "Python" # String to test the old way of formatting method in Python
y = 10 # Integer to test the old way of formatting method in Python

print("My Name is %s Iam %s Developer With %d Years Exp" % (n, l, y)) # Using multiple placeholders with variables

# Control Floating Point Number of Digits After The Decimal Point with %.Nf where N is the number of digits after the decimal point

myNumber = 10 # Integer to test the old way of formatting method in Python
print("My Number is: %d" % myNumber) # Using %d as a placeholder for integer
print("My Number is: %f" % myNumber) # Using %f as a placeholder for float
print("My Number is: %.2f" % myNumber) # Using %.2f to limit the float to 2 decimal places

# Truncate String to N Characters with %.Ns where N is the number of characters to keep

myLongString = "Hello Peoples of Elzero Web School I Love You All" # String to test the old way of formatting method in Python
print("Message is %s" % myLongString) # Using %s as a placeholder for string
print("Message is %.5s" % myLongString) # Using %.5s to truncate the string to 5 characters

print(f"{'End of Course 017- Strings Formatting in Python (Old Way)'}")

# End Course 017 - Strings Formatting in Python (Old Way)
# -------------------------------------------------------------------------------------------------------------
# Note: The old way of formatting strings is not recommended, it is better to use the new way of formatting strings using f-strings or the format() method which will be covered in the next courses.
# -------------------------------------------------------------------------------------------------------------
