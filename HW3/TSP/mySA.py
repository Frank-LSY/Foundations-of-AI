#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 15:24:16 2019
Simulated annealingg Algorithm for the TSP

@author: Shuyu Lu (Frank)
"""
from TSP import TSP_Problem, Standard_Cities
import math
import random
import matplotlib.pyplot as plt
from SA import *




problem = TSP_Problem(Standard_Cities)

best_distance = []
steps = 20000  # the initial steps
i = 0
while i<10:

    temperature = 100
    output = sim_anneal(problem,steps,temperature)
    #print(output[3])
    if output[3]<20000:
        #print(steps)
        steps = steps + 500
        continue
    else:
        print("Initial tour:")
        print(output[0])
        print("Initial tour distance: {}".format(output[1]))
        print("Initial temprature: {}".format(temperature))
        print("Number of tours tried: {}".format(output[2]))
        print("Number of tours accepted: {}".format(output[3]))
        print("The best tour found:")
        print(output[4])
        print("The best tour found distance: {}".format(output[5]))
        best_distance.append(output[5])
        i += 1
mean = 0
for item in best_distance:
    mean += item
mean = mean/len(best_distance)

print(mean)