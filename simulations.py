# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 00:14:41 2022

@author: Stefan H. Mueller
"""

import PT_continuous as pt
import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import gamma
from scipy.optimize import curve_fit

"""
This script produces the data presented in supplementary Figure 5
of the paper "The role of auxiliary domains in modulating CHD4 activity 
suggests mechanistic commonality between enzyme families" Zhong et. al.
doi: https://doi.org/10.1101/2022.06.13.496015 
"""

"""
A multi-step Markov process is simulated. The experimentally observed values
(see Figures 6 and 7) correspond to the absorption time of the simulated
Markov-process. This time until absorption follows a Phase-type distribution
see for example: Bladt, M. (2005): "A Review on Phase-type Distributions and 
their Use in Risk Theory." ASTIN Bulletin, 35(1), 145-161. 
doi:10.1017/S0515036100014100
"""

"""
A numerical calculation of a 5-step phase-type distribution with 4 identical 
rate constants and one different rate is implemented in 
the separate file PT_continous.py and initialized here
"""
PT = pt.PT_gen()

def gamma_pdf(x,n,k):
    """
    A gamma distribution probability density function
    """
    return gamma.pdf(x,n,scale=1/k,loc=0)

def change_kN(kN,k2):
    """
    This function calculates pdfs for varying kN (the rate constant of 
    the 4 identical steps). The generated pdfs are then fitted to gamma 
    distributions to determine the apparent rate constants that are experimentally
    accesible.
    """
    n_app = []
    k_app = []
    for k1 in kN:
        PT_pdf = PT.pdf(t,k1,k2)    #calculate PT-pdf
        #fit this curve to a gamma pdf:
        g_fit,pcov = curve_fit(gamma_pdf,t,PT_pdf,bounds = ([0,0],[np.inf,np.inf]),p0=[6,1])
        n_app.append(g_fit[0])
        k_app.append(g_fit[1])
    return n_app,k_app
def change_kx(kN,k2):
    """
    This function calculates pdfs for varying kx (the rate constant of 
    the one different step). The generated pdfs are then fitted to gamma 
    distributions to determine the apparent rate constants that are experimentally
    accesible.
    """
    n_app = []
    k_app = []
    for kx in k2:
        PT_pdf = PT.pdf(t,kN,kx)
        #fit this curve to a gamma pdf:
        g_fit,pcov = curve_fit(gamma_pdf,t,PT_pdf,bounds = ([0,0],[np.inf,np.inf]),p0=[6,1])
        n_app.append(g_fit[0])
        k_app.append(g_fit[1])
    return n_app,k_app


#%% the actuall calculations
"""
the calculation happens in the following lines and can take a few minutes
both rate constants are varried separetly while the other one is kept constant.
"""

result = []
n=1
t = np.arange(0.1,200,0.1)
#test kN logarithmically spaced
kN = np.logspace(-2, 2,100)
#and kx from 0 to 1
kx = [0.1,0.3,0.5,0.7]
all_results_kn = []
for k in kx:
    result = change_kN(kN,k)
    all_results_kn.append(result)

"""
for completion we also calculate appearent N and k for varying kx.
This is not shown in the paper though.
"""
kx = np.logspace(-2, 2,100)
kN = [0.1,0.3,0.5,0.7]
all_results_kx = []
for k in kN:
    result = change_kx(k,kx)
    all_results_kx.append(result)
    
#%% now save the results:
    
"""
we just save the obtained simulation results is .csv files.
The file plots.py contains a script for visualization
"""
    
    
import pandas as pd
dataNapp = {'0.1':[],'0.3':[],'0.5':[],'0.7':[],'kx':[]}
datakapp = {'0.1':[],'0.3':[],'0.5':[],'0.7':[]}
keys = dataNapp.keys()
# print(keys)
for result,key in zip(all_results_kn,keys):
    dataNapp[key] = result[0]
    datakapp[key] = result[1]
dataNapp['kx'] = list(kx)   
df_Napp = pd.DataFrame(dataNapp)
df_kapp = pd.DataFrame(datakapp)
#concatenate all data to one dataFrame
df_all = df_Napp.join(df_kapp,lsuffix='_napp',rsuffix='_kapp')
#and save to a csv-file
df_all.to_csv('change_kN.csv')

#%% now save the results for the varried kx
kN = np.logspace(-2, 2,100)
dataNapp = {'0.1':[],'0.3':[],'0.5':[],'0.7':[],'kN':[]}
datakapp = {'0.1':[],'0.3':[],'0.5':[],'0.7':[]}
keys = dataNapp.keys()
# print(keys)
for result,key in zip(all_results_kx,keys):
    dataNapp[key] = result[0]
    datakapp[key] = result[1]

dataNapp['kN'] = list(kN)   

df_Napp = pd.DataFrame(dataNapp)
df_kapp = pd.DataFrame(datakapp)
df_all = df_Napp.join(df_kapp,lsuffix='_napp',rsuffix='_kapp')
df_all.to_csv('change_kx.csv')

