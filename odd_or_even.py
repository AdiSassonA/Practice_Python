#!/usr/bin/env python3
#This is answer to exercise number 7

number = int(input("insert number: "))
if (number % 2) == 0:
    if (number > 4):
        print("{0} is even and multiple of 4".format(number))
    else:
        print("{0} is even and less then 4".format(number))
else:
    if (number > 4):
        print("{0} is odd and multiple of 4".format(number))
    else:
        print("{0} is odd and less then 4".format(number))
check1,num1 = input("insert two more numbers: ").split()
num=int(num1)
check=int(check1)
if (num % check) == 0:
    print(num,"divided by",check)
else:
    print(num,"is not divided by",check)
