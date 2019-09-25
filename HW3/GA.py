# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:48:15 2019

Genetic Algorithm for the TSP 

@authors: Milos Hauskrecht and Giacomo Nebbia
"""

from TSP import TSP_Problem, Standard_Cities
from population import Population
import random
import os

#parameters
N_POP = 500 # population size
NUM_GENERATIONS = 500 #number of generations to run
MUTATION_PROB = 0.05 #probability of an individual being mutated
CULLING_PERC = 0.05 #percentage of the least fit individuals to be removed
ELITE_PERC = 0.05 #proportion of best individuals to carry over from one generation to the next
OUT_DIR = 'fig/' #directory where to place the plots (it will be automatically created if not existent)

#create output directory if not present
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)


#initialize the TSP problem
problem=TSP_Problem(Standard_Cities)


#store generation-specific stats information
fitness_vals = []
min_fitness_vals = []
pop_size = []

#generate initial population
population = Population(problem, N_POP = N_POP)

#store average and min fitess values for the current population
fitness_vals.append(population.mean_fitness())
min_fitness_vals.append(population.min_fitness())
pop_size.append(len(population))  
    
# simulate for the MAX_ITERATION number of generations
for curr_iter in range(NUM_GENERATIONS):
    
    # create a new population
    population = population.build_a_new_generation(CULLING_PERC= CULLING_PERC, ELITE_PERC = ELITE_PERC, M_RATE=MUTATION_PROB)
    
    #store stats for the current population
    fitness_vals.append(population.mean_fitness())
    best_fitness=population.min_fitness()
    min_fitness_vals.append(best_fitness)
    pop_size.append(len(population))
    
    # print stats for every 50th population
    if curr_iter % 50 == 0:
        print('Iteration [{}] of [{}] ({:.2f}%) -- Best solution: cost = [{:.2f}] -- Population size [{}]'.format(curr_iter, MAX_ITERATIONS, curr_iter * 100 / MAX_ITERATIONS, best_fitness, len(population)))   
    

best_solution = population.get_best_individual()
print("Best solution found has cost [{:.2f}]\n{}".format(best_solution.fitness, best_solution.tour))

 #plot results
import matplotlib.pyplot as plt
plt.plot(list(range(len(fitness_vals))), fitness_vals, label = 'Avg')
plt.plot(list(range(len(fitness_vals))), min_fitness_vals, label = 'Min')
plt.xlabel('Generations')
plt.ylabel('Cost (opposite trend of fitness)')
pars_as_str_title = 'N_pop = {}, p_mut = {:.2f}, p_cull={:.2f}, p_elite={:.2f}'.format(N_POP, MUTATION_PROB, CULLING_PERC, ELITE_PERC)
plt.title('Evolution [{}]'.format(pars_as_str_title))
plt.legend()
pars_as_str_file = 'N_pop_{}_p_mut_{:02d}_p_cull_{:02d}_p_elite_{:02}'.format(N_POP, int(MUTATION_PROB * 100), int(CULLING_PERC * 100), int(ELITE_PERC * 100))
plt.savefig(OUT_DIR + 'evolution_{}.png'.format(pars_as_str_file))
plt.show()
