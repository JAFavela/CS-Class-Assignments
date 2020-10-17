"""
@course:            CS 2302 Data Structures
@author:            Jorge A Favela
@assignment:        Lab 6 
@instructor:        Dr. Olac Fuentes
Last Modified:      Mon Apr 27 22:52:40 2020
Purpose of program: Find the most influential vertex(person) from a graph of facebook relationships
"""
import numpy as np
import matplotlib.pyplot as plt
import math
import graph_AL as graphAL
import graph_AM as graphAM
import hash_table_chain as htc
import random as r
from timeit import default_timer as timer

filename = 'facebook_combined.txt'

def file2Edges(): # Reads text file to a list of edges
    edges=[]
    with open(filename) as fc:
        for i in fc.read().split('\n'):
            edges.append([int(i.split(' ')[0]),int(i.split(' ')[1])])
    return edges

def numVert(edgeLst): # Returns the total number of verticies in the graph
    h=htc.HashTableChain(len(edgeLst)*2)
    cnt=0
    for i in edgeLst:
        for j in i:
            if h.insert(j,j)==1:
                cnt+=1
    return cnt

def out_degrees(G): # Computes a list of out degrees for each vertex
    L = [0 for i in range(G.am.shape[0])]
    for src in range(len(G.am)):
        for dst in range(len(G.am)):
            if G.am[src,dst] !=-1:
                L[src]+=1
    return L

def adjGraph(edgeLst): # Creates an adjacency list graph given a list of edges
    adG=graphAL.Graph(numVert(edgeLst))
    for i in edgeLst:
       adG.insert_edge(i[0],i[1])
    return adG

def mtxGraph(edgeLst): # Creates an adjacency matrix graph given a list of edges
    maG=graphAM.Graph(numVert(edgeLst))
    for i in edgeLst:
        maG.insert_edge(i[0],i[1])
    return maG

def randomWalk(adG,steps): # Implements the random walk algorithm
    V=adG.al
    v=r.randint(0,len(V)) # Chooses a random vertex in graph V
    visited= [0 for i in range(len(V))] # List keeps track of how many times each vertex was visited
    for i in range(steps):
        visited[v]+=1
        N=V[v] # N is the set of neighbors of v
        if len(N)==0:
            v=r.randint(0,len(V))
        else:
            v=(r.choice(N)).dest      
    p=[i/steps for i in visited] # p is a list of probabilities that each vertex will be visited at any given time
    return p    

def iterative(maG): # Implements the iterative computation algorithm
    vFrac=1/maG.am.shape[0]
    p=np.full(maG.am.shape[0],vFrac) # p is a 1D array where p[0]=p[1]=...=p[|V|-1] = 1/|V|
    T=np.zeros(maG.am.shape) # T is the transition matrix, where T[i,j] is the probability of going from vertex i to vertex j
    oD=(out_degrees(maG))
    for i in range(len(maG.am)):
        if oD[i]==0:
            T[i,:]=vFrac
        else:
            for j in range(maG.am.shape[0]):
                if maG.am[i,j]==-1:
                    T[i,j]== 0
                else:
                    T[i,j]=1/oD[i]
    for i in range(1000): # Process is repeated until convergence is reached
        p=np.dot(p,T)
    return p
  
def vImp(p): # Identifies the most important vertex given p
    high=0
    indx=0
    for i in range(len(p)):
        if p[i]>high:
            high=p[i]
            indx=i
    return indx,high
    
if __name__ == "__main__":   
    edges=file2Edges()
    adG=adjGraph(edges)
    maG=mtxGraph(edges)

    print('Using random walk method (100,000 steps) and adjacency list representation:')
    for i in range(1,11):
        p=randomWalk(adG,100000)
        Vimp,pVal=vImp(p)
        print('Iteration',i,'most important vertex:',Vimp,', with p =',pVal)
        for i in range(maG.am.shape[0]):
            for j in adG.al[i]:
                if j.dest==Vimp:
                    adG.delete_edge(i,j.dest)
    print()
    print('Using iterative method and adjacency matrix representation:')
    for i in range(1,11):
        p=iterative(maG)
        Vimp,pVal=vImp(p)
        print('Iteration',i,'most important vertex:',Vimp,', with p =',pVal.round(5))
        for i in range(maG.am.shape[0]):
            for j in range(maG.am.shape[1]):
                if i==Vimp:
                    if maG.am[i,j]==1:
                        maG.delete_edge(i,j)
                if j==Vimp:
                    if maG.am[i,j]==1:
                        maG.delete_edge(i,j)
                        
