##5) Write a Python program to convert temperatures to and from celsius, fahrenheit.


print('''Are you enter the temp in celcius or fahrenheit

      if fahrenheit then type F otherwise C

      ''')

ch=input()
if ch=="F" or ch=="f":
    temp=float(input("Enter the temperature in Fahrenheit"))
    c=(5*(temp-32))/9
    print("YOu answer in celcius is ",c)

else:
    temp=float(input("Enter the temperature in Celcius"))
    c=((9*temp)+(32*5))/5
    print("YOu answer in celcius is ",c)