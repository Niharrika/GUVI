#Program to find sum of all natural numbers between 1-n
n=int(input("Enter number : "))
d=0
for i in range (1,n+1):
    d=d+i
print("Sum of natural numbers : ",d)
