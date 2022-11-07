# Conservation of momentum (ii)

```{admonition} Questions to be answered
1. What is the closure problem?
1. What is K-theory?
1. What is the Ekman spiral and how is it derived?
1. Why is the wind profile in the atmosphere logarithmic?
```

$\def\pd#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\rhobar{\overline{\rho}}$
$\def\pdd#1#2{\dfrac{\partial^2 #1}{\partial#2^2}}$
$\def\uibar{\overline{u_i}}$
$\def\uiprime{u_i^\prime}$
$\def\ujbar{\overline{u_j}}$
$\def\ujprime{u_j^\prime}$
$\def\ubar{\overline{u}}$
$\def\vbar{\overline{v}}$
$\def\wbar{\overline{w}}$
$\def\uwflux{\overline{u^\prime w^\prime}}$
$\def\vwflux{\overline{v^\prime w^\prime}}$
$\def\zom{z_{\mathrm{0m}}}$

## The closure problem
The starting point is the equation as derived in the previous section.

$$
  \pd{\ubar}{t}
=
- \pd{\overline{ u^\prime w^\prime }}{z}
+ f \left( \vbar - v_g \right) \\
  \pd{\vbar}{t}
=
- \pd{\overline{ v^\prime w^\prime }}{z}
- f \left( \ubar - u_g \right)
$$

This set cannot be solved, because Reynolds averaging introduced two new variables $\uwflux$ and $\vwflux$.
This problem is called the _closure problem_.
The work of Prandtl brought forward the philosophy of treating turbulent fluxes as diffusive fluxes, which allow the equations to be closed as:

$$
\uwflux &= - K_m \pd{\ubar}{z} \\
\vwflux &= - K_m \pd{\vbar}{z} \\
$$

This approach is called *K-theory*, and variable $K_m$ is called the *eddy diffusivity*.

## The Ekman spiral
Ekman used the simplest form of K-theory by choosing a constant value for $K_m$ and in addition he assumed a steady state, and no geostrophic wind in the north-south direction ($v_g = 0$). This gives the set:

$$
0 &= K_m \pdd{\ubar}{z} + f \vbar \\
0 &= K_m \pdd{\vbar}{z} - f \left( \ubar - u_g \right)
$$

He solved the set analytically for the following boundary conditions: $\ubar(z = 0) = 0$, $\vbar(z = 0) = 0$ and $\ubar(z = \infty) = u_g$, $\vbar(z = \infty) = 0$.
The solution is

$$
\ubar &= u_g \left( 1 - \exp \left( - \gamma z \right) \cos \left( \gamma z \right) \right) \\
\vbar &= u_g \left(     \exp \left( - \gamma z \right) \sin \left( \gamma z \right) \right) \\
\gamma &= \left( \dfrac{f}{2 K_m} \right)^\frac{1}{2}
$$


## The logarithmic wind profile
The lab experiments of Prandtl showed that K-theory with constant values of $K_m$ does not reproduce the logarithmic profiles that were observed in the lab or in the atmosphere.

The eddy diffusivity $K_m$, with units of $\mathrm{m^2\ s^{-1}}$ can be seen as a multiplication of a length scale that measures the scale of mixing eddies, and a velocity scale that measures the intensity of mixing.
Prandtl discovered that the relevant length scale is the distance from the wall, whereas the relevant mixing intensity is the surface friction $u_*$ which is defined as $u_*^2 \equiv \left( \uwflux^2_0 + \vwflux^2_0 \right)^\frac{1}{2}$.

If we assume that the boundary layer is much deeper than the surface layer, we can assume that the momentum flux is by approximation constant in the surface layer. If we then align our coordinate system with the wind, we can write

$$
\uwflux \approx \uwflux_0 &= - K_m \pd{\ubar}{z} \\
                  - u_*^2 &= - \kappa z u_* \pd{\ubar}{z} \\
                    u_*^2 &= \kappa z u_* \pd{\ubar}{z}
$$

With some reshuffling, we can rewrite the equation and subsequently integrate it from $z_1$ to $z_2$

$$ 
\int_{z_1}^{z_2} \pd{\ubar}{z} \textrm{d}z &= \int_{z_1}^{z_2} \dfrac{u_*}{\kappa} \dfrac{1}{z} \textrm{d}z \\
u(z_2) - u(z_1) &= \dfrac{u_*}{\kappa} \left( \ln(z_2) - \ln(z_1) \right) \\
u(z_2) - u(z_1) &= \dfrac{u_*}{\kappa} \ln \left( \dfrac{z_2}{z_1} \right)
$$

If we assume the logarithmic profile to be zero at the roughness length for momentum $\zom$ then, the wind $u$ at height $z$ can be computed following

$$ 
u(z) = \dfrac{u_*}{\kappa} \ln \left( \dfrac{z}{\zom} \right)
$$

This the famous expression for the logarithmic wind profile, also known in fluid dynamics as the *law of the wall*.
