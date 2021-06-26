a=672
b=38
c=0
q=0

a_f=a
b_f=b
mods=[]
q_vals=[]
x_vals=[]
y_vals=[]
while(True):
    c=a%b
    q=a//b
    mods.append(c)
    q_vals.append(q)
    print(mods[len(mods)-1])
    if(mods[len(mods)-1]==0):
        break
    a=b
    b=c


x_vals.append(1)
x_vals.append(0)
y_vals.append(0)
y_vals.append(1)
#OBTENER COEFICIENTES
for i in range(0,len(q_vals)-1):
    print(q_vals[i])
    x_vals.append(x_vals[i]-(q_vals[i]*x_vals[i+1]))
    y_vals.append(y_vals[i]-(q_vals[i]*y_vals[i+1]))

# print(x_vals[-1])
# print(y_vals[-1])
#APLICAR  ax+by=MCD
print("Respuesta: ",mods[-2])
print("Respuesta extendida: ",(a_f*x_vals[-1])+(b_f*y_vals[-1]))



