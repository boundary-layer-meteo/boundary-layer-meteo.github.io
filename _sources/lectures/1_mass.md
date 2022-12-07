# Conservation of mass

```{admonition} Questions to be answered
1. What is the equation for conservation of mass in the atmospheric boundary layer?
1. Which assumptions are made to get to this equation?
```

## Derivation
Density $\rho$ is the variable that captures the mass of the atmosphere.
For a certain control volume $\delta x\, \delta y\, \delta z$, the mass $M$ is

$$
M = \rho \, \delta x \, \delta y \, \delta z
$$

If we want to estimate mass changes within a time period $\delta t$, then the change of mass is the balance of all fluxes through the faces of the control volume.
We can write out the balance:

$$
\rho_{x, y, z, t+\delta t} \, \delta x \, \delta y \, \delta z - \rho_{x, y, z, t} \, \delta x \, \delta y \, \delta z
&= \left( \rho u \right)_{x, y, z, t} \, \delta y \, \delta z \, \delta t - \left( \rho u \right)_{x + \delta x, y, z, t} \, \delta y \, \delta z \, \delta t \\
&+ \left( \rho v \right)_{x, y, z, t} \, \delta x \, \delta z \, \delta t - \left( \rho v \right)_{x, y + \delta y, z, t} \, \delta x \, \delta z \, \delta t \\
&+ \left( \rho w \right)_{x, y, z, t} \, \delta x \, \delta y \, \delta t - \left( \rho w \right)_{x, y, z + \delta z, t} \, \delta x \, \delta y \, \delta t
$$

If we assume that the box and the time step are infinitisimal, then we can use a Taylor expansions of the following kind, to substitute in the differences that are calculated in the equation above.

$$
\left( \rho u \right)_{x + \delta x, y, z, t} = \left( \rho u \right)_{x, y, z, t} + \left( \dfrac{ \partial \rho u }{ \partial x } \right)_{x, y, z, t} \delta x
$$

Substitution leads to the following equation, where the $x, y, z, t$ subscript is omited since it applies to all partial derivatives.

$$
\dfrac{ \partial \rho }{ \partial t } \, \delta x \, \delta y \, \delta z \, \delta t
= - \dfrac{ \partial \rho u }{ \partial x } \, \delta x \, \delta y \, \delta z \, \delta t
  - \dfrac{ \partial \rho v }{ \partial y } \, \delta x \, \delta y \, \delta z \, \delta t
  - \dfrac{ \partial \rho w }{ \partial z } \, \delta x \, \delta y \, \delta z \, \delta t
$$

And after dividing out the volume and time, and moving all terms to the left hand side, we get the conservation of mass equation.

$$
\dfrac{ \partial \rho }{ \partial t } + \dfrac{\partial \rho u}{\partial x} + \dfrac{\partial \rho v}{\partial y} + \dfrac{\partial \rho w}{\partial z} = 0
$$

or in index notation. Note that small perturbations also requires that the layer is shallow to the extent that the density change between the surface and the top of the boundary layer is small compared to the mean density $\overline{\rho}$.


$$
\dfrac{ \partial \rho }{ \partial t } + \dfrac{\partial \rho u_j}{\partial x_j} = 0
$$

We can also rewrite this expression into the Lagrangian form of the conservation of mass:

$$
\dfrac{\partial \rho}{\partial t} + u_j \dfrac{\partial \rho}{\partial x_j} = - \rho \dfrac{\partial u_j}{\partial x_j}
$$

---

## The Boussinesq approximation
We split the density into a slow moving part and a part that contains the fluctuations due to turbulence $\rho = \overline{\rho} + \rho^\prime$.
We can rewrite the conservation of mass as

$$
\dfrac{ \partial \overline{\rho} }{ \partial t } + \dfrac{ \partial \rho^\prime }{ \partial t } 
+ u_j \dfrac{\partial \overline{\rho} }{\partial x_j} + u_j \dfrac{\partial \rho^\prime}{\partial x_j}
= - \left( \overline{\rho} + \rho^\prime \right) \dfrac{\partial u_j}{\partial x_j}
$$

If we assume that the mean density state is changing so slowly in space and time to the extent that it can be assumed constant, and we further assume that $\rho^\prime \ll \overline{\rho}$, then the equation reduces to:

$$
\overline{\rho} \dfrac{\partial u_j}{\partial x_j} = 0
$$

or

$$
\dfrac{\partial u_j}{\partial x_j} = 0
$$

The latter equation is the conservation of mass we use to study atmospheric boundary layers, and is often called conservation of volume due to the absence of a density term.
