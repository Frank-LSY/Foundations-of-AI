#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:01:00 2019
breadth first search with the elimination of all state repeats
- relies on  Puzzle8.py module

@author: Shuyu Lu (Frank)
"""

from Puzzle8 import *


#### ++++++++++++++++++++++++++++++++++++++++++++++++++++
#### breadth first search

###check all the state of repeats
def check_state_repeats(node,node_hash):
    if node_hash.in_hashp(node.state):                      #check whether the node is in the hash table
        if node.g > node_hash.get_hash_value(node.state):   #compare the depth of the node and previous same node in has table
            return 1
        else:
            return 0
    else:
        return 0

def breadth_first_search_repeats(problem):
    queue = deque([])
    all_nodes = []          #all generated nodes
    nodes_expanded = []     #all expanded nodes
    max_queue_len = 0
    root = TreeNode(problem, problem.initial_state)
    node_hash = HashTable()         #use hash table to store repeats
    queue.append(root)
    max_queue_len = max(max_queue_len,len(queue))
    while len(queue) > 0:
        next = queue.popleft()

        if next.goalp():
            del (queue)
            del (node_hash)

            ####calculate the final statistics
            generated_nodes = len(all_nodes)+1
            expanded_nodes = len(nodes_expanded)
            len_sol_path = len(next.path())

            #### return the path and statistics in a list
            return [next.path(),generated_nodes,expanded_nodes,max_queue_len,len_sol_path]

        elif check_state_repeats(next,node_hash):    #check the repeat
            continue
        else:
            nodes_expanded.append(next)
            node_hash.add_hash(next.state,next.g)                  #add non-repeated node to hash table
            new_nodes = next.generate_new_tree_nodes()
            for new_node in new_nodes:
                queue.append(new_node)
                all_nodes.append(new_node.state)
            max_queue_len = max(max_queue_len, len(queue))
    print('No solution')
    return NULL


problem = Puzzle8_Problem(Example1)
output = breadth_first_search_repeats(problem)
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
output = breadth_first_search_repeats(problem)
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
output = breadth_first_search_repeats(problem)
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
output = breadth_first_search_repeats(problem)
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

####Solution to Example 5 may take too long to calculate using vanilla bfs
problem=Puzzle8_Problem(Example5)
output=  breadth_first_search_repeats(problem)
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