# Exercises chapter 6
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$
$\def\gemafg#1#2{\pafg{\overline{#1}}{#2}}$

##
The one-dimensional conservation equation for heat reads:

$$
\pafg{\overline{\theta}}{t}~=~-~\pafg{\overline{w'\theta'}}{z}
$$

a) Discuss which terms have been neglected from this equation

b) Explain the mathematical steps and definitions to derive the mixed-layer equation for the bulk potential temperature that reads:

$$
\pafg{ {<\overline{\theta}}>}{t}~=~\frac{\overline{w'\theta'(0)}-\overline{w'\theta'(h)}}{h}.
$$

c) Assuming that we are in an encroachment situation and the sensible heat flux and h are constant on time, find an expression for $<{\overline{\theta}}>$
as a function of time. The assumption of sensible heat flux and h constant on time is reasonable in the afternoon hours
and during a relative short time. Discuss this assumption.

d) Derive a similar expression but now assuming that the entrainment flux is 20$\%$ of the surface flux. Compare
your formulations and discuss their implications.

e) Discuss the additional equations that we need to include in order to have a more physical description of the entrainment flux.

##
The atmospheric boundary layer height is 300 m at 0600 UTC, the temperature
lapse rate is 5 K/km and the initial temperature is $\theta$ is 285 K . Assuming that the sensible heat flux varies with time over this land
according to (t is given in hours):

$$
\overline{w'\theta'(0)}&=c_1 \sin \left( \frac{\pi(t-t_0)}{c_2} \right ) \\ 
c_1&=0.2\ Km\ s{-1} \\
c_2&=12\ hours
$$

a) Under encroachment conditions, find the boundary layer height at 14 UTC, if the entrainment flux and subsidence are neglectable.

b) Calculate the boundary layer height at 14 UTC assuming that there is a closure assumption between the
heat flux at the surface and at the entrainment zone:

$$
\overline{w'\theta'(z_i)}~=~-\beta \overline{w'\theta'(0)},
$$

where $\beta$ is 0.2.

c) Calculate the mixed-layer potential temperature in the Convective Boundary Layer
at 14.00 for both cases. Discuss the results.

##
Given an arbitrary mixed layer, we can assume that the mixed layer potential temperature
($\left<\overline{\theta}\right>$ and the potential temperature jump ($\Delta\theta$)) evolve with time according to

$$
\pafg{\left<{\overline{\theta}}\right>}{t} &=\frac{\overline{w'\theta'}(0)-\overline{w'\theta'}(h)}{h} \ \
        \pafg{\Delta\theta}{t} &= \gamma_\theta\pafg{h}{t} - \pafg{\left<\overline{\theta}\right>}{t}\ \
        \overline{w'\theta'}(h) &= - \pafg{h}{t}\Delta\theta
$$

At 12 UTC, the mixed layer temperature is 290 K. At the top of the mixed layer, there is an inversion
with an initial temperature above equal to 296 K.
Above the inversion the temperature increases 0.05 K every 10 m.
The surface flux $\overline{w'\theta'}(0)$ is 185 $W/m^2$.

a) Draw the vertical profile of the potential temperature and the heat flux.
Describe the different regions in the CBL.

b) Find an expression for the time evolution of $h$ without evaluating it. Do this

1. assuming no entrainment and no potential temperature inversion (encroachment).
2. assuming $\overline{w'\theta'}(h) = -\beta \,\overline{w'\theta'}(0)$. In this case, consider a situation in which $\Delta\theta$ is relatively constant in time $\left(\pafg{\Delta\theta}t\right)\approx 0$ and unknown (negating the use of eq. 6.45).
3. making no assumptions, except that $\overline{w'\theta'}(h) = -\beta \,\overline{w'\theta'}(0)$. 
   In this case, can you determine $\pafg{h}{t}$ without knowing $\Delta\theta$?

c) If $h$ is 1000 m at 12 UTC, what is the boundary layer growth rate and the temperature change per hour in the CBL?

d) Calculate the convective velocity at the same time and estimate how long it takes a parcel to travel from the
    surface to the top of the atmospheric boundary layer

##

{numref}`fig:61`, {numref}`fig:62`, and {numref}`fig:63` show the vertical profiles of the potential temperature measured by radiosondes in the USA at 11, 17 and 23 UTC the 20th June 1997 (local time=UTC-6 hours).

```{figure} figures/figset61.png
:name: fig:61
Vertical profile of potential temperature and specific humidity measured by radiosondes at 11 UTC
```

```{figure} figures/figset62.png
:name: fig:62
Vertical profile of potential temperature and specific humidity measured by radiosondes at 17 UTC
```

```{figure} figures/figset63.png
:name: fig:63
Vertical profile of potential temperature and specific humidity measured by radiosondes at 23 UTC
```

a) Describe the main characteristics of the radiosoundings.

b) Give the evolution of the boundary layer depth.

c) Assuming an entrainment velocity equal to 0.01 m/s, find the entrainment
flux at 17 UTC.

##
During the 27th of July 2002, the vertical profile of potential temperature
and heat flux (see {numref}`fig:64` and {numref}`fig:65`) were measured by an aircraft above Cabauw. The heat flux measurements were
taken around 12.45 UTC.

a) Estimate the boundary layer height at 8.15 UTC and 12.45.
Calculate the velocity of the growth of the convective boundary
layer.

b) Calculate the terms (storage, turbulent flux divergence) of the
potential temperature equation in the mixed layer.

c) Was the advection of potential temperature an important term
during the 27th July 2002?

d) The heat flux can be related to the gradient of the mean potential
temperature as follows

$$
\overline{w'\theta'(z)}=-K_h\pafg{\overline{\theta}}{z}
$$

Using the information from the vertical flux of potential temperature
                                                          and heat flux, calculate the exchange coefficient $K_h$ at z=500 m (time 12.45).
This coefficient can also be calculated using convective scaling. The expression reads:

$$
    K_h=\kappa w_*z\left(1-\frac{z}{h}\right )^2
$$

Calculate $K_h$ at 500 m and at 12.45 using this expression and compare it with the previous calculation.

```{figure} figures/figset64.png
:name: fig:64
Vertical profile of potential temperature measured above Cabauw during the 27th July 2002
```

```{figure} figures/figset65.png
:name: fig:65
Vertical profile of sensible heat flux measured above Cabauw during the 27th July 2002
```
