#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module contains functions for ray tracing visulisations.

Created on Thu Nov 24 17:19:22 2022

@author: mw
"""
import matplotlib.pyplot as plt
import numpy as np
import raybundle
from raybundle import *

plt.style.use('dark_background')

def ray_plot_two_lens(ray , lens1 , lens2, out , title):
    '''
    FUNCTION PLOTS RAY DIAGRAM FOR A SYSTEM WITH TWO REFRACTING SURFACES.

    Parameters
    ----------
    ray : RAY
        OBJECT OF RAY CLASS.
    lens1 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE FIRST INCIDENT BY RAYS.
    lens2 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE SECONDLY INCIDENT BY RAYS.
    out : OUTPUT PLANE
        OBJECT OF OUTPUT PLANE CLASS.
    title : STRING
        TITLE OF THE GRAPH.

    Returns
    -------
    None.

    '''
    lens1.propagate_ray(ray)
    lens2.propagate_ray(ray)
    out.propagate_ray(ray)
    
    x_values = [i[0] for i in ray.vertices()]
    z_values = [i[2] for i in ray.vertices()]

    plt.plot(z_values, x_values, '-', color = 'white', label = 'Ray', lw = 0.5)
    plt.axvline(x = out.z0, color = 'gray', label = 'Output Plane')
    plt.axhline(y = 0, xmin = 0, xmax = z_values[-1])
    
    if lens1._curvature == 0 :
        apradius = lens1._ap_radius
        y = np.linspace(-apradius, apradius, 20)
        x = [lens1._z0 for i in y]
        plt.plot(x, y, '-', color = '#C6FFFD', 
                 label = 'Plane Refracting Surface')
    else:
        radius1 = 1 / lens1._curvature
        ang_lim = abs(np.pi - np.arcsin(lens1._ap_radius / radius1))
        angle = np.linspace(np.pi/2+ ang_lim, 3 * np.pi/2 - ang_lim, 150) 
        x = radius1 * np.cos(angle) + (lens1._z0 + radius1)
        y = radius1 * np.sin(angle) 
        figure, axes = plt.subplots(1) 
        plt.plot(x, y, color = '#C6F4FF', label = 'Single Refracting Surface') 
    
    if lens2._curvature == 0 :
        apradius = lens2._ap_radius
        y = np.linspace(-apradius, apradius, 20)
        x = [lens2._z0 for i in y]
        plt.plot(x, y, '-', color = '#C6FFFD',
                 label = 'Plane Refracting Surface')
    else:
        radius2 = 1 / lens2._curvature
        ang_lim2 = abs(np.pi - np.arcsin(lens2._ap_radius / radius2))
        angle1 = np.linspace(np.pi/2 - ang_lim2 , -np.pi/2 + ang_lim2, 150) 
        angle1 = np.linspace(np.arcsin(lens2._ap_radius / radius2),
                             -np.arcsin(lens2._ap_radius / radius2), 150)
        xx = radius2 * np.cos(angle1) + (lens2._z0-radius2)
        yy = radius2 * np.sin(angle1) 
        plt.plot(xx, yy, color = '#C6F4FF', 
                 label = 'Single Refracting Surface') 

    plt.legend()
    plt.xlabel('$z /mm$')
    plt.ylabel('$x /mm$')
    plt.title(title)
    plt.show()

def ray_plot_one_lens(ray , lens1 , out , title):
    '''
    FUNCTION PLOTS RAY DIAGRAM FOR A SYSTEM WITH ONE REFRACTING SURFACE.
    

    Parameters
    ----------
    ray : RAY
        OBJECT OF RAY CLASS.
    lens1 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE FIRST INCIDENT BY RAYS.
    out : OUTPUT PLANE
        OBJECT OF OUTPUT PLANE CLASS.
    title : STRING
        TITLE OF THE GRAPH.

    Returns
    -------
    None.

    '''
    
    lens1.propagate_ray(ray)
    out.propagate_ray(ray)
    
    x_values = [i[0] for i in ray.vertices()]
    z_values = [i[2] for i in ray.vertices()]

    plt.plot(z_values, x_values, '-', color = 'white', label = 'Ray', 
             lw = 0.5)
    plt.axvline(x = out.z0, color = 'gray', label = 'Output Plane')
    plt.axhline(y = 0, xmin = 0, xmax = z_values[-1])
    
    if lens1._curvature == 0 :
        apradius = lens1._ap_radius
        y = np.linspace(-apradius, apradius, 20)
        x = [lens1._z0 for i in y]
        plt.plot(x, y, '-', color = '#C6FFFD', 
                 label = 'Plane Refracting Surface')
    else:
        radius1 = 1 / lens1._curvature
        ang_lim = abs(np.pi - np.arcsin(lens1._ap_radius / radius1))
        angle = np.linspace(np.pi/2+ ang_lim, 3 * np.pi/2 - ang_lim, 150) 
        x = radius1 * np.cos(angle) + (lens1._z0 + radius1)
        y = radius1 * np.sin(angle) 
        plt.plot(x, y, color = '#C6F4FF', label = 'Single Refracting Surface') 

    plt.legend()
    plt.xlabel('$z /mm$')
    plt.ylabel('$x /mm$')
    plt.title(title)
    plt.show()

def multi_ray_plot_one_lens(ray , ray1 , ray2 , lens1 , out , title):
    '''
    FUNCTION PLOTS RAY DIAGRAM FOR A SYSTEM WITH ONE 
    REFRACTING SURFACE FOR MULTIPLE RAYS.

    Parameters
    ----------
    ray : RAY
        OBJECT OF RAY CLASS.
    ray1 : RAY
        OBJECT OF RAY CLASS.
    ray2 : RAY
        OBJECT OF RAY CLASS.
    lens1 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE FIRST INCIDENT BY RAYS.
    out : OUTPUT PLANE
        OBJECT OF OUTPUT PLANE CLASS.
    title : STRING
        TITLE OF THE GRAPH.

    Returns
    -------
    None.

    '''

    lens1.propagate_ray(ray)
    out.propagate_ray(ray)
    x_values = [i[0] for i in ray.vertices()]
    z_values = [i[2] for i in ray.vertices()]

    plt.plot(z_values, x_values, '-', color = 'white', lw = 0.5)
    plt.axvline(x = out._z0, color = 'gray', label = 'Output Plane')
    plt.axhline(y = 0, xmin = 0, xmax = z_values[-1])
    
    lens1.propagate_ray(ray1)
    out.propagate_ray(ray1)
    x_values1 = [i[0] for i in ray1.vertices()]
    z_values1 = [i[2] for i in ray1.vertices()]
    
    plt.plot(z_values1, x_values1, '-', color = 'white', lw = 0.5)
    
    lens1.propagate_ray(ray2)
    out.propagate_ray(ray2)
    x_values2 = [i[0] for i in ray2.vertices()]
    z_values2 = [i[2] for i in ray2.vertices()]
    
    plt.plot(z_values2, x_values2, '-', color = 'white', label = 'Ray',
             lw = 0.5)
    
    if lens1._curvature == 0 :
        apradius = lens1._ap_radius
        y = np.linspace(-apradius, apradius, 20)
        x = [lens1._z0 for i in y]
        plt.plot(x, y, '-', color = '#C6FFFD', 
                 label = 'Plane Refracting Surface')
    else:
        radius1 = 1 / lens1._curvature
        ang_lim = abs(np.pi - np.arcsin(lens1._ap_radius / radius1))
        angle = np.linspace(np.pi/2+ ang_lim, 3 * np.pi/2 - ang_lim, 150) 
        x = radius1 * np.cos(angle) + (lens1._z0 + radius1)
        y = radius1 * np.sin(angle) 
        plt.plot(x, y , color = '#C6F4FF', 
                 label = 'Single Refracting Surface') 

    plt.legend()
    plt.xlabel('$z /mm$')
    plt.ylabel('$x /mm$')
    plt.title(title)
    plt.tight_layout()
    plt.show()

def multi_bundle_plot_two_lens(bundle, lens1, lens2, output, axis):
    '''
    FUNCTION PLOTS RAY DIAGRAM OF INCIDENT BEAMS FOR SYSTEM WITH 
    TWO REFRACTING SURFACES.

    Parameters
    ----------
    bundle : RAY BUNDLE
        OBJECT OF RAY BUNDLE CLASS. REPRESENTATIVE OF A COLLECTION OF INCIDENT 
        COLLIMATED RAYS.
    lens1 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE FIRST INCIDENT BY RAYS.
    lens2 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE SECONDLY INCIDENT BY RAYS.
    out : OUTPUT PLANE
        OBJECT OF OUTPUT PLANE CLASS. 
    axis : AXES SUBPLOT
        NAME OF THE AXES OF A SUBPLOT THE FIGURE IS BEING PLOTTED ON.

    Returns
    -------
    None.

    '''

    for i in range(len(bundle)):
        lens1.propagate_ray(bundle[i])

    for i in range(len(bundle)):
        lens2.propagate_ray(bundle[i])

    for i in range(len(bundle)):
        output.propagate_ray(bundle[i])
        
    xx = [bundle[i].vertices()[j][0] for i \
          in range(0, len(bundle)) for j in range(0, 4)] 
    zz = [bundle[i].vertices()[j][2] for i \
          in range(0, len(bundle)) for j in range(0, 4)]
    
    j = 0
    for i in range(0, len(bundle)):
        axis.plot(zz[j:j + 4], xx[j:j + 4], color = 'white', lw = 0.2)
        j += 4
    
    if lens1._curvature == 0 :
        apradius = lens1._ap_radius
        y = np.linspace(-apradius, apradius, 20)
        x = [lens1._z0 for i in y]
        axis.plot(x, y, '-', color = '#C6FFFD', 
                  label = 'Plane Refracting Surface')
    else:
        radius1 = 1 / lens1._curvature
        ang_lim = np.arcsin(lens1._ap_radius / radius1)
        angle = np.linspace(np.pi - ang_lim, np.pi + ang_lim, 150)
        x = radius1 * np.cos(angle) + (lens1._z0 + radius1)
        y = radius1 * np.sin(angle) 
        axis.plot(x, y , color = '#C6F4FF', 
                  label = 'Single Refracting Surface') 
    
    if lens2._curvature == 0 :
        apradius = lens2._ap_radius
        y = np.linspace(-apradius, apradius, 20)
        x = [lens2._z0 for i in y]
        axis.plot(x, y, '-', color = '#C6FFFD', 
                  label = 'Plane Refracting Surface')
    else:
        radius2 = 1 / lens2._curvature
        angle1 = np.linspace(np.arcsin(lens2._ap_radius / radius2),
                             - np.arcsin(lens2._ap_radius / radius2), 150)
        xx = radius2 * np.cos(angle1) + (lens2._z0 - radius2)
        yy = radius2 * np.sin(angle1) 
        axis.plot(xx, yy , color = '#C6F4FF', 
                  label = 'Single Refracting Surface') 
    
    outradius = output._ap_radius
    y = np.linspace(-outradius, outradius, 40)
    x = [output._z0 for i in y]
    axis.plot(x, y, '-', color = 'gray', label = 'Output Plane')
    #axis.legend()
    return

def single_bundle_plot(bundle, lens1, output, title):
    '''
    FUNCTION PLOTS RAY DIAGRAM OF A BUNDLE RAY FOR A SYSTEM WITH ONE 
    REFRACTING SURFACE.

    Parameters
    ----------
    bundle : RAY BUNDLE
        OBJECT OF RAY BUNDLE CLASS. REPRESENTATIVE OF A COLLECTION OF INCIDENT 
        COLLIMATED RAYS.
    lens1 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE FIRST INCIDENT BY RAYS.
    out : OUTPUT PLANE
        OBJECT OF OUTPUT PLANE CLASS. 
    title : STRING
        TITLE OF THE GRAPH.

    Returns
    -------
    None.

    '''
   
    for i in range(len(bundle)):
        lens1.propagate_ray(bundle[i])

    for i in range(len(bundle)):
        output.propagate_ray(bundle[i])
        
    xx = [bundle[i].vertices()[j][0] for i \
          in range(0, len(bundle)) for j in range(0, 3)] 
    zz = [bundle[i].vertices()[j][2] for i \
          in range(0, len(bundle)) for j in range(0, 3)]
    
    j = 0
    for i in range(0,len(bundle)):
        plt.plot(zz[j:j + 3], xx[j:j + 3], color = 'white', lw = 0.2)
        j += 3
    
    if lens1._curvature == 0 :
        apradius = lens1._ap_radius
        y = np.linspace(-apradius, apradius, 20)
        x = [lens1._z0 for i in y]
        plt.plot(x, y, '-', color = '#C6FFFD', 
                 label = 'Plane Refracting Surface')
    else:
        radius1 = 1 / lens1._curvature
        ang_lim = abs(np.pi - np.arcsin(lens1._ap_radius / radius1))
        angle = np.linspace(np.pi/2 + ang_lim, 3 * np.pi/2 - ang_lim, 150) 
        x = radius1 * np.cos( angle ) + (lens1._z0+radius1)
        y = radius1 * np.sin( angle ) 
        plt.plot( x, y , color = '#C6F4FF', 
                 label = 'Single Refracting Surface') 
    
    plt.legend()
    plt.title(title)
    plt.xlabel('$x / mm$')
    plt.ylabel('$z / mm$')
    plt.show()
    return

def spot_plot_two(bundle, lens1, lens2, output, title , axis):
    '''
    FUNCTION PLOTS SPOT DIAGRAM AT THE SPECIFIED OUTPUT X,Y PLANE FOR A 
    SYSTEM WITH TWO REFRACTING SURFACES.

    Parameters
    ----------
    bundle : RAY BUNDLE
        OBJECT OF RAY BUNDLE CLASS. REPRESENTATIVE OF A COLLECTION OF INCIDENT 
        COLLIMATED RAYS.
    lens1 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE FIRST INCIDENT BY RAYS.
    lens2 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE SECONDLY INCIDENT BY RAYS.
    output : OUTPUT PLANE
        OBJECT OF OUTPUT PLANE CLASS. 
    title : STRING
        TITLE OF THE GRAPH.

    Returns
    -------
    None.

    '''
    
    for i in range(len(bundle)):
        lens1.propagate_ray(bundle[i])

    for i in range(len(bundle)):
        lens2.propagate_ray(bundle[i])

    for i in range(len(bundle)):
        output.propagate_ray(bundle[i])
        
    output_p = RayBundle.output_positions(bundle)
    origin_p = RayBundle.input_positions(bundle)
    
    axis.plot([i[0] for i in output_p],[i[1] for i in output_p], '.',
              color = 'white', label = 'z = Paraxial Focal Plane')
    axis.title.set_text(title)
    axis.set_xlim([-0.013, 0.013])
    axis.set_ylim([-0.013, 0.013])
    
    rms1 = RayBundle.rms(bundle, output_p)

    return
    
def spot_plot_one(bundle, lens1, output, title):
    '''
    FUNCTION PLOTS SPOT DIAGRAM AT THE SPECIFIED OUTPUT X,Y PLANE FOR A 
    SYSTEM WITH ONE REFRACTING SURFACE.
    
    Parameters
    ----------
    bundle : RAY BUNDLE
        OBJECT OF RAY BUNDLE CLASS. REPRESENTATIVE OF A COLLECTION OF INCIDENT 
        COLLIMATED RAYS.
    lens1 : SPHERICAL REFRACTION
        OBJECT OF SPHERICAL REFRACTION CLASS. 
        THE SURFACE FIRST INCIDENT BY RAYS.
    output : OUTPUT PLANE
        OBJECT OF OUTPUT PLANE CLASS. 
    title : STRING
        TITLE OF THE GRAPH.

    Returns
    -------
    None.

    '''
    
    for i in range(len(bundle)):
        lens1.propagate_ray(bundle[i])

    for i in range(len(bundle)):
        output.propagate_ray(bundle[i])
        
    output_p = RayBundle.output_positions(bundle)
    origin_p = RayBundle.input_positions(bundle)
    
    plt.plot([i[0] for i in output_p], [i[1] for i in output_p], '.',
             color = 'white', label = 'z = Paraxial Focal Plane')
    plt.legend()
    plt.title(title)
    plt.xlabel('$x / mm$')
    plt.ylabel('$y / mm$')
    plt.tight_layout()
    plt.show()
    
    rms1 = RayBundle.rms(bundle,output_p)

    return

