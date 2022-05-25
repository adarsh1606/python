##9)Write a Python program that accepts a string and calculate the number of digits and letters. Go to the editor
##Sample Data : Python 3.2
##Expected Output :
##Letters 6
##Digits 2

string=input("Enter the string")
l=0
d=0
for i in string:
    if ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122:
        l+=1
    elif ord(i)>=48 and ord(i)<=57:
        d+=1
print("The number of letter in the string is ",l)
print("The number of digit in the string is ",d)