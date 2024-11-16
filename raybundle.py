#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains class and methods to create a ray bundle to model collimated 
light sources.

Created on Sun Nov 13 16:23:07 2022

@author: MinnieWang
"""

import ray
from ray import *
import numpy as np
import matplotlib.pyplot as plt

class RayBundle(ray):
    '''
    CLASS REPRESENTS A BUNDLE OF INDIVIDUAL RAYS.
    '''
    
    def __init__(self, center = [0, 0, 0], direction = [0, 0, 1]):
        '''
        INSTANTIATION METHOD FOR RAY BUNDLE CLASS TO DEFINE RAY ATTRIBUES 
        AND PATH AND DIRECTIONS.

        Parameters
        ----------
        center : LIST, OPTIONAL
            LIST CONTAINING THREE ELEMENTS DESCRIBING THE CENTER POSITION OF A 
            COLLIMATED BEAM. THE DEFAULT IS [0, 0, 0].
        direction : LIST, OPTIONAL
            LIST CONTAINING THREE ELEMENTS DESCRIBING THE DIRECTION OF A 
            COLLIMATED BEAM. THE DEFAULT IS [0, 0, 1].

        Returns
        -------
        None.

        '''
        self._center = np.array(center)
        self._position = [] 
        self._direction = np.array(direction)
        return
    
    def collimated_beam_square(diameter = 10, direction = [0, 0, 1], n = 1): 
        '''
        FUNCTION GENERATES RAY BUNDLE WITH RAYS DISTRIBUTED WITH 
        UNIFORM DENSITY IN CARTESIAN SEPARATION.

        Parameters
        ----------
        diameter : FLOAT, OPTIONAL
            DIAMETER OF THE BUNDLE OF COLLIMATED BEAM. THE DEFAULT IS 10.
        direction : LIST, OPTIONAL
            LIST CONTAINING THREE ELEMENTS DESCRIBING THE DIRECTION OF 
            INDIVIDUAL RAYS IN A COLLIMATED BEAM. THE DEFAULT IS [0, 0, 1].
        n : INTEGER, OPTIONAL
            CROSS-SECTIONAL DENSITY OF THE RAYS, IN N PER MM^2. 
            THE DEFAULT IS 1.

        Returns
        -------
        LIST
            LIST CONTAINS RAY OBJECTS WITH DEFINED POSITINO AND DIRECTION THAT 
            MAKE UP THE COLLIMATED BEAM.

        '''
        xxyy = [[i, j] for i in np.linspace(-diameter / 2, diameter / 2, \
                                            num = diameter*n) for j in \
                np.linspace(-diameter/2,diameter/2, num = diameter*n)]
        xy = [i for i in xxyy if (i[0] ** 2 + i[1] ** 2) <= (diameter / 2) \
              ** 2]
        x = [i[0] for i in xy]
        y = [i[1] for i in xy]
        z = [0 for i in xy]
        positions = np.array(list(zip(x, y, z)))
        return [ray(pos = i, dire = direction) for i in positions]
    
    def collimated_beam_cir(diameter = 5, direction = [0, 0, 1]):
        '''
        FUNCTION GENERATES RAY BUNDLE WITH RAYS DISTRIBUTED WITH UNIFORM 
        DENSITY IN POLAR COORDINATES.

        Parameters
        ----------
        diameter : FLOAT, OPTIONAL
            DIAMETER OF THE BUNDLE OF COLLIMATED BEAM. THE DEFAULT IS 5.
        direction : LIST, OPTIONAL
            LIST CONTAINING THREE ELEMENTS DESCRIBING THE DIRECTION OF 
            INDIVIDUAL RAYS IN A COLLIMATED BEAM. THE DEFAULT IS [0, 0, 1].

        Returns
        -------
        LIST
            LIST CONTAINS RAY OBJECTS WITH DEFINED POSITINO AND DIRECTION THAT 
            MAKE UP THE COLLIMATED BEAM.

        '''
        counter = 0
        positions = []
        r = 0
        radius = diameter / 2
        for i in range(int(2 * radius) + 1):
            if r == 0:
                positions.append((0,0, 0))
            else:
                x = [(r * 0.5) * np.cos(i) for i \
                     in np.linspace(0, 2 * np.pi, num = counter + 1)][:-1]
                y = [(r * 0.5) * np.sin(i) for i \
                     in np.linspace(0, 2 * np.pi, num = counter + 1)][:-1]
                z = [0 for i in x]  
                pos = list(zip(x, y, z))
                for i in range(len(pos)):
                    positions.append(pos[i])
            counter += 6
            r += 1
        positions = np.array(positions)
        return [ray(pos = i, dire = direction) for i in positions]
    
    def input_positions(bundle):
        '''
        FUNCTION EXTRACTS THE INPUT POSITION OF INDIVIDUAL RAYS IN A RAY 
        BUNDLE.

        Parameters
        ----------
        bundle : RAY BUNDLE
            RAY BUNDLE CONTAINING INDIVIDUAL RAYS.

        Returns
        -------
        position : LIST
            LIST CONTAINING THE INPUT POSITIONS OF THE INDIVIDUAL RAYS OF A 
            RAY BUNDLE.

        '''
        position = []
        for i in range(len(bundle)):
            position.append(bundle[i].vertices()[0])
        return position
    
    def intercept_positions(bundle):
        '''
        FUNCTION EXTRACTS THE INTERCEPT POSITION OF INDIVIDUAL RAYS WITH THE 
        FIRST OPTICAL ELEMENT IN A RAY BUNDLE.

        Parameters
        ----------
        bundle : RAY BUNDLE
            RAY BUNDLE CONTAINING INDIVIDUAL RAYS.

        Returns
        -------
        position : LIST
            LIST CONTAINING THE INTERCEPT POSITIONS OF THE INDIVIDUAL RAYS 
            OF A RAY BUNDLE.
        
        '''
        position = []
        for i in range(len(bundle)):
            position.append(bundle[i].vertices()[1])
        return position
    
    def intercept_positions2(bundle):
        '''
        FUNCTION EXTRACTS THE INTERCEPT POSITION OF INDIVIDUAL RAYS WITH THE 
        SECOND OPTICAL ELEMENT IN A RAY BUNDLE.

        Parameters
        ----------
        bundle : RAY BUNDLE
            RAY BUNDLE CONTAINING INDIVIDUAL RAYS.

        Returns
        -------
        position : LIST
            LIST CONTAINING THE INTERCEPT POSITIONS OF THE INDIVIDUAL RAYS 
            OF A RAY BUNDLE.
        
        '''
        position = []
        for i in range(len(bundle)):
            position.append(bundle[i].vertices()[2])
        return position
    
    def output_positions(bundle):
        '''
        FUNCTION EXTRACTS THE INTERCEPT POSITION OF INDIVIDUAL RAYS WITH THE 
        OUTPUT PLANE IN A RAY BUNDLE.

        Parameters
        ----------
        bundle : RAY BUNDLE
            RAY BUNDLE CONTAINING INDIVIDUAL RAYS.

        Returns
        -------
        position : LIST
            LIST CONTAINING THE OUTPUT POSITIONS OF THE INDIVIDUAL RAYS OF A 
            RAY BUNDLE.
        
        '''
        position = []
        for i in range(len(bundle)):
            position.append(bundle[i].vertices()[-1])
        return position
    
    def rms(bundle, output):
        '''
        FUNCTION OUTPUTS THE ROOT MEAN SQURE SPOT RADIUS OF RAYS AT THE 
        SPECIFIED OUTPUT PLANE.

        Parameters
        ----------
        bundle : LIST
            LIST CONTAINS INDIVIDUAL RAY OBJECTS.
        output : LIST
            LIST CONTAINS OUTPUT POSITIONS OF INDIVIDUAL RAYS.

        Returns
        -------
        FLOAT
            ROOT MEAN SQUARE SPOT RADIUS.

        '''
        rms = sum([output[i][0] ** 2 + output[i][1] ** 2 for i \
                   in range(len(output))])
        print('RMS: ', np.sqrt(rms / len(bundle)))
        return np.sqrt(rms / len(bundle))
        
    def three_d_plot(bundle, title):
        '''
        FUNCTION PLOTS THREE DIMENSIONAL RAY TRAJECTORY.

        Parameters
        ----------
        bundle : LIST
           LIST CONTAINS INDIVIDUAL RAY OBJECTS.

        Returns
        -------
        None.

        '''
        intercepts = len(bundle[0].vertices())
        xx = [bundle[i].vertices()[j][0] for i in range(0, len(bundle)) for \
              j in range(0, intercepts)] #extract x and z values
        yy = [bundle[i].vertices()[j][1] for i in range(0, len(bundle)) for \
              j in range(0, intercepts)]
        zz = [bundle[i].vertices()[j][2] for i in range(0, len(bundle)) for \
              j in range(0, intercepts)]
        ax = plt.axes(projection = '3d')
        ax.plot3D(xx, yy ,zz)
        ax.set_title(title)
        ax.set_xlabel("$x$ / $mm$")
        ax.set_ylabel("$y$ / $mm$")
        ax.set_zlabel("$z$ / $mm$")
        j = 0
        for i in range(0,len(bundle)):
            ax.plot(xx[j:j + 4], yy[j:j + 4], zz[j:j + 4], color = 'white', 
                    alpha = 0.05)
            j += 4
        return




