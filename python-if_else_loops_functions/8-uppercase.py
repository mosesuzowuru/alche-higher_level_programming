#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        old_ord = ord(char)
        if old_ord > 96 and old_ord < 123:
            new_ord = old_ord - 32
            new_char = chr(new_ord)
            result = result + new_char
        else:
            result = result + char
    print("{}".format(result))