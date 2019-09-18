#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 18:32:46 2019

@author: Frank Lu
"""

# a heuristic function for the 'current' state and the target state
# currently returns misplaced tile heuristic
def h_function(state,target_state):
    heuristic = 0
    for i in range(len(state)):
        if state[i] != target_state[i]:
            heuristic += 1      ##calculate the sum of manhattan distance
    return heuristic