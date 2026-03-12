'''12/03/26
1. Write a program to find the greatest of four numbers entered by the user. '''

a1 = int(input("Enter 1st number: "))
a2 = int(input("Enter 2nd number: "))
a3 = int(input("Enter 3rd number: "))
a4 = int(input("Enter 4th number: "))
greatest = a1
if a2>greatest:
    greatest = a2
if a3>greatest:
    greatest = a3
if a4>greatest:
    greatest = a4

print("Greatest number is:", greatest)