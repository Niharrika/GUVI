#Program to check whether a string is palindrome or not
string=input("Enter string : ")
s=(string[::-1])
print("Reversed String : ",s)
if (s==string):
    print("This is Palindrome")
else:
    print("This is not Palindrome")
