#Program to find sum of first and last digit of a number
n=int(input("Enter number : "))
i=0
d=0
last=n%10
while n>0:
    n=n//10
    d=i+1
s=d+last
print("Sum of first and last digits are:",s)


