# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 12:52:19 2019

Population class for GA algorithm

@authors: Milos Hauskrecht and Giacomo Nebbia
"""

import random
import math
# from selection_probability import scores_to_probabilities

def scores_to_probabilities(fitness_list):
    """uses Boltzman distribution to calculate the probabilities"""
    min_fitness = min(fitness_list)
    temperature = max(fitness_list) - min_fitness
    if (temperature == 0):
        temperature = 0.0001  
    scores = [math.exp(-(fit - min_fitness)/temperature) for fit in fitness_list]    
    sum_scores = sum(scores)   
    return [score / sum_scores for score in scores]

def random_pick_from_the_distribution(distribution):
    sample =  random.random()
    cumsum=0
    for i in range(len(distribution)):
        cumsum+=distribution[i]
        if sample <= cumsum:
            return i
    return -1

def compare_individual(individual):
    return individual.fitness

class Individual():
    """This class represents a population's individual"""
    
    def __init__(self, tour, fitness):
        self.tour = tour
        self.fitness = fitness

class Population():
    """This class represents a population of individuals"""
    
    def __init__(self, problem, individuals = [], N_POP = 100):
        
        self.problem = problem
        if len(individuals) == 0:
            individuals = [problem.generate_random_tour() for _ in range(N_POP)]
            
        fitness = self.compute_fitness(individuals)        
        self.individuals = [Individual(tour, fit) for tour, fit in zip(individuals, fitness)]
        
    def __len__(self):
        return len(self.individuals)
        
    def compute_fitness(self, individuals):
        #fitness is the cost of the current individual (which is a tour in the TSP)
        return [self.problem.evaluate_tour(individual) for individual in individuals]

    def get_best_individual(self):      
        return min(self.individuals, key = compare_individual)

    
    ## returns top scored tours
    def elite_selection(self,elite_perc):
        n_elite = int(len(self) * elite_perc)
        sorted_individuals = sorted(self.individuals, key = compare_individual) 
        return [ind.tour for ind in sorted_individuals[:n_elite]]
    
    ## returns a subpopulation of individuals from the whole population 
    ## that will be considerd for reproduction by eliminating the weakest tours
    def culling(self,culling_perc):
        n_culling = int(len(self) * culling_perc)
        sorted_individuals = sorted(self.individuals, key = compare_individual, reverse = True)
        return sorted_individuals[n_culling:]
 
    # calculates population stats: average score
    def mean_fitness(self):
        return sum([ind.fitness for ind in self.individuals]) / len(self)

    # calculates population statsL the best score     
    def min_fitness(self):
        return min(self.individuals, key = compare_individual).fitness    

 
    ## returns  a new generation of the same size as the current population
    def build_a_new_generation(self, CULLING_PERC = 0.05, ELITE_PERC = 0.05, M_RATE=0.05, TWO_CHILDREN=True): 
        
        pop_size=len(self.individuals)
        
        # elite selection: move the best to the new population
        new_generation = self.elite_selection(ELITE_PERC)
        
        # culling: cut the least fit individuals
        individuals = self.culling(CULLING_PERC)
        
        # calculate probabilities for being selected to a crossover
        probabilities = scores_to_probabilities([ind.fitness for ind in individuals])
        ### fill the rest of the population with children generated via crossover
        while len(new_generation) < pop_size:
            
            #randomly pick two individuals that will reproduce
            # pick first 
            idx_x = random_pick_from_the_distribution(probabilities)
            # now pick the second one but assure it is not the same individual
            idx_y = idx_x
            resample_count = 0
            while(idx_y == idx_x):
               #this is to avoid that the same individual is sampled twice in the pair
               idx_y = random_pick_from_the_distribution(probabilities)
               resample_count += 1
               if resample_count == 10:
                  idx_y = idx_x + 1
                  if idx_x == (len(individuals) -1):
                      idx_y = idx_x - 1
                      
            # perform cross-over
            children = self.problem.crossover_tours(individuals[idx_x].tour, individuals[idx_y].tour)
            if TWO_CHILDREN:
                new_generation+=children
            else:
                new_generation.append(children[0])
        # if we use two children we can have one too many so reduce population by 1 
        if len(new_generation) > pop_size:
            new_generation=new_generation[:pop_size]
        
        # now apply muation
        mutation_indexes=random.sample(range(pop_size),int(pop_size*M_RATE))
        for ind in mutation_indexes:
            new_generation[ind]=self.problem.permute_tour(new_generation[ind])
        
        # create new population and return it
        new_population=Population(self.problem,individuals=new_generation)
        return new_population
    