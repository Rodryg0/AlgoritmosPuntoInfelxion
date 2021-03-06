import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol
from scipy.misc import derivative 
import math

def dorada(xu,xl,f):
    k = 0
    R=(math.sqrt(5)-1)/2  
    while (xu - xl) > .1 :
        d = R*(xu-xl)
        x1 = xl + d
        x2 = xu - d
        k = k + 1         
        print('k= ', k,' x1 ',x1,' f(x1) ',f(x1),' x2 ',x2,' f(x2) ',f(x2),' d ',d)
        if f(x1) < f(x2):
            xl=x2
        else:
            xu=x1  
    if f(x1) < f(x2):
        return x1
    else:
        return x2
    return x
     
xl=0
xu=4          
f=lambda x:x**2-np.sin(x)
x=dorada(xu,xl,f)
y=f(x)
print(x," ",y)

X = np.linspace(0,4,100)
Y= f(X)
plt.plot(X,Y)
plt.plot(x,y,"o")
