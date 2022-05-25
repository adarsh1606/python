##7) write a python program input a list from the user and print even list 
print("Enter the size of the elements")
n=int(input())
l=[]
print("Enter the elements")
for i in range(0,n):
    element=int(input())
    l.append(element)
lis=[]
for i in range(0,n):
    if l[i]%2==0:
        lis.append(l[i])
print(lis)