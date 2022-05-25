####5. Write a Python program to count the number of strings where the string length is 2 or more
####and the first and last character are same from a given list of strings.

print("Enter the size of the elements")
n=int(input())
l=[]
print("Enter the elements")
for i in range(0,n):
    element=input()
    l.append(element)
count=0
for i in l:
    if len(i)>1 and i[0]==i[-1]:
        count+=1
print("The number of the element which fulfill the condition is : ", count)