# This is a comment in Python
# Comments are ignored by the Python interpreter

# ----------Examples of Comments-----------------------
# Informations About File
# License
# Who Created The File
# When The File Created
# Why The File Created
# -----------Like this---------------------------------

# 01 - Write Beside The Programming Line
print("01 - Hello, World!")  # This prints a greeting message

# 02- Write Before The Programming Line
# this line prints a welcome message
print("02 - Welcome to Python programming.")

# 03 - Multi-Line Comments
"""
This is a multi-line comment.
It can span multiple lines.
Useful for detailed explanations or documentation.
"""
print("03 - Multi-line comments are useful!")

# 04 - Using Hash for Multi-Line Comments
# This is another way to write multi-line comments.
# Each line starts with a hash symbol.
# This method is often used for quick notes or explanations.
print("04 - Using hash for multi-line comments.")

# 05 - Commenting Out Code
# The following line is commented out and will not execute.
# print("This line is commented out and won't run.")
print("05 - Commented out code won't execute.")

# 06 - Using Comments for TODOs
todo = "Implement feature X"  # TODO: Implement feature X
print("06 - TODO comments help track tasks.")

# 07 - Using Comments for Documentation
def add(a, b):
    """This function adds two numbers and returns the result."""
    return a + b # Return the sum of a and b
print("07 - Function documentation helps understand code.")
print(add(5, 3))  # Output: 8

# 08 - Using Comments for Debugging
# print("Debugging info: Variable x =", x)  # Uncomment for debugging purposes
print("08 - Comments can assist in debugging.")

# 09 - Using Comments to Explain Complex Logic
# The following code calculates the factorial of a number.
def factorial(n):
    """Calculate the factorial of a number n."""
    if n == 0 or n == 1:
        return 1  # Base case: factorial of 0 or 1 is 1
    else:
        return n * factorial(n - 1)  # Recursive case
print("09 - Factorial of 5 is", factorial(5))  # Output: 120

# 10 - Using Comments for Version Control
# Version 1.0 - Initial release
# Version 1.1 - Bug fixes and improvements
print("10 - Version control comments help track changes.")

# 11 - Using Comments for Code Readability
# This section of code handles user input and validation.
user_input = input("Enter a number: ")
try:
    number = int(user_input)  # Convert input to integer
    print("You entered:", number) # Display the entered number
except ValueError:
    print("Invalid input. Please enter a valid number.")  # Handle invalid input
print("11 - Comments enhance code readability.")

# End of the examples
