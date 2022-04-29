n,r=map(int,input().split())
for i in range(0,r+1):
    if(i%2==0):
        continue
    else:
        print(n,"x",i,"=",n*i)