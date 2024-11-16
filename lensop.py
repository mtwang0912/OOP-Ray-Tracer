#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains function for lens optimisation. 

Created on Thu Oct 27 15:38:14 2022

@author: MinnieWang
"""

import opticalelement
import ray
import sphericalrefraction
import outputplane
import raybundle
from raybundle import *
from terminatedray import *
from ray import *
from sphericalrefraction import *
from outputplane import *
import numpy as np
import matplotlib.pyplot as plt

#%% Lens Optimisation

def rms(xc1):
    '''
    FUNCTION CALCULATES THE ROOT MEAN SQUARE SPOT RADIUS GIVEN THE THICKNESS 
    AND CURVATURE OF A PLANO-CONVEX LENS.

    Parameters
    ----------
    xc1 : TUPLE
        TUPLR CONTAINING PARAMETERS X (THICKNESS) AND C1 
            (CURVATURE OF SURFACE 1).

    Returns
    -------
    FLOAT
        ROOT MEAN SQUARE SPOT RADIUS OF A PLANO-CONVEX LENS WITH THICKNESS X 
        AND CURVATURE C1 AT Z0 = 200.

    '''
    
    x,c1= xc1
    thickness = x
    n_glass = 1.5168
    S1 = SphericalRefraction(z0 = 100, curv = c1, n1 = 1, n2 = n_glass, 
                             aprad = 20)
    S2 = SphericalRefraction(z0 = 100 + thickness, curv = 0, n1 = n_glass, 
                             n2 = 1, aprad = 20)
    FP = OutputPlane(z0 = 200, aprad = 400)

    # RMS spot radius
    bundle = RayBundle.collimated_beam_cir(diameter = 10, direction= [0,0,1])
    for i in range(len(bundle)):
        S1.propagate_ray(bundle[i])
    for i in range(len(bundle)): #propagate all points to lens surface
        S2.propagate_ray(bundle[i])
    for i in range(len(bundle)):
        FP.propagate_ray(bundle[i])        
    output_p = RayBundle.output_positions(bundle)
    
    return RayBundle.rms(bundle, output_p)

#%% Optimisation

# bnds = ((0, 10), (-0.05, 0.05), (-0.05, 0.05)) 
# bnds = ((0, 20), (-0.05, 0.05))
# popt = opt.minimize(rms,(1, 0.01), method = 'TNC', bounds = bnds)
# popt = opt.minimize(rms,(1, 0.01), bounds = bnds)

#%%

def focal(ray):
    '''
    FUNCTION RETURNS AN APPROXIMATION OF THE POSITION OF THE PARAXIAL FOCAL 
    POINT GIVEN A RAY'S TRAJECTORY.

    Parameters
    ----------
    ray : RAY
        RAY FROM WHICH THE PARAXIAL FOCAL PLANE IS DEDUCED.

    Returns
    -------
    f : FLOAT
        Z - POSITION OF THE PARAXIAL FOCAL PLANE.

    '''
    popt = np.polyfit([i[2] for i in ray.vertices()[-2:]], 
                      [i[0] for i in ray.vertices()[-2:]],1)
    f = abs(popt[1] / popt[0])
    return f

#%%

def sph_abe(r1, r2, n, o, i, h, f):
    '''
    FUNCTION RETURNS THE LONGITUDINAL AND TRANSVERSE SPHERICAL ABERRATION 
    FOR A GIVEN OPTICAL SYSTEM.

    Parameters
    ----------
    r1 : FLOAT
        RADIUS OF FIRST LENS.
    r2 : FLOAT
        RADIUS OF THE SECOND LENS.
    n : FLOAT
        REFRACTIVE INDEX OF THE LENS.
    o : FLOAT
        OBJECT DISTANCE.
    i : FLOAT
        IMAGE DISTANCE.
    h : FLOAT
        DISTANCE FROM THE OPTICAL AXIS AT WHICH THE OUTERMOST RAY ENTERS THE 
        LENS.
    f : FLOAT
        FOCAL LENGTH OF THE LENS.

    Returns
    -------
    None.

    '''
    s = (r2 + r1) / (r2 - r1)
    p = (i - o) / (i + o)
    exp_terms = (((n + 2) * (s ** 2)) / (n - 1)) + 2 * (2 * n + 2) * s * p + \
        (3 * n + 2)*((n - 1) ** 2) * (p ** 2) + (n ** 3) / (n - 1)
    l = (((h ** 2) * (i ** 2)) / (8 * n * (n - 1) * (f ** 3))) * exp_terms
    t = (h / i) * l
    print('The longitudinal spherical aberration is = ', l)
    print('The transverse spherical aberration is = ', t)
    return 




