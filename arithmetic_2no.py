##10)  write a program to calculate sum, difference  ,multiplication, divide,modulus...


n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
op=input("Enter the operator ")

if op=="+":
    res=n1+n2
    print(res)
elif op=="-":
    res=n1-n2
    print(res)
elif op=="*":
    res=n1*n2
    print(res)
elif op=="/":
    res=n1/n2
    print(res)
elif op=="%":
    res=n1%n2
    print(res)
    