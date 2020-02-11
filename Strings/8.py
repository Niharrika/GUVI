#Program to find total number of alphabets, digits or special char in a string
string=input("Enter string : ")
d=0
l=0
c=0
for i in string:
    if i.isdigit():
        d=d+1
    elif i.isalpha():
        l=l+1
    else:
        c=c+1 
print("Alphabets",l)
print("Digits",d)
print("Characters",c)
