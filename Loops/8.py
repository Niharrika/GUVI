#Program to find sum of all odd numbers between 1-n
n=int(input("Enter number : "))
d=0
for i in range (1,n+1):
    if (i%2!=0):
        d=d+i
print("Sum of the given even numbers : ",d)
