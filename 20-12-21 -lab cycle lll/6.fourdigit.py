for i in range(2000,10000,2):
    for j in range(38,1000,1):
        if i==j*j:
            string=str(i)
            if int(string[0])%2==0:
                if int(string[1])%2==0:
                    if int (string[2])%2==0:
                        if int(string[3])%2==0:
                          print (i)