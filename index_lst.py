##9)Write a Python program access the index of a list.

lis_1=[]
size=int(input("Enter the size elements of the list1"))

for i in range(size):
    ele=int(input())
    lis_1.append(ele)
print("Enter the index of the element which you have printed")
ind=int(input())
print(lis_1[ind])