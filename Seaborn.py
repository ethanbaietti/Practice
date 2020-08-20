#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:35:41 2020

@author: ethanbaietti
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_excel("Pokemon2.xlsx", index_col=0)

df.head()

sns.lmplot(x = 'Attack' , y = 'Defense', data = df) #scatter plot

#scatter plot with no regression line and grouped by stage
sns.lmplot(x = 'Attack' , y = 'Defense', data = df, fit_reg = False, hue = 'Stage')

#Adjusting the axis with Matplotlib

plt.ylim(0, None)
plt.xlim(0, None) 


# Boxplot
sns.boxplot(data = df)

#Boxplot clean up with pandas clean up
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis = 1)

sns.boxplot(data = stats_df)

