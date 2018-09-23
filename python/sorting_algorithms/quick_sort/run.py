# run.py
# demonstrates a quick sort using quick_sort.py

from quick_sort import *


myarray = [3,8,7,1,2,4,5,6]
print("(UNSORTED) ", myarray)
print("\n ... performing quick sort ... \n")
myarray = quick_sort(myarray, 0, len(myarray)-1)
print("(SORTED)   ", myarray)
