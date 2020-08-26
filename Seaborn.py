# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:43:08 2020

@author: ethan.baietti
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

#Seaborn Themes -Violin PLots

sns.set_style('whitegrid')
sns.violinplot(x = 'Type 1', y = 'Attack', data = df)

pkmn_type_colors = ['#78C850',
                    '#F08030',  
                    '#6890F0',  
                    '#A8B820',  
                    '#A8A878',  
                    '#A040A0',  
                    '#F8D030',  
                    '#E0C068',  
                    '#EE99AC',  
                    '#C03028',  
                    '#F85888',  
                    '#B8A038',  
                    '#705898',  
                    '#98D8D8',  
                    '#7038F8',  
                   ]



sns.violinplot(x = 'Type 1' , y = 'Attack', data = df, palette=pkmn_type_colors)

##Swarm Plot
sns.swarmplot(x= 'Type 1', y = 'Attack', data = df, palette = pkmn_type_colors)



#Overlaaying Plots
plt.figure(figsize=(10,6))

#Create Plot
sns.violinplot(x= 'Type 1',
               y = 'Attack',
               data = df,
               inner = None, #remove bars inside violin
               palette = pkmn_type_colors)



sns.swarmplot(x = 'Type 1',
              y = 'Attack',
              data = df,
              color = 'k',
              alpha = 0.7)

plt.title('Attack by Type')

#Melt DataFrame

melted_df = pd.melt(stats_df, 
                    id_vars = ['Name','Type 1', 'Type 2'],
                    var_name = 'Stat')

melted_df.head()

print(stats_df.shape)
print(melted_df.shape)

sns.swarmplot(x = 'Stat', y = 'value', data = melted_df, hue = 'Type 1')



















