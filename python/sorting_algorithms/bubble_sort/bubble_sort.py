# bubble_sort.py
# Implements bubble sort algorithm

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp
    return arr

def bubble_sort(arr):
    isSorted = False

    unsorted_array_last_position = len(arr)-1

    while not isSorted:
        isSorted = True
        for i in range(0, unsorted_array_last_position, 1):
            if arr[i] > arr[i+1]:
                swap(arr, i, i+1)
                isSorted = False

        unsorted_array_last_position -= 1

    return arr
