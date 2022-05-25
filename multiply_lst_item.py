####2. Write a Python program to multiplies all the items in a list.

print("Enter the size of the elements")
n=int(input())
l=[]
print("Enter the elements")
for i in range(0,n):
    element=int(input())
    l.append(element)
p=1
for i in range(0,n):
    p=l[i]*p
print("The product of all the element in list is: " , p)