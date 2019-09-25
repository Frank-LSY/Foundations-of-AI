#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 11:15:16 2019
Traveling Salesman Problem (TSP) problem

@author: Milos Hauskrecht (milos)
"""

import random
import math

class TSP_Problem:
    
    Cities=[]
    NumCities=0
    
    
    def __init__(self, Cities):
        self.Cities=Cities
        self.NumCities=len(self.Cities)
    
    # generates a random tour
    def generate_random_tour(self):
        return [0] + random.sample(range(1,self.NumCities),self.NumCities-1)

    # generates a new tour using a local permutation of a tour
    # this local permutation is also used to implement mutate op if used in the GA            
    def permute_tour(self, tour):
        end_points=random.sample(range(self.NumCities),2)
#        print(end_points)
        if (end_points[0]< end_points[1]):
            new_tour=tour[0:end_points[0]+1]+ list(reversed(tour[end_points[0]+1: end_points[1]]))+tour[end_points[1]:self.NumCities]
        else:
            auxtour=tour+tour
            #print('Aux tour {}'.format(auxtour))
            end_points[1]=end_points[1]+self.NumCities
            newa_tour=auxtour[end_points[0]:end_points[0]+1]+ list(reversed(auxtour[end_points[0]+1: end_points[1]])) + auxtour[end_points[1]:end_points[0]+self.NumCities]
            #print("Intermediate step {}".format(newa_tour))
            j=newa_tour.index(0)
            new_tour=newa_tour[j:]+newa_tour[0:j]
        return new_tour
    
    # defines crossover of the two tours for use in the GA
    # generates two new tours
    def crossover_tours(self,tour1,tour2):
        child1 = []
        child2=[]
        tour1aux=tour1+tour1
        tour2aux=tour2+tour2
        end_points=random.sample(range(self.NumCities),2)
#        print(end_points)
        if (end_points[0]> end_points[1]):
            end_points[1]=end_points[1]+self.NumCities
        #generate the first child
        childP1 = []
        childP2 = []
        for i in range(end_points[0], end_points[1]):
            childP1.append(tour1aux[i])
        childP2 = [item for item in tour2aux[end_points[0]:end_points[0]+self.NumCities] if item not in childP1]
        child1 = childP1 + childP2
        j=child1.index(0)
        child1=child1[j:]+child1[0:j]
        # generate the second child
        childP1 = []
        childP2 = []
        for i in range(end_points[0], end_points[1]):
            childP1.append(tour2aux[i])
        childP2 = [item for item in tour1aux[end_points[0]:end_points[0]+self.NumCities] if item not in childP1]
        child2 = childP1 + childP2
        j=child2.index(0)
        child2=child2[j:]+child2[0:j]    
        return [child1,child2]
    # evaluates the quality of a tour
    def evaluate_tour(self,tour):
        #print(tour)
        res=0
        for i in range(self.NumCities-1):
            res+=self.TSP_Distance(self.Cities[tour[i]],self.Cities[tour[i+1]])
        return res+self.TSP_Distance(self.Cities[tour[self.NumCities-1]],self.Cities[tour[0]])
    # calculates a TSP distance in between two cities (currently uses Manhattan distance)
    def TSP_Distance(self,coord1,coord2):
        ## implements Manhattan distance
        res=0
        for i in range(len(coord1)):
            res+=abs(coord1[i]-coord2[i])
        return res

# a list of Cities (their coordinates) to use in the assignment    
Standard_Cities= [
        (7.630520, 3.549164),
        (4.839835, 0.822996),
        (5.043007, 4.991792),
        (2.801917, 2.749705),
        (4.379292, 4.651019),
        (7.828340, 0.882077),
        (2.630909, 6.329537),
        (3.123377, 0.307382),
        (2.813100, 7.403270),
        (5.180621, 5.032747),
        (3.132675, 6.776844),
        (1.100392, 3.105084),
        (6.328253, 6.868632),
        (0.672972, 6.346699),
        (6.531493, 5.135151),
        (3.731491, 1.377488),
        (6.641961, 4.448046),
        (5.286243, 2.896708),
        (3.855679, 2.528306),
        (3.100002, 7.835636),
        (4.750185, 4.513944),
        (4.056279, 6.779125),
        (3.670612, 7.973412),
        (2.040161, 2.187459),
        (7.068120, 6.700557),
        (2.524146, 2.151348),
        (7.010522, 6.929094),
        (5.296346, 1.146134),
        (1.457847, 3.339806),
        (2.360706, 0.967076),
        (6.785015, 5.049559),
        (1.088368, 6.888971),
        (7.200540, 1.790072),
        (3.828022, 2.041351),
        (3.890284, 1.638676),
        (3.579832, 6.441091),
        (3.656363, 2.923428),
        (6.521193, 7.968213),
        (6.703210, 6.748472),
        (6.469462, 2.326698),
        (3.701814, 5.000961),
        (1.835885, 5.525316),
        (7.569855, 5.431781),
        (2.030067, 3.869593),
        (2.508856, 3.872015),
        (6.101347, 2.566932),
        (5.761558, 5.247081),
        (1.150817, 0.320061),
        (3.387590, 5.463640),
        (1.617236, 7.775387),
        (4.250819, 0.155697),
        (0.137775, 1.977584),
        (5.673515, 6.554512),
        (7.921431, 0.129109),
        (2.177936, 4.165043),
        (4.741635, 5.255069),
        (2.445578, 2.280457),
        (1.188459, 3.094138),
        (2.037981, 6.401203),
        (3.903425, 5.620263),    
        ]