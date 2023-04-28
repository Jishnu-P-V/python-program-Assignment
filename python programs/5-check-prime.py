num=int(input("enter the number"))
flag=0
for i in range(2,num//2+1):
    if(num%i == 0):
        flag=1
if(flag==1):
    print(str(num)+" is not a prime number")
else:
    print(str(num)+" is a prime number")
