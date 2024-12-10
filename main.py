string = input("Enter a string: ")
string_len = len(string)


if string.isalpha() or string.isdigit() and string_len > 5 and string_len < 11:
    print(f'Valid Input: {string}')