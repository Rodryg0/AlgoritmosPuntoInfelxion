import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol
from scipy.misc import derivative 

def exhaustiva(xk,xk_n,f):
    k = 0
    while f(xk_n) < f(xk):
        xk=xk_n
        xk_n= xk_n + h
        k += 1
        print('k= ', k, ' xk = ',xk, ' f(xk)=',f(xk),' xk_n ',xk_n,' f(xk_n)= ',f(xk_n))
    return xk  
              
x=1
h=0.1             
f=lambda x:x**2-np.sin(x)
x=exhaustiva(x,h,f)
y=f(x)
print(x," ",y)

X = np.linspace(0,4,100)
Y= f(X)
plt.plot(X,Y)
plt.plot(x,y,"o")
              
        
