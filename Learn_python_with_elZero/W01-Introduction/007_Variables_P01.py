# --------------------------------------
# -- Variables --
# ---------------
# Syntax => [Variable Name] [Assignment Operator] [Value]
#
# Name Convention and Rules
# [1] Can Start With (a-z A-Z) Or Underscore
# [2] You Cannot With Num Or Special Characters
# [3] Can Include (0-9) Or Underscore
# [4] Cannot Include Special Characters
# [5] Name is Not Like name [ Case Sensitive ]
# --------------------------------------

name = "Osama Elzero"  # Single Word => Normal
myName = "Osama Elzero"  # Two Words => camelCase
my_name = "Osama Elzero"  # Two Words => snake_case

print(name)
print(myName)
print(my_name)

# Assign The Same Value To Many Variables
a = b = c = 100
print(a)  # 100 => 100
print(b)  # 100 => 100
print(c)  # 100 => 100
print(a, b, c)  # 100 100 100
print(a + b + c)  # 300 => 100 + 100 + 100
print(a * b * c)  # 1000000 => 100 * 100 * 100
print(a / b / c)  # 0.001 => 100 / 100 / 100
print(a - b - c)  # -100 => 100 - 100 - 100
print(a ** 3)  # 1000000 => 100 ** 3
print("="*50)
# Assign Different Values To Many Variables
a, b, c = 10, 20, 30  # a = 10, b = 20, c = 30
print(a)  # 10 => 10
print(b)  # 20 => 20
print(c)  # 30 => 30
print(a, b, c)  # 10 20 30
print(a + b + c)  # 60 => 10 + 20 + 30
print(a * b * c)  # 6000 => 10 * 20 * 30
print(a / b / c)  # 0.016666666666666666 => 10 / 20 / 30
print(a - b - c)  # -40 => 10 - 20 - 30
print(a ** 3)  # 1000 => 10 ** 3
print("="*50)

# You Can Use The Variable Before It Is Created
# print(my_variable)  # NameError: name 'my_variable' is not defined

my_variable = "Hello Python"  # Create The Variable After Use It
print(my_variable)  # Hello Python  => Hello Python
print("="*50)

# You Can Reassign The Variable To Another Value And Type

my_variable = "Hello Python"  # String
print(my_variable)  # Hello Python  => Hello Python
my_variable = 100  # Integer
print(my_variable)  # 100  => 100
my_variable = 100.5  # Float
print(my_variable)  # 100.5  => 100.5
my_variable = [1, 2, 3]  # List
print(my_variable)  # [1, 2, 3]  => [1, 2, 3]
my_variable = (1, 2, 3)  # Tuple
print(my_variable)  # (1, 2, 3)  => (1, 2, 3)
my_variable = {"One": 1, "Two": 2}  # Dictionary
print(my_variable)  # {'One': 1, 'Two': 2}  => {'One': 1, 'Two': 2}
my_variable = {1, 2, 3}  # Set
print(my_variable)  # {1, 2, 3}  => {1, 2, 3}
print("="*50) 
