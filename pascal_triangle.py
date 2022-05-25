##4) write a program to display Pascal's triangle
##
##       1
##     1 1
##   1 2 1
##  1 3 3 1
## 1 4 6 4 1

##


##
##
##5)  write a program to check whether a given number is a perfect square

num=int(input("Enter the number"))
flag=0
for i in range(1,num+1):
        if num==(i*i):
            print("Yes it is a perfect square number")
            flag=1
            break
if flag==0:
    print("No it is not a perfect square number")
            