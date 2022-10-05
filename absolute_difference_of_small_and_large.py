x=list(map(str,input().split()))
for i in x:
    for j in i:
        p=min(i)
        q=max(i)
        print(abs(ord(p)-ord(q)),end=" ")
        break