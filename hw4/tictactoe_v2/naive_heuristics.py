#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:47:03 2019

@author: milos
"""

from heuristics import Heuristics

class NaiveHeuristics(Heuristics):
    def __init__(self):
        super().__init__()
        self.patterns = {'iiiii': 100,
                         'iiii': 20,
                         '_iii_': 1}