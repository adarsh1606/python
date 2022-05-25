##3) write a python program to copy a list into other list

lis_1=[]
size=int(input("Enter the size of the list"))
for i in range(size):
    ele=int(input())
    lis_1.append(ele)

lis_2=[]
lis_2=lis_1
print("The list 1 is copy into list 2 is :", lis_2)