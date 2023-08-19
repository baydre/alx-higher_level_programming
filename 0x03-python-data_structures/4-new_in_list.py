#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if int(idx) < 0:
        return my_list
    if int(idx) > (len(my_list) - 1):
        return my_list
    else:
        return [my_list[i] if i != idx
                else element for i in range(len(my_list))]
