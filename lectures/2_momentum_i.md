# Conservation of momentum (i)

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

## Conservation of momentum in an incompressible atmospheric boundary layer.
Wind is a key ingredient of boundary layer meteorology.
The evolution of wind speed is generally covered via the conservation of momentum, also known as the Navier-Stokes equations.

First, we introduce the equations for horizontal momentum for an incompressible flow, where we have already introduced the mean density $\rhobar$, and we will also split the other thermodynamic variable $p$ in a mean and a perturbation.

$$
\pd{u}{t} + u_j \pd{u}{x_j} &= - \dfrac{1}{\rhobar} \pd{\overline{p}}{x} - \dfrac{1}{\rhobar} \pd{p^\prime}{x} + f v + \nu \pdd{u}{x_j} \\
\pd{v}{t} + u_j \pd{v}{x_j} &= - \dfrac{1}{\rhobar} \pd{\overline{p}}{y} - \dfrac{1}{\rhobar} \pd{p^\prime}{y} - f u + \nu \pdd{v}{x_j}
$$

We can now substitute the mean pressure gradient by the geostrophic wind definitions $fv_g \equiv \dfrac{1}{\rhobar}\pd{p}{x}$ and $fu_g \equiv - \dfrac{1}{\rhobar}\pd{p}{y}$ to get:

$$
\pd{u}{t} + u_j \pd{u}{x_j} &= - \dfrac{1}{\rhobar} \pd{p^\prime}{x} + f \left( v - v_g \right) + \nu \pdd{u}{x_j} \\
\pd{v}{t} + u_j \pd{v}{x_j} &= - \dfrac{1}{\rhobar} \pd{p^\prime}{y} + f \left( u - u_g \right) + \nu \pdd{v}{x_j}
$$

For the vertical momentum equations, we briefly take a step back and reintroduce the density perturbation and multiply the equation with $\rho$:

$$
\left( \rhobar + \rho^\prime \right) \pd{w}{t} + \left( \rhobar + \rho^\prime \right) u_j \pd{w}{x_j} = - \pd{\overline{p}}{z} - \pd{p^\prime}{z} - \left( \rhobar + \rho^\prime \right) g + \nu \pdd{w}{x_j}
$$

We know that in on the larger scales, the flow is in hydrostatic balance $\pd{\overline{p}}{z} = - \rhobar g$, and hence we can eliminate these very large terms from the equation. If we divide out $\rho$ again, and neglect perturbations, we get:

$$
\pd{w}{t} + u_j \pd{w}{x_j} = - \dfrac{1}{\rhobar} \pd{p^\prime}{z} - \dfrac{\rho^\prime}{\rhobar} g + \nu \pdd{w}{x_j}
$$

With index notation, we can combine the three momentum equations:

$$
\pd{u_i}{t} + u_j \pd{u_i}{x_j} = \pd{p^\prime}{x_i} - f \epsilon_{ij3} \left( u_j - u_{g,j} \right) - \delta_{i3} \dfrac{\rho^\prime}{\rhobar} g + \nu \pdd{u_i}{x_j}
$$

The last step is to put the advection term in the flux form. With the help of the chain rule, we can write:

$$
\pd{u_i u_j}{x_j} = u_j \pd{u_i}{x_j} + u_i \pd{u_j}{x_j}
$$

The latter term is zero because of incompressibility, thus we can write our final equation as:

$$
\pd{u_i}{t} + \pd{u_i u_j}{x_j} = - \dfrac{1}{\rhobar} \pd{p^\prime}{x_i} + f \epsilon_{ij3} \left( u_j - u_{g,j} \right) - \delta_{i3} \dfrac{\rho^\prime}{\rhobar} g + \nu \pdd{u_i}{x_j}
$$

## Reynolds averaging the velocity components
We will now introduce the Reynolds averaging of the velocity components, thus we split all velocity instances in a mean and a perturbation.

$$
\pd{\uibar}{t} + \pd{\uiprime}{t}
+ \pd{\uibar \ujbar}{x_j}
+ \pd{\uiprime \ujbar}{x_j}
+ \pd{\uibar \ujprime}{x_j}
+ \pd{\uiprime \ujprime}{x_j}
= \\ 
- \dfrac{1}{\rhobar} \pd{p^\prime}{x_i}
+ f \epsilon_{ij3} \left( \ujbar + \ujprime - u_{g,j} \right)
- \delta_{i3} \dfrac{\rho^\prime}{\rhobar} g
+ \nu \pdd{\uibar}{x_j}
+ \nu \pdd{\uiprime}{x_j}
$$

