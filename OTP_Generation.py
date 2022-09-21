a=input()
b=[]
for i in a:
    if int(i)%2==0:
        continue
    r=int(i)*int(i)
    if r not in b:
        b.append(r)
for i in b:
    print(i,end='')