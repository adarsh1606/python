##4 ) Write a Python function that takes two lists
##and returns True if they have at least one common member.


lis_1=[]
size=int(input("Enter the size of the list1  "))
for i in range(size):
    ele=int(input())
    lis_1.append(ele)

lis_2=[]
size=int(input("Enter the size of the list2  "))
for i in range(size):
    ele=int(input())
    lis_2.append(ele)

print()
print("The list 1 is ", lis_1)
print("The list 2 is ", lis_2)

len1=len(lis_1)
len2=len(lis_2)
flag=0
for i in range(0,len1):
    for j in range(0,len2):
        flag=1
        break
    if flag==1:
        break
    
if flag==1:
    print("it is true that list have atleast one element is same")
else:
    print("False, lists does not contain same element")
