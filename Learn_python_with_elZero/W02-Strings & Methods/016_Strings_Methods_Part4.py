# ---------------------
# -- Strings Methods --
# ---------------------

# starting Course 016 - Strings Methods in Python
print(f"{'Starting Course 016- Strings Methods in Python'}")


# 01- replace(Old Value, New Value, Count) -- Optional Parameter
# Count => How many times you want to replace the old value with the new value
# If you don't put the count it will replace all the old values with the new value

a = "Hello One Two Three One One" # String to test the replace method
print(a.replace("One", "1")) # Replace all "One" with "1"
print(a.replace("One", "1", 1)) # Replace only the first "One" with "1"
print(a.replace("One", "1", 2)) # Replace only the first two "One" with "1"

# 02- join(Iterable) -- Iterable => A list, tuple, set, dictionary
# join method is used to join the elements of an iterable (like list, tuple, set, dictionary)
# into a single string with a specified separator.


myList = ["Osama", "Mohamed", "Elsayed"] # List to test the join method
print("-".join(myList)) # Join the elements of the list with "-" as separator
print(" ".join(myList)) # Join the elements of the list with " " (space) as separator
print(", ".join(myList))  # Join the elements of the list with ", " as separator
print(type(", ".join(myList))) # The result is a string

print(f"{'End of Course 016- Strings Methods in Python'}")
# End Course 016 - Strings Methods in Python
# -------------------------------------------------------------------------------------------------------------

# Note: There is no method to split a string into a list in this course, it will be covered in the next course.
# -------------------------------------------------------------------------------------------------------------
# End of File
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------

