n=int(input())
m=0
a=list(map(int,input().split()))
for i in a:
    if(a.count(i)>n//2):
        m=i
print(m)