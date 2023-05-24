import math
import numpy as np
import sys
from Particle3D import Particle3D
import Functions as fun
# import backend.Functions as fun
import json


def update_positions(planetlist, F, dt, numstep, N):
    """
    Updates the position of all planets using the leap function from Particle3D
    for the given number of time steps, and writes position data to a file.
    """
    print("hello1")
    with open("data.json", "r") as file:
        # write the Python object to the JSON file
        existing_data = json.load(file)

    for i in range(numstep):
        print(i)
        for j in range(len(planetlist)):
            planetlist[j].leap_pos2nd(dt, F[j, :])

        force_new = fun.R_Force(planetlist, N)

        for k in range(len(planetlist)):
            A = 0.5 * (F[k, :] + force_new[k, :])
            planetlist[k].leap_velocity(dt, A)

        F = force_new
        if (i%5 == 0):
            data = {
                "time": i,
                "planets": [       { planetlist[l].label : {
                        "x": planetlist[l].position[0],
                        "y": planetlist[l].position[1],
                        "z": planetlist[l].position[2]
                    } for l in range(N) }
                ]
            }
            existing_data.append(data)
            with open("data.json", "w") as file:
            # write the Python object to the JSON file
                json.dump(existing_data, file)
    return planetlist

def calculate_orbital_period(orbit, orbit_sun, alpha, T_period, numstep, N):
    """
    Calculates the angle through which each planet has moved, and from this, the orbital period.
    """
    for i in range(numstep):
        for l in range(N):
            orbit[l, i, :] = planetlist[l].position
            orbit_sun[l, i, :] = Particle3D.sep(orbit[0, i, :], orbit[l, i, :])
            if i > 0 and l > 0:
                if l != 4:
                    orbit_sun[l, i, :] = Particle3D.sep(orbit[0, i, :], orbit[l, i, :])
                    b_vec = orbit_sun[l, i - 1, :]
                    c_vec = orbit_sun[l, i, :]
                else:
                    orbit_sun[l, i, :] = Particle3D.sep(orbit[3, i, :], orbit[l, i, :])
                    b_vec = orbit_sun[l, i - 1, :]
                    c_vec = orbit_sun[l, i, :]
                bdotc = np.dot(b_vec, c_vec)
                mod_b = np.linalg.norm(b_vec)
                mod_c = np.linalg.norm(c_vec)
                cosa = bdotc / (mod_b * mod_c)
                alpha[l] += math.acos(cosa)
                n_orbits = alpha[l] / (2 * math.pi)
                T_period[l] = numstep / n_orbits
        yield T_period

def calculate_apsides(planetlist, apsis, N):
    """
    Calculates the maximum and minimum approach of each planet (except the moon), and the 
    apo- and perigee values for the moon.
    """
    for m in range(N - 1):
        if m != 3:
            apsis[m, i, :] = Particle3D.sep(planetlist[0].position, planetlist[m + 1].position)
        else:
            apsis[m, i, :] = Particle3D.sep(planetlist[3].position, planetlist[m + 1].position)
        yield apsis

def track_energy(planetlist, Totalenergy, timelist, numstep):
    """
    Keeps track of the total energy of the system, which will be plotted in matplotlib.
    """
    for i in range(numstep):
        Totalenergy.append(fun.totalenergy(planetlist, N))
        timelist.append(i)
        yield Totalenergy, timelist