##3) Write a Python program to check whether an alphabet is a vowel or consonant.

apha=input("Enter only single character  ")
if apha=="a" or apha=="e" or apha=="i" or apha=="o" or apha=="u" or apha=="A" or apha=="E" or apha=="I" or apha=="O" or apha=="U":
    print("Yes,it is a vowel")
elif ord(apha)>=65 and ord(apha)<=90 or ord(apha)>=97 and ord(apha)<=122:
    print("yes, it is a consonant")
else:
    print("Not, valid")
