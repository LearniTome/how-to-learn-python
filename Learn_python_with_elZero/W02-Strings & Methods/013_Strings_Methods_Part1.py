# ---------------------
# -- Strings Methods --
# ---------------------

print(f"{'Starting Course 013 - Strings Methods in Python'}")

# 01- strip() rstrip() lstrip() => Remove Spaces Or Specific Characters From The Start Or The End Of The String => Default Is Space Character => Can Be Specific Character

a = "    I Love Python    " # String With Leading And Trailing Spaces
print(a.strip()) # Remove Leading And Trailing Spaces
print(a.rstrip()) # Remove Trailing Spaces
print(a.lstrip()) # Remove Leading Spaces

a = "#####I Love Python####" # String With Leading And Trailing #
print(a.strip("#")) # Remove Leading And Trailing #
print(a.rstrip("#")) # Remove Trailing #
print(a.lstrip("#")) # Remove Leading #

a = "@#@#@#I Love Python@#@#@#" # String With Leading And Trailing @#@ # Characters
print(a.strip("@#")) # Remove Leading And Trailing @#@ # Characters
print(a.rstrip("@#")) # Remove Trailing @#@ # Characters
print(a.lstrip("@#")) # Remove Leading @#@ # Characters

# 02- title() => Convert The First Character Of Each Word To Uppercase If The First Character Is A Letter => Other Characters Are Left As Is => Words Are Separated By Spaces Or Non-Letter Characters

b = "I Love 2d Graphics and 3g Technology and python" # String With Leading And Trailing Spaces
print(b.title()) # output: "I Love 2D Graphics And 3G Technology And Python"

# 03- capitalize() => Convert The First Character Of The String To Uppercase If The First Character Is A Letter => Other Characters Are Converted To Lowercase => Leading Spaces Are Ignored

b = "I Love 2d Graphics and 3g Technology and python" # String With Leading And Trailing Spaces
print(b.capitalize()) # output: "I love 2d graphics and 3g technology and python"

# 04- zfill => Fill The String With Leading Zeros (0) Until It Reaches The Specified Width => If The String Is Already At Or Exceeds The Specified Width, It Is Returned Unchanged => If The String Starts With A Sign (+ or -), The Zeros Are Inserted After The Sign

c, d, e, f = "1", "11", "111", "1111" # Strings With Different Lengths

print(c) # output: "1"
print(d) # output: "11"
print(e) # output: "111"
print(f) # output: "1111"

print(c.zfill(4)) # output: "0001" # Fill With Leading Zeros To Make The Length 4
print(d.zfill(4)) # output: "0011" # Fill With Leading Zeros To Make The Length 4
print(e.zfill(4)) # output: "0111" # Fill With Leading Zeros To Make The Length 4
print(f.zfill(4)) # output: "1111" # Already Length 4, So No Change

# 05- upper() lower() => Convert All Characters In The String To Uppercase Or Lowercase => Non-Alphabetic Characters Are Left As Is => Note: This Method Does Not Modify The Original String, It Returns A New String

g = "osama"

print(g.upper()) # output: "OSAMA"

# 06- lower() => Convert All Characters In The String To Lowercase => Non-Alphabetic Characters Are Left As Is => Note: This Method Does Not Modify The Original String, It Returns A New String

h = "OSama"

print(h.lower()) # output: "osama"

# End of File Course 013 - Strings Methods in Python

print(f"{'End Course 013 - Strings Methods in Python'}")

