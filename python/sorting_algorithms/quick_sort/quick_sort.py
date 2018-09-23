# quick_sort.py
# implements the quick sort algorithm

def swap(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def quick_sort(arr, left, right):
    if left < right:
        pivotIndex = right
        wall = partition(arr, pivotIndex, left, right)

        quick_sort(arr, left, wall-1)
        quick_sort(arr, wall+1, right)

    return arr


def partition(arr, pivotIndex, left, right):
        pivotValue = arr[pivotIndex]
        wall = left

        for i in range(left, right):
            if (arr[i] <= pivotValue):
                swap(arr, i, wall)
                wall += 1

        swap(arr, right, wall)
        return wall
