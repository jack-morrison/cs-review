#!/usr/bin/env python3
# run.py
# demonstrates a bubble sort using bubble_sort.py

from bubble_sort import *


myarray = [3,8,7,1,2,4,5,6]
print("(UNSORTED) ", myarray)
print("\n ... performing bubble sort ... \n")
myarray = bubble_sort(myarray)
print("(SORTED)   ", myarray)
