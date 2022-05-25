####3. Write a Python program to get the largest number from a list.
####
print("Enter the size of the elements")
n=int(input())
l=[]
print("Enter the elements")
for i in range(0,n):
    element=int(input())
    l.append(element)
lar=l[0]
for i in range(n):
    if l[i]>lar:
        lar=l[i]
print("The largest element of the list is" , lar)