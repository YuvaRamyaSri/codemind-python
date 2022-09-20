n,m=map(int,input().split())
for i in range(1,10):
    if(n==i and m==(i+1) or n==1 and m==10 or n==10 and m==1 or n==(i+1) and m==i):
        print("Yes")
        break
else:
    print("No")
