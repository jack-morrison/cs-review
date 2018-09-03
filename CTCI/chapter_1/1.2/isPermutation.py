# Given 2 strings, write a method to decide if one is a permutation of the other.

def string_to_dict_of_counts(inString):
    counts = {}
    for char in inString:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    return counts

def check_dict_equivalence(d1, d2):
    for key in d1:
        if (key in d1) and (key in d2) and (d1[key] == d2[key]):
            continue
        else:
            return False
    return True
