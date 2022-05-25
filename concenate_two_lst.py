##Exercise Question 2: Concatenate two lists index-wise

size=int(input("Enter the size of the both list"))
ls_1=[]
for i in range(0,size):
    ele=input()
    ls_1.append(ele)
    
ls_2=[]
for i in range(0,size):
    ele=input()
    ls_2.append(ele)

for i in range(0,size):
    ls_1[i]=ls_1[i]+ls_2[i]

print(ls_1)