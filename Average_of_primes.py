n=int(input())
c=0
s=0
l=list(map(int,input().split()))
def is_prime(s):
    if(s==1):
        return 0
    if(s==2):
        return 1
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
    else:
        return 1
for i in l:
    if(is_prime(i)):
        s=s+i
        c+=1
m=s/c
print('%0.2f'%m)