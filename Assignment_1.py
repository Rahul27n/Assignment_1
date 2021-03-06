# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vzqTl9EKn3RSm3FZuonN0aOftlRwrxsD
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Let us set the number of leap years we have to choose from as 4900
simlen = int(4900)

print("Let the random variable X={0,1} represent the outcome whether a leap year has 53 Tuesdays or not.")
print("X=0 indicates the leap year does not have 53 Tuesdays and X=1 indicates the leap year has 53 Tuesdays.")

prob = 2/7 #Probability of the event that the leap year has 53 Tuesdays i.e, X=1

#Generating sample data using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)

#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#Calculating the probability
err_n = np.size(err_ind)/simlen
# No of leap years having 53 Tuesdays
#Using Simulation
yr_sim = simlen*(err_n)
#Using exact probability
yr_act = simlen*(prob)
#Theory vs Simulation
print("Probability-simulation,actual:",err_n,prob)
print("No.of leap years-simulation,actual:",yr_sim,yr_act)
print("Samples generated:",data_bern)

#Actual bar plot
data1 = {'Yr_53_Tuesdays':(yr_act),'Yr_52_Tuesdays':(4900-yr_act)}
no_of_tuesdays = list(data1.keys())
no_of_years = list(data1.values())

fig = plt.figure(figsize = (8,4))

#creating the plot
plt.bar(no_of_tuesdays,no_of_years,color = 'Green',width = 0.08)
plt.xlabel("No of Tuesdays in a leap year")
plt.ylabel("Number of leap years")
plt.title("Distribution of the 4900 leap years having 53 Tuesdays or not(actual)")
plt.show()

#Simulation bar plot
data2 = {'Yr_53_Tuesdays':(yr_sim),'Yr_52_Tuesdays':(4900-yr_sim)}
no_of_tuesdays = list(data2.keys())
no_of_years = list(data2.values())

fig = plt.figure(figsize = (8,4))

#creating the plot
plt.bar(no_of_tuesdays,no_of_years,color = 'Green',width= 0.08)
plt.xlabel("No of Tuesdays in a leap year")
plt.ylabel("Number of leap years")
plt.title("Distribution of the 4900 leap years having 53 Tuesdays or not(simulated)")
plt.show()