##2) Write a Python program to check a triangle is equilateral, isosceles or scalene


n1=int(input("Enter the first side"))
n2=int(input("Enter the second side"))
n3=int(input("Enter the third side"))

if n1==n2==n3:
    print("The triangle is equilateral")
elif n1!=n2!=n1:
    print("The triangle is scalene")
else:
    print("The triangle is isoscales")
