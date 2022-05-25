##6) write a program to  find the sum of the series 1 +11 + 111 + 1111 + .. n terms


n=int(input("Enter the no of the terms"))
s=0
res=0
for i in range(n):
    s=s*10+1
    res=res+s
print(res)