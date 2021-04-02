# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 17:42:41 2021

@author: Galanodel

Anaconda 2020.11 py3_0 wtih conda 4.9.2 spyder 4.1.5
"""

import implementation as imp

N = 10**5
m = 4
Q = (0, 1/3, 2/3, 1)


for q in Q:
    imp.mix(N,m,m,q)