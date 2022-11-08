# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 23:57:58 2022

@author: Stefan H. Mueller
"""

from scipy.linalg import expm
import numpy as np
from scipy.stats import rv_continuous


class PT_gen(rv_continuous):

    """A phase type distribution, with 5 steps. The 4 first steps are
    identical, the last one is different"""

    def _pdf(self, x, k1,k2):
        """
        The probability density is defined as F(x) = 1-a*exp(Sx)*Id
        a is a vector that defines the starting probabily. We simulate a
        system always starting in state 1.
        S is the rate matrix associated with the simulated Markov-process.
        Id is the identity column vector.
        """
        if isinstance(k1, np.ndarray):
            k1=k1[0]
        if isinstance(k2, np.ndarray):
            k2=k2[0]
        # print(k1)
        S = np.array([[-k1, k1,  0,  0,  0,  0],
                      [0  ,-k1, k1,  0,  0,  0],
                      [0  ,  0,-k1, k1,  0,  0],
                      [0  ,  0,  0,-k1, k1,  0],
                      [0  ,  0,  0,  0,-k1, k1],
                      [0  ,  0,  0,  0,  0,-k2]])
        Id = np.array([[1],
                       [1],
                       [1],
                       [1],
                       [1],
                       [1]])
        S0 = -np.matmul(S,Id)
        a = np.array([[1,0,0,0,0,0]])
        
        PT = lambda i: np.matmul(a, np.matmul(expm(S*i),S0))[0][0]
        return np.array(list(map(PT,x)))
    def _cdf(self, x, k1,k2):
        """
        here we define the cumulative probability density function explicitly
        """
        if isinstance(k1, np.ndarray):
            k1=k1[0]
        if isinstance(k2, np.ndarray):
            k2=k2[0]
        # print(k1)
        S = np.array([[-k1, k1,  0,  0,  0,  0],
                      [0  ,-k1, k1,  0,  0,  0],
                      [0  ,  0,-k1, k1,  0,  0],
                      [0  ,  0,  0,-k1, k1,  0],
                      [0  ,  0,  0,  0,-k1, k1],
                      [0  ,  0,  0,  0,  0,-k2]])
        Id = np.array([[1],
                       [1],
                       [1],
                       [1],
                       [1],
                       [1]])
        # S0 = -np.matmul(S,Id)
        a = np.array([[1,0,0,0,0,0]])
        
        PT = lambda i: 1-np.matmul(a, np.matmul(expm(S*i),Id))[0][0]
        return np.array(list(map(PT,x)))
    def _sf(self,x,k1,k2):
        """
        here we define the survival function (1-cdf) explicitly
        """
        if isinstance(k1, np.ndarray):
            k1=k1[0]
        if isinstance(k2, np.ndarray):
            k2=k2[0]
        # print(k1)
        S = np.array([[-k1, k1,  0,  0,  0,  0],
                      [0  ,-k1, k1,  0,  0,  0],
                      [0  ,  0,-k1, k1,  0,  0],
                      [0  ,  0,  0,-k1, k1,  0],
                      [0  ,  0,  0,  0,-k1, k1],
                      [0  ,  0,  0,  0,  0,-k2]])
        Id = np.array([[1],
                       [1],
                       [1],
                       [1],
                       [1],
                       [1]])
        # S0 = -np.matmul(S,Id)
        a = np.array([[1,0,0,0,0,0]])
        PT = lambda i: np.matmul(a, np.matmul(expm(S*i),Id))[0][0]
        return np.array(list(map(PT,x)))
    
    
if __name__ in "__main__":
    #just a little test:
    from matplotlib import pyplot as plt
    PT = PT_gen(name='PT',shapes = "k1,k2")
    t = np.arange(0,100,0.1)
    plt.plot(PT.sf(t,0.1,0.3))