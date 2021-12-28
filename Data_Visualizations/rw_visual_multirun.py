#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:23:54 2021

@author: thewatchman
"""

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.

while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the plotting window.
    plt.figure(dpi=226, figsize=(10, 6))
    
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,  s=1, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none')
    
    #Emphasize the first and last points.
    plt.scatter(0, 0, s=100, c='green', edgecolor='none')
    plt.scatter(rw.x_values[-1], rw.y_values[-1],  s=100, c='red', edgecolor='none')
    
    # Remove the axes.
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)
    plt.axis('off')
    
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    
    if keep_running == 'n':
        break
    