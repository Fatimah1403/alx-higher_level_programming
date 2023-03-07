#!/usr/bin/python3
for alpha_letters in range(ord('a'), ord('z') + 1):
    if chr(alpha_letters) != 'e' and chr(alpha_letters) != 'q':
        print("{:c}".format(alpha_letters), end="")
