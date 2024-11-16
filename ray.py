#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains class and methods to represent optical rays in cartesian 
coordinates.

Created on Thu Nov 10 16:04:29 2022

@author: MinnieWang
"""

import numpy as np
import math
import matplotlib.pyplot as plt

class ray:
    '''
    CLASS REPRESENTS OPTICAL RAYS IN CARTESIAN COORDINATES
    '''
    
    def __init__(self, pos = [0,0,0], dire = [0,0,1]):
        '''
        INSTANTIATION METHOD FOR RAY CLASS TO DEFINE RAY ATTRIBUES AND PATH 
        AND DIRECTIONS.

        Parameters
        ----------
        pos : LIST, OPTIONAL
            LIST WITH THREE ELEMENTS CONTAINING THE POSITION OF THE RAY IN 
            CARTESIAN COORDINATES. THE DEFAULT IS [0,0,0].
        dire : LIST, OPTIONAL
            LIST WITH THREE ELEMENTS CONTAINING THE VECTOR DIRECTION OF THE 
            RAY IN CARTESIAN COORDINATES. THE DEFAULT IS [0,0,1].

        Raises
        ------
        Exception
            ERROR IS RAISED WHEN THE DIRECTION VECTOR IS 0, INDICATING 
            A NON-PROPAGATING RAY.

        Returns
        -------
        None.
        '''
        if dire[0] == dire[1] == dire[2] == 0:
            raise Exception('Error: \tDirection vector cannot be [0,0,0], \
                            this indicates a stationary ray.')
        self._position = np.array(pos)
        self._direction  = np.array(dire) 
        self._path = np.vstack([self._position])
        self._pastdirections = np.vstack([self._direction])
        
    def __repr__(self): 
        '''
        FUNCTION FORMATS OURPUT WHEN THE OBJECT IS CALLED BY ITSELF
        
        Returns
        -------
        POSITION AND DIRECTION ATTRIBUTES.
        '''
        return "Position=%r, Direction=%r" % (list(self._position),
                                              list(self._direction))
    
    def __str__(self): 
        '''
        FUNCTION FORMATS INFORMAL REPRESENTATION WHEN OBJECT IS PRINTED.
        
        Returns
        -------
        POSITION AND DIRECTION ATTRIBUTES.
        
        '''
        return "r=%r, k=%r" % (list(self._position), list(self._direction))
    
    def p(self): 
        '''
        FUNCTION RETURNS THE CURRENT POSITION ATRIBUTE OF THE OBJECT.
        
        Returns
        -------
        POSITION ATTRIBUTE.
        
        '''
        return self._position
    
    def k(self): 
        '''
        FUNCTION RETURNS THE CURRENT DIRECTION ATRIBUTE OF THE OBJECT.
        
        Returns
        -------
        DIRECTION ATTRIBUTE.
        '''
        return self._direction
    
    def append(self,p,k):
        '''
        FUNCTION APPENDS NEW POSITION AND DIRECTION ATTRIBUTES TO THE RAY.

        Parameters
        ----------
        p : LIST
            LIST WITH THREE ELEMENTS CONTAINING THE POSITION OF THE RAY IN 
            CARTESIAN COORDINATES..
        k : LIST
            LIST WITH THREE ELEMENTS CONTAINING THE VECTOR DIRECTION OF THE 
            RAY IN CARTESIAN COORDINATES..

        Raises
        ------
        Exception
            ERROR IS RAISED WHEN NONETYPE OBJECT IS BEING APPENDED, OR OBJECT 
            BEING APPENDED IS OF THE WRONG FORM.

        Returns
        -------
        None.

        '''
        if type(k) == 'NoneType':
            raise Exception('Error: \tCannot append Nonetype object.')
        if type(p) == 'NoneType':
            raise Exception('Error: \tCannot append Nonetype object.')
        if len(p) != 3:
            raise Exception('Error: \tThis simulation is three-dimensional,\
                            therefore all positions must have x,y,z \
                                components.')
        if len(k) != 3:
            raise Exception('Error: \tThis simulation is three-dimensional, \
                            therefore all directions must have x,y,z \
                                components.')
        if k[0] == k[1] == k[2] == 0:
            raise Exception('Error: \tDirection vector cannot be [0,0,0], \
                            this indicates a stationary ray.')
        if any([isinstance(i,str) for i in p]) == \
            True or any([isinstance(i,str) for i in k]) == True:
            raise Exception('Error: \tA string is an invalid input for \
                            position and direction attributes.')
        self._path = np.vstack([self._path, np.array(p)])
        self._pastdirections = np.vstack([self._pastdirections, np.array(k)])
        self._position = np.array(p) # updating attributes
        self._direction = np.array(k)
        return 
    
    def vertices(self):
        ''' 
        FUNCTIONR RETURNS ALL THE POINTS ALONG THE RAY TRAJECTORY.
        
        Returns
        -------
        None.
        '''
        return self._path 




