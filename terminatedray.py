#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains terminated ray class.

Created on Thu Nov 10 16:04:53 2022

@author: MinnieWang
"""

import opticalelement
import ray
import sphericalrefraction
import outputplane
from opticalelement import *
from ray import *
from sphericalrefraction import *
from outputplane import *
import numpy as np
import math

class TerminatedRay():
    ''' CLASS REPRESENTS RAYS THAT HAVE BEEN TERMINATED. '''
    
    def __init__(self, pos, dire):
        '''
        INSTANTIATION METHOD FOR TERMINATED RAY CLASS

        Parameters
        ----------
        pos : LIST
            LIST WITH THREE ELEMENTS CONTAINING THE POSITION OF THE RAY IN 
            CARTESIAN COORDINATES.
        dire : LIST
            LIST WITH THREE ELEMENTS CONTAINING THE VECTOR DIRECTION OF THE 
            RAY IN CARTESIAN COORDINATES. 

        Returns
        -------
        None.

        '''
        self.position = np.array(pos) 
        self.direction  = np.array(dire) 
    