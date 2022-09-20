n=int(input())
l=list(map(int,input().split()))
p=int(input())
c=0
def is_prime(s):
    if(s==1):
        return 0
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
    else:
        return 1
for i in l:
    if(is_prime(i) and i>=p):
        c+=1
print(c)