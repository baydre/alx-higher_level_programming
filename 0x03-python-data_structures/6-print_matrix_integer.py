#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for arr in matrix:
            for item in range(len(arr)):
                if item < (len(arr) - 1):
                    print("{:d}".format(arr[item]), end=' ')
                else:
                    print("{:d}".format(arr[item]), end=' ')
            print()
