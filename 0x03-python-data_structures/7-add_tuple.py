#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 0:
        b1, b2 = 0, 0
    elif len(tuple_b) == 1:
        b1, = tuple_b
        b2 = 0
    else:
        b1, b2 = tuple_b
    a1, a2 = tuple_a
    result1 = a1 + b1
    result2 = a2 + b2
    return(result1, result2)
