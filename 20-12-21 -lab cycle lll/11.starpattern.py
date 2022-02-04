def star(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end="")
        print("")
k=4
star(k)
for i in range (k-1,0,-1):
    print((k-i) * '' + i * '*')