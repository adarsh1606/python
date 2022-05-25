####4. Write a Python program to get the smallest number from a list.
##
print("Enter the size of the elements")
n=int(input())
l=[]
print("Enter the elements")
for i in range(0,n):
    element=int(input())
    l.append(element)
small=l[0]
for i in range(n):
    if l[i]<small:
        small=l[i]
print("The smallest element of the list is" , small)