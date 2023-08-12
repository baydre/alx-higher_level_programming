#!/usr/bin/python3
from sys import argv
argc = len(argv) - 1


def sum_args():
    sum = 0
    for i in range(1, len(argv)):
        sum += int(argv[i])
    return sum


if __name__ == "__main__":
    if (argc == 0):
        print("{}".format(argc))
    else:
        print("{}".format(sum_args()))
