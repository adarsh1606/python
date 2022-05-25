##1) write a program to find out the sum of an A.P. series


n=int(input("Enter the number of the terms"))
d=int(input("Enter the common differnce"))
a=int(input("Enter the first term"))
sum=(n*(2*a+(n-1)*d))/2
print("The sum of the AP is ",sum)

