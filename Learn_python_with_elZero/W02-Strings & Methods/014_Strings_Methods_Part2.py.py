# ---------------------
# -- Strings Methods --
# ---------------------

# Starting Course 014 - Strings Methods in Python
print(f"{'Starting Course 014 - Strings Methods in Python'}")

# 01- split() rsplit()
# => Split The String Into A List Of Substrings Based On A Specified Delimiter
# => Default Delimiter Is Any Whitespace
# => Can Specify A Different Delimiter
# => Can Limit The Number Of Splits Using The Maxsplit Parameter
# => rsplit() Works From The Right Side Of The String
# => split() Works From The Left Side Of The String

a = "I Love Python and PHP and MySQL" # String With Spaces Between Words
print(a.split()) # Default Split By Spaces => ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL'] # Split string into a list of words based on spaces between them

b = "I-Love-Python-and-PHP-and-MySQL" # String With Hyphens Between Words
print(b.split("-")) # Split By Hyphen => ['I', 'Love', 'Python', 'and', 'PHP', 'and', 'MySQL'] # Split string into a list of words based on hyphens between them

c = "I-Love-Python-and-PHP-and-MySQL" # String With Hyphens Between Words # Limit The Number Of Splits To 3 From The Left Side
print(c.split("-", 3)) # ['I', 'Love', 'Python', 'and-PHP-and-MySQL'] # Split string into a list of words based on hyphens between them, but only perform 3 splits from the left side

d = "I-Love-Python-and-PHP-and-MySQL" # String With Hyphens Between Words # Limit The Number Of Splits To 3 From The Right Side
print(d.rsplit("-", 3)) # ['I-Love-Python-and', 'PHP', 'and', 'MySQL'] # Split string into a list of words based on hyphens between them, but only perform 3 splits from the right side

# 02- center() ljust() rjust()
# => Align The String Within A Specified Width By Padding It With A Specified Character (Default Is Space)
# => center() Centers The String
# => ljust() Left Aligns The String
# => rjust() Right Aligns The String
# => If The Specified Width Is Less Than Or Equal To The Length Of The String, The Original String Is Returned Unchanged
# => If The Padding Character Is Not A Single Character, Only The First Character Is Used
# => These Methods Do Not Modify The Original String, They Return A New String

e = "Osama" # String With 5 Characters
print(e.ljust(9))  # Spaces to the right to make the total width 9 characters
print(e.center(9))  # Spaces on both sides to center the text (9 characters wide)
print(e.center(9, "#"))  # Hashes on both sides to center the text (9 characters wide)
print(e.center(15, "@"))  # @ on both sides to center the text in a wider field (15 characters wide)

# 03- count() => Count The Number Of Occurrences Of A Substring In The String
# => Can Specify A Start And End Position To Limit The Search Range
# => This Method Is Case-Sensitive
# => It Returns An Integer Representing The Count Of Occurrences
# => If The Substring Is Not Found, It Returns 0
# => This Method Does Not Modify The Original String

f = "I Love Python and PHP Because PHP is Easy" # String With Multiple PHP Words
print(f.count("PHP"))  # Count All PHP Words => 2 # Count occurrences of "PHP" in the string
print(f.count("PHP", 0, 25)) # Count PHP Words From Position 0 To 25 => 1 # Count occurrences of "PHP" in the string from index 0 to 25

# 04- swapcase()
# => Swap The Case Of Each Character In The String
# => Uppercase Characters Are Converted To Lowercase And Vice Versa
# => Non-Alphabetic Characters Are Left As Is
# => This Method Does Not Modify The Original String, It Returns A New String

g = "I Love Python" # Mixed Case String
h = "i lOVE pYTHON" # Mixed Case String

print(g.swapcase()) # Swap Case => i lOVE pYTHON # Convert uppercase letters to lowercase and vice versa in the string
print(h.swapcase()) # Swap Case => I Love Python # Convert uppercase letters to lowercase and vice versa in the string

# 05- startswith() endswith()
# => Check If The String Starts Or Ends With A Specified Substring
# => Can Specify Start And End Positions To Limit The Check Range
# => Returns True If The String Starts Or Ends With The Specified Substring Within The Given Range, Otherwise Returns False
# => This Method Is Case-Sensitive
# => It Does Not Modify The Original String
# => Note: The End Position Is Not Included In The Check Range (Up To But Not Including The End Index)
# => If Start And End Are Not Specified, The Check Is Performed On The Entire String

i = "I Love Python" # String To Check Start And End Words
print(i.startswith("I")) # True # Check if the string starts with "I"
print(i.startswith("S")) # False # Check if the string starts with "S"
print(i.startswith("P", 7, 12)) # True # Check if the substring from index 7 to 11 starts with "P"

# 06- endswith()
# => Check If The String Ends With A Specified Substring
# => Can Specify Start And End Positions To Limit The Check Range
# => Returns True If The String Ends With The Specified Substring Within The Given Range, Otherwise Returns False
# => This Method Is Case-Sensitive
# => It Does Not Modify The Original String

j = "I Love Python" # String To Check End Words
print(j.endswith("n")) # True # Check if the string ends with "n"
print(j.endswith("S")) # False # Check if the string ends with "S"
print(j.endswith("e", 2, 6)) # True # Check if the substring from index 2 to 5 ends with "e"

# End of File Course 014 - Strings Methods in Python
print(f"{'End Course 014 - Strings Methods in Python'}")

