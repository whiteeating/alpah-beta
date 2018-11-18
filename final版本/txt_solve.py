    # -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 20:15:55 2018

@author: 14194
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:54:13 2018

@author: 14194
"""

import os
import sys
import re
import numpy as np
import pandas as pd
from datetime import datetime
match1 = '系统消息'
def matchh(value):
    match2=value
    return match2
match2 = '2'
l = [0]
person =[]
able_person = []
file = open('record.txt','r',encoding='utf-8')
def wipe_empty():
    fnew = open('result.txt','w',encoding='utf-8')
    lines = file.readlines()
    l = [x for x in lines]
    for n in range(len(l)):
        data = l[n].strip()
        if len(data)!= 0:
            data = data+'\n'
            if match1 not in l[n]:
                fnew.write(l[n])
            else:
                l[n] = l[n+1] = ''
                fnew.write(l[n])
                fnew.write(l[n+1])
    fnew.close()
def select_1(value):
    fnew = open('result.txt','r+',encoding='utf-8')
    filenew = open('final_result.txt','w',encoding='utf-8')
    f = fnew.readlines()
    l = [x for x in f]
    match2=value
    print(match2+'ok1')
    for n in range(len(l)):
        if match2 in l[n]:
            filenew.write(l[n-1])
            l[n] = match2+'\n'
            filenew.write(l[n])
    fnew.close()
    pass
def select_QQ(value):
    wipe_empty()
    select_1(value)
    f = open('final_result.txt','r',encoding='utf-8')
    qqNum = open('QQ_NUM.txt','w')
    b = 1
    s = set(l)
    for line in f.readlines():
        rule = re.compile(r'[1-9][0-9]{5,9}')
        r = re.compile(r'[1-9](0){6,10}')
        m1 = r.search(line)
        if m1:
            b = m1.group()
            b = int(b)
        m = rule.search(line)
        if m:
            a  = m.group()
            a = int(a)
            #print(m.group())
            person.append(a)
        s = set(person)
    for x in s:
        if x!=b:
            able_person.append(x)
            x = str(x)
            qqNum.write(x+'\n')
    return able_person
if __name__ == "__main__":
    wipe_empty()
    select_1(value)
    select_QQ(value)
    
    
    
    
           
    
           
    
