#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
implementation of the evaluation function driven search
@author: Frank Lu
"""

from Puzzle8 import *


#### ++++++++++++++++++++++++++++++++++++++++++++++++++++
#### evaluation function driven search


def eval_function_driven_search(problem):
    queue = Priority_Queue()
    all_nodes = []          #all generated nodes
    nodes_expanded = []     #all expanded nodes
    max_queue_len = 0       #maximum queue length
    root = TreeNode(problem, problem.initial_state)
    queue.add_to_queue(root)
    max_queue_len = max(max_queue_len, len(queue.queue))
    while (queue.is_empty() == False):
        next = queue.pop_queue()
        if next.goalp():
            del (queue)

            ####calculate the final statistics
            generated_nodes = len(all_nodes)+1
            expanded_nodes = len(nodes_expanded)
            len_sol_path = len(next.path())-1

            #### return the path and statistics
            return [next.path(),generated_nodes,expanded_nodes,max_queue_len,len_sol_path]
        else:
            nodes_expanded.append(next)
            new_nodes = next.generate_new_tree_nodes()
            for new_node in new_nodes:
                queue.add_to_queue(new_node)
                all_nodes.append(new_node.state)
            max_queue_len = max(max_queue_len, len(queue.queue))
    print('No solution')
    return NULL


problem = Puzzle8_Problem(Example1)
output = eval_function_driven_search(problem)
print('Solution:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])

problem = Puzzle8_Problem(Example2)
output = eval_function_driven_search(problem)
print('Solution:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])

problem = Puzzle8_Problem(Example3)
output = eval_function_driven_search(problem)
print('Solution:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])
