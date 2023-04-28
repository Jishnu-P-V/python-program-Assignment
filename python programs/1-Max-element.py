lis = []
size = int(input("enter the size of list"))
print("enter the numbers")
for i in range(size):
    num = int(input())
    lis.append(num)
maxelement= list[0]
for i in range(size):
    if(lis[i]>maxelement):
        maxelement=lis[i]
print("max number is "+str(maxelement))
