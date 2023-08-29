#!/usr/bin/python3
def safe_print_division(a, b):
    decimal = None
    try:
        decimal = a / b
    except:
        pass
    finally:
        if decimal is not None:
            print("Inside result: {}".format(decimal))
        else:
            print("Inside result: None")
    return (decimal)
