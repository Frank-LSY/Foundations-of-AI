#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:32:46 2019

@author: Frank Lu
"""

# a heuristic function for the 'current' state and the target state
# currently manhattan distance heuristic
def h_function(state,target_state):
    manhattan  = {1:[0,1,2,1,2,3,2,3,4],  ##the manhatan distance matrix
                  2:[1,0,1,2,1,2,3,2,3],
                  3:[2,1,0,3,2,1,4,3,2],
                  4:[1,2,3,0,1,2,1,2,3],
                  5:[2,1,2,1,0,1,2,1,2],
                  6:[3,2,1,2,1,0,3,2,1],
                  7:[2,3,4,1,2,3,0,1,2],
                  8:[3,2,3,2,1,2,1,0,1],
                  9:[4,3,2,3,2,1,2,1,0]}
    heuristic = 0

    for i in range(len(state)):
        for j in range(len(target_state)):
            if state[i] == target_state[j]:
                heuristic += manhattan[j+1][i]  ##calculate the sum of manhattan distance
                break
    # print(state)
    # print(target_state)
    # print(heuristic)
    return heuristic