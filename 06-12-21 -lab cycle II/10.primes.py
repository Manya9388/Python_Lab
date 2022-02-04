limit=int(input("find prime numbers to limit:"))
print("All prime numbers to limit",limit,"are:")
for num in range(2,limit+1):
    i=2
    for i in range(2,num):
        if(num%i==0):
            i=num
            break;
    if(i!=num):
        print(num,end=" ")