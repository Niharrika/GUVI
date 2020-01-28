number = int(input("Please Enter any Number: "))
last=number%10
while (number >= 10):
    number = number // 10
print(number,last)
