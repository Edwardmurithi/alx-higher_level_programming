#!/usr/bin/python3

# function that prints a string in uppercase followed by a new line.
def uppercase(str):
    for char in str:
        ascii_value = ord(char)
        if 97 <= ascii_value <= 122:  # check if the character is lowercase
            ascii_value -= 32  # convert to uppercase by substracting 32
        print(chr(ascii_value), end="")
    print()  # print new line after printing uppercase string
