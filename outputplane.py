#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains functions for the output plane class.
 
Created on Thu Nov 10 16:06:57 2022

@author: MinnieWang
"""

import opticalelement
from opticalelement import *
import numpy as np
        
class OutputPlane(OpticalElement):
    
    def __init__(self, z0 = 10, curv = 0, n1 = 1, n2 = 1, aprad = 100):
        '''
        INSTANTIATION FUNCTION FOR OUTPUT PLANE OBJECTS.
        
        Parameters
        ----------
        z0 : FLOAT, OPTIONAL
            INTERCEPT OF THE SURFACE WITH THE Z-AXIS. THE DEFAULT IS 10.
        curv : FLOAT, OPTIONAL
            CURVATURE OF THE SPHERICAL SURFACE, WHERE CURVATURE = 1 / R.
            THE DEFAULT IS 0.
        n1 : FLOAT, OPTIONAL
            REFRACTIVE INDEX FOR Z<Z0. THE DEFAULT IS 1. 
        n2 : FLOAT, OPTIONAL
            REFRACTIVE INDEX FOR Z>Z0. THE DEFAULT IS 1. 
        aprad : FLOAT, OPTIONAL
            MAXIMUM EXTENT OF THE SURFACE FROM THE OPTICAL AXIS. 
            THE DEFAULT IS 100.

        Returns
        -------
        None.

        '''
        self._z0 = z0
        self._curvature = curv #curvature = 1 / R
        self._n1 = n1
        self._n2 = n2
        self._ap_radius = aprad
        return 
    
    def intercept(self, ray):
        '''
        METHOD CALCULATES THE INTERCEPT BETWEEN THE RAY AND THE OUTPUT PLANE.

        Parameters
        ----------
        ray : RAY
            OBJECT OF RAY CLASS.

        Returns
        -------
        NUMPY.NDARRAY
            INTERCEPT POSITION BETWEEN RAY AND OUTPUT PLANE.

        '''
        l = (self._z0 - ray._position[2]) / ray._direction[2] 
        return ray._position + l * ray._direction

    def propagate_ray(self, ray):
        '''
        METHOD PROPAGATES RAY TO THE OUTPUT PLANE, AND APPENDS NEW 
        POSITION AND DIRECTION TO THE RAY.

        Parameters
        ----------
        ray : RAY
            OBJECT OF RAY CLASS.

        Returns
        -------
        None.

        '''
        intercept = self.intercept(ray)
        ray.append(intercept, ray._direction)
        return
    


    
    