#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for raytracer simulation testing.
"""

import opticalelement
import terminatedray
import ray
import sphericalrefraction
import outputplane
import plotter
from plotter import *
from terminatedray import *
from opticalelement import *
from ray import *
from sphericalrefraction import *
from outputplane import *
import numpy as np
import math
import random

#%% ray class testing

def T1():
    '''Ray class functions testing.'''
    print('... Ray: Class Testing ...')
    success = True
    ray1 = ray()

#input length

    try:
        ray1.append([0,0,0],[0,0])
        print('Test Failed \t\t Invalid input length')
        success = False
    except:
        print('Test Passed \t\t Invalid input length')
        

#0 direction

    try:
        ray1 = ray(dire = [0,0,0])
        print('Test Failed \t\t Null direction instantiation')
        success = False
    except:
        print('Test Passed \t\t Null direction instantiation')

    try:
        ray1.append([0,0,0],[0,0,0])
        print('Test Failed \t\t Null direction input')
        success = False
    except:
        print('Test Passed \t\t Null direction input')
        
#representation
    p = [0,0,0]
    d = [0,0,1]
    RAY = ray(pos = p, dire = d)
    
    if p[0] == RAY.p()[0] and p[1] == RAY.p()[1] and p[2] == RAY.p()[2]:
        print('Test Passed \t\t Access method: position')
    else:
        print('Test Failed \t\t Access method: position')
        success = False

    if d[0] == RAY.k()[0] and d[1] == RAY.k()[1] and d[2] == RAY.k()[2]:
        print('Test Passed \t\t Access method: direction')
    else:
        print('Test Failed \t\t Access method: direction')
        success = False
        
#invalid input (string)

    try:
        ray1.append(['hello',0,0],[0,0,1])
        print('Test Failed \t\t String input')
        success = False
    except:
        print('Test Passed \t\t String input')
        
#vertices
    
    p1 = [0,0,1]
    k1 = [0,0,1]
    RAY.append(p = p1, k = k1)
    
    if RAY.vertices()[-1][0] == p1[0] and RAY.vertices()[-1][1] == p1[1] and \
        RAY.vertices()[-1][2] == p1[2]:
        print('Test Passed \t\t Append method: position')
    else:
        print('Test Failed \t\t Append method: position')
        success = False

    if k1[0] == RAY.k()[0] and k1[1] == RAY.k()[1] and k1[2] == RAY.k()[2]:
        print('Test Passed \t\t Append method: direction')
    else:
        print('Test Failed \t\t Append method: direction')
        success = False

    if success == False:
        print('... Ray: The class has not passed all tests ...')
    else: 
        print('... Ray: The class has passed all tests ... \n\n')


#%% terminated ray testing

def T2():
    '''Terminated ray class functions testing.'''
    print(' ... Terminated Ray: Class Testing ...')
    success = True
    
    R1 = ray()
    R1 = TerminatedRay(pos = [0,0,0], dire = [0,0,1])
    if type(R1) == TerminatedRay:     
        print('Test Passed \t\t Terminated ray class overriding')
    else:
        print('Test Failed \t\t Terminated ray class overriding')
        success = False
    
    position = [1,2,3]
    direction = [4,5,6]
    R1 = ray(pos = position, dire = direction)
    R2 = TerminatedRay(R1._position, R1._direction)
    if sum(R2.position) == sum(position) and sum(R2.direction) == \
        sum(direction):     
        print('Test Passed \t\t Terminated ray class attributes inheritance')
    else:
        print('Test Failed \t\t Terminated ray class attributes inheritance')
        success = False

    if success == False:
        print('... Terminated Ray: The class has not passed all tests ...')
    else: 
        print('... Terminated Ray: The class has passed all tests ... \n\n')


#%% spherical refraction

#valid input for parameters

def T3():
    '''Spherical refraction class functions testing.'''
    print(' ... Spherical Refraction: Class Testing ...')
    success = True
    try:
        S1 = SphericalRefraction(aprad = 0)
        print('Test Failed \t\t Size of lens is zero')
        success = False
    except:
        print('Test Passed \t\t Size of lens is zero')
        
    try:
        S = SphericalRefraction(n1 = 'n')
        print('Test Failed \t\t String input')
        success = False
    except:
        print('Test Passed \t\t String input')
    
    try:
        S = SphericalRefraction(n1 = [0,1])
        print('Test Failed \t\t More than one value inputted for a parameter')
        success = False
    except:
        print('Test Passed \t\t More than one value inputted for a parameter')
    
    try:
        SSRS = SphericalRefraction(z0 = 1, curv = 0.03, n1 = 1, n2 = 1.5, 
                                   aprad = 20)
        RAY = ray(pos = [0,0,0], dire = [-1,0,0])
        SSRS.propagate_ray(RAY)
        print('Test Failed \t\t Appending Nonetype object')
        success = False
    except:
        print('Test Passed \t\t Appending Nonetype object')

    try:
        R1 = TerminatedRay(pos = [0,0,0], dire = [0,0,1])
        SSRS.propagate_ray(R1)
        print('Test Failed \t\t Propagation of terminated ray')
        success == False
    except:
        print('Test Passed \t\t Propagation of terminated ray')
        
    try:
        R2 = ray(pos = [2,0,0], dire = [-2,0,1])
        PLANO = SphericalRefraction(z0 = 1, curv = 0, n1 = 1.5, n2 = 1, 
                                    aprad = 20)
        PLANO.propagate_ray(R2)
        print('Test Failed \t\t Total Internal Reflection')
        success = False
    except:
        print('Test Passed \t\t Total Internal Reflection')

    if success == False:
        print('... Spherical Refraction: The class has not passed all \
              tests ...')
    else: 
        print('... Spherical Refraction: The class has passed all tests \
              ... \n\n')
        

#%% optical element

def T4():
    '''Optical Element class functions testing.'''
    print(' ... Optical Element: Class Testing ...')
    success = True
    
    try:
        O = OpticalElement()
        R = ray()
        O.propagate_ray(R)
        print('Test Failed \t\t Undefined optical element parent class ray \
              propagation')
        success == False
    except:
        print('Test Passed \t\t Undefined optical element parent class ray \
              propagation')      
   
    if success == False:
        print('... Optical Element: The class has not passed all tests ...')
    else: 
        print('... Optical Element: The class has passed all tests ... \n\n')


#%% raybundle

def T5():
    '''Ray bundle class functions testing.'''
    print(' ... Ray Bundle: Class Testing ...')
    success = True
    
    B1 = RayBundle(center = [1,2,3])
    if sum(B1._center) == sum([1,2,3]):
        print('Test Passed \t\t Center of beam instantiation')
    else:
        print('Test Failed \t\t Center of beam instantiation')
        success = False
    
    d = 10
    B2 = RayBundle.collimated_beam_cir(diameter = d)
    positions = [B2[i]._position for i in range(len(B2))]
    if (max([i[0] for i in positions]) - min([i[0] for i in positions])) == d:
        print('Test Passed \t\t Collimated beam size instantiation')
    else:
        print('Test Failed \t\t Collimated beam size instantiation ')
        success = False
    
    k = [10,10,100]
    B3 = RayBundle.collimated_beam_cir(direction = k)
    B3_1 = B3[0]._direction
    if sum(B3_1) == sum(k):
        print('Test Passed \t\t Collimated beam direction instantiation')
    else:
        print('Test Failed \t\t Collimated beam direction instantiation ')
        success = False

    if success == False:
        print('... Ray Bundle: The class has not passed all tests ...')
    else: 
        print('... Ray Bundle: The class has passed all tests ... \n\n')

#%%
T1()
T2()
T3()
T4()
T5()
