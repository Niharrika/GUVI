#Program to calculate sum of digits of a number
n=(input("Enter number : "))
d=0
for i in n:
    d=d+int(i)
print("Sum of digits:",int(d))
