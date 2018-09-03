# Write a method to replace all spaces in a string with '%20'. You may assume
# that the string has sufficient space at the end to hold the additional
# characters, and that you are given the "true" length of the string.

def URLify(inString):
    s = inString.strip()
    for char in s:
        if char == " ":
            s = s.replace(char, "%20")
    return s
