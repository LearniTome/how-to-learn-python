# ---------------------
# -- Strings Methods --
# ---------------------

# starting Course 015 - Strings Methods in Python
print(f"{'Starting Course 015 - Strings Methods in Python'}")

# 01- index(SubString, Start, End)

# => Return The Lowest Index Of The Substring If Found In The String
# => Raises A ValueError If The Substring Is Not Found
# => Optional Parameters Start And End To Limit The Search Within A Specific Range
# => This Method Is Case-Sensitive
# => Note: The End Position Is Not Included In The Search Range (Up To But Not Including The End Index)
# => If Start And End Are Not Specified, The Search Is Performed On The Entire String

a = "I Love Python" # String With 13 Characters # Index 0 To 12 => Total 13 Character
print(a.index("P"))  # Index Number 7
print(a.index("P", 0, 10)) # Index Number 7
print(a.index("P", 0, 5))  # Through Error ValueError: substring not found

# 02- find(SubString, Start, End)

# => Similar To index() Method But Instead Of Raising An Error If The Substring Is Not Found, It Returns -1
# => Return The Lowest Index Of The Substring If Found In The String
# => Returns -1 If The Substring Is Not Found
# => Optional Parameters Start And End To Limit The Search Within A Specific Range
# => This Method Is Case-Sensitive
# => Note: The End Position Is Not Included In The Search Range (Up To But Not Including The End Index)
# => If Start And End Are Not Specified, The Search Is Performed On The Entire String

b = "I Love Python" # String With 13 Characters # Index 0 To 12 => Total 13 Character
print(b.find("P"))  # Index Number 7
print(b.find("P", 0, 10))  # Index Number 7
print(b.find("P", 0, 5))  # -1

# 03- rjust(Width, Fill Char) ljust(Width, Fill Char)

# => Right Justify Or Left Justify The String Within The Specified Width
# => Fill Char Is Optional (Default Is Space Character)
# => If The Specified Width Is Less Than Or Equal To The Length Of The String, The Original String Is Returned Unchanged
# => If The Fill Character Is Not A Single Character, Only The First Character Is Used
# => These Methods Do Not Modify The Original String, They Return A New String


c = "Osama" # String With 5 Characters
print(c.rjust(10)) # Spaces to the left to make the total width 10 characters
print(c.rjust(10, "#")) # Hashes to the left to make the total width 10 characters

d = "Osama" # String With 5 Characters
print(d.ljust(10)) # Spaces to the right to make the total width 10 characters
print(d.ljust(10, "#")) # Hashes to the right to make the total width 10 characters

# 04- splitlines() => Split The String At Line Breaks And Return A List Of Lines

# => Line Breaks Are Not Included In The Resulting List
# => Can Handle Different Types Of Line Breaks (\n, \r, \r\n)
# => If There Are No Line Breaks In The String, The Resulting List Contains The
# => Original String As The Only Element
# => This Method Does Not Modify The Original String It Returns A New List Of Lines

e = """First Line
Second Line
Third Line""" # Multi-line String

print(e.splitlines()) # Split the string at line breaks and return a list of lines

f = "First Line\nSecond Line\nThird Line" # Multi-line String With \n Line Breaks

print(f.splitlines()) # Split the string at line breaks and return a list of lines

# 05- expandtabs() istitle() isspace() islower() isidentifier() isalpha() isalnum()
# => expandtabs(Tab Size) => Replace Tab Characters (\t) In The String With Spaces, Based On The Specified Tab Size (Default Is 8)
# => istitle() => Check If The String Is In Title Case (First Letter Of Each Word Is Uppercase, All Other Letters Are Lowercase)
# => isspace() => Check If The String Contains Only Whitespace Characters (Spaces, Tabs, Newlines) And Is Not Empty
# => islower() => Check If All Alphabetic Characters In The String Are Lowercase And There Is At Least One Alphabetic Character
# => isidentifier() => Check If The String Is A Valid Python Identifier (Starts With A Letter Or Underscore, Followed By Letters, Digits, Or Underscores)
# => isalpha() => Check If All Characters In The String Are Alphabetic (Letters) And There Is At Least One Character
# => isalnum() => Check If All Characters In The String Are Alphanumeric (Letters And Digits) And There Is At Least One Character

# 05-01 expandtabs(Tab Size) => Replace Tab Characters (\t) In The String With Spaces, Based On The Specified Tab Size (Default Is 8)
# => Default Tab Size Is 8 Spaces Per Tab Character
# => If A Tab Character Is Encountered, It Is Replaced With Enough Spaces To Move The Cursor To The Next Tab Stop
# => Tab Stops Are Typically Set At Every 8th Character Position (0, 8, 16, 24, ...)
# => This Method Does Not Modify The Original String, It Returns A New String With Tabs Expanded

g = "Hello\tWorld\tI\tLove\tPython" # String With Tab Characters (\t)
print(g.expandtabs(2)) # Replace tabs with 2 spaces per tab character # Expand tabs to spaces with a tab size of 2 spaces

# 05-02 istitle() => Check If The String Is In Title Case (First Letter Of Each Word Is Uppercase, All Other Letters Are Lowercase)
# => Words Are Separated By Spaces Or Non-Letter Characters

