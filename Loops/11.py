#Program to find first and last digit of a number
n=int(input("Enter number : "))
i=0
d=0
last=n%10
while n>0:
    n=n//10
    d=i+1
print("The first digit is",d)
print("The last digit is",last)


