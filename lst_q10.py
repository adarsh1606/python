##Exercise Question 3: Given a Python list. Turn every item of a list
##into its square

size=int(input("Enter the size of the both list"))
ls_1=[]
for i in range(0,size):
    ele=int(input())
    ls_1.append(ele)
for i in range(0,size):
    ls_1[i]=ls_1[i]**2
print(ls_1)