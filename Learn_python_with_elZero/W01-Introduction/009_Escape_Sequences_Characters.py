
# ----------------------------
# Escape Sequences Characters In Python
# ----------------------------
# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed (New Line)
# \r => Carriage Return (Reset To Beginning Of The Line)
# \t => Horizontal Tab (Indentation)
# \xhh => Character Hex Value (hh is Hexadecimal Value)
# ----------------------------

print("="*50)

# Back Space (\b)
print("Hello\bWorld")  # Will Remove o Before b (Back Space Effect)
print("HelloWorld")    # Normal Print Without Back Space  Effect

# Escape New Line + Back Slash (\newline + \) (Used To Split Long Lines)
print("Hello \
I Love \
Python")

# Escape Back Slash (\\)
print("I Love Back Slash \\")

# Escape Single Quote (\')
print('I Love Single Quote \'Test\' ')

# Escape Double Quotes (\")
print("I Love Double Quotes \"Test\" ")

# Line Feed (New Line) (\n)
print("Hello World\nSecond Line")

# Carriage Return (\r)  # Reset To Beginning Of The Line
print("123456\rABCDE")  # Will Replace 12345 With ABCDE
print("123456\rAbcde") # Will Replace 12345 With Abcde

# Horizontal Tab (\t)  # Indentation (4 Spaces)
print("Hello\tPython") # Will Add Tab Space Between Hello And Python (4 Spaces)
print("Hello    Python") # Normal Print Without Tab Space (4 Spaces)

# Character Hex Value (\xhh)  # hh is Hexadecimal Value
print("\x48\x65\x6C\x6C\x6F")  # Hello in Hexadecimal
print("\x48\x65\x6C\x6C\x6F World")  # Hello World in Hexadecimal
print("\x4F\x73") # Os in Hexadecimal

print("="*50)

# Escape Sequences Characters

# \n New Line
print("Hello\nWorld") # \W is not a valid escape sequence, so it will be treated as a normal character
print("Hello")
print("World")
print("="*50)

# \t Tab
print("Hello\tWorld") # \W is not a valid escape sequence, so it will be treated as a normal character
print("Hello    World")
print("="*50)

# \\ Backslash
print("Hello\\World")
print("Hello \\World") # \W is not a valid escape sequence, so it will be treated as a normal character

print("="*50)

# \' Single Quote
print('Hello\'World') # Use \' to include a single quote in a single-quoted string
print('Hello' + "'" + 'World') # Alternative way to include a single quote
print("Hello'World") # Use double quotes to include a single quote without escaping
print('Hello\'World') # Use \' to include a single quote in a single-quoted string
print("Hello\'World") # Use \' to include a single quote in a double-quoted string
print("Hello'World") # Use double quotes to include a single quote without escaping
print('Hello\'World') # Use \' to include a single quote in a single-quoted string
print("="*50)
