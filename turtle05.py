# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:06:08 2020

@author: USER
"""

import turtle as t
e=t.Turtle
x=int(input('請輸入圖形邊數:'))
for i in range(x):
    t.forward(100)
    t.right(360/x)