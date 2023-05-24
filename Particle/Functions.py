import math
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D 
import sys


def force(m1,m2,r):
    """
    Method to return the gravtitational force bewteen two planets.
    Force is given by
    F(m1, m2) = (g*m1*m2)/(r1**2)

    :return: force acting on particle as Numpy array
    
    g is the gravitational constant, G, is in the units of Au per day per kg.
    """
    g = 1.476147E-34
    r1 = np.linalg.norm(r)          #r1 = planet separation scalar
    r_hat = r/r1
    F = -r_hat*(g*m1*m2)/(r1**2)
    return F

def R_Force(planetlist,N):
    """
    Function to return the total force from all other planets on each planet 
    in the system. Two for-loops were used to create a matrix where the top diagonal
    was filled and then the bottom diagonal was set equal and opposite (using Newton III). 
    Then using np.sum, the matrix was collapsed leaving an array of the total force.
    """
    A = np.zeros([N,N,3])
    for i in range(N):
        for j in range (i+1,N):
            a = Particle3D.sep(planetlist[i].position,planetlist[j].position)
            A[i,j,:] = force(planetlist[i].mass,planetlist[j].mass,a)
            A[j,i,:] = -A[i,j,:]
    
    Total_force = np.sum(A,axis=1)   
    return Total_force