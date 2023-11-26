data=list(range(1,21))
i=0

for i in range(0,len(data)):
    if (i+1)%2==1:
        print("%d"%data[data[i]],end=" ")
    i=i+1