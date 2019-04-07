#!/usr/bin/env python3
'''
Given an image represented by an NxN matrix,
write a method to rotate the image by 90 degrees.

Can you do this in place?
'''

import sys
from random import *

def main():
    try:
        N = int(sys.argv[1])
        if N <= 0:
            raise ValueError

        print("\n\tOk, let's create a %dx%d matrix of random ints, then rotate it 90 degrees.\n" % (N, N))

        print("\tStarting Matrix:\n")
        matrix = init_2d_matrix(N)
        print_matrix(matrix)

        print("\tRotated Matrix:\n")
        matrix = rotate_matrix(matrix)
        print_matrix(matrix)

    except ValueError:
        print("\n\tError: Expected positive integer input argument!")
        print("\tUsage: rotate_matrix.py [N]\n")
        sys.exit(1)


def init_2d_matrix(N):
    ## Generate a NxN matrix, where each element is between 0-99, inclusive.
    return [[randint(0, 99) for i in range(N)] for j in range(N)]


def print_matrix(matrix):
    ## Print a matrix row by row
    for x in range(len(matrix)):
        ## Print with leading zeros for single digit elements
        row = [str(item).zfill(2) for item in matrix[x]]
        print("\t", row)
    print("")


def rotate_matrix(matrix):
    n = len(matrix)

    ## A NxN matrix has n/2 "layers"
    ## We'll rotate one layer at a time.
    for l in range(0, int(n/2)):
        start = l
        end = n - 1 - l
        for i in range(start,end):
            offset = i - start
            ## save top element
            top = matrix[start][i]
            ## left --> top
            matrix[start][i] = matrix[end-offset][start]
            ## bottom --> left
            matrix[end-offset][start] = matrix[end][end-offset]
            ## right --> bottom
            matrix[end][end-offset] = matrix[i][end]
            ## top --> right
            matrix[i][end] = top;

    return matrix

main()
