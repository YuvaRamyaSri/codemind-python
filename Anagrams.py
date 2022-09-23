n=input()
m=input()
n=n.lower()
m=m.lower()
p=[]
q=[]
if(len(n)==len(m)):
    for i in n:
        p.append(i)
    for i in m:
        q.append(i)
if(p==q):
    print("False")
else:
    print("True")
           