# Markov-simulation

This repository contains scripts to simulate the time to absorption for a 5 step Markov process, in which 4 steps have 
identical rate constants (transition probabilities) and one rate is different. The time until absorption is described by a Phase-type distribution.
The result is fitted to a Gamma-distribution and finally the appearent number of steps as found by fitting to Gamma distributions is compared to the 
real underlying system.
This code is part of the paper "The role of auxiliary domains in modulating CHD4 activity suggests mechanistic commonality between enzyme families"
by Zhong et. al. and serves to understand if observed FRET states that yield apparent rate constant and number of steps through Gamma-fits are likely to over-
or underestimate the rates and numbers of real kinetic intermediates.
