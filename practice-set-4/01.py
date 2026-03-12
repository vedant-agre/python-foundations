'''12/03/26
Write a program to store seven fruits in a list entered by the user. '''

fruits = []

for i in range(7):
    fruit=input(f"Enter the {i+1}th fruit: ")
    fruits.append(fruit)

print(fruits)