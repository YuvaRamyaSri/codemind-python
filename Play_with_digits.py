n=int(input())
s=0
d=0
l=list(map(int,input().split()))
for i in l:
    while(i!=0):
        d=i%10
        i=i//10
        s=s+d
print(s)