#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The python file plots all the figures included in the report. 

Created on Sat Nov 26 16:35:42 2022

@author: MinnieWang
"""
import opticalelement
import terminatedray
import ray
import sphericalrefraction
import outputplane
import raybundle
import lensop
from lensop import *
from raybundle import *
from terminatedray import *
from opticalelement import *
from ray import *
from sphericalrefraction import *
from outputplane import *
import plotter
from plotter import *
import pandas as pd
import scipy.optimize

#%% Figure 1

RAY = ray(pos = [0.01,0,0], dire = [0,0,1])
RAY1 = ray(pos = [5,0,0], dire = [0,0,1])
RAY2 = ray(pos = [-5,0,0], dire = [0,0,1])

SSRS = SphericalRefraction(z0 = 100, curv = 0.03, n1 = 1, n2 = 1.5, aprad = 20)
OUT = OutputPlane(z0 = 250, aprad = 200)
title1 = 'Figure 1: Tracing the trajectory of a ray through the specified \
spherical surface.'
plotter.multi_ray_plot_one_lens(RAY, RAY1, RAY2, SSRS, OUT, 
                                title = title1)

#%% Figure 2

RAY = ray(pos = [0,0,0], dire = [0,0,1])
RAY1 = ray(pos = [10,0,0], dire = [0,0,1])
RAY2 = ray(pos = [20,0,0], dire = [0,0,1])

SSRS = SphericalRefraction(z0 = 100, curv = 0.03, n1 = 1, n2 = 1.5, aprad = 20)
OUT = OutputPlane(z0 = 250, aprad = 200)
title2 = 'Figure 2: Investigation of a spherical surface\'s \
ability for image formation.'
plotter.multi_ray_plot_one_lens(RAY,RAY1,RAY2, SSRS, OUT, title2)

#%% Figure 3

BUNDLE = RayBundle.collimated_beam_cir(diameter = 5, direction = [0,0,1])

SSRS = SphericalRefraction(z0 = 100, curv = 0.03, n1 = 1, n2 = 1.5, aprad = 20)
OUT = OutputPlane(z0 = 250, aprad = 200)
title3 = 'Figure 3: Tracing the trajectory of collimated rays'
plt.ylim(-4,4)
plotter.single_bundle_plot(BUNDLE, SSRS, OUT, title3)

#%% Figure 4

BUNDLE = RayBundle.collimated_beam_cir(diameter = 5, direction = [0,0,1])

SSRS = SphericalRefraction(z0 = 100, curv = 0.03, n1 = 1, n2 = 1.5, aprad = 20)
FOC = OutputPlane(z0 = 166.66670666666667, aprad = 200) # paraxial focal plane
title4 = 'F4: Spot diagram at the paraxial focal plane'
plt.figure(figsize = [8,8])
plotter.spot_plot_one(BUNDLE, SSRS, FOC, title4)

#%% Figure 5

fig,(ax1, ax2) = plt.subplots(2)
title5 = 'Figure 5: Trajectories for the plano-convex lens in both \
orientations'
fig.suptitle(title5)
BUNDLE = RayBundle.collimated_beam_cir(diameter = 10 , direction = [0,0,1])

thickness = 5
n_glass = 1.5168

PLANO = SphericalRefraction(z0 = 100, curv = 0, n1 = 1, n2 = n_glass,
                            aprad = 20)
CON = SphericalRefraction(z0 = 100 + thickness, curv = 0.02, n1 = n_glass,
                          n2 = 2, aprad = 20)
OUT = OutputPlane(z0 = 400, aprad = 20)

plotter.multi_bundle_plot_two_lens(BUNDLE, PLANO, CON, OUT, ax1)

BUNDLE1 = RayBundle.collimated_beam_cir(diameter = 10, direction = [0,0,1])

PLANO1 = SphericalRefraction(z0 = 100 + thickness, curv = 0, n1 = n_glass, 
                             n2 = 1, aprad = 20)
CON1 = SphericalRefraction(z0 = 100, curv = 0.02, n1 = 1, n2 = n_glass, 
                           aprad = 20)

ax2.set_xlabel('$z$ / $mm$')
ax1.set_ylabel('$x$ / $mm$')
ax2.set_ylabel('$x$ / $mm$')

plotter.multi_bundle_plot_two_lens(BUNDLE1, CON1, PLANO1, OUT, ax2)
plt.tight_layout()
plt.show()

#%% Figure 6

thickness = 5
n_glass = 1.5168

d = 10


BUNDLE = RayBundle.collimated_beam_cir(diameter = d, direction = [0,0,1])
PLANO = SphericalRefraction(z0 = 100, curv = 0, n1 = 1, n2 = n_glass, 
                            aprad = 20)
CON = SphericalRefraction(z0 = 100 + thickness, curv = 0.02, n1 = n_glass, 
                          n2 = 2, aprad = 20)
OUT = OutputPlane(z0 = 400, aprad = 400)

# Finding the focal plane
RAY = ray(pos = [1,0,0], dire = [0,0,1])
PLANO.propagate_ray(RAY)
CON.propagate_ray(RAY)
OUT.propagate_ray(RAY)
OUT = OutputPlane(z0 = lensop.focal(RAY), aprad = 400)

#plotter.spot_plot_two(BUNDLE , PLANO , CON , OUT, 'Plane side first')

#plt.subplot(1, 2, 2) # convex first
BUNDLE1 = RayBundle.collimated_beam_cir(diameter = d, direction = [0,0,1])

PLANO1 = SphericalRefraction(z0 = 100 + thickness, curv = 0, n1 = n_glass, 
                             n2 = 1, aprad = 20)
CON1 = SphericalRefraction(z0 = 100, curv = 0.02, n1 = 1, n2 = n_glass, 
                           aprad = 20)

# Finding the focal plane
RAY1 = ray(pos = [1,0,0], dire = [0,0,1])
CON1.propagate_ray(RAY1)
PLANO1.propagate_ray(RAY1)
OUT.propagate_ray(RAY1)
OUT1 = OutputPlane(z0 = lensop.focal(RAY1), aprad = 400)

#Plot

def exp(x, a, b, c):
    return a * np.exp(b * x) + c

def quad(x, a, b, c):
    return a * (x ** 2) + b * x + c

t15_df = pd.read_csv('T15_cir.csv')


d = [-i for i in t15_df['Diameter / mm']]
d1 = [i for i in t15_df['Diameter / mm']]
dd = d + d1
r1 = [i for i in t15_df['RMS (Convex first)']]
r11 = [i for i in t15_df['RMS (Convex first)']]
rr1 = r1 + r11
popt_c = np.polyfit(dd, rr1, 2)
r2 = [i for i in t15_df['RMS (Plano first)']]
r22 = [i for i in t15_df['RMS (Plano first)']]
rr2 = r2 + r22
popt_p = np.polyfit(dd, rr2, 2)

diff = t15_df['RMS (Plano first)'] - t15_df['RMS (Convex first)']
fig,ax = plt.subplots()
x = np.linspace(0, 25, 100)
x1 = np.linspace(25, 40, 100)
title6 = 'Figure 6: Investigation of the performance of plano-convex lens \
in both orientations'
fig.suptitle(title6)
ax.plot(t15_df['Diameter / mm'],t15_df['RMS (Plano first)'],color="blue", 
        marker=".", label = '$RMS_{p}$')
ax.plot(t15_df['Diameter / mm'],t15_df['RMS (Convex first)'],color="red", 
        marker=".", label = '$RMS_{c}$')
ax.set_xlabel("Diameter / $mm$", fontsize = 14)
ax.legend()
#ax.set_yscale('log')
ax.set_ylabel("RMS Spot Radius / $mm$",color="white",fontsize=14)
ax2=ax.twinx()

popt, pcov = scipy.optimize.curve_fit(exp, t15_df['Diameter / mm'][:13], 
                                      diff[:13])
ax2.plot(x, exp(x,*popt), '--', label = 'Fit Line')
print('Fit equation for increase in difference is :', popt[0], '* exp(', 
      popt[1], 'x) + ', popt[2])

ax2.plot(t15_df['Diameter / mm'], diff, color="gray",marker=".")
ax2.set_ylabel("$RMS_{p} - RMS_{c}$ / $mm$",color="gray",fontsize=14)
ax2.legend()
plt.tight_layout()
plt.show()

#%% Figure 7

fig,ax = plt.subplots(figsize=(10,10))
title7 = 'Figure 7: Plano-Convex Lens Optimisation by Minimisation of \
RMS Spot Radius'
fig.suptitle(title7)
ax1 = plt.subplot(2,2,1)
ax2 = plt.subplot(2,2,2)
ax3 = plt.subplot(2,2,3)
ax4 = plt.subplot(2,2,4)
plt.figure(figsize = [80,80])

#TNC

th = 4.94301552
n_glass = 1.5168

BUNDLE = RayBundle.collimated_beam_cir(diameter = 10, direction = [0,0,1])

CON = SphericalRefraction(z0 = 100, curv = 0.02880949, n1 = 1, n2 = n_glass,
                          aprad = 20)
PLANO = SphericalRefraction(z0 = 100 + th, curv = 0, n1 = n_glass, n2 = 1, 
                            aprad = 20)
OUT = OutputPlane(z0 = 200, aprad = 400)
ax1.set_ylabel('$y$ / $mm$')
plotter.spot_plot_two(BUNDLE, CON, PLANO, OUT, 'Method 1: BFGS', ax1)
print('^^ Method = TNC')

#Nelder-Mead

th = 20

BUNDLE1 = RayBundle.collimated_beam_cir(diameter = 10, direction = [0,0,1])

CON = SphericalRefraction(z0 = 100, curv = 0.02674652, n1 = 1, n2 = n_glass, 
                          aprad = 20)
PLANO = SphericalRefraction(z0 = 100 + th, curv = 0, n1 = n_glass, n2 = 1, 
                            aprad = 20)
OUT = OutputPlane(z0 = 200, aprad = 400)

plotter.spot_plot_two(BUNDLE1, CON, PLANO, OUT, 'Method 2: Nelder-Mead', ax2)
print('^^ Method = Nelder-Mead')

#L-BFGS-B

th = 1.00140564

BUNDLE2 = RayBundle.collimated_beam_cir(diameter = 10, direction = [0,0,1])

CON = SphericalRefraction(z0 = 100, curv = 0.0294035, n1 = 1, n2 = n_glass, 
                          aprad = 20)
PLANO = SphericalRefraction(z0 = 100 + th, curv = 0, n1 = n_glass, n2 = 1, 
                            aprad = 20)
OUT = OutputPlane(z0 = 200, aprad = 400)
ax3.set_xlabel('$x$ / $mm$')
ax3.set_ylabel('$y$ / $mm$')
plotter.spot_plot_two(BUNDLE2, CON, PLANO, OUT, 'Method 3: L-BFGS-B', ax3)
print('^^ Method = L-BFGS-B')

#SLSQP

th = 0.98921642

BUNDLE2 = RayBundle.collimated_beam_cir(diameter = 10, direction = [0,0,1])

CON = SphericalRefraction(z0 = 100, curv = 0.02940531, n1 = 1, n2 = n_glass, 
                          aprad = 20)
PLANO = SphericalRefraction(z0 = 100 + th, curv = 0, n1 = n_glass, n2 = 1, 
                            aprad = 20)
OUT = OutputPlane(z0 = 200, aprad = 400)
ax4.set_xlabel('$x$ / $mm$')
plotter.spot_plot_two(BUNDLE2, CON, PLANO, OUT, 'Method 3: SLSQP', ax4)
print('^^ Method = SLSQP')
fig.tight_layout()
plt.show()

#%% Figure 8a

th = 1.00140564
n_glass = 1.5168
fig,ax = plt.subplots()

B1 = RayBundle.collimated_beam_cir(diameter = 10, direction = [0,0,1])

CON = SphericalRefraction(z0 = 100, curv = 0.029403, n1 = 1, n2 = n_glass, 
                          aprad = 20)
PLANO = SphericalRefraction(z0 = 100 + th, curv = 0, n1 = n_glass, n2 = 1, 
                            aprad = 20)
OUT = OutputPlane(z0 = 250, aprad = 20)

title8a = 'Figure 8a: Trajectory of beam through optimised lens by \
L-BFGS-B method'
ax.title.set_text(title8a)
ax.set_xlabel('$z$ / $mm$')
ax.set_ylabel('$x$ / $mm$')
ax.set_ylim([-7.5,7.5])
plt.tight_layout()
plotter.multi_bundle_plot_two_lens(B1, CON , PLANO , OUT , ax)
plt.show()

#%% Figure 8b

fig,ax = plt.subplots(figsize=(10,10))
title8b = 'Figure 8b: Demonstration of spherical aberration with \
optimised lens'
ax.title.set_text(title8b)
ax.set_xlabel('$z$ / $mm$')
ax.set_ylabel('$x$ / $mm$')
ax.set_xlim([198.5, 201.5])
ax.set_ylim([-0.08, 0.08])

plotter.multi_bundle_plot_two_lens(B1, CON , PLANO , OUT , ax)
plt.tight_layout()
plt.show()

ray1 = ray(pos = [0.01,0,0], dire = [0,0,1])
CON.propagate_ray(ray1)
PLANO.propagate_ray(ray1)
OUT.propagate_ray(ray1)

fp = lensop.focal(ray1)
print('The paraxial focal point is at z =', fp, 'mm.')
print('The circle of least confusion is at z = 200 mm.')

sa = lensop.sph_abe(r1 = 1/CON._curvature, r2 = 0, n = n_glass, o = 100, 
                    i = 250, h = 5, f = fp)
#lensop.sph_abe(r1, r2, n, o, i, h, f)

#%% TSA and LSA analysis
th = 1.00140564
n_glass = 1.5168
RAY = ray(pos = [0.01,0,0], dire = [0,0,1])
CON = SphericalRefraction(z0 = 100, curv = 0.02940, n1 = 1, n2 = n_glass, 
                          aprad = 20)
PLANO = SphericalRefraction(z0 = 100 + th, curv = 0, n1 = n_glass, n2 = 1, 
                            aprad = 20)
OUT = OutputPlane(z0 = 300, aprad = 400)
CON.propagate_ray(RAY)
PLANO.propagate_ray(RAY)
OUT.propagate_ray(RAY)

f = lensop.focal(RAY)

FP = OutputPlane(z0 = f, aprad = 400)
BUNDLE = RayBundle.collimated_beam_cir(diameter = 10, direction = [0,0,1])

for i in range(len(BUNDLE)):
    CON.propagate_ray(BUNDLE[i])
for i in range(len(BUNDLE)):
    PLANO.propagate_ray(BUNDLE[i]) 
for i in range(len(BUNDLE)):
    FP.propagate_ray(BUNDLE[i]) 

output = RayBundle.output_positions(BUNDLE)
out_x = [i[0] for i in output]
print('The actual transverse spherical aberration is: ', max(out_x))
#rms = RayBundle.rms(BUNDLE, output) 

#LSA analysis

ray_c = ray(pos = [0.001,0,0], dire = [0,0,1])
ray_f = ray(pos = [5,0,0], dire = [0,0,1])
elems = [CON, PLANO, OUT]
CON.propagate_ray(ray_c)
PLANO.propagate_ray(ray_c)
OUT.propagate_ray(ray_c)

CON.propagate_ray(ray_f)
PLANO.propagate_ray(ray_f)
OUT.propagate_ray(ray_f)
f1 = abs(lensop.focal(ray_c) - lensop.focal(ray_f))

print('The actual longitudinal spherical aberration is: ', f1)

lensop.sph_abe(1/CON._curvature, 0, n_glass, 100, 100, 5, f)

#%% Figure 9

#%matplotlib 
plt.figure(num = 9)
title9 = 'Figure 9: Optimised plano-convex lens ray trajectory'
RayBundle.three_d_plot(B1, title = title9)
plt.show()





