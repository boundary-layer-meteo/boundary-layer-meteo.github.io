# Conservation of momentum (i)

$$
\def\pd#1#2{\dfrac{\partial #1}{\partial #2}} \\
\def\rhobar{\overline{\rho}} \\
\def\pdd#1#2{\dfrac{\partial^2 #1}{\partial#2^2}}
$$


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

With index notation, we can combine the momentum equations to get the set that we need before we introduce the Reynolds averaging for the velocity components

$$
\pd{u_i}{t} + u_j \pd{u_i}{x_j} = \pd{p^\prime}{x_i} - f \epsilon_{ij3} \left( u_j - u_{g,j} \right) - \delta_{i3} \dfrac{\rho^\prime}{\rhobar} g + \nu \pdd{u_i}{x_j}
$$

