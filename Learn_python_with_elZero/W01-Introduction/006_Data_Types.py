# ----------------------------
# type()
# All Data in Python is Object
# ----------------------------

print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

print(type([1, 2, 3, 4, 5]))  # list => List

print(type((1, 2, 3, 4, 5)))  # tuple => Tuple

print(type({"One": 1, "Two": 2, "Three": 3}))  # dict => Dictionary

print(type(2 == 2))  # bool => Boolean

# -----------------------------
# -- 01- Python Data Types ---
# -----------------------------

# All data types in Python are classes and all variables are instances (objects) of these classes.

# Examples of Data Types in Python

print(type(10))          # integer

print(type(3.14))       # float

print(type(1 + 2j))     # complex

print(type("Hello"))    # string

print(type(True))     # boolean

print(type(False))    # boolean

print(type([1, 2, 3]))  # list

print(type((1, 2, 3)))  # tuple

print(type({1, 2, 3}))  # set

print(type({"name": "Alice", "age": 30}))  # dictionary

print(type(None))       # NoneType

print(type(range(5)))  # range

print(type(b"Hello"))   # bytes

print(type(bytearray(5)))  # bytearray

print(type(memoryview(b"Hello")))  # memoryview


print("="*50)
print(" Welcome to Python Data Types Tutorial ")
print("="*50)

# [1] Numbers (Integer, Float, Complex)
print("\n01- Number Data Types:")
my_integer = 42
my_float = 3.14
my_complex = 1 + 2j

print(f"Integer Example: {my_integer} - Type: {type(my_integer)}")
print(f"Float Example: {my_float} - Type: {type(my_float)}")
print(f"Complex Example: {my_complex} - Type: {type(my_complex)}")

# [2] Strings
print("\n02- String Data Type:")
my_string = "Hello Python!"
my_multiline = """This is
a multiline
string"""

print(f"String Example: {my_string} - Type: {type(my_string)}")
print(f"Multiline Example:\n{my_multiline}")

# Mini Quiz
print("\n"+"="*20)
print("Mini Data Types Quiz")
print("="*20)

# Quiz Questions
quiz_value1 = 10.5
quiz_value2 = "42"
quiz_value3 = True

print("\nGuess the data types:")
print(f"1- What's the type of {quiz_value1}?")
print(f"2- What's the type of {quiz_value2}?")
print(f"3- What's the type of {quiz_value3}?")

# Quiz Answers (using bilt-in Function : type())
print("\nAnswers using bilt-in Function : type() :")
print(f"1- {type(quiz_value1)}")
print(f"2- {type(quiz_value2)}")
print(f"3- {type(quiz_value3)}")


