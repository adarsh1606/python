##10) write a program to print the sum of all the prime number till n terms

num=int(input("Enter the number"))
sum=0
for j in range(1,num+1):
    flag=0
    for i in range(1,(j//2)+1):
        if j%i==0:
            flag+=1
    if flag==1:
        sum+=j
print("The sum of the prime number is ",sum)