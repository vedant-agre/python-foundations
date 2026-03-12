'''12/03/26
Write a program to input eight numbers from the user and display all the unique 
numbers (once). 
'''
numbers = set()

for i in range(8):
    number = int(input("Enter the number to add in the set: "))
    numbers.add(number)

print(numbers)