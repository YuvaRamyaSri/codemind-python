a=input()
b=list(a.split( ))
l=100
for i in b:
    c=0
    for j in i:
        if j in 'aeiou':
            c+=1
    if l>c:
        l=c
print(l)