#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) is None:
        return (None)
    else:

        num_max = my_list[0]
        for i in my_list:
            if i > num_max:
                num_max = i
        return (num_max)
