n=int(input())
last=n%10
while(n>=10):
    n=n//10
print(last+n)
