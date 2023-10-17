#!/usr/bin/env python
# coding: utf-8

# In[18]:


from copy import copy, deepcopy
import time
import random
import math
import numpy as np
import sys
sys.setrecursionlimit(10**9)
def pprint(A):
    if A.ndim==1:
        print(A)
    else:
        w = max([len(str(s)) for s in A]) 
        print(u'\u250c'+u'\u2500'*w+u'\u2510') 
        for AA in A:
            print(' ', end='')
            print('[', end='')
            for i,AAA in enumerate(AA[:-1]):
                w1=max([len(str(s)) for s in A[:,i]])
                print(str(AAA)+' '*(w1-len(str(AAA))+1),end='')
            w1=max([len(str(s)) for s in A[:,-1]])
            print(str(AA[-1])+' '*(w1-len(str(AA[-1]))),end='')
            print(']')
        print(u'\u2514'+u'\u2500'*w+u'\u2518')  
Temperature=0
def data():
    file=open("simulated_input.txt",'r')
    pointer=file.read();
    start=[]
    goal=[]
    temp=[]
    flag=0
    T=""
    for ptr in pointer:
        if(ptr=="B"):
            flag=1
        if(ptr=="\n"):
            continue
        if(ptr==" "):
            continue
        elif(len(start)<3):
            if(flag==1):
                temp.append("0")
                flag=0
            else:
                temp.append(ptr)
            if(len(temp)==3):
                start.append(temp)
                temp=[]
        elif(len(goal)<3):
            if(flag==1):
                temp.append("0")
                flag=0
            else:
                temp.append(ptr)
            if(len(temp)==3):
                goal.append(temp)
                temp=[]
        else:
            T=T+ptr
    return start,goal,int(T)


def manhatten(start,goal):
    ans=0
    for i in range(3):
        for j in range(3):
            if(start.config[i][j]==0):
                continue
            for k in range(3):
                for l in range(3):
                    if(goal.config[k][l]==start.config[i][j]):
                        x,y=k,l
            ans+=abs(x-i)+abs(y-j)
    return ans



def misplaced(start,goal):
    ans=0
    for i in range(3):
        for j in range(3):
            if(start.config[i][j]==0):
                continue
            if(start.config[i][j]!=goal.config[i][j]):
                ans=ans+1
    return ans


# In[5]:


def manhatten1(start,goal):
    ans=0
    for i in range(3):
        for j in range(3):
            for k in range(3):
                for l in range(3):
                    if (goal.config[k][l] == start.config[i][j]):
                        x, y = k, l
            ans+=abs(x-i)+abs(y-j)
    return ans


# In[6]:


def misplaced1(start,goal):
    ans=0
    for i in range(3):
        for j in range(3):
            if(start.config[i][j]!=goal.config[i][j]):
                ans=ans+1
    return ans


# In[7]:


def hybrid(start,goal):
    return manhatten(start,goal)*misplaced(start,goal)


# In[8]:


class cooling_function:
    def __init__(self,temp,cooling_coefficient):
        self.temp=temp
        self.coefficient=cooling_coefficient
    def next(self):
        self.temp=self.temp-(1-self.coefficient)*self.temp
        return self.temp
    def show(self):
        return self.temp


# In[9]:


class Node:
    def __init__(self,start):
        self.config=deepcopy(start)
        self.g_value=0
        self.h_value=0
        self.parent=None
        self.f_value=self.g_value+self.h_value
    def __eq__(self,node):
        if(node!=None):
            return self.config == node.config
        return False
    def __str__(self):
        string=''
        for x in self.config:
                for y in x:
                    if(y==0):
                        string+="B "
                    else:
                        string+=str(y)+" "
                string+="\n"
        return string
    def neighbours(self):
        lis=[]
        x=0
        y=0
        for i in range(3):
            for j in range(3):
                if self.config[i][j]=="0":
                    x,y=i,j
        if(x>0):
            temp=deepcopy(self)
            temp.config[x][y],temp.config[x-1][y]=temp.config[x-1][y],temp.config[x][y]
            lis.append(temp)
            
        if(y>0):
            temp2=deepcopy(self)
            temp2.config[x][y],temp2.config[x][y-1]=temp2.config[x][y-1],temp2.config[x][y]
            lis.append(temp2)
        if(x<2):
            temp3=deepcopy(self)
            temp3.config[x][y],temp3.config[x+1][y]=temp3.config[x+1][y],temp3.config[x][y]
            lis.append(temp3)
        if(y<2):
            temp4=deepcopy(self)
            temp4.config[x][y],temp4.config[x][y+1]=temp4.config[x][y+1],temp4.config[x][y]
            lis.append(temp4)
        return lis
    def Path(self):
        path=[]
        current=self
        while(current.parent!=None):
            path.append(current.config)
            current=current.parent
        path.reverse()
        return path


