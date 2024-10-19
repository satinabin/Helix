# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:04:06 2021

@author: muzi
"""

#生成随机序列
import random
def seqgen(l):
    base = ['A','T','C','G']
    s = ''
    for i in range(l):
        s += random.choice(base)
    return s

#检测有无长度≥4的均聚
def homorun(s):
    homo = True
    for i in range(0,len(s)-3):
        run = s[i:i+4]
        if run == run[0]*4:
            homo = False
            break
    return homo

#检测GC含量
def GCcontent(s):
    count = 0
    for i in s:
        if i == 'G' or i == 'C':
            count = count + 1
    GC = float(count/len(s))
    return GC

#单条链筛选
def main(l,gcl,gch):
    while True:
        s = seqgen(l)
        homo = homorun(s)
        GC = GCcontent(s)
        if homo == True and gcl < GC < gch:
            return s
