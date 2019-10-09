#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 22:04:35 2019
The file includes:
- backward chain method 

@author: frank
"""

# backward chain KB search process

from Propositional_KB_agent import *

theorem_path = []
theorem_need_prove = []

def check_cond_part(conditions,KB,theorem):
    for cond in conditions:
        if set(KB.FB)>set(cond):
            for consequent in KB.RB:
                if theorem==consequent.then_part and cond==consequent.cond_part:
                    print("Using rule {} prove {}: success!".format(consequent.name, theorem))
            # print(cond)
            return True
    else:
        return False

# def prove_path(theorem_path)

def backwardchain(KB,theorem):
    # print(count)

    theorem_path.append(theorem)
    if theorem not in theorem_need_prove:
        theorem_need_prove.append(theorem)
    # print("theorem_path: ")
    # print(theorem_path)
    # print("theorem need to prove:")
    # print(theorem_need_prove)
    conditions=[]
    new_theorems=[]
    # print(theorem)
    if theorem in KB.FB:
        print("The theorem is in the FB!")
        return  True
    else:
        for consequent in KB.RB:
            if theorem==consequent.then_part:
                # print("Add rule {} to sequence of theorem: {}.".format(consequent.name,theorem))
                conditions.append(consequent.cond_part)
        # print(conditions)
        if conditions==[]:
            # print("Can't prove the theorem: {}!".format(theorem))
            for consequent in KB.RB:
                if theorem in consequent.cond_part:
                    print("Using rule {} prove {}: failed!".format(consequent.name,consequent.then_part))
            theorem_need_prove.remove(theorem)
            return False

        else:
            if check_cond_part(conditions,KB,theorem):
                KB.add_fact(theorem)
                # print(count)
                print("Theorem {} is Proved!".format(theorem))
                theorem_need_prove.remove(theorem)
                if len(theorem_need_prove)>0:
                    backwardchain(KB,theorem_need_prove[len(theorem_need_prove)-1])
                    return True
            else:
                for cond in conditions:
                    new_theorems += (list(set(cond).difference(set(KB.FB))))
                    new_theorems=list(set(new_theorems))
                    # print(new_theorems)
                    for theorem_to_prove in new_theorems:
                        if backwardchain(KB,theorem_to_prove):
                            return True
                    # else:
                    #     continue
                    # break



KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem1))
if backwardchain(KBase, theorem1):
    print("\nThe initial theorem: {} is proved!\n".format(theorem1))
else:
    print("\nWe can't prove the initial theorem: {}!\n".format(theorem1))
new_theorem_path = list(set(theorem_path))
new_theorem_path.sort(key=theorem_path.index)
print("All the theorem trying to prove: ")
for theo in new_theorem_path:
    print(theo)
theorem_path.clear()
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)

input("Press Enter to continue.")
print('\n')


KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem2))
if backwardchain(KBase, theorem2):
    print("\nThe initial theorem: {} proved!\n".format(theorem2))
else:
    print("\nWe can't prove the initial theorem: {}!\n".format(theorem2))

new_theorem_path = list(set(theorem_path))
new_theorem_path.sort(key=theorem_path.index)
print("All the theorem trying to prove: ")
for theo in new_theorem_path:
    print(theo)
theorem_path.clear()
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)

input("Press Enter to continue.")
print('\n')


KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem3))
if backwardchain(KBase, theorem3):
    print("\nThe initial theorem: {} proved!\n".format(theorem3))
else:
    print("\nWe can't prove the initial theorem: {}!\n".format(theorem3))

new_theorem_path = list(set(theorem_path))
new_theorem_path.sort(key=theorem_path.index)
print("All the theorem trying to prove: ")
for theo in new_theorem_path:
    print(theo)
theorem_path.clear()
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)


input("Press Enter to continue.")
print('\n')


KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem4))
if backwardchain(KBase, theorem4):
    print("\nThe initial theorem: {} proved!\n".format(theorem4))
else:
    print("\nWe can't prove the initial theorem: {}!\n".format(theorem4))

new_theorem_path = list(set(theorem_path))
new_theorem_path.sort(key=theorem_path.index)
print("All the theorem trying to prove: ")
for theo in new_theorem_path:
    print(theo)
theorem_path.clear()
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)
print('\n')

input("Press Enter to continue.")
print('\n')


KBase=KB(init_RB,init_FB)
print("Initial theorem to prove: {}".format(theorem5))
if backwardchain(KBase, theorem5):
    print("\nThe initial theorem: {} proved!\n".format(theorem5))
else:
    print("\nWe can't prove the initial theorem: {}\n!".format(theorem5))

new_theorem_path = list(set(theorem_path))
new_theorem_path.sort(key=theorem_path.index)
print("All the theorem trying to prove: ")
for theo in new_theorem_path:
    print(theo)
theorem_path.clear()
print("The fact base after the procedure: ")
for fact in KBase.FB:
    print(fact)
print('\n')