#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    l_num = ((number * -1) % 10) * -1
else:
    l_num = number % 10

if l_num > 5:
    print(f'Last digit of {number:d} is {l_num:d} \
and is greater than 5')
elif l_num == 0:
    print(f'Last digit of {number:d} is {l_num:d} and is 0')
elif l_num < 6:
    print(f'Last digit of {number:d} is {l_num:d} \
and is less than 6 and not 0')
