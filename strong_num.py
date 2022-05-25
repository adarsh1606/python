##2) write a program to check whether a number is a Strong Number or not.

num=int(input("Enter the number"))
temp=num
sum=0
while num!=0:
    d=num%10
    fact=1
    for i in range(1,d+1):
        fact*=i
    sum+=fact
    num//=10
if sum==temp:
    print("Yes, it is a strong number")
else:
    print("No, it is not a strong number")