# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:09:52 2019

@author: Soumyabrata Bhattacharjee
Eucledian Norm which is the square root of the sum of squares of a vector
"""
import numpy as np
x = [1, 11] # MOdife the vector as per need
y = np.square(x)
z = np.sum(y)
s = np.sqrt(z)
print ('The Eucledian Norm of the vector is ',s)