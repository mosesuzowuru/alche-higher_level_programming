#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        c = ord(letter) in range(97, 123)
        print("{}".format(chr(ord(letter) - 32 if c else ord(letter))), end="")
    print()