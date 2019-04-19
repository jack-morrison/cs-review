#!/usr/bin/env python3

def insertion_sort(values):
    i = 1
    while i < len(values):
        x = values[i]
        j = i - 1

        while j >= 0 and values[j] > x:
            values[j+1] = values[j]
            j-=1
        
        values[j+1] = x
        i+=1

    return values

print(insertion_sort([4,1,6,71,14,99,123]))
