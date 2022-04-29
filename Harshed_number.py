n=int(input( ))
c=0
temp=n
while(n!=0):
    d=n%10
    n=n//10
    c=c+d
if(temp%c==0):
    print("True")
else:
    print("False")