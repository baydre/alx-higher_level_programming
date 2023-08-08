def uppercase(str):
    for char in str:
        ascii_code = ord(char)

        if 97 <= ascii_code <= 122:
            uppercase_char = chr(ascii_code - 32)
        else:
            uppercase_char = char

        print(uppercase_char, end='')

    print()
