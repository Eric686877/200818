# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:17:37 2020

@author: USER
"""
import random as r
n=r.randint(0,10)
while True:
    try:
        a=int(input('請輸入數字:'))
    except:
        print('請輸入正確的整數')
        continue
    if a==n:
        print('恭喜答對')
        break
    else:
        print('錯了哈哈')