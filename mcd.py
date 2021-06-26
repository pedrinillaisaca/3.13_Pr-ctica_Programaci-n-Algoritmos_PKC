a=672
b=38
c=0
mods=[]
while(True):
    c=a%b
    mods.append(c)    
    if(mods[len(mods)-1]==0):
        break
    a=b
    b=c

print(mods[len(mods)-2])