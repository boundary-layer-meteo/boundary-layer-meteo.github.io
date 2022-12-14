$\def\uh{\hat{u}}$
$\def\xh{\hat{x}}$
$\def\th{\hat{t}}$

# Wind

```{admonition} Questions to be answered in this chapter
1. How does wind generate turbulence?
2. What is the importance of the Reynolds number?
3. What is the importance of the Coriolis force for the boundary layer?
4. Why is the wind profile in the surface layer logarithmic?
```

## Conservation of momentum.
Wind is a key ingredient of boundary layer meteorology.
The evolution of wind speed is generally covered via the conservation of momentum, also known as the Navier-Stokes equations.

$$
\dfrac{\partial u_i}{\partial t} + \dfrac{\partial u_j u_i}{\partial x_j} = - f_0 \epsilon_{ij3} \left( u_j - u_{g,j} \right) - \delta_{i3} \dfrac{\rho^\prime}{\rho_0} g + \nu \dfrac{\partial^2 u_i}{\partial x_j^2}
$$

For now, we forget about buoyancy to focus only on wind under neutral conditions.

```{admonition} Conservation of momentum under neutral conditions
$$
\dfrac{\partial u_i}{\partial t} + \dfrac{\partial u_j u_i}{\partial x_j} = - f_0 \epsilon_{ij3} \left( u_j - u_{g,j} \right) + \nu \dfrac{\partial^2 u_i}{\partial x_j^2}
$$
```

We will make the equation dimensionless.
We define $\hat{u} = u / U$, $\hat{x} = x / L$, and $\hat{t} = t/T$ and substitute this into the equation above.

$$
\dfrac{U}{T} \dfrac{\partial \uh_i}{\partial \th} + \dfrac{U^2}{L}\dfrac{\partial \uh_j \uh_i}{\partial \xh_j} &= - f_0 U \epsilon_{ij3} \left( \uh_j - \uh_{g,j} \right) + \dfrac{\nu U}{L^2} \dfrac{\partial^2 \uh_i}{\partial \xh_j^2} \\
\dfrac{U^2}{L} \dfrac{\partial \uh_i}{\partial \th} + \dfrac{U^2}{L}\dfrac{\partial \uh_j \uh_i}{\partial \xh_j} &= - f_0 U \epsilon_{ij3} \left( \uh_j - \uh_{g,j} \right) + \dfrac{\nu U}{L^2} \dfrac{\partial^2 u_i}{\partial x_j^2} \\
\dfrac{\partial \uh_i}{\partial \th} + \dfrac{\partial \uh_j \uh_i}{\partial \xh_j} &= - \dfrac{f_0 L}{U} \epsilon_{ij3} \left( \uh_j - \uh_{g,j} \right) + \dfrac{\nu}{U L} \dfrac{\partial^2 \uh_i}{\partial \xh_j^2}
$$

```{admonition} Non-dimensional conservation of momentum under neutral conditions
$$
\dfrac{\partial \uh_i}{\partial \th} + \dfrac{\partial \uh_j \uh_i}{\partial \xh_j} = - \dfrac{1}{Ro} \epsilon_{ij3} \left( \uh_j - \uh_{g,j} \right) + \dfrac{1}{Re} \dfrac{\partial^2 \uh_i}{\partial \xh_j^2}
$$
```

```{admonition} Reynolds number
$$
Re \equiv \dfrac{UL}{\nu}
$$
```

```{admonition} Rossby number
$$
Ro \equiv \dfrac{U}{f_0 L}
$$
```

## Reynolds averaging the conservation of momentum under neutral conditions

$$
\dfrac{\partial u_i}{\partial t} + \dfrac{\partial u_j u_i}{\partial x_j} = - f_0 \epsilon_{ij3} \left( u_j - u_{g,j} \right)
$$

```{admonition} RANS and horizontal homogeneity
$$
\dfrac{\partial \overline{u}_i}{\partial t} = - \dfrac{\partial \overline{w^\prime u^\prime}}{\partial z}  - f_0 \epsilon_{ij3} \left( \overline{u}_j - u_{g,j} \right)
$$
```

## The closure problem and mixing-length theory

$$
\overline{w^\prime \phi^\prime} = - K \dfrac{\partial \overline{\phi}}{\partial z}
$$

$$
- \dfrac{\partial \overline{w^\prime u^\prime}}{\partial z} = - \dfrac{\partial}{\partial z} \left(- K \dfrac{\partial \overline{u}_i}{\partial z} \right)
 = \dfrac{\partial}{\partial z} \left( K \dfrac{\partial \overline{u}_i}{\partial z} \right)
$$

## The Ekman layer
bla.

## The logarithmic wind profile (or law of the wall)
bla.
