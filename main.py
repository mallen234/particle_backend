import math
import numpy as np
import sys
from Particle.Particle3D import Particle3D
# import backend.Functions as fun
import Particle.Planets3D as Planets3D
import time

def main():
    N,dt,numstep = 12,1,1000
    planetlist = []
    inputfile = open("planetdata.txt","r")


    for i in range (N):
        p = Particle3D.readfromfile(inputfile)  #initialsing the planets from file
        planetlist.append(p)
    F = Particle3D.R_Force(planetlist,N)
        
    print("hello0")
    start_time = time.time()
    Planets3D.update_positions(planetlist, F, dt, numstep, N)  #Running the simulation
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

main()