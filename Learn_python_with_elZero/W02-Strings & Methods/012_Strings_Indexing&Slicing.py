# ---------------------------------
# Strings Indexing & Slicing in Python
# ---------------------------------
# [1] All Data in Python is Object ( String - Integer - Float - List - Tuple - Dictionary - Set )
# [2] Object Contain Elements ( Character - Number - Item )
# [3] Every Element Has Its Own Index ( Numbered )
# [4] Python Use Zero Based Indexing ( Index Start From Zero )
# [5] Use Square Brackets To Access Element
# [6] Enable Accessing Parts Of Strings, Tuples or Lists
# ---------------------------------

print(f"{'Starting Course 012 - Strings Indexing & Slicing in Python'}")

# 01- Indexing ( Access Single Item ) => [Index] => Zero Based Indexing => Negative Indexing => Reverse Indexing

myString = "I Love Python" # Index 0 To 12 => Total 13 Character

# 02- Positive Indexing ( Start From 0 ) => I=0 , L=1 , o=2 , v=3 , e=4 , space=5 , P=6 , y=7 , t=8 , h=9 , o=10 , n=11
print(myString[0])  # Index 0 => I
print(myString[9])  # Index 9 => t

# 03- Negative Indexing ( Start From -1 ) => n=-1 , o=-2 , h=-3 , t=-4 , y=-5 , P=-6 , space=-7 , e=-8 , v=-9 , o=-10 , L=-11 , space=-12 , I=-13
print(myString[-1])  # Index -1 => First Character From End => n
print(myString[-6])  # Index -6 => 6th Character From End => P

# Slicing ( Access Multiple Sequence Items ) => [Start:End] => [Start:End:Steps]
# [Start:End] End Not Included => Default Start Is 0 (If Not Written) => Default End Is Length Of Sequence (If Not Written)
# [Start:End:Steps] Steps Not Included (How Many To Skip) => Default Is 1 (No Skip) => Can Be Negative (Reverse)

# 04- Slicing [Start:End] => End Not Included => [Start:End] => [Start:End:Steps] => Steps Not Included
print(myString[8:11])  # yth (End Not Included) => 8,9,10 => 3 Character
print(myString[3:5])  # ov (Start Included) (End Not Included) => 3,4 => 2 Character
print(myString[0:1])  # I (End Not Included) => Single Character => 0 => 1 Character

# 05- Slicing [Start:End] => If Start Or End Not Here Will Take Default Value ( Start=0 , End=Length Of Sequence )
print(myString[:10])  # If Start Is Not Here Will Start From 0 (I Love Pyt)
print(myString[5:])  # If End Is Not Here Will Go To The End (e Python)
print(myString[:])  # Full Data (I Love Python) => If Start & End Not Here Will Go To The Full Data

# 06- Slicing [Start:End:Steps] => Steps Not Included (How Many To Skip) => Default Is 1 (No Skip) => Can Be Negative (Reverse)
print(myString[0::1])  # Full Data (I Love Python) => If Start & End Not Here Will Go To The Full Data
print(myString[::1])  # Full Data (I Love Python) => If Start & End Not Here Will Go To The Full Data

# 07- Slicing [Start:End:Steps] => Steps Not Included (How Many To Skip) => Default Is 1 (No Skip) => Can Be Negative (Reverse)
print(myString[::2]) # I o eton (Skip 1 Character)
print(myString[::3]) # I v yhn (Skip 2 Character)

# 08- Slicing [Start:End:Steps] => Steps Not Included (How Many To Skip) => Default Is 1 (No Skip) => Can Be Negative (Reverse)
print(myString[::-1])  # Reverse The String (no Start & End) => nohtyP evoL I
print(myString[::-2])  # Reverse The String And Skip 1 Character => nhto eo I

# 09- Slicing [Start:End:Steps] => Steps Not Included (How Many To Skip) => Default Is 1 (No Skip) => Can Be Negative (Reverse)
print(myString[5::-1])  # Start From Index 5 To The Beginning And Reverse It => evoL I
print(myString[10:5:-1])  # Start From Index 10 To Index 6 And Reverse It => ohtyP

# End of File Course 012 - Strings Indexing & Slicing in Python
print(f"{'End Course 012 - Strings Indexing & Slicing in Python'}")

