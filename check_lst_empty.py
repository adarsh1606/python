##2 ) Write a Python program to check a list is empty or not.

l=[]
size=int(input("Enter the size of the list"))
for i in range(size):
    ele=int(input())
    l.append(ele)
if len(l)>0:
    print("The list is not empty ")
else:
    print("The list is empty")