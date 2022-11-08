# Markov-simulation

This repository contains scripts to simulate the time to absorption for a 5 step Markov process, in which 4 steps have 
identical rate constants (transition probabilities) and one rate is different. The time until absorption is described by a Phase-type distribution.
The result is fitted to a Gamma-distribution and finally the appearent number of steps as found by fitting to Gamma distributions is compared to the 
real underlying system.
This code is part of the paper "The role of auxiliary domains in modulating CHD4 activity suggests mechanistic commonality between enzyme families"
by Zhong _et. al._ (see https://www.biorxiv.org/content/10.1101/2022.06.13.496015v2.full) and serves to understand if observed FRET states that yield apparent rate constant and number of steps through Gamma-fits are likely to over-
or underestimate the rates and numbers of real kinetic intermediates.

## Implementation

The Phase-type distributiuon is implemented by subclassing rv_continous from scipy.sats (see https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.rv_continuous.html) in the PT_continous.
While this is  sufficient to calculate PDF,CDF and SF this implementation is not capable of creating random variables through the rv_continous.rvs() method.
This is likely due to the numerical calculation of the matrix exponential in the PT-pdf.
The actual calculation is implemented in simulations.py. This script creates csv files with the simulated data, plots.py provides a simple script for plotting the results.

## Dependencies

-scipy.linalg
-numpy
-scipy.stats.rv_continuous
-scipy.stats.gamma
-scipy.optimize
-matplotlib.pyplot
