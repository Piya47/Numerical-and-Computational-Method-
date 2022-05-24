# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:36:35 2022

@author: User
"""

#Created by Sofia Fadzil 17186913 for SIF2007 16/3
#ASSIGNMENT1 3A)
import numpy as np
import matplotlib.pyplot as mpl
def f(x):
    return np.sin(x)

print('f(x)= sin x')
x= np.arange(0,2*np.pi,0.1)
print(x, f(x)) 
mpl.plot(x,f(x),'o-')
mpl.show()

