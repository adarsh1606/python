####1. Write a Python program to sum all the items in a list.
print("Enter the size of the elements")
n=int(input())
l=[]
for i in range(0,n):
   element=int(input())
   l.append(element)
s=0
for i in range(0,n):
    s=s+l[i]
print("The sum of the list is ",s)