##7 )Write a Python program to generate and print a list of first and last 5 elements where the values are square
##of numbers between 1 and 30 (both included). list contain value from 1 to 30

   
lis_1=[]
size=int(input("Enter the size atlest more than 5 elements of the list1"))
print("Please enter all the values between 1 to 30 both inclusive")
for i in range(size):
    ele=int(input())
    lis_1.append(ele)
print()
print(lis_1)
print("printed the square of 5 element of the list in left to rigth")
for i in range(0,5):
    print(lis_1[i]*lis_1[i], end=" ")
print()
print("printed the square of 5 element of the list in right to left ")
for i in range(len(lis_1)-1,len(lis_1)-6,-1):
    print(lis_1[i]*lis_1[i], end=" ")
