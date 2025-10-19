# ---------------------------------
# -- Strings Formatting New Ways --
# ---------------------------------

# starting Course 018 - Strings Formatting in Python (New Ways)
print(f"{'Starting Course 018- Strings Formatting in Python (New Ways)'}")


name = "Osama" # String to test the new way of formatting method in Python
age = 36 # Integer to test the new way of formatting method in Python
rank = 10 # Float to test the new way of formatting method in Python

print("My Name is: " + name) # Concatenation using + operator
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error - You cannot concatenate string and integer directly

print("My Name is: {}".format("Osama")) # Using {} as a placeholder for string
print("My Name is: {}".format(name))  # Using {} as a placeholder for string with variable
print("My Name is: {} My Age: {}".format(name, age)) # Using {} and {} as placeholders for string and integer with variables
print("My Name is: {:s} Age: {:d} & Rank is: {:f}".format(name, age, rank)) # Using {:s}, {:d} and {:f} as placeholders for string, integer and float with variables

# {:s} => String (Also works with numbers)
# {:d} => Number (Integer)
# {:f} => Float (Decimal Number)

n = "Osama" # String to test the new way of formatting method in Python
l = "Python" # String to test the new way of formatting method in Python
y = 10 # Integer to test the new way of formatting method in Python

print("My Name is {} Iam {} Developer With {:d} Years Exp".format(n, l, y)) # Using multiple placeholders with variables

# 01- Control Floating Point Number of Digits After The Decimal Point

myNumber = 10 # Integer to test the new way of formatting method in Python
print("My Number is: {:d}".format(myNumber)) # Using {:d} as a placeholder for integer
print("My Number is: {:f}".format(myNumber)) # Using {:f} as a placeholder for float
print("My Number is: {:.2f}".format(myNumber)) # Using {:.2f} to limit the float to 2 decimal places

# 02- Truncate String to N Characters

myLongString = "Hello Peoples of Elzero Web School I Love You All" # String to test the new way of formatting method in Python
print("Message is {}".format(myLongString)) # Using {} as a placeholder for string
print("Message is {:.5s}".format(myLongString)) # Using {:.5s} to truncate the string to 5 characters
print("Message is {:.13s}".format(myLongString))  # Using {:.13s} to truncate the string to 13 characters

# 03- Format Money with Comma or Underscore as Thousand Separator

myMoney = 500162350198 # Integer to test the new way of formatting method in Python

print("My Money in Bank Is: {:d}".format(myMoney)) # Without Separator
print("My Money in Bank Is: {:_d}".format(myMoney)) # With Underscore as Separator
print("My Money in Bank Is: {:,d}".format(myMoney)) # With Comma as Separator

# 04- ReArrange Items in format() Method

a, b, c = "One", "Two", "Three" # Strings to test the rearranging in format method
print("Hello {} {} {}".format(a, b, c))  # Hello One Two Three
print("Hello {1} {2} {0}".format(a, b, c))  # Hello Two Three One
print("Hello {2} {0} {1}".format(a, b, c))  # Hello Three One Two

x, y, z = 10, 20, 30 # Integers to test the rearranging in format method
print("Hello {} {} {}".format(x, y, z)) # Hello 10 20 30
print("Hello {1:d} {2:d} {0:d}".format(x, y, z)) # Hello 20 30 10
print("Hello {2:f} {0:f} {1:f}".format(x, y, z)) # Hello 30.000000 10.000000 20.000000
print("Hello {2:.2f} {0:.4f} {1:.5f}".format(x, y, z)) # Hello 30.00 10.0000 20.00000

# 05- Format in Version 3.6+ Using f-Strings (Literal String Interpolation)

myName = "Osama" # String to test the f-Strings method in Python
myAge = 36  # Integer to test the f-Strings method in Python

print("My Name is : {myName} and My Age is : {myAge}") # Without f before the string
print(f"My Name is : {myName} and My Age is : {myAge}") # With f before the string



# end of Course 018 - Strings Formatting in Python (New Ways)
print(f"{'End of Course 018- Strings Formatting in Python (New Ways)'}")
# -------------------------------------------------------------------------------------------------------------
# Note: The new ways of formatting strings using the format() method and f-Strings are recommended because they are more flexible and easier to read than the old way of formatting strings using the % operator.
# -------------------------------------------------------------------------------------------------------------
