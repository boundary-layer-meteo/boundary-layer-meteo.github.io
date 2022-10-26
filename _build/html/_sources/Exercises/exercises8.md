# Exercises chapter 8
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$
$\def\gemafg#1#2{\pafg{\overline{#1}}{#2}}$

##
The following picture shows some examples of characteristic shapes of plumes dispersing in various atmospheric regimes.

Link each of the plume shapes with the corresponding name and with the most adequate temperature profile (where the dashed line is
the adiabatic lapse rate and the continuous line is the ambient temperature).

```{figure} figures/figset81.png
:name: fig:81
```

##
Starting from the Gaussian formula

$$
C=\frac{Q}{2\pi\sigma_y \sigma_zU}
exp\left[-\frac{y^2}{2\sigma_y^2}-\frac{(z-H)^2}{2\sigma_z^2}-\frac{(z+H)^2}{2\sigma_z^2}\right]
$$

where $H=100m$ is the effective source height, find:

a) The concentration at ground in the centerline of the plume $C(x,0,0)U/Q$.

b) Plot $C(x,0,0)U/Q$ as function of the distance $x$ (from 0 to 3000 m) for the following stability classes:
1. unstable conditions (Pasquill class A): $\sigma_y(x)=0.22x(1+0.0001x)^{-0.5}$, $\sigma_z(x)=0.20x$
2. neutral conditions (Pasquill class D): $\sigma_y(x)=0.08x(1+0.0001x)^{-0.5}$, $\sigma_z(x)=0.06x(1+0.0015x)^{-0.5}$

c) For the unstable condition find at which distance $x$ the ground concentration $C(x,0,0)U/Q$ reaches a maximum. 
```{hint}
:class: tip, dropdown
The maximum of the function $f(x)$ is reached at $x$ for which $\pafg{f}{x}=0$.
```

##
The *skewness* of the vertical velocity is defined as:

$$
S_w=\frac{\overline{w'}^3}{\sigma_w^3}
$$

and its vertical profile in a convective boundary layer is shown in the following figure.

```{figure} figures/figset82.png
:name: fig:82
Vertical profile of skewness of the vertical velocity in a convective boundary layer (numerical simulation)
```

How would smoke disperse from a 200 m high stack if the Convective Boundary Layer were 900 m thick and if the vertical profile of
$S_w$ were negative instead of positive like the profile shown in the picture? 

```{hint}
:class: tip, dropdown
Relate the skewness profile to the updraft and downdraft structures in the convective boundary layer. 
```


##
Starting from the Gaussian formula for an instantaneous release written in in two-dimensional form:

$$
C=\frac{Q}{2\pi\sigma_x
\sigma_z}exp\left[-\frac{(x-Ut)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}\right]
$$

prove that

a) $K_x=\frac{1}{2}\pafg{\sigma_x^2}{t}$

b) $K_z=\frac{1}{2}\pafg{\sigma_z^2}{t}$

```{hint}
:class: tip, dropdown
Hint: calculate

$$
\pafg{C}{t} + U\pafg{C}{x} \\
\pafg{^2 C}{x^2} \\
\pafg{^2 C}{z^2}
$$

and show that

$$
\pafg{C}{t} + U\pafg{C}{x}=K_x\pafg{^2 C}{x^2}+K_z\pafg{^2 C}{z^2}
$$
```
