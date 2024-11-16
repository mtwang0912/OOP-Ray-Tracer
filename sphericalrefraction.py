#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains spherical refraction class and methods modelling refracting 
surfaces. 

Created on Thu Nov 10 16:06:16 2022

@author: MinnieWang
"""
import opticalelement
import terminatedray
from terminatedray import *
from opticalelement import *
import numpy as np
import math

class SphericalRefraction(OpticalElement): # OpticalElement is base class.

    def __init__(self, z0 = 10, curv = 0.5, n1 = 1, n2 = 1, aprad = 50):
        '''
        INSTANTIATION METHOD FOR SPHERICAL REFRACTOR.

        Parameters
        ----------
        z0 : FLOAT OPTIONAL
            INTERCEPT OF THE SURFACE WITH THE Z-AXIS. THE DEFAULT IS 0.
        curv : FLOAT, OPTIONAL
            CURVATURE OF THE SPHERICAL SURFACE, WHERE CURVATURE = 1 / R.
            THE DEFAULT IS 0.
        n1 : FLOAT, OPTIONAL
            REFRACTIVE INDEX FOR Z<Z0. THE DEFAULT IS 1.
        n2 : FLOAT, OPTIONAL
            REFRACTIVE INDEX FOR Z>Z0. THE DEFAULT IS 1.
        aprad : FLOAT, OPTIONAL
            MAX EXTENT OF THE SURFACE FROM THE OPTICAL AXIS. THE DEFAULT IS 1.

        Returns
        -------
        None.

        '''
        if aprad == 0:
            raise Exception('Error: \tSize of the lens cannot be zero.')
        if any([isinstance(i,str) for i in [z0, curv, n1, n2, aprad]]) == True:
            raise Exception('Error: \tString is an invalid input.')
        if any([type(i)==list for i in (z0, curv, n1, n2, aprad)]) == True:
            raise Exception('Error: \tEach attribute only takes one value \
                            input.')
        self._z0 = z0
        self._curvature = curv #curvature = 1/R
        self._n1 = n1
        self._n2 = n2
        self._ap_radius = aprad
        return
    
    def intercept(self, ray):
        '''
        FUNCTION FINDS THE INTERCEPT BETWEEN A RAY AND A SPHERICAL SURFACE.

        Parameters
        ----------
        ray : RAY
            THE INCIDENT RAY FOR WHICH THE INTERCEPT IS SOUGHT AFTER.

        Returns
        -------
        COORDINATES OF THE INTERCEPT POINT.

        '''
        k = ray._direction / np.linalg.norm(ray._direction) 
        if self._curvature == 0:
            l = (self._z0 - ray._position[2])/k[2]
            return ray._position + k * l
        else:
            origin = np.array([0,0,(1/self._curvature) + self._z0])
            r = - origin + ray._position 
            # distance vector from ray position to origin of sphere, by vectors
            a = np.dot(r,k)**2-(np.linalg.norm(r)**2 - (1/self._curvature)**2)
            if a <= 0:
                return None
            else: 
                l1 = - np.dot(r,k) + np.sqrt(a) 
                l2 = - np.dot(r,k) - np.sqrt(a) 
                l = min([l1,l2]) 
                return ray._position + k * l
    
    def snell(self, in_dir, n_hat):
        '''
        METHOD FIND THE VECTOR DIRECTION OF THE REFRACTED RAY, USING THREE 
        DIMENSIONAL SNELL'S LAW.

        Parameters
        ----------
        in_dir : NUMPY ARRAY WITH THREE ELEMENTS
            THREE DIMENSIONAL ARRAY OF UNIT VECTOR THAT DESCRIBES THE D
            IRECTION OF THE INCIDENT RAY.
        n_hat : NUMPY ARRAY WITH THREE ELEMENTS
            THREE DIMENSIONAL ARRAY OF UNIT VECTOR THAT DESCRIBES THE NORMAL 
            VECTOR TO THE SURFACE OF THE REFRACTOR.


        Returns
        -------
        REFRACTED RAY VECTOR DIRECTION.

        '''
        
        mu = self._n2/self._n1
        #mu = self._n1/self._n2
        theta1 = math.degrees(math.\
                              acos(np.dot(in_dir,n_hat)/(np.linalg.norm\
                                                         (in_dir)*np.linalg.\
                                                             norm(n_hat)))) 
        if math.sin(math.radians(theta1)) > mu: #total internal reflection
            return None
            #return
        else:
            t = n_hat*np.sqrt(1-((mu**2)*(1-(np.dot(n_hat,in_dir)**2)))) \
                + mu*(in_dir - (np.dot(n_hat,in_dir)*n_hat))
            return t

        
    def propagate_ray(self, ray):
        '''
        METHOD PROPAGATES A RAY TO THE REFRACTING SURFACE, AND FINDS INTERCEPT 
        AND REFRACTED DIRECTION AND APPEND NEW ATTRIBUTES TO THE RAY OBJECT.

        Parameters
        ----------
        ray : RAY
            RAY BEING PROPAGATED TO THE REFRACTING SURFACE.

        Raises
        ------
        Exception
            TERMINATED RAYS CANNOT BE PROPAGATED. RAYS THAT DO NOT INTERCEPT 
            THE REFRACTING SURFACE CANNOT BE PROPAGATED.

        Returns
        -------
        None.

        '''
        intercept = self.intercept(ray)
        if type(ray) == 'TerminatedRay':
            raise Exception('Error: \tCannot propagate terminated ray.')
        else:
            if type(intercept) != np.ndarray and intercept == None:
                print('The ray does not propagate to incident the surface, \
                      therefore has been terminated')
                orig_position = ray._position
                orig_direction = ray._direction
                # Override original class with class TerminatedRay
                ray = terminatedray.TerminatedRay(pos = orig_position, 
                                                  dire = orig_direction) 
                raise Exception('Error: \tThe ray does not propagate to \
                                incident the surface.')
                return 
            else:
                if self._curvature == 0:
                    surf_n = [0,0,self._z0]
                    surf_n = surf_n/np.linalg.norm(surf_n)
                    new_k = self.snell(ray._direction/np.linalg.norm\
                                       (ray._direction), surf_n)
                else:
                    surf_n = intercept - [0,0,self._z0 - 1/self._curvature]
                    surf_n = surf_n/np.linalg.norm(surf_n)
                    new_k = self.snell(ray._direction/np.linalg.norm\
                                       (ray._direction), surf_n)
                ray.append(intercept, new_k)
        return
    
    
    
    
    
    
    
    
    
    
    
    
    
    