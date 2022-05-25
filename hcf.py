####8) Write a Python program to get the highest common factor (HCF) of two positive integers.
##
n1=int(input("Enter the first number  "))
n2=int(input("Enter the second number  "))
m=min(n1,n2)
for i in range(m,0,-1):
    if n1%i==0 and n2%i==0:
        hcf=i
        break
print("The HCF of two number is " ,hcf)