one = "I Love Python And 3G" # Title Case String # Title Case String (First Letter Of Each Word Is Uppercase, All Other Letters Are Lowercase)
two = "I Love Python And 3g" # Not A Title Case String (3g Is Not Title Case) # Not A Title Case String (3g Is Not Title Case)
print(one.istitle()) # True # Check if the string is in title case # (first letter of each word is uppercase, all other letters are lowercase)
print(two.istitle()) # False # Check if the string is in title case # (first letter of each word is uppercase, all other letters are lowercase)

# 05-03 isspace() => Check If The String Contains Only Whitespace Characters (Spaces, Tabs, Newlines) And Is Not Empty
# => Returns True If The String Contains Only Whitespace Characters And Is Not Empty
# => Returns False If The String Contains Any Non-Whitespace Characters Or Is Empty

three = " " # String With Only Space Character # String With Only Space Character # String With Only Space Character # String With Only Space Character
four = "" # Empty String # Empty String # Empty String # Empty String
print(three.isspace()) # True # Check if the string contains only whitespace characters (spaces, tabs, newlines) and is not empty # (returns True if the string contains only whitespace characters and is not empty)
print(four.isspace())  # False # Check if the string contains only whitespace characters (spaces, tabs, newlines) and is not empty # (returns True if the string contains only whitespace characters and is not empty)

# 05-04 islower() => Check If All Alphabetic Characters In The String Are Lowercase And There Is At Least One Alphabetic Character
# => Returns True If All Alphabetic Characters In The String Are Lowercase And There Is At Least One Alphabetic Character
# => Returns False If The String Contains Any Uppercase Alphabetic Characters Or Does Not Contain Any Alphabetic Characters

five = 'i love python' # All Lowercase String # All Lowercase String # All Lowercase String # All Lowercase String # All Lowercase String # All Lowercase String
six = 'I Love Python' # Not All Lowercase String # Not All Lowercase String # Not All Lowercase String # Not All Lowercase String # Not All Lowercase String
print(five.islower()) # True # Check if all alphabetic characters in the string are lowercase and there is at least one alphabetic character # (returns True if all alphabetic characters in the string are lowercase and there is at least one alphabetic character)
print(six.islower()) # False # Check if all alphabetic characters in the string are lowercase and there is at least one alphabetic character # (returns True if all alphabetic characters in the string are lowercase and there is at least one alphabetic character)

# 05-05 isidentifier() => Check If The String Is A Valid Python Identifier (Starts With A Letter Or Underscore, Followed By Letters, Digits, Or Underscores)
# => A Valid Identifier Cannot Be A Reserved Keyword In Python (e.g., if, else, while, for, etc.)
# => Returns True If The String Is A Valid Identifier, Otherwise Returns False
# => This Method Is Useful For Validating Variable Names, Function Names, And Other Identifiers
seven = "osama_elzero" # Valid Python Identifier
eight = "OsamaElzero100" # Valid Python Identifier
nine = "Osama--Elzero100" # Not A Valid Python Identifier (Contains Invalid Characters)

print(seven.isidentifier()) # True # Check if the string is a valid Python identifier # (starts with a letter or underscore, followed by letters, digits, or underscores)
print(eight.isidentifier()) # True # Check if the string is a valid Python identifier # (starts with a letter or underscore, followed by letters, digits, or underscores)
print(nine.isidentifier())  # False # Check if the string is a valid Python identifier # (starts with a letter or underscore, followed by letters, digits, or underscores)

# 05-06 isalpha() => Check If All Characters In The String Are Alphabetic (Letters) And There Is At Least One Character
# => Returns True If All Characters In The String Are Alphabetic And There Is At Least One Character
# => Returns False If The String Contains Any Non-Alphabetic Characters (Digits, Spaces, Punctuation) Or Is Empty
# => This Method Is Case-Sensitive, So It Considers Both Uppercase And Lowercase Letters As Alphabetic Characters

x = "AaaaaBbbbbb" # String With Only Alphabetic Characters
y = "AaaaaBbbbbb111" # String With Alphabetic And Numeric Characters
print(x.isalpha()) # True # Check if all characters in the string are alphabetic (letters) and there is at least one character
print(y.isalpha())  # False # Check if all characters in the string are alphabetic (letters) and there is at least one character

# 05-07 isalnum() => Check If All Characters In The String Are Alphanumeric (Letters And Digits) And There Is At Least One Character
# => Returns True If All Characters In The String Are Alphanumeric And There Is At Least One Character
# => Returns False If The String Contains Any Non-Alphanumeric Characters (Spaces, Punctuation) Or Is Empty
# => This Method Is Case-Sensitive, So It Considers Both Uppercase And Lowercase Letters As Alphanumeric Characters

u = "AaaaaBbbbbb" # String With Only Alphabetic Characters
z = "AaaaaBbbbbb111"  # String With Alphabetic And Numeric Characters
print(u.isalnum()) # True # Check if all characters in the string are alphanumeric (letters and digits) and there is at least one character
print(z.isalnum())  # True # Check if all characters in the string are alphanumeric (letters and digits) and there is at least one character

# End of File Course 015 - Strings Methods in Python
print(f"{'End Course 015 - Strings Methods in Python'}")
