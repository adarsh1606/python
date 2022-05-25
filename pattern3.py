# 3) Write a python program to print a following pattern


##
##   *****
##    ****
##     ***
##      **
##       *
##        *
##        **
##        ***
##        ****
##        *****

        
n=int(input("Enter the number"))
for i in range(1,n):
    for k in range(1,i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print()
for i in range(1,n+1):
    for z in range(1,n+1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")

    print()