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

def cooling_strategy(init_temperature,no_of_steps,i):
    part_steps = 0.3 * no_of_steps
    half_temperature = init_temperature/2
    if i < part_steps:
        temperature = init_temperature - (half_temperature / part_steps ** 2) * (i ** 2)
        #print(temperature)
    else:
        temperature = (half_temperature / (part_steps - no_of_steps) ** 2) * (i - no_of_steps) ** 2
        #print(temperature)
    return temperature

def sim_anneal(TSP_problem,no_of_steps,init_temperature):
    init_tour = TSP_problem.generate_random_tour()
    init_distance = TSP_problem.evaluate_tour(init_tour)

    last_tour = init_tour
    last_tour_distance = init_distance
    tour_tried = 0
    tour_accepted = 0
    energy_atlas = []
    half_temperature = init_temperature/2
    part_steps = 0.3 * no_of_steps
    for i in range(no_of_steps):
        temperature = cooling_strategy(init_temperature,no_of_steps,i)
        tour = TSP_problem.permute_tour(last_tour)
        tour_tried += 1
        tour_distance = TSP_problem.evaluate_tour(tour)
        distance_changed = last_tour_distance-tour_distance
        #print(distance_changed)
        if distance_changed>0:
            probability = 1
            last_tour = tour
            last_tour_distance = tour_distance
            tour_accepted += 1
            energy_atlas.append(tour_distance)
        else:
            probability = math.exp(distance_changed/temperature)
            x = random.random()
            #print(x)
            if x>probability:
                continue
            else:
                last_tour = tour
                last_tour_distance = tour_distance
                tour_accepted += 1
                energy_atlas.append(tour_distance)

    return [init_tour,round(init_distance,6),tour_tried,tour_accepted,last_tour,round(last_tour_distance,6)]


def main():
    # try Simulated annealing algorithm
    problem = TSP_Problem(Standard_Cities)
    steps = 100000
    temperature = 100
    output = sim_anneal(problem,steps,temperature)
    print("Initial tour:")
    print(output[0])
    print("Initial tour distance: {}".format(output[1]))
    print("Initial temprature: {}".format(temperature))
    print("Number of tours tried: {}".format(output[2]))
    print("Number of tours accepted: {}".format(output[3]))
    print("The best tour found:")
    print(output[4])
    print("The best tour found distance: {}".format(output[5]))

if __name__ == "__main__":
    main()

#Simulated annealing algorithm with different steps and temperature tired
# steps_arr = [100000,200000,400000,800000,1600000]
# temperature_arr = [10000,1000,100,1,0.1]
# for steps in steps_arr:
#     for temperature in temperature_arr:
#         output = sim_anneal(problem,steps,temperature)
#         output = sim_anneal(problem, steps, temperature)
#         print("Steps:{}  Temperature:{}".format(steps,temperature))
#         print("Initial tour distance: {}".format(output[1]))
#         print("Number of tours tried: {}".format(output[2]))
#         print("Number of tours accepted: {}".format(output[3]))
#         print("The best tour found distance: {}".format(output[5]))