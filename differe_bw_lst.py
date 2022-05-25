##8) Write a Python program to get the difference between the two lists. means that difference between 1st element both and then 2nd element for both list and so on.

lis_1=[]
size=int(input("Enter the size of the list1 or list2 both are same size  "))
    
for i in range(size):
    ele=int(input())
    lis_1.append(ele)

lis_2=[]
for i in range(size):
    ele=int(input())
    lis_2.append(ele)

diff=[]
for i in range(size):
    diff.append(lis_1[i]-lis_2[i])
print(diff)
