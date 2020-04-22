# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:13:06 2020

@author: h5904
"""

f = open("IntegerArray.txt","r")

A=[int(ele) for ele in f.read().splitlines()]

def Merge_Sort(array):
    
    if len(array) <= 1:
        return 0,array
    else:
        mid = len(array) // 2
        left= array[:mid]
        right = array[mid:]
        a,left=Merge_Sort(left)
        b,right=Merge_Sort(right)
        
    x,y,d = 0,0,a+b
    res=[]
    while x<len(left) and y<len(right):
        if left[x] < right[y]:
            res.append(left.pop(0))            
        else :
            res.append(right.pop(0))
            d+=len(left)         
           
    if len(left)-x-1 >=0:
        res+=left[x:len(left)]
    if len(right)-y-1 >=0:
        res+=right[y:len(right)]
        
    return d,res  

a,b = Merge_Sort(A)
print (a)
