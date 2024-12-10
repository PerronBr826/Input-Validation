# Input Validation Starter
# 12/10/24
# Bryce Perron & Josh Phillips

string = input("Enter a string: ")
string_len = len(string)


if string.isalpha() or string.isdigit():
    if string_len > 5 and string_len < 11:
        print(f'Valid Input: {string}')
    else:
        print("Input must be between 6 and 10 characters long.")
else:
    print("Input must be alphabetic or numeric (but not both).")