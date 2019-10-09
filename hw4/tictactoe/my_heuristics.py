#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:47:03 2019

@author: milos
"""

from heuristics import Heuristics

class MyHeuristics(Heuristics):
    def __init__(self):
        super().__init__()
        self.patterns = {'iiiii': 100,
                         '_iiii_': 80, #
                         'ii_ii': 80,  #
                         '_iii_': 20,
                         '__iii__': 30,  #
                         'iii__': 20,
                         '_i_ii_': 10,
                         '_ii__': 10,
                         '__ii_': 10,
                         'ii___': 3,    #
                         '__i__': 1,
                         'itttt_': 4,   #
                         'ittt_': 1,    #
                         '_ttt_': 5,    #
                         '_tt_t_': 2,   #
                         'itt_t_': 1,    #
                         't_t_t': 1     #
                         }
        reversed_patterns = {''.join(reversed(p[0])): p[1] for p in self.patterns.items()}
        self.patterns.update(reversed_patterns)