# -*- coding: utf-8 -*-
import random

text_file = open("HW4.txt", "r")
lines = text_file.readlines()
text_file.close()

#pre-process of data
def data_process():
    tem,Adj_= [],[]
    for ele in lines:
        tem.append(ele.split())
    Adj_pre = [[int(ele2) for ele2 in ele] for ele in tem]
    
    for ele in Adj_pre:
        for ele2 in ele:
            if ele[0] != ele2 and set((ele[0],ele2)) not in Adj_:
                Adj_.append(set((ele[0],ele2)))   
                
    Edgelist = [sorted(list(par)) for par in Adj_ ]
    Nodelist = [i+1 for i in range(200)]
    return Edgelist , Nodelist
    #print(Edgelist)



def Kager_Algo(Edgelist,Nodelist):
    
    while len(Nodelist) > 2 :
        
        choose = random.choice(Edgelist)
        remove_node ,left_node = choose[0] ,choose[1] # define the node will be remove or left
        
        Nodelist.remove(remove_node)  #remove the node
        Edgelist = [x for x in Edgelist if x != choose]  # remove the edge
        
        for ele in Edgelist:   # transform the node of edge whose vertexs is connect to the removed node to the left node
            if remove_node in ele :
                idx = ele.index(remove_node)
                ele[idx] = left_node
        Edgelist = [sorted(par) for par in Edgelist]    
        
    #print(Edgelist)
    return len(Edgelist)


def operation(times) :
    
    count = 1000000000
    for i in range(times):
        res = Kager_Algo(data_process()[0],data_process()[1])
        print(count)
        if res < count :
            count = res
            
    return count

operation(1000)



