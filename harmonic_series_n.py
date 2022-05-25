##8) Write a program  to display the n terms of harmonic series and their sum. Go to the editor
##1 + 1/2 + 1/3 + 1/4 + 1/5 ... 1/n terms

num=int(input("Enter the number"))
sum=0
for i in range(1,num+1):
    sum=sum+(1/i)
print(sum)