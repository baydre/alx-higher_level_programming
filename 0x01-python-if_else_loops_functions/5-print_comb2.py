#!/usr/bin/python3
for digit in range(0, 100):
    if digit < 99:
        print(f"{digit:02d}, ", end='')
    else:
        print(f"{digit:02d}")
