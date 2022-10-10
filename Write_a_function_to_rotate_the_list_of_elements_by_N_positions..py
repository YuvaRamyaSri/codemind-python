n=int(input())
a=list(map(int,input().split()))
k=int(input())
for i in range(k):
    c=a.pop()
    a.insert(0,c)
print(*a)