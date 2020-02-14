#Program to check whether a number is palindrome or not
n=(input("Enter number : "))
d=""
for i in n:
    d=n
a=(d[::-1])
if(a==n):
    print("This is a palindrome number")
else:
    print("This is not a palindrome number")
