#Program to find number of vowels and consonants
string=input("Enter string :")
v=0
c=0
for i in string:
    if (i=='a'):
        v=v+1
    elif (i=='e'):
        v=v+1
    elif (i=='i'):
        v=v+1
    elif (i=='o'):
        v=v+1
    elif (i=='u'):
        v=v+1
    else:
        c=c+1
print("Vowels",v)
print("Consonants",c)
