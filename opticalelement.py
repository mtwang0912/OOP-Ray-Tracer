#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains functions and class for optical elements.

Created on Thu Nov 10 16:05:47 2022

@author: MinnieWang
"""

import ray
from ray import *

class OpticalElement:
    
    def propagate_ray(self, ray):
        '''
        FUNCTION PROPAGATES RAY THROUGH THE OPTICAL ELEMENT.

        Parameters
        ----------
        ray : RAY
            OBJECT OF RAY CLASS WITH SPECIFIED PROPAGATION DIRECTION AND 
            POSITION.

        Raises
        ------
        NotImplementedError
            ERROR IS RAISED WHEN THE USER ATTEMPTS TO PROPAGATE A RAY THROUGH 
            AN UNSPECIFIED OPTICAL ELEMENT.

        Returns
        -------
        None.

        '''
        "propagate a ray through the optical element"
        raise NotImplementedError()
    