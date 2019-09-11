#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
vanilla breadth first search
- relies on  Puzzle8.py module

@author: Milos Hauskrecht (milos)
"""

from Puzzle8 import *


 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### breadth first search

def breadth_first_search(problem):
     queue =deque([])
     root=TreeNode(problem,problem.initial_state)
     queue.append(root)   
     while len(queue)>0:
         next=queue.popleft()
         if next.goalp():
             del(queue)
             return next.path()
         else:
             new_nodes=next.generate_new_tree_nodes()
             for new_node in new_nodes:
                  queue.append(new_node)         
     print('No solution')
     return NULL

  
problem=Puzzle8_Problem(Example1) 
output=  breadth_first_search(problem)
print('Solution Example 1:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example2) 
output=  breadth_first_search(problem)
print('Solution Example 2:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example3) 
output=  breadth_first_search(problem)
print('Solution Example 3:')
print_path(output)

wait = input("PRESS ENTER TO CONTINUE.")

problem=Puzzle8_Problem(Example4) 
output=  breadth_first_search(problem)
print('Solution Example 4:')
print_path(output)

# Solution to Example 5 may take too long to calculate using vanilla bfs
# problem=Puzzle8_Problem(Example5) 
# output=  breadth_first_search(problem)
# print('Solution Example 5:')
# print_path(output)
