##6)Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.


n1=int(input("Enter the first number  "))
n2=int(input("Enter the second number  "))
if n1==n2 or n1-n2==5 or n2-n1==5 or n1+n2==5:
    print("True")
else:
    print("False")
