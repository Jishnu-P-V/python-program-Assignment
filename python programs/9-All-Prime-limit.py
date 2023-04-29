limit = int(input("enter the limit"))
for i in range(2,limit+1):
    flag=1 
    for j in range(2,i):
        if i % j == 0:
            flag=0
            break
    if flag == 1:
        print(i)