#!/bin/env/python3

num = int(input("Enter a number: "))

Sum = 0

while(num > 0):
    dig = n % 10
    Sum = Sum + dig
    num = num // 10
print("Total sum of digit is: ",Sum)

