# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 15:30:04 2021

@author: muzi
"""

#检测有无长度≥5的相同序列
def subword(s1,s2,subl):
    sub = True
    list1 = []
    for i in range(len(s1)):
        word1 = s1[i:i+subl]
        list1.append(word1)
    for j in range(len(s2)-subl):
        if s2[j:j+subl] in list1:
            sub = False
            break
    return sub

#生成互补序列
def complement(s):
    dictDNA = {'A':'T','T':'A','C':'G','G':'C'}
    com = []
    for i in s:
        com.append(dictDNA[i])
    com.reverse()
    coms = ''.join(com)
    return coms

#两条链筛选
def main(s1,s2,subl):
    sub = subword(s1,s2,subl)
    resub = subword(s1,complement(s2),subl)
    ortho = sub and resub
    return ortho
