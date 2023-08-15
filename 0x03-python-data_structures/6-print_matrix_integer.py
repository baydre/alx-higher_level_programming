#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    def print_list(list = []):
        for i in range(len(list)):
            if i < (len(list)-1):
                print("{:d}".format(list[i]), end=' ')
            else:
                print("{:d}".format(list[i]))
    return(list(map(print_list, matrix)))
