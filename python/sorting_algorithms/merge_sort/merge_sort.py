#!/usr/bin/env python3

def mergeSort(values):
    # A list of size 1 is sorted.
    if len(values) == 1:
        return values

    # Recursively split input list into halves until there are n lists of size 1.
    # We'll refer to these two halves as `left` and `right`.
    if len(values) > 1:
        left = values[:(len(values)//2)]
        right = values[(len(values)//2):]

        mergeSort(left)
        mergeSort(right)


        #merge by comparing the first elements of each list
        l=0 #index of left
        r=0 #index of right
        m=0 #index into merged list
        #if items remain on both sides to be added to the merged list
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                values[m] = left[l]
                l+=1
            else:
                values[m] = right[r]
                r+=1
            m+=1
        #if only left items remain to be added to the merged list, add them all
        while l < len(left):
            values[m]=left[l]
            l+=1
            m+=1
        #if only right items remain to be added to the merged list, add them all
        while r < len(right):
            values[m]=right[r]
            r+=1
            m+=1
        return values


print(mergeSort([4,1,6,71,14,99,123]))
