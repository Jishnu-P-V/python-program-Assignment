string=input("enter the string\n")
result=''
for i in range(len(string)-1,-1,-1):
    result=result+string[i]
print(result) 
