# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 11:03:09 2020

@author: USER
"""

import random as r
n=r.randint(0,20)
i=0
while i<5:
    i=i+1
    try:
        a=int(input('請輸入數字:'))
    except:
        print('請輸入正確的整數')
        continue
    if a==n:
        print('恭喜答對,玩了',i,'次')
        break
    elif a>n:
        print('猜太大了')
    else:
        print('猜太小了')
    
print('遊戲結束')