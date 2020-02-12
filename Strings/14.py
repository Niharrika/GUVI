#Program to find first occurence of a character in a given string
string=input("Enter string : ")
char=input("Enter character : ")
d=0
for i in range(len(string)):
    if(string[i]==char):
        d=1
        break
print(i+1)
