n=input()
n=n.lower()
n=n.split()
def is_pal(s):
    if(s==s[::-1]):
        return 1
    else:
        return 0
c=0
for i in n:
    if(is_pal(i)):
        c+=1
print(c)