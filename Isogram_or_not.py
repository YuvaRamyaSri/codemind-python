n=input()
c=0
p=[]
for i in n:
   q=n.count(i)
   if(q==1):
       c+=1
if(c==len(n)):
    print("True")
else:
    print("False")