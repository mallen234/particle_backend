import math
import numpy as np
import sys
from Particle3D import Particle3D 
# import backend.Functions as fun
import Planets3D as Planets3D
import Functions as fun

def main():
    N,dt,numstep = 12,1,1000
    planetlist = []
    inputfile = open("planetdata.txt","r")


    for i in range (N):
        p = Particle3D.readfromfile(inputfile)  #initialsing the planets from file
        planetlist.append(p)
    F = fun.R_Force(planetlist,N)
        
    print("hello0")
    Planets3D.update_positions(planetlist, F, dt, numstep, N)  #Running the simulation

main()