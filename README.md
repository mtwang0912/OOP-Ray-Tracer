# OOP-Ray-Tracer
Object Orientation Programming: Optical Ray Tracer Simulation

The full report is available at: https://github.com/mtwang0912/OOP-Ray-Tracer/blob/main/02020640_ray.pdf

# Overview of Achievements
The project successfully developed a simulation to model the behavior of light rays interacting with optical elements, focusing on spherical aberrations. The simulation was capable of:
- Accurately modeling ray optics with minimal errors when neglecting spherical aberration, achieving a deviation as low as 3.4 × 10^-8% in non-aberrant conditions.
- Investigating spherical aberrations and demonstrating the relationship between transverse spherical aberration (TSA) and longitudinal spherical aberration (LSA) with a 1.5% deviation from the true value.
- Optimizing lens parameters to minimize aberrations, specifically focusing on plano-convex lenses and demonstrating the success of different optimization methods.

# Key Technical Features of the Code
- **Object-Oriented Programming**: Used object-oriented programming to model optical elements, making the code modular and extendable.
- **Mathematical Modelling**: Implemented a three-dimensional version of Snell’s Law to accurately simulate ray refraction through lenses.
- **Optimization Algorithms**:
  - Utilized various optimization methods from the scipy.optimize library, including Nelder-Mead, Conjugate Gradient (CG), L-BFGS-B, TNC, and Sequential Least Squares Quadratic Programming (SLSQP).
  - Developed functions that take lens parameters as input and return the root mean square (RMS) spot radius to identify configurations that minimize spherical aberrations.
- **Ray Propagation and Analysis**: Simulated ray tracing to identify intersection points and calculate deviations between simulated and theoretical focal points.
- **Performance and Accuracy Evaluation**: Analyzed results using RMS spot radius and examined the behavior of incident beams of varying diameters.

# Results
## Simulation Accuracy:
Achieved a high level of precision in ray optics without considering spherical aberration, with only 2.25 × 10^-6 mm deviation from the theoretical paraxial focal point.

## Optimization Results:
- The simulation consistently identified plano-convex lenses with a convex anterior surface as optimized configurations.
- The average curvature of optimized lenses was 0.02902 ± 0.0005 mm, demonstrating high consistency across different minimization methods.

## Aberration Analysis:
- The RMS spot radius and associated aberrations were measured for various lens configurations.
- The mean ratio between LSA and TSA showed a 1.5% deviation from the theoretical value, highlighting the effectiveness of the simulation in modeling spherical aberration.

## Limitations Identified:
- The simulation's assumption of light as a geometric ray, without accounting for wave properties, introduced systematic errors in modeling TSA and LSA.
- Optimization was limited by the set boundaries to prevent non-intercepting rays, potentially restricting more optimal solutions.
