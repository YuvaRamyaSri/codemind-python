n=list(map(str,input().split()))
s=[]
for i in n:
    c=0
    for j in i:
        if(j in "aeiouAEIOU"):
            c+=1
    s.append(c)
dup=[]
for i in s:
    if(i==max(s)):
        dup.append(i)
print(len(dup))