#!/usr/bin/env python3
#This is answer to exercise number 16
#This script generate new password

import random
import string
strength = input("This is the password generatore, would you prefer your password weak or strong? ")
length = int(input("what is the password length? "))
if strength == "weak":
    def randomString(length):
        letters = string.ascii_lowercase + string.digits + string.punctuation
        return ''.join(random.choice(letters) for i in range(length))
if strength == "strong":
    def randomString(length):
        letters = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(letters) for i in range(length))

print (randomString(length))
