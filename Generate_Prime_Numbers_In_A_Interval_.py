n=int(input())
m=int(input())
def is_prime(s):
    if(s==1):
        return 0
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
    else:
        return 1
for i in range(n,m+1):
    if(is_prime(i)):
        print(i)