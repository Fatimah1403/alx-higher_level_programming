#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    new_dict = []
    for value in a_dictionary:
        if not math.isnan(value):
            new_dict.append(value)
