#!/usr/bin/python3

"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    word = 0

    while word < len(text) and text[word] == " ":
        word = word + 1

    while word < len(text):
        print(text[word], end="")
        if text[word] == "\n" or text[word] in ".?:":
            if text[word] in ".?:":
                print("\n")
            word += 1
            while word < len(text) and text[word] == " ":
                word += 1
            continue
        word += 1
