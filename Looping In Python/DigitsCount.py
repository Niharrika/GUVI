number = int(input("Please Enter any Number: "))
count = 0
while(number > 0):
    number = number // 10
    count = count + 1
print("Number of Digits in a Given Number = %d" %count)
