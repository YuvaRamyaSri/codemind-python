n=input()
c=0
for i in n:
    if(i in "~!@#$%^&*()_+?:}{/><,.';\|"):
        c+=1
print(c)