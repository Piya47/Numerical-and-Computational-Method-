# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:50:47 2022

@author: User
"""


#Created by Sofia Fadzil 17186913 for SIF2007 16/3
#ASSIGNMENT1 3C)

import numpy as np
import matplotlib.pyplot as mpl

def f(x):
    return (x**2)*(np.exp(-x))
#print('f(0)=',f(0),'\n','f(2)=',f(2))
print('f(x)= x^2(e^-x)')
x= np.arange(0,2,0.1)
print(x, f(x)) #check balik kena tukar radian
mpl.plot(x,f(x),'o-')
mpl.show()
