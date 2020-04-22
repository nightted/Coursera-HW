# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:45:18 2020

@author: h5904
"""

text_file = open("HW3.txt", "r")
lines = text_file.readlines()
Lists = [int(x.rstrip()) for x in lines]
text_file.close()

def IndexMid(Lists,left,right):
    
    tem = sorted([Lists[left],Lists[left+(right-left)//2],Lists[right]])
    
    return Lists.index(tem[1])


def Partition(Lists,left,right,pivot_position):
        store_number = left+1
        pivot = Lists[pivot_position]
        for i in range(left+1,right+1,1):
            if Lists[i] < pivot:
                Lists[store_number] , Lists[i] = Lists[i] , Lists[store_number]
                store_number += 1
        Lists[store_number-1] , Lists[pivot_position] = Lists[pivot_position] , Lists[store_number-1]
        return store_number-1

def Quicksort(Lists,left,right):
   
    if left < right:
        
        pivot_idx = IndexMid(Lists,left,right) #choose the index of pivot (Mid)
        #pivot_idx = left #choose the index of pivot (First element)
        #pivot_idx = right #choose the index of pivot (Last element)
        pivot_position = left #The position to store the pivot temporaily
        Lists[pivot_position] , Lists[pivot_idx] = Lists[pivot_idx] , Lists[pivot_position] # Exchange the pivot element to the temporary storage position
        
        finalpivot = Partition(Lists,left,right,pivot_position)
        Global_count[0] += right - left
        Quicksort(Lists,left,finalpivot-1)
        Quicksort(Lists,finalpivot+1,right)
        
Global_count = [0]
#Lists = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
Quicksort(Lists,0,len(Lists)-1)
print(Lists,Global_count)
