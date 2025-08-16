#!/usr/bin/python3
for i in range(26):
    letter = chr(ord('a') + i)
    if letter != 'q' and letter != 'e':
        print(letter, end="")
