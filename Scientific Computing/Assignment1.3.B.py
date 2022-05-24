# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 12:08:41 2022

@author: User
"""

#Created by Sofia Fadzil 17186913 for SIF2007 16/3
#ASSIGNMENT1 3B)

import numpy as np
import matplotlib.pyplot as mpl

def f(x):
    return np.exp(-x)
#print('f(0)=',f(0),'\n','f(1)=',f(1)) #tanya dr kenapa dia ada space
#print('f(0)=',f(0),)
#print('\n')
#print('f(1)=',f(1))
print('f(x)= e^-x')
x= np.arange(0,1,0.1)
print(x, f(x)) #check balik kena tukar radian
mpl.plot(x,f(x),'o-')
mpl.show()