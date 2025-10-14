# 011 Strings (Sequence of Characters)
print("="*80)
# -------------
# -- Strings --
# -------------
# Strings in Python are sequences of characters used to store and manipulate text data.
myStringOne = 'This is Single Quote' # String
myStringTwo = "This is Double Quotes" # String

print(myStringOne)
print(myStringTwo)

# Strings can be defined using single quotes (' ') or double quotes (" ").
myStringThree = 'This is Single Quote "Test"' # String
myStringFour = "This is Double Quotes 'Test'" # String

print(myStringThree)
print(myStringFour)

# For multi-line strings, you can use triple quotes (''' ''' or """ """).
myStringFive = '''First
Second 'Test' "Test"
Third'''

# Using triple single quotes for multi-line string with both single and double quotes inside
myStringSix = """First
Second "Test" \\\'Test'
Third"""

print(myStringFive)
print(myStringSix)

print("="*80)

print("="*50)
# Strings are used to store text data in Python.
# They are enclosed in either single quotes (' ') or double quotes (" ").

single_quoted_string = 'Hello, World!'
double_quoted_string = "Hello, World!"
multiline_string = """This is a multiline string.
It can span multiple lines."""
raw_string = r"C:\Users\Name"  # Raw string to ignore escape sequences
formatted_string = f"Hello, {'World'}!"  # Formatted string (f-string)
print(single_quoted_string)  # Output: Hello, World!
print(double_quoted_string)  # Output: Hello, World!
print(multiline_string)  # Output: This is a multiline string. It can span multiple lines.
print(raw_string)  # Output: C:\Users\Name
print(formatted_string)  # Output: Hello, World!
print("="*50)

# String Operations
# Concatenation
greeting = "Hello" # String
name = "Alice" # String
full_greeting = greeting + ", " + name + "!" # Concatenation
print(full_greeting)  # Output: Hello, Alice!

# Repetition
laugh = "Ha" * 3 # Repetition
print(laugh)  # Output: HaHaHa
print("="*50)

# String Indexing and Slicing
sample_string = "Hello, World!"
print(sample_string[0])  # Output: H (First character)
print(sample_string[-1])  # Output: ! (Last character)
print(sample_string[0:5])  # Output: Hello (Substring from index 0 to 4)
print(sample_string[7:])  # Output: World! (Substring from index 7 to end)
print(sample_string[:5])  # Output: Hello (Substring from start to index 4)
print(sample_string[::2])  # Output: Hlo ol! (Every second character)
print("="*50)

# String Methods
text = "  Hello, World!  "  # String with leading and trailing spaces
print(text.lower())  # Output: "  hello, world!  " (Convert to lowercase)
print(text.upper())  # Output: "  HELLO, WORLD!  " (Convert to uppercase)
print(text.strip())  # Output: "Hello, World!" (Remove leading and trailing spaces)
print(text.replace("World", "Python"))  # Output: "  Hello, Python!  " (Replace substring)
print(text.split(","))  # Output: ['  Hello', ' World!  '] (Split string into a list)
print("World" in text)  # Output: True (Check if substring exists)
print(text.find("World"))  # Output: 8 (Find index of substring)
print(text.count("o"))  # Output: 2 (Count occurrences of substring)
print("="*50)

# String Formatting
name = "Alice"  # String
age = 30  # Integer
formatted = "My name is {} and I am {} years old.".format(name, age)  # Using format() method
print(formatted)  # Output: My name is Alice and I am 30 years old.
formatted_fstring = f"My name is {name} and I am {age} years old."  # Using f-string
print(formatted_fstring)  # Output: My name is Alice and I am 30 years old.
print("="*50)

# Escape Sequences in Strings
print("Hello\nWorld")  # New line (\n)
print("Hello\tWorld")  # Tab (\t)
print("He said, \"Hello!\"")  # Double quote (\")
print('It\'s a beautiful day!')  # Single quote (\')
print("C:\\Users\\Name")  # Backslash (\\)
print("="*50)

# String Immutability
immutable_string = "Hello"  # Strings are immutable
# immutable_string[0] = 'h'  # This will raise an error
new_string = 'h' + immutable_string[1:]  # Create a new string instead
print(new_string)  # Output: hello
print(immutable_string)  # Output: Hello  # Original string remains unchanged
print("="*50)

# String Membership Testing
sample_text = "The quick brown fox" # String
print("quick" in sample_text)  # Output: True (Substring exists)
print("slow" not in sample_text)  # Output: True (Substring does not exist)
print("="*50)

# String Length
length = len(sample_text)  # Get length of string
print(f"Length of sample_text: {length}")  # Output: Length of sample_text: 19
print("="*50)

# String Iteration
for char in "Python":  # Iterate over each character in the string "Python"
    print(char) # Output: P y t h o n (each character on a new line)
print("="*50)
# Mini Quiz
print("Mini Strings Quiz")
print("="*50)
print("Hello" + " " + "Elzero") # Hello Elzero
print("Hello" + " " + "Web") # Hello Web
print("I Love " + "Programming") # I Love Programming
print("I Love " + "Elzero") # I Love Elzero
print("="*50)

print("Hello\nWorld") # New line
print("Hello\tWorld") # Tab
print("He said, \"Hello!\"") # Double quote
print('It\'s a beautiful day!') # Single quote
print("C:\\Users\\Name") # Backslash

print("="*50)
print("My name is {} and I am {} years old.".format("Alice", 30)) # Using format() method
print(f"My name is {'Alice'} and I am {30} years old.") # Using f-string
print("="*50)

