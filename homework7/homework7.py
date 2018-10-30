#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 13:15:25 2018

@author: dannywitt
"""

# =============================================================================
# # 1 Probability Generator 
# def string_to_tups(string, i):
#     #Convert a string with '|' delimiters into all possible distinct tuple 
#     #pairs (i.e., combinations) of the letters from string argument.
#     #1. Remove delimiters to get string of letters
#     import re
#     delim = '|'
#     just_letters = re.split("["+"//".join(delim)+"]", string)
#     #2. Convert string of letters into tuples of size "i" with all possible unique 
#     #combinations of letters 
#     import itertools
#     tuple_i_combinations = list(itertools.combinations(just_letters, i))
#     return tuple_i_combinations
# 
# 
# def letter_probs(the_string, i, letter):
#     #import itertools
#     list_of_tups = string_to_tups(the_string, i)
#     print(list_of_tups)
#     count_letter_in_tups = 0
#     for tup in list_of_tups:
#         if tup.count(letter) > 0:
#             count_letter_in_tups += 1
#         else:
#             continue
#     probability = ((count_letter_in_tups) / (len(list_of_tups)))*100
#     return print('Probability of {} in combination size i={} is {}%.'
#                  .format(letter, i, probability))
#  
# ###Test###
# string_practice = 'A|A|A|B|Z'
# size = 3
# letter = 'Z'
# 
# letter_probs(string_practice, size, letter)
# =============================================================================

#2 Battery Class

class Battery:
    """Goal: introspect the batter level of the Tesla Model S."""
    
    def __init__(self, power = 100):
        self.power = power
        return
    
    @property
    def power(self):
        return self._power
        
    @power.setter
    def power(self, pwr_level):
        if pwr_level > 100 or pwr_level < 0:
            raise ValueError("Battery power level out of possible range.")
        self._power = pwr_level
        
    def __repr__(self):
        """String representation of class objects."""
        return 'Battery Power is {}%.'.format(self.power) 

#3 Car Class
        
class Car(Battery):
    """Car should inherit the Battery type. 
        #1 contains method called draw (returns iterator to -1 from batter pwr)
        #2 contains method called throttle (executes iterator with next)"""
    def __init__(self, power = 100):
        """initialize type Car, with inheritance from Battery class"""
        super().__init__(power)
        self.iterator = self.draw()
        return
    
    def draw(self):
        self.decrease_pwr = iter(range(self.power, 0, -1))
        return self.decrease_pwr
        
    def throttle(self):
        """returns current power of battery by executing next on iterator built from draw"""
        return next(self.iterator)
        

car1 = Car(18)
print(car1)
print(car1.throttle())
print(car1.throttle())
print(car1.throttle())
print(car1.throttle())