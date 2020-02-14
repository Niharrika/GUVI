#Program to calculate product of digits of a number
n=(input("Enter number : "))
d=1
for i in n:
    d=d*int(i)
print("Product of digits:",int(d))
