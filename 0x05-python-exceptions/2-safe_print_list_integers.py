#!/usr/bin/python3
def safe_print_list_intgers(my_list=[], x=0):
    count = 0
    for item in range(x):
        try:
            print("{}".format(my_list[i]), end='')
            counter += 1
        except(TypeError, ValueError):
            pass
    print()
    return (counter)
