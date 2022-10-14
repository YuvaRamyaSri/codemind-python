n=input()
c=0
v="aeiouAEIOU"
for i in n:
    if(i in v):
        c+=1
if c:
    print(c)
else:
    print(0)