We are interested to retrieve the evolution of the mean velocity $\uibar$, so we take the mean of the entire equation. 

$$
\overline{ \pd{\uibar}{t}
+ \pd{\uiprime}{t}
+ \pd{\uibar \ujbar}{x_j}
+ \pd{\uiprime \ujbar}{x_j}
+ \pd{\uibar \ujprime}{x_j}
+ \pd{\uiprime \ujprime}{x_j}
= } \\ 
\overline {- \dfrac{1}{\rhobar} \pd{p^\prime}{x_i}
+ f \epsilon_{ij3} \left( \ujbar + \ujprime - u_{g,j} \right)
- \delta_{i3} \dfrac{\rho^\prime}{\rhobar} g
+ \nu \pdd{\uibar}{x_j}
+ \nu \pdd{\uiprime}{x_j}}
$$

Subsequently, we make use of the rule $\overline{A + B} = \overline{A} + \overline{B}$.

$$
  \overline{ \pd{\uibar}{t} }
+ \overline{ \pd{\uiprime}{t} }
+ \overline{ \pd{\uibar \ujbar}{x_j} }
+ \overline{ \pd{\uiprime \ujbar}{x_j} }
+ \overline{ \pd{\uibar \ujprime}{x_j} }
+ \overline{ \pd{\uiprime \ujprime}{x_j} }
= \\
  \overline{ - \dfrac{1}{\rhobar} \pd{p^\prime}{x_i} }
+ \overline{ f \epsilon_{ij3} \left( \ujbar + \ujprime - u_{g,j} \right) }
- \overline{ \delta_{i3} \dfrac{\rho^\prime}{\rhobar} g }
+ \overline{ \nu \pdd{\uibar}{x_j} }
+ \overline{ \nu \pdd{\uiprime}{x_j} }
$$

Subsequently, we make use of the rules $\overline{\pd{A}{t}} = \pd{\overline{A}}{t}$, $\overline{A^\prime} = 0$, $\overline{\overline{A} + B} = \overline{A} + \overline{B}$, and $\overline{cA} = c \overline{A}$ to end at

$$
  \pd{\uibar}{t}
+ \pd{\uibar \ujbar}{x_j}
=
- \pd{\overline{ \uiprime \ujprime }}{x_j}
+ f \epsilon_{ij3} \left( \ujbar - u_{g,j} \right)
+ \nu \pdd{\uibar}{x_j}
$$

If we define velocity scale $U$, length scale $L$, time scale $L / U$, then we can estimate a typical magnitude of the left-hand side terms and the turbulent flux term as $U^2/L$, $f U$ for the velocity term, and $\nu U / L^2$ for the viscous term.
We can compute now the dimensionless ratio that compares the magnitude of the advection to the viscous forces as

$$
\dfrac{U^2}{L} \dfrac{\nu U}{L^2} = \dfrac{U L}{\nu} = Re
$$

and do the same for the ratio of advection to rotation:

$$
\dfrac{U^2}{L} \dfrac{1}{f U} = \dfrac{U}{f L} = Ro
$$

In that way, we have defined the Reynolds number $Re$ and Rossby number $Ro$. Taking $U = 1$, $L = 10^3$, and $f = 10^{-4}$, we find that $Re = 10^8$, and $Ro = 10$. Therefore, the viscous force can be safely neglected, but the Coriolis force cannot.

The final conservation of mass equation is:

$$
  \pd{\uibar}{t}
+ \pd{\uibar \ujbar}{x_j}
=
- \pd{\overline{ \uiprime \ujprime }}{x_j}
+ f \epsilon_{ij3} \left( \ujbar - u_{g,j} \right)
$$


In order to study turbulence, we often simplify this set even further, by assuming horizontal homogeneity (except for the large-scale pressure force) and assuming that $\overline{w} = 0$, thus no subsidence. The set then reduces to

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

This set of equation has been the starting point of the important work of Ekman.

