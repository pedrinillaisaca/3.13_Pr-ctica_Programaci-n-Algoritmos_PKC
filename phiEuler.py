def getOperation(a,b):
    mods=[]
    while(True):
        c=a%b
        mods.append(c)    
        if(mods[len(mods)-1]==0):
            break
        a=b
        b=c

    # print(mods[len(mods)-2])
    return mods[len(mods)-2] 

def runPhiEuler(num):
    cont=0
    for i in range(0,num):
        if(getOperation(i,num)==1):
            cont+=1
    return cont

print(runPhiEuler(5))    