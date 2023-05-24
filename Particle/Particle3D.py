import math
import numpy as np

class Particle3D(object):
    """
    Class to describe 3D particles.

    Properties:
    label(string) - describes particle identity
    position(Numpy array) - position in the 3D space defined by (x, y, z)
    velocity(float) - velocity in the 3D space defined by (x, y, z)
    mass(float) - particle mass

    Methods:
    * __init__ to initialise the properties
    * __str__ to print the particle properties
    *Return the object's kinetic energy
    *Update velocity of a particle for given timestep and force vector
    *First-order update of particle position for given timestep
    *Second-order update of particle position for given timestep and force
    *Create a 3D  particle from a file entry
    *Return the relative vector separation of two particles
    """

    def __init__(self,lab,pos,vel,mass):
        self.label = lab
        self.position = pos
        self.velocity = vel
        self.mass = mass


    def __str__(self):
        return (self.label) + " " + str(self.position[0]) + " " + str(self.position[1]) + " " + str(self.position[2])


    def kinetic_energy(self):
        """
        return kinetic energy as
        (1/2)*mass*vel^2
        """
        return 0.5*self.mass*np.dot(self.velocity,self.velocity)

    
    
    # Time integration methods
    
    def leap_velocity(self, dt, force):
        """
        First-order velocity update for given timestep,
        v(t+dt) = v(t) + dt*(f(t)/m)
        """
        self.velocity = self.velocity + dt*force/self.mass 


    def leap_pos1st(self, dt):
        """
        First-order position update for given timestep,
        r(t+dt) = r(t) + dt*v(t)
        """
        self.position = self.position + dt*self.velocity


    def leap_pos2nd(self, dt,f):
        """
        Second- order position update for given timestep and force,
        r(t+dt) = r(t) + dt*v(t) +1/2*dt^2*(f(t)/m)
        """
        self.position = self.position + dt*self.velocity + ((0.5*dt**2)*f)/self.mass


    @staticmethod
    def readfromfile(filehandle):
        line = filehandle.readline()
        linesplit = line.split(" ")

        l=linesplit[0]
        x1,x2,x3 = linesplit[1],linesplit[2],linesplit[3]
        v1,v2,v3 = linesplit[4],linesplit[5],linesplit[6]
        m1=linesplit[7]

        x = np.array([x1,x2,x3],float)
        v = np.array([v1,v2,v3],float)
        m = np.array([m1],float)
        particle = Particle3D(l,x,v,m)
        
        return particle


    @staticmethod
    def sep(v1,v2):
        vectordiff = np.subtract(v1,v2)
        
        return vectordiff
    
    @staticmethod
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
        

    
