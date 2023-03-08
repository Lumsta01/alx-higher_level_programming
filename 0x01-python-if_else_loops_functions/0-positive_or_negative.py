#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} \n is positive")

if number == 0:
    print(f"{number} \n is zero")

if number < 0:
    print(f"{number} \n is negative")

