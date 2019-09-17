#!/usr/bin/env python3
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = []
for number in a:
    if (number % 2 == 0):
        b.append(number)
#b = [number for number in a if number % 2 == 0]
print(b)
