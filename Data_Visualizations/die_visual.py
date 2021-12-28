#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 18:20:49 2021

@author: thewatchman
"""

from die import Die
import pygal

# Create two D6 dice.
die = Die()


# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
print(results)


# Analyze the results.
frequencies = []


for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)

# Vizualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a single D6 dice 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
