#!/usr/bin/env python3

# Given a string, write a function to check if it is a permutation of a
# palindrome. A palindrome is a word or phrase that is the same forwards and
# backwards. A permutation is a rearrangement of letters. The palindrome does not
# need to be limited to just dictionary words.

# This solution is case and white-space sensitive.

def palindromePermutation(str):
    isPalPerm = False               # Innocent until prov-- False until proven True

    counts = {}                     # {Character[number of occurances],...}
    for char in str:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1

    oddCounts = 0                   # Only need to consider odd valued counts
    for key in counts:
        if (counts[key] % 2 != 0):
            oddCounts += 1

    if oddCounts <= 1:              # PalPerm is False with > 1 odd count
        isPalPerm = True

    return isPalPerm



print(palindromePermutation('tacocat'))
print(palindromePermutation('not a palperm'))
