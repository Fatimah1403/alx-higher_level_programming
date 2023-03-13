#!/usr/bin/python3
def max_integer(my_list=[]):
    list = len(my_list)
    if list == 0:
        return None
    else:
        max_num = my_list[0]
        for i in range(1, list):
            if my_list[i] > max_num:
                my_list[i] = max_num
        return (max_num)
