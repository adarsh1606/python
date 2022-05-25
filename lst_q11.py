##Exercise Question 4: Given a Python list. Turn every item of a list into its cube
##
##
size=int(input("Enter the size of the both list"))
ls_1=[]
for i in range(0,size):
    ele=int(input())
    ls_1.append(ele)
for i in range(0,size):
    ls_1[i]=ls_1[i]**3
print(ls_1)