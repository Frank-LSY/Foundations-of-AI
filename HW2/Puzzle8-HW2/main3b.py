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

def check_state_repeats(node,node_hash):
    if node_hash.in_hashp(node.state):                      #check whether the node is in the hash table
        if node.g > node_hash.get_hash_value(node.state):   #compare the depth of the node and previous same node in has table
            return 1
        else:
            return 0
    else:
        return 0

def eval_function_driven_search_repeats(problem):
    queue = Priority_Queue()
    all_nodes = []          #all generated nodes
    nodes_expanded = []     #all expanded nodes
    max_queue_len = 0       #maximum queue length
    root = TreeNode(problem, problem.initial_state)
    node_hash = HashTable()         #use hash table to store repeats
    queue.add_to_queue(root)
    max_queue_len = max(max_queue_len, len(queue.queue))
    while (queue.is_empty() == False):
        next = queue.pop_queue()
        if next.goalp():
            del (queue)
            del (node_hash)

            ####calculate the final statistics
            generated_nodes = len(all_nodes)+1
            expanded_nodes = len(nodes_expanded)
            len_sol_path = len(next.path())-1

            #### return the path and statistics
            return [next.path(),generated_nodes,expanded_nodes,max_queue_len,len_sol_path]

        elif check_state_repeats(next, node_hash):  # check the repeat
            continue
        else:
            nodes_expanded.append(next)
            node_hash.add_hash(next.state,next.g)                  #add non-repeated node to hash table
            new_nodes = next.generate_new_tree_nodes()
            for new_node in new_nodes:
                #print(new_node.h)
                queue.add_to_queue(new_node)
                all_nodes.append(new_node.state)
            max_queue_len = max(max_queue_len, len(queue.queue))
    print('No solution')
    return NULL


problem = Puzzle8_Problem(Example1)
output = eval_function_driven_search_repeats(problem)
print('Solution Example 1:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])

wait = input("PRESS ENTER TO CONTINUE.")

problem = Puzzle8_Problem(Example2)
output = eval_function_driven_search_repeats(problem)
print('Solution Example 2:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])

wait = input("PRESS ENTER TO CONTINUE.")

problem = Puzzle8_Problem(Example3)
output = eval_function_driven_search_repeats(problem)
print('Solution Example 3:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])

wait = input("PRESS ENTER TO CONTINUE.")

problem = Puzzle8_Problem(Example4)
output = eval_function_driven_search_repeats(problem)
print('Solution Example 4:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])

wait = input("PRESS ENTER TO CONTINUE.")

problem = Puzzle8_Problem(Example5)
output = eval_function_driven_search_repeats(problem)
print('Solution Example 5:')
print_path(output[0])
print('Total nodes generated: ')
print(output[1])
print('Total nodes expanded: ')
print(output[2])
print('Maximum length of the queue: ')
print(output[3])
print('The length of the solution path: ')
print(output[4])