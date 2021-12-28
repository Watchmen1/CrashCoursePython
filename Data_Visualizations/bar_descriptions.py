#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 18:08:51 2021

@author: thewatchman
"""

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['public-apis','system-design-primer','Python']

plot_dicts = [
    {'value': 165506, 'label': 'Description of public-apis.'},
    {'value': 147617, 'label': 'Description of system-design-primer.'},
    {'value': 121690, 'label': 'Description of Python.'}
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')