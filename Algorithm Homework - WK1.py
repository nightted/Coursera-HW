# -*- coding: utf-8 -*-
"""
Algorithm HW1
""" 

def Multiple(x,y):
    
    if len(str(x))//2 == 0 or len(str(y))//2 == 0 :
        return x*y
    
    X,Y = str(x) , str(y)
    x_1st_half = int(X[:len(str(x))//2])
    x_2nd_half = int(X[len(str(x))//2:])   
    y_1st_half = int(Y[:len(str(y))//2])
    y_2nd_half = int(Y[len(str(y))//2:])
    order_x = len(str(x)) - len(str(x))//2
    order_y = len(str(y)) - len(str(y))//2
    
    '''
    這裡要注意不同長度的數字相乘,會有不同order,故要分開計算!!!
    '''
    return Multiple(x_1st_half,y_1st_half)*(pow(10,order_x))*(pow(10,order_y)) + Multiple(x_2nd_half,y_1st_half)*(pow(10,order_y))+Multiple(x_1st_half,y_2nd_half)*(pow(10,order_x)) + Multiple(x_2nd_half,y_2nd_half)
    
print (Multiple(3141592653589793238462643383279502884197169399375105820974944592,2718281828459045235360287471352662497757247093699959574966967627))
