n=int(input())
p=abs(n)
t=n
rev=0
while(p!=0):
    d=p%10
    p=p//10
    rev=rev*10+d
if(t<0):
    print('-%d'%rev)
else:
    print(rev)