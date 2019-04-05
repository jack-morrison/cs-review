#!/usr/bin/env python3

def main():
    print("\n\tLet's do some string compression!\n\tCome on, try me...\n\tGive me a string and I'll try to compress it...\n\n")

    inString = input("\tEnter a string to compress: ")
    outString = compress(inString)

    if outString == inString:
        print("\n\tMy compression methods are no good here!\n")
    else:
        difference = len(inString) - len(outString)
        print("\n\tThe compressed string is: " + outString + " -- " + str(difference) + " characters shorter!\n")

    return 1



def compress(inString):
    compressed = ""
    count = 0

    for i in range(len(inString)):
        if i != 0 and inString[i] != inString[i-1]:
            compressed += inString[i-1] + str(count)
            count = 0
        count += 1

    compressed += inString[-1] + str(count)

    return min(inString, compressed, key=len)


main()
