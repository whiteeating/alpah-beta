# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 09:26:42 2018

@author: 14194
"""
import os 
import random
import math 
from txt_solve import select_QQ
l = []
def randomNum():
    for n in range(7):
        a = random.randint(1,20)
        l.append(a)
    f = random.sample(l[:-1],2)
    a,b = f[0],f[1]
    return a,b
def fun_1(a,x,b):
    return a*x+b
def fun_2(x,y):
    return x+y
def fun_3(x,y):
    return x*y
def fun_4(a,x,b):
    return a/x+b
def run_draw():
    result = [1,2,3,4,5,6]
    for n in range(6):
        a,b = randomNum()
        for i in range(4):
            randnum = random.randint(1,4)
            if randnum == 1:
                result[n] = fun_1(a,l[-1],b)
                if result[n]>40:
                    result[n] = result[n]%40
            if randnum == 2:
                result[n] = fun_2(a,b)
                if result[n]>40:
                    result[n] = result[n]%40
            if randnum == 3:
                result[n] = fun_3(a,b)  
                if result[n]>40:
                    result[n] = result[n]%40
            if randnum == 4:
                result[n] = fun_1(a,l[-1],b)
                if result[n]>40:
                    result[n] = result[n]%40
    return result
def draw_winner(value):
    result = run_draw()
    bonus = select_QQ(value)
    winner = [bonus[p] for p in result]
    return winner
    
            
                
            
            
            
        
        

    

    
    
        