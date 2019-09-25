# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:48:15 2019

Genetic Algorithm for the TSP 

@authors: Shuyu Lu (Frank)
"""

from TSP import TSP_Problem, Standard_Cities
from population import Population
import random
import os
import matplotlib.pyplot as plt
import numpy as np

#default parameters
N_POP = 500 # population size
MAX_ITERATIONS = NUM_GENERATIONS = 500 #number of generations to run
MUTATION_PROB = 0.05 #probability of an individual being mutated
CULLING_PERC = 0.05 #percentage of the least fit individuals to be removed
ELITE_PERC = 0.05 #proportion of best individuals to carry over from one generation to the next
OUT_DIR0 = 'fig1/' #directory where to place the plots (it will be automatically created if not existent)


#initialize the TSP problem


#
# #generate initial population
#
# #store average and min fitess values for the current population
    
# simulate for the MAX_ITERATION number of generations
def genetic_algorithm(population, num_generations, culling_perc, elite_perc, mutation_prob):
    #store generation-specific stats information
    fitness_vals = []
    min_fitness_vals = []
    pop_size = []

    for curr_iter in range(num_generations):

        # create a new population
        population = population.build_a_new_generation(CULLING_PERC=culling_perc, ELITE_PERC=elite_perc,
                                                       M_RATE=mutation_prob)

        # store stats for the current population
        fitness_vals.append(population.mean_fitness())
        best_fitness = population.min_fitness()
        min_fitness_vals.append(best_fitness)
        pop_size.append(len(population))

        # print stats for every 50th population
        if curr_iter % 50 == 0:
            print('Iteration [{}] of [{}] ({:.2f}%) -- Best solution: cost = [{:.2f}] -- Population size [{}]'.format(
                curr_iter, num_generations, curr_iter * 100 / num_generations, best_fitness, len(population)))

    best_solution = population.get_best_individual()
    print("Best solution found has cost [{:.2f}]\n{}".format(best_solution.fitness, best_solution.tour))

    return [best_solution, fitness_vals, min_fitness_vals]

def plot_result(fitness_vals, min_fitness_vals,n_pop, num_generations, mutation_porb, culling_perc, elite_perc,out_dir):
    plt.cla()
    plt.plot(list(range(len(output[1]))), fitness_vals, label='Avg')
    plt.plot(list(range(len(output[1]))), min_fitness_vals, label='Min')
    plt.xlabel('Generations')
    plt.ylabel('Cost (opposite trend of fitness)')
    pars_as_str_title = 'N_pop = {}, p_mut = {:.2f}, p_cull={:.2f}, p_elite={:.2f}'.format(n_pop, mutation_porb,
                                                                                           culling_perc, elite_perc)
    plt.title('Evolution [{}]'.format(pars_as_str_title))
    plt.legend()
    pars_as_str_file = 'N_gen_{}_N_pop_{}_p_mut_{:02d}_p_cull_{:02d}_p_elite_{:02}'.format(num_generations,n_pop, int(mutation_porb * 100),
                                                                                  int(culling_perc * 100),
                                                                                  int(elite_perc * 100))
    plt.savefig(out_dir + 'evolution_{}.png'.format(pars_as_str_file))

    return

#generate initial population
problem=TSP_Problem(Standard_Cities)


#create output directory if not present
#generations
OUT_DIR = OUT_DIR0+"NUM_GENERATIONS/"
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)
for num_generations in range(200,1001,100):
    population = Population(problem, N_POP=N_POP)
    print("Number of Generations: {}".format(num_generations))
    output = genetic_algorithm(population, num_generations, CULLING_PERC, ELITE_PERC, MUTATION_PROB)
    # plot results
    plot_result(output[1],output[2],N_POP, num_generations, MUTATION_PROB, CULLING_PERC, ELITE_PERC, OUT_DIR)

#create output directory if not present
#populations
OUT_DIR = OUT_DIR0+"POP/"
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)
for n_pop in range(250,751,50):
    population = Population(problem, N_POP=n_pop)
    print("Population: {}".format(n_pop))
    output = genetic_algorithm(population, NUM_GENERATIONS, CULLING_PERC, ELITE_PERC, MUTATION_PROB)
    # plot results
    plot_result(output[1],output[2],n_pop,NUM_GENERATIONS, MUTATION_PROB, CULLING_PERC, ELITE_PERC, OUT_DIR)

#create output directory if not present
#mutation probability
OUT_DIR = OUT_DIR0+"MUTATION_PROB/"
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)
for mutation_prob in np.arange(0.00,0.30,0.05):
    population = Population(problem, N_POP=N_POP)
    print("Mutation probability: {}".format(mutation_prob))
    output = genetic_algorithm(population, NUM_GENERATIONS, CULLING_PERC, ELITE_PERC, mutation_prob)
    # plot results
    plot_result(output[1],output[2],N_POP, NUM_GENERATIONS,mutation_prob, CULLING_PERC, ELITE_PERC,OUT_DIR)

#create output directory if not present
#culling percentage
OUT_DIR = OUT_DIR0+"CULLING_PERC/"
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)
for culling_perc in np.arange(0.00,0.30,0.05):
    population = Population(problem, N_POP=N_POP)
    print("Culling oercentage: {}".format(culling_perc))
    output = genetic_algorithm(population, NUM_GENERATIONS, culling_perc, ELITE_PERC, MUTATION_PROB)
    # plot results
    plot_result(output[1],output[2],N_POP, NUM_GENERATIONS, MUTATION_PROB, culling_perc, ELITE_PERC, OUT_DIR)

#create output directory if not present
#elite percentage
OUT_DIR = OUT_DIR0+"ELITE_PERC/"
if not os.path.isdir(OUT_DIR):
    os.mkdir(OUT_DIR)
for elite_perc in np.arange(0.00,0.30,0.05):
    population = Population(problem, N_POP=N_POP)
    print("Elite percentage: {}".format(elite_perc))
    output = genetic_algorithm(population, NUM_GENERATIONS, CULLING_PERC, elite_perc, MUTATION_PROB)
    # plot results
    plot_result(output[1],output[2],N_POP, NUM_GENERATIONS, MUTATION_PROB, CULLING_PERC, elite_perc, OUT_DIR)