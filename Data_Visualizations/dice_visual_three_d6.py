#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 15:12:49 2021

@author: thewatchman
"""

from die import Die
import pygal

# Create two D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(1000)]

# =============================================================================
# for roll_num in range(1000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
# =============================================================================
    
print(results)


# Analyze the results.

max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]

# =============================================================================
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
# =============================================================================
    
print(frequencies)

# Vizualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [str(x) for x in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual4.svg')