i#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    key_to_dele = []
    for key in a_dictionary.items():
        if a_dictionary[key] == value:
            key_to_dele.append(key)
    for key in key_to_dele:
        del a_dictionary[key]
    return a_dictionary
