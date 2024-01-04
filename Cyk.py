# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 16:50:26 2021

@author: JimmyLpz
"""

non_terminals = ["S", "A", "B", "C"]
terminals = ["a","b"]
  
# Rules of the grammar
R = {
     "S": [["A","B",],["B","C"]],
     "A": [["B", "A"], ["a"]],
     "B": [["C", "C"], ["b"]],
     "C": [["A","B"],["a"]] 
    }


def cyk(w):
    n = len(w)
      
    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
  
    # Filling in the table
    for j in range(0, n):
  
        # Iterate over the rules
        for LR, rule in R.items():
            for RR in rule:
                  
                # If a terminal is found
                if len(RR) == 1 and \
                RR[0] == w[j]:
                    T[j][j].add(LR)
  
        for i in range(j, -1, -1):   
               
            # Iterate over the range i to j + 1   
            for k in range(i, j + 1):     
  
                # Iterate over the rules
                for LR, rule in R.items():
                    for RR in rule:
                          
                        # If a terminal is found
                        if len(RR) == 2 and \
                        RR[0] in T[i][k] and \
                        RR[1] in T[k][j]:
                            T[i][j].add(LR)
                            
  
   
    if len(T[0][n-1]) != 0:
        print("Aceptada")
    else:
        print("Rechazada")

w = "b a b".split()#we used the method split for converts string in
#other type of data lisk a list breaking in pieces.
print(w)  

cyk(w)