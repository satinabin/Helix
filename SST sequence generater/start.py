# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 10:18:13 2021

@author: muzi
"""

import sys
sys.path.append('lib')
import Main

def getslist():
    filename = input('输入文件名：')
    f = open(filename,'r')
    slist = f.read().splitlines()
    f.close()
    return slist

slist = getslist()
while True:
    l = int(input('序列长度='))
    n = int(input('序列数量='))
    subl = int(input('允许最大子序列长度='))
    gcl = float(input('GC含量下限='))
    gch = float(input('GC含量上限='))
    slist = Main.Main(l,n,slist,subl,gcl,gch)
    nlist = []
    for i in slist:
        nlist.append(i+'\n')
    ff = open('seq_new.txt','w')
    ff.writelines(nlist)
    ff.close()
    print('completed!')
