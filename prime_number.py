n=int(input( ))
fc=2
for i in range(2,n):
    if(n%i==0):
        fc=fc+1
if(fc==2):
    print("prime")
else:
    print("not a prime")