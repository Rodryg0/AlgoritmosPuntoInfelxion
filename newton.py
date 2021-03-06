import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol
from scipy.misc import derivative 
import math


def newton(f,x):
    k=0
    f1=lambda x:2*x-np.cos(x)
    f2=lambda x:2+np.sin(x)
    while f(x)>=x:
        xn=x-f1(x)/ f2(x)
        x=xn
        print(xn)
        k = k + 1
       
    return x

f=lambda x:x**2-np.sin(x)
x=newton(f,.5)
y=f(x)
print(x," ",y)

X = np.linspace(0,4,100)
Y= f(X)
plt.plot(X,Y)
plt.plot(x,y,"o")
