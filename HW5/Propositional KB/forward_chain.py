#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:04:35 2019
The file includes:
- forward chain method

@author: frank
"""

# forward chain KB search process

from Propositional_KB_agent import *

def forwardchain(KB,theorem):
    #print(KB.FB)
    for consequent in KB.RB:
        if consequent.then_part in KB.FB:
            continue
        else:
            if set(KB.FB)>set(consequent.cond_part):
                antecedent = ",".join(consequent.cond_part)
                print("The new added rule is {}. The antecedent part is {}. The consequent part is {}.".format(consequent.name,antecedent,consequent.then_part))
                KB.add_fact(consequent.then_part)
            if theorem in KB.FB:
                print("Theorem {} is successfully proved!".format(theorem))
                return True
    print("Theorem {} prove failed!".format(theorem))
    return False

KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem1))
forwardchain(KBase,theorem1)
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)
print('\n')

KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem2))
forwardchain(KBase,theorem2)
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)
print('\n')


KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem3))
forwardchain(KBase,theorem3)
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)
print('\n')

KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem4))
forwardchain(KBase,theorem4)
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)
print('\n')

KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem5))
forwardchain(KBase,theorem5)
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)
print('\n')