'''
12/03/26
create an empty dictionary. Allow 4 friends to enter their favorite language as 
value and use key as their names. Assume that the names are unique. '''

d = dict()

for i in range (3):
    name = input("Enter friends name: ")
    lang = input("Enter Language name: ")
    d.update({name: lang})

print(d)