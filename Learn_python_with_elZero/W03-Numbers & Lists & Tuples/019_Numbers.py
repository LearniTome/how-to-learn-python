# -------------
# -- Numbers --
# -------------

# starting Course 019 - Numbers in Python
print(f"{'Starting Course 019- Numbers in Python'}")

# There are three types of numbers in Python: Integer, Float, and Complex


# 01- Integer = Whole Numbers (Positive or Negative) without a Decimal Point

print(type(1)) # Positive Integer
print(type(100)) # Positive Integer
print(type(10)) # Positive Integer
print(type(-10)) # Negative Integer
print(type(-110)) # Negative Integer
print(type(0)) # Zero Integer

# 02- Float = Numbers (Positive or Negative) with a Decimal Point or in Exponential (E) Notation

print(type(1.500)) # Positive Float
print(type(100.99)) # Positive Float
print(type(-10.99)) # Negative Float
print(type(0.99)) # Positive Float
print(type(-0.99)) # Negative Float
print(type(10e5)) # Positive Float in Exponential Notation (10 * 10^5)
print(type(-10E5)) # Negative Float in Exponential Notation (-10 * 10^5)

# 03- Complex = Numbers with a Real and Imaginary Part

myComplexNumber = 5+6j # Complex Number

print(type(myComplexNumber)) # Complex Number Type

print("Real Part Is: {}".format(myComplexNumber.real)) # Accessing the Real Part of the Complex Number
print("Imaginary Part Is: {}".format(myComplexNumber.imag)) # Accessing the Imaginary Part of the Complex Number

# [1] You Can Convert From Int To Float or Complex
# [2] You Can Convert From Float To Int or Complex
# [3] You Cannot Convert Complex To Any Type (Will Raise Error) Directly

# Examples of Conversions

# Convert Int to Float or Complex

print(100) # Integer
print(float(100)) # Convert Integer to Float
print(complex(100)) # Convert Integer to Complex

# Convert Float to Int or Complex

print(10.50) # Float
print(int(10.50)) # Convert Float to Integer
print(complex(10.50)) # Convert Float to Complex

# Convert Complex to Other Types (Will Raise Error)

print(10+9j) # Complex
# print(int(10+9j))  # Error - Cannot Convert Complex to Int
# print(float(10+9j))  # Error - Cannot Convert Complex to Float

print(f"{'End of Course 019- Numbers in Python'}")
# End Course 019 - Numbers in Python
# -------------------------------------------------------------------------------------------------------------
# Note: In Python, numbers are immutable data types, meaning their values cannot be changed after they are created. Any operation that modifies a number will create a new number object.
# -------------------------------------------------------------------------------------------------------------
# End of File
# -------------------------------------------------------------------------------------------------------------
