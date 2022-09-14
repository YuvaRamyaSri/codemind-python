n=int(input())
rev=0
d=0
def is_prime(s):
    for i in range(2,int(s**0.5)+1):
        if(s%i==0):
            return 0
    else:
        return 1
if(is_prime(n)):
    while(n!=0):
        d=n%10
        n=n//10
        rev=rev*10+d
    if(is_prime(rev)):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")