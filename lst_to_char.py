##10)  Write a Python program to convert a list of characters into a string.



ch=[]
size=int(input("Enter the size of the list"))
print("Enter the elements")
for i in range(0,size):
    ele=input()
    ch.append(ele)
string=""
for i in range(0,size):
    string=string+ch[i]
print(string)