# In[10]:


def algorithm(start,goal,heuristic,cooling):
    current=start
    node_count=1
    current.h_value=heuristic(current,goal)
    '''Temperature object'''
    t=cooling
    while t.show()>1:
        node_count+=1
        '''Checking Goal '''
        if current==goal:
            path=current.Path()
            return path,node_count
        '''Generating Neighbourhood '''
        succ=current.neighbours()
        
        '''Random value generation'''
        rand_indx=random.randint(0,len(succ)-1)
        random_child=succ[rand_indx]
        random_child.h_value=heuristic(random_child,goal)
        
        '''Energy DifferenceComputation'''
        delta_E=current.h_value-random_child.h_value
        if(delta_E>=0):
            random_child.parent=current
            current=random_child
        else:
            p=random.uniform(0,1)
            acc_prob=math.exp(delta_E/t.show())
            if p<=acc_prob:
                random_child.parent=current
                current=random_child
        t.next()
    path=[]
    return path,node_count


# In[11]:


def print_node(coeff,goal,path,node_count,time_taken,heuristic):
    print("Heuristic Detail : %s" %(heuristic))
    print("Coefficient used is : %f"  %(coeff))
    if len(path)==0:
        print("Failure")
    else:
        print("Successful")
        print("Total Number of nodes in the Sub_Optimal Path = %s"%(len(path)))
        Cost=len(path)
        for x in path:
            B1=np.array(x)
            pprint(B1)
        print("Total (Sub)Optimal Cost = %s"%(Cost))
    print("Total nodes explored : %s"%(node_count))
    print("Time taken : %s"%(time_taken))



if __name__ == "__main__":
    a,b,Temperature=data()
    start=Node(a)
    goal =Node(b)
    print("Start State")
    print(start)
    print("Goal State")
    print(goal)
    '''Coefficient'''
    coeff=0.97
    cooler=cooling_function(Temperature,coeff)
    print("Initital Temperature",Temperature)
    '''Misplaced Tiles'''
    start_time=time.time()
    path,node_count=algorithm(start,goal,misplaced,deepcopy(cooler))
    time_taken=time.time()-start_time
    '''Manhattan'''
    start_time1=time.time()
    path1,node_count1=algorithm(start,goal,manhatten,deepcopy(cooler))
    time_taken1=time.time()-start_time1
    '''Misplaced Tiles (Blank Space as Tile)'''
    start_time2=time.time()
    path2,node_count2=algorithm(start,goal,misplaced1,deepcopy(cooler))
    time_taken2=time.time()-start_time2
    '''Manhattan Distance (Blank Space as Tile)'''
    start_time3=time.time()
    path3,node_count3=algorithm(start,goal,manhatten1,deepcopy(cooler))
    time_taken3=time.time()-start_time3
    '''Hybrid Heuristic'''
    start_time4=time.time()
    path4,node_count4=algorithm(start,goal,hybrid,deepcopy(cooler))
    time_taken4=time.time()-start_time4

    print_node(coeff,goal,path,node_count,time_taken,"Misplaced Tiles")
    print_node(coeff,goal,path1,node_count1,time_taken1,"Manhatten Distance")
    print_node(coeff,goal,path2,node_count2,time_taken2,"Misplaced Tiles (Blank Space as Tile)")
    print_node(coeff,goal,path3,node_count3,time_taken3,"Manhattan Distance (Blank Space as Tile)")
    print_node(coeff,goal,path4,node_count4,time_taken4,"Hybrid Heuristic H3")
