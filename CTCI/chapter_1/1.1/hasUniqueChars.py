# Implement an algorithm to determine if a string has allunique characters.
# What if you cannot use additional data structures?

def hasUniqueChars(stringIn):
    if (len(stringIn) > 128):   # ASCII characters are the first 128 Unicode values
        return False

    char_set = [False for _ in range(128)]
    for char in stringIn:

        # ord() is a Python Built-in that given a string of length one,
        # returns an integer representing the Unicode
        val = ord(char)

        if (char_set[val]):
            return False

        char_set[val] = True

    return True
