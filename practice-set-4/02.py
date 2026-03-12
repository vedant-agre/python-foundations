'''
12/03/26
Write a program to accept marks of 6 students and display them in a sorted 
manner.'''

marks = []
for i in range(0,6):
    ind_marks = int(input(f"Enter marks of student {i+1}: "))
    marks.append(ind_marks)
marks.sort(reverse=True)
print(marks)