#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_new = []
    for item in range(list_length):
        decimal = 0
        try:
            decimal = my_list_1[item] / my_list_2[item]
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        finally:
            list_new.append(decimal)
    return list_new
