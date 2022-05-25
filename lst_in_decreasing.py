##Exercise Question 1: Given a Python list you should be able to display
##Python list in the decreasing order

size=int(input("Enter the size of the list "))
ls=[]
for i in range(0,size):
    ele=int(input())
    ls.append(ele)


ls.sort(reverse=True)
print(ls)
