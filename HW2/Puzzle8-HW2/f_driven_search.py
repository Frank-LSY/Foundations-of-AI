#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
implementation of the evaluation function driven search
@author: milos
"""

from Puzzle8 import *

 #### ++++++++++++++++++++++++++++++++++++++++++++++++++++
 #### evaluation function driven search         
        
 
def eval_function_driven_search(problem):
     queue = Priority_Queue()
     root=TreeNode(problem,problem.initial_state)
     queue.add_to_queue(root)   
     while (queue.is_empty() == False):
         next=queue.pop_queue()
         if next.goalp():
             del(queue)
             return next.path()
         else:
             new_nodes=next.generate_new_tree_nodes()
             for new_node in new_nodes:
                  queue.add_to_queue(new_node)         
     print('No solution')
     return NULL
  
problem=Puzzle8_Problem(Example1) 
output=  eval_function_driven_search(problem)
print('Solution:')
print_path(output)

problem=Puzzle8_Problem(Example2) 
output=  eval_function_driven_search(problem)
print('Solution:')
print_path(output)

problem=Puzzle8_Problem(Example3) 
output=  eval_function_driven_search(problem)
print('Solution:')
print_path(output)
 