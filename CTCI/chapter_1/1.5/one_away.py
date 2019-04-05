#!/usr/bin/env python3

def main():

    welcomeString = """
        Give me two strings, and I'll tell you if they're one edit away!

        There are 3 types of edits.
        1) Replacement (ex. `pale` --> `bale`)
        2) Insertion   (ex. `pale` --> `pales`)
        3) Deletion    (ex. `pale` --> `pae`)
        """

    print(welcomeString)

    stringA = input("\tInput stringA: ")
    stringB = input("\tInput stringB: ")

    # Insertion and Deletion will be considered together, as they're identical opposite operations.
    # Replacement will be considered separately, and only in the case where stringA and stringB have the same length.

    if (len(stringA) == len(stringB)):
        oneEditAway = evalReplacement(stringA, stringB)
    else:
        oneEditAway = evalInsertOrDelete(stringA, stringB)

    print("\n\t'{}' and '{}' are one edit away?: {}\n".format(stringA, stringB, oneEditAway))

    return 1


def evalReplacement(A, B):
    mismatch = 0

    for i in range(0, len(A)):
        if A[i] != B[i]:
            mismatch += 1
        if mismatch > 1:
            return False

    return True


def evalInsertOrDelete(A, B):
    A = set(A)
    B = set(B)
    
    if len(A) > len(B):
        diff = A.difference(B)
    else:
        diff = B.difference(A)

    if len(diff) == 1:
        return True
    else:
        return False

main()
