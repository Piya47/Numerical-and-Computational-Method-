# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:55:17 2022

@author: User
"""


#Created by Sofia Fadzil 17186913 for SIF2007 16/3
#ASSIGNMENT1 3D)

import numpy as np
import matplotlib.pyplot as mpl
def f(x):
    return x**(5/2)
#print('f(0)=',f(0),'\n','f(1)=',f(1))
print('f(x)= x**(5/2)')
x= np.arange(0,1,0.1)
print(x, f(x)) 
mpl.plot(x,f(x),'o-')
mpl.show()
