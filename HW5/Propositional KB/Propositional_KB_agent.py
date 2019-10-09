#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:04:35 2019
The file includes:
- KB class and Rule class definitions
- Rules, facts and theorems for the animal identification problem

@author: milos
"""

# Knowledge base (KB) definition
# It consists of: (1) a rule base (or RB) and (2) a facts base (or FB)
# A rule base consists of a list of rules
# A fact base consists of a list of facts/propositions known to be true

class KB:
    RB=[]
    FB=[]
    
    # initializes the KB with a list of rules and a list of facts (if given)
    def __init__(self,init_RB=[],init_FB=[]):
        self.RB=init_RB
        self.FB=init_FB.copy()
        
    # clears the FB and initializes it with init_FB
    def reset_FB(self,init_FB=[]):
        self.FB=init_FB.copy()
        
    # adds a rule to RB    
    def add_rule(self, rule):
        self.RB.append(rule)
 
    # adds a fact to FB   
    def add_fact(self,fact):
        self.FB.append(fact)
   
    # checks if a fact is in FB
    def is_in_FB(self,fact):
        if fact in self.FB:
            return True
        else:
            return False
    
    # prints rule base    
    def print_RB(self):
        for rule in KBase.RB:
            print(rule.name)
            print('If:', rule.cond_part)
            print('Then:', rule.then_part)
            print(' ')
    
    #prints fact base       
    def print_FB(self):
        for fact in KBase.FB:
            print(fact)
        
                
# a rule has a name and is defined by its condition and then parts
class Rule:
    name=''
    cond_part=[]
    then_part=''
    def __init__(self,rname,condpart,thenpart):
       self.name=rname
       self.cond_part=condpart
       self.then_part=thenpart
       

# *******************************************************************
# now we define the animal identification problem to experiment with
# *******************************************************************       

# rules for the animal identification problem        
init_RB=[]
init_RB.append(Rule('R1',['has_hair'],'is_a_mammal'))
init_RB.append(Rule('R2',['gives_milk'],'is_a_mammal'))
init_RB.append(Rule('R3',['has_feathers'],'is_a_bird')) 
init_RB.append(Rule('R4',['flies','lays_eggs'],'is_a_bird')) 
init_RB.append(Rule('R5',['is_a_mammal','eats_meat'],'is_a_carnivore')) 
init_RB.append(Rule('R6',['is_a_mammal','has_pointed_teeth','has_claws','the_animals_eyes_point_forward'],'is_a_carnivore'))
init_RB.append(Rule('R7',['is_a_mammal','has_hoofs'],'is_an_ungulate'))
init_RB.append(Rule('R8',['is_a_mammal','chews_cud'],'is_an_ungulate'))
init_RB.append(Rule('R9',['is_a_mammal','chews_cud'],'is_even-toed'))
init_RB.append(Rule('R10',['is_a_carnivore','has_a_tawny_color','has_dark_spots'],'is_a_cheetah'))
init_RB.append(Rule('R11',['is_a_carnivore', 'has_a_tawny_color', 'has_black_stripes'],'is_a_tiger'))
init_RB.append(Rule('R12',['is_an_ungulate','has_long_legs','has_a_long_neck','has_a_tawny_color','has_dark_spots'],'is_a_giraffe'))
init_RB.append(Rule('R13',['is_an_ungulate', 'has_a_white_color','has_black_stripes'],'is_a_zebra'))
init_RB.append(Rule('R14',['is_a_bird','does_not_fly','has_long_legs','has_a_long_neck','is_black_and_white'],'is_an_ostrich'))
init_RB.append(Rule('R15',['is_a_bird','does_not_fly','swims','is_black_and_white'],'is_a_penguin'))
init_RB.append(Rule('R16',['is_a_bird','is_a_good_flyer'],'is_an_albatross'))

# facts/propositions known to be true for the animal we want to identify
init_FB=['gives_milk','chews_cud','has_long_legs','has_a_long_neck','has_a_tawny_color','has_dark_spots']

KBase=KB(init_RB,init_FB)

# here are theorems to prove
theorem1='is_a_giraffe'
theorem2='is_a_penguin'
theorem3='is_a_mammal'
theorem4='has_a_tawny_color'
theorem5='is_a_bird'