n=int(input())
c=0
def is_pli(s):
    p=s
    rev=0
    d=0
    while(s!=0):
        d=s%10
        s=s//10
        rev=rev*10+d
    if(rev==p):
        return 1
    else:
        return 0
l=list(map(int,input().split()))
for i in range(n):
    if(is_pli(l[i])):
        c+=1
print(c)