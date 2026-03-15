'''
12/03/26
7. Write a program to print the following star pattern. 
  * 
 *** 
***** for n = 3

'''
n = int(input("ENter a number for steps: "))
for i in range (1,n+1):
    space = n-i
    star = (2*i)-1
    print(" "*space,end="")
    print("*"*star)

