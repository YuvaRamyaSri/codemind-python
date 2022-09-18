n=int(input())
a=list(map(int,input().split()))
l=[]
k=[]
for i in range(n):
    if a[i]%2==0:
        l.append(a[i])
    else:
        k.append(a[i])
i=0
j=0
while i<len(k) or j<len(l):
    if i<len(k):
        print(k[i],end=' ')
        i+=1
    if j<len(l):
        print(l[j],end=' ')
        j+=1
if n%2!=0:
    print('0')