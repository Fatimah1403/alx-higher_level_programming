#!/usr/bin/python3
def multiple_returns(sentence):
    new_s = len(sentence)
    if new_s == 0:
        result = (0, None)
        return result
    else:
        result = (new_s, sentence[0:1])
        return result
