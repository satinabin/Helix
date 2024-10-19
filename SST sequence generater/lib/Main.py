# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 16:19:39 2021

@author: muzi
"""

import SeqFilter as SF
import OrthoFilter as OF

#总函数
def Main(l,n,slist,subl,gcl,gch):
    n0 = len(slist)
    while len(slist) < n0+n:
        s = SF.main(l,gcl,gch)
        sp = True
        if slist == []:
            slist.append(s)
        elif slist != []:
            for i in slist:
                sp = sp and OF.main(i,s,subl)
            if sp == True:
                slist.append(s)
    return slist
