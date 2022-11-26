# Exercises week 4
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$
$\def\gemafg#1#2{\pafg{\overline{#1}}{#2}}$

```{hint}
:class: tip
Pay attention to the units! 
```

##
The one-dimensional conservation equation for heat reads:

$$
\pafg{\overline{\theta}}{t}~=~-~\pafg{\overline{w'\theta'}}{z}
$$

a) Discuss which terms have been neglected from total conservation equation for heat to come to this equation

<details>
  <summary>Answer</summary>

The total conservation equation for heat is

$$
\underbrace{\gemafg{\theta}{t}}_{\rm Tendency} + \underbrace{\overline{u_j}\gemafg{\theta}{x_j}}_{\rm Advection} + \underbrace{\gemafg{u_j'\theta'}{x_j}}_{\rm Turbulent\ heat\ flux } = \underbrace{\nu_\theta\pafg{^2\overline{\theta}}{x_j^2}}_{\rm Molecular\ diffusion} - \underbrace{\frac{1}{\rho\,c_p}\gemafg{Q_j}{x_j}}_{\rm Radiation} - \underbrace{\frac{{ L_v}\,E}{\rho c_p}}_{\rm Latent\ heat\ release}
$$

The neglected terms are:
* **advection**: No advection is present. This automatically follows from using the assumption of horizontal homogeneity and the absence of subsidence.
* **horizontal turbulent heat flux**: Due to horizontal homogeneity, it is assumed that the horizontal turbulent heat flux is equal for all $x$ and $y$, causing the terms with $i$ equal to 1 or 2 to vanish.
* **diffusion**: The impact of dissipation is relatively small under daytime (convective) conditions.
* **radiation**: The impact of radiation is relatively small under these conditions as well.
* **latent heat release**: In the case of clear skies, there is no condensation/evaporation.

</details>

b) Explain the mathematical steps and definitions to derive the mixed-layer equation for the bulk potential temperature that reads:

$$
\pafg{ {\left< \overline{\theta}\right>}}{t}~=~\frac{\overline{w'\theta'(0)}-\overline{w'\theta'(h)}}{h}.
$$

<details>
  <summary>Answer</summary>

To get to the mixed-layer equations, the conservation equation has to be integrated with height over the whole boundary layer.

$$
\int_{z_0}^h \! \pafg{\overline{\theta}}{t} \, \delta z = - \int_{z_0}^h \! \pafg{}{z}(\overline{w'\theta'}) \delta z
$$(eq6.7)

Integrating the right-hand-side of equation {eq}`eq6.7`, we find:

$$
- \int_{z_0}^h \! \pafg{}{z}(\overline{w'\theta'}) \delta z = \overline{w'\theta'}(z_0) - \overline{w'\theta'}(h)
$$(eq6.12)

Since one of the limits of the integration ($h$) is changing on time,
we have to use of the Leibniz rule to solve the left-hand-side of integral {eq}`eq6.7`:

For an arbitrary scalar, $\psi$, and limits a and b, the Leibniz rule is: 

$$
\pafg{}{t} \int_a^b \! \psi \, \mathrm{d}z = \int_a^b \! \pafg{\psi}{t} \, \mathrm{d}z - \psi(a) \pafg{a}{t} + \psi(b) \pafg{b}{t}.
$$(eq6.8)


We substitute $ \psi = \theta $ in Equation {eq}`eq6.8` and use the limits $z_0$ and h. 
This gives: 

$$
\pafg{}{t} \underbrace{ \int_{z_0}^h \! \overline\theta \, \delta z}_{<\theta> h}  =~ \int_{z_0}^h \!\pafg{\overline\theta }{t} \, \delta z-
\underbrace{\overline\theta (z_0) \pafg{z_0}{t}}_{=0} + \overline\theta (h) \pafg{h}{t}
$$

We reorganise this equation to find:

$$
\int_{z_0}^h \! \pafg{\overline\theta}{t} \, \delta z &= \pafg{}{t}[<\theta> h] - \overline\theta(h) \pafg{h}{t}\\
&= h \pafg{<\theta>}{t} + <\theta> \pafg{h}{t} - \overline\theta(h) \pafg{h}{t}\\
&= h \pafg{<\theta>}{t} + \pafg{h}{t} \underbrace{[<\theta>-\overline\theta(h)]}_{0}
$$


Throughout the mixed layer, $\theta$ is homogeneous, so the second term cancels, resulting in:

$$
\int_{z_0}^h \! \pafg{\overline{\theta}}{t} \, \delta z = h \pafg{<\theta>}{t}
$$(eq6.11)


Finally, substitution of {eq}`eq6.11` and {eq}`eq6.12` on the original equation {eq}`eq6.7` results in:

$$
h \pafg{<\theta>}{t} = \overline{w'\theta'}(z_0) - \overline{w'\theta'}(h)
$$

or, alternatively:

$$
\pafg{<\theta>}{t} = \frac{1}{h}[ \overline{w'\theta'}(z_0) - \overline{w'\theta'}(h)]
$$(for:61b)

</details>

c) Assuming that we are in an encroachment situation and the sensible heat flux and h are constant on time, find an expression for $\left< {\overline{\theta}} \right>$
as a function of time. The assumption of sensible heat flux and h constant on time is reasonable in the afternoon hours
and during a relative short time. Discuss this assumption.

<details>
  <summary>Answer</summary>

In case of encroachment, the vertical turbulent heat flux is 0 near the entrainment zone since there is no inversion, so 

$$
\pafg{\left<\overline{\theta}\right>}{t} = \frac{\overline{w'\theta'}\left(0\right)}{h}
$$

This expression shows that if the boundary lower growth has become minimal, the heating of the boundary layer is proportional to the surface heat flux and inversely proportional to the boundary layer height. All energy (in the form of heat) is equally distributed over the mixed layer.

Near the end of the afternoon, $h$ is approximately constant. This assumption is therefore valid. However, the sensible heat flux changes rapidly in that period. The derived equation is still valid in those situations if the heat flux is considered as a function of time.

</details>

d) Derive a similar expression but now assuming that the entrainment flux is 20$\%$ of the surface flux. Compare
your formulations and discuss their implications.

<details>
  <summary>Answer</summary>

In this case $\overline{w'\theta'}(h) = -\beta \overline{w'\theta'}(0)$ with $\beta=0.2$ 
(the downward heat flux at the boundary layer top is equal to 20% of the upward heat flux at the surface),
so Equation {eq}`for:61b` changes into

$$
\pafg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}\left(0\right)+ 0.2\,\overline{w'\theta'}\left(0\right)}{h} \\
\pafg{\left<\overline{\theta}\right>}{t} &= \frac{1.2\,\overline{w'\theta'}\left(0\right)}{h}
$$

The difference is that the influx of energy (in the form of heat) is enhanced by 20% due to entrainment of warm air that originates from the free troposphere. 
Therefore, for equal boundary layer heights, the boundary layer would heat up 1.2 times as fast for the same surface heat flux. 
However, note that due to entrainment the boundary layer grows faster and therefore, the heat has to be spread over a larger volume. 

</details>

e) Discuss the additional equations that we need to include in order to have a more physical description of the entrainment flux.

<details>
  <summary>Answer</summary>

The entrainment flux has to be related to the boundary layer growth rate:

$$
\overline{w'\theta'}(h) &= - w_e \,\Delta\theta\\
 &= - \afg{h}t \,\Delta\theta
$$

In this equation $w_e$ is the entrainment velocity in m s$^{-1}$ and $\Delta\theta$ is the potential temperature jump at the inversion. In order to evaluate this equation, the time evolution of $\Delta\theta$ has to be known. This is given by:

$$
\afg{\Delta\theta}{t} = \gamma_{\theta}\afg{h}{t}- \afg{\left<\overline{\theta}\right>}{t}
$$

($\partial$ can be replaced by d, since all variables in this equation are only dependent on time.) 

In the end, the system of governing equations is 

$$
\pafg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}\left(z_0\right)-\overline{w'\theta'}\left(h\right)}{h}\\
\overline{w'\theta'}(h) &= - \afg{h}t \,\Delta\theta = -w_e \Delta\theta \\
\afg{\Delta\theta}{t} &= \gamma_{\theta}\afg{h}{t}- \afg{\left<\overline{\theta}\right>}{t}
$$

$w_e$ is the entrainment velocity.

</details>

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

<details>
  <summary>Answer</summary>

In case of encroachment:

$$
\afg{\Delta\theta}{t} &= 0 \\
\gamma_{\theta}\afg{h}{t}- \afg{\left<\overline{\theta}\right>}{t} &= 0\\
\afg{h}{t} &= \frac{1}{\gamma_{\theta}}\afg{\left<\overline{\theta}\right>}{t}
$$

Since in the case of encroachment, $\overline{w'\theta'}(h)=0$, Equation {eq}`for:61b` becomes

$$
\afg{\left<\overline{\theta}\right>}{t} = \frac{\overline{w'\theta'}\left(0\right)}{h}
$$

Therefore, 

$$
\afg{h}{t} = \frac{1}{\gamma_{\theta}}\frac{\overline{w'\theta'}_0}{h} 
$$(for:62a)

$$
h\,\rm{d}h &= \frac{\overline{w'\theta'}_0}{\gamma_{\theta}} \rm{d}t\\
\int_{h_1}^{h_2}{h\ {\rm d}h} &= \int_{t1}^{t2}{\frac{\overline{w'\theta'}_0}{\gamma_{\theta}}{\rm d}t}\\
\dfrac{1}{2}\ h_2^2-\dfrac{1}{2}\ h_1^2 &=  \frac{1}{\gamma_\theta} \int_{t1}^{t2}{\overline{w'\theta'}_0{\rm\,d}t}
$$

Finally,

$$
h_2 = \sqrt{h_1^2 + \frac{2}{\gamma_\theta} \int_{t1}^{t2}{\overline{w'\theta'}_0{\rm\,d}t}}
$$

Substituting the heat flux results in

$$
h_2 = \sqrt{h_1^2 + \frac{2}{\gamma_\theta} \int_{t1}^{t2}{c_1 \sin\left(\frac{\pi\left(t-t_0\right)}{c_2}\right){\rm\,d}t}}
$$

In this equation, the integral is given by 

$$
\int_{t1}^{t2}{c_1 \sin\left(\frac{\pi\left(t-t_0\right)}{c_2}\right){\rm\,d}t} &= c_1 \left[{-\frac{c_2}{\pi}\cos\left(\frac{\pi\left(t-t_0\right)}{c_2}\right)}\right]_{t_1}^{t_2}\\
 &= \frac{c_1\,c_2}{\pi} \left({\cos\left(\frac{\pi\left(t_1-t_0\right)}{c_2}\right)-\cos\left(\frac{\pi\left(t_2-t_0\right)}{c_2}\right)}\right)_{t_1}^{t_2}\\
 &\approx 4125 {\rm\,K\,m}
$$

for $t_1=t_0=0600\rm\,UTC$ and $t_2=1400\rm\,UTC$. Substituting this value, $h_1$, $c_1$ and $c_2$ nets $h\left(1400\rm\,UTC\right)\approx 1319\rm\,m$

</details>

b) Calculate the boundary layer height at 14 UTC assuming that there is a closure assumption between the
heat flux at the surface and at the entrainment zone:

$$
\overline{w'\theta'(z_i)}~=~-\beta \overline{w'\theta'(0)},
$$

where $\beta$ is 0.2.

<details>
  <summary>Answer</summary>

This exercise is solved under the assumption that the boundary layer growth is still only due to encroachment, so $\Delta\theta=0$. In this case, the boundary layer height development is not related to the entrainment flux. The governing equations are:

$$
\afg{h}{t} &= \frac{1}{\gamma_{\theta}}\afg{\left<\overline{\theta}\right>}{t}\\
\afg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}\left(0\right)-\overline{w'\theta'}\left(h\right)}{h} \\
 &= \left(1+\beta\right) \frac{\overline{w'\theta'}\left(0\right)}{h} \\
 &= \left(1+\beta\right) \frac{\overline{w'\theta'}_S}{h}
$$

This results in 

$$
\afg{h}{t} = \frac{1+\beta}{\gamma_{\theta}}\frac{\overline{w'\theta'}_S}{h}
$$

Due to the analogy with Equation {eq}`for:62a`, this results in 

$$
h_2 &= \sqrt{h_1^2 + \frac{2}{\gamma_\theta} \int_{t1}^{t2}{\left(1+\beta\right)\overline{w'\theta'}_S{\rm\,d}t}}\\
 &= \sqrt{h_1^2 + \frac{2\,\left(1+\beta\right)}{\gamma_\theta} \int_{t1}^{t2}{\overline{w'\theta'}_S{\rm\,d}t}}
$$

Since the solution to the integral and the values of $h_1$, $\beta$ and $\gamma_\theta$ are known, the answer can be found: $h_2 \approx 1439\rm\,m$

</details>

c) Calculate the mixed-layer potential temperature in the Convective Boundary Layer
at 14.00 for both cases. Discuss the results.

<details>
  <summary>Answer</summary>

Due to the relation 

$$
\afg{h}{t} = \frac{1}{\gamma_{\theta}}\afg{\left<\overline{\theta}\right>}{t}
$$

It is known that

$$
\afg{\left<\overline{\theta}\right>}{t} &= \gamma_\theta \afg{h}{t}\\
\Delta{\left<\overline{\theta}\right>} &= \gamma_\theta \Delta{h}\\
\left<\overline{\theta}\right>_2 &= \left<\overline{\theta}\right>_1 + \gamma_\theta \left(h_2-h_1\right)
$$

The resulting mixed layer potential temperatures are $290.1\rm\,K$ in the case of encroachment 
and $290.7\rm\,K$ in the case of entrainment flux without the associated boundary layer growth. 

Note that the solution presented here is not the complete analytical solution, since we neglected the growth of the boundary layer that is associated to the entrainment flux. In case this is taken into account, a factor 2 appears before $\beta$ in the final equation for $h_2$ as well as some extra terms that deal with the initial inversion conditions.

</details>

##
Given an arbitrary mixed layer, we can assume that the mixed layer potential temperature
($\left<\overline{\theta}\right>$) and the potential temperature jump ($\Delta\theta$) evolve with time according to

$$
\pafg{\left<{\overline{\theta}}\right>}{t} &=\frac{\overline{w'\theta'}(0)-\overline{w'\theta'}(h)}{h} \\
\pafg{\Delta\theta}{t} &= \gamma_\theta\pafg{h}{t} - \pafg{\left<\overline{\theta}\right>}{t}\\
\overline{w'\theta'}(h) &= - \pafg{h}{t}\Delta\theta
$$

At 12 UTC, the mixed layer temperature is 290 K. At the top of the mixed layer, there is an inversion
with an initial temperature above equal to 296 K.
Above the inversion the temperature increases 0.05 K every 10 m.
The surface flux $\overline{w'\theta'}(0)$ is 185 $W/m^2$ (which is $0.15\rm\,K\,m\,s^{-1}$).

a) Draw the vertical profile of the potential temperature and the heat flux.
Describe the different regions in the CBL.

<details>
  <summary>Answer</summary>

```{figure} figures/exercise6_3.png
:name: fig:6

Boundary layer profiles of potential temperature **a** and sensible heat flux **b** at 12 UTC. The dashed lines denote the idealized profiles.
```

The profiles are drawn in {numref}`fig:6`. From bottom to top, the layers are:
* the surface layer
* the mixed layer
* the entrainment zone
* the free troposphere
</details>

b) If $h$ is 1000 m at 12 UTC, what is the boundary layer growth rate and the temperature change per hour in the CBL?

```{hint}
:class: tip, dropdown
Assume (like in question 2b) that 

$$
\overline{w'\theta'(h)}~=~-\beta \overline{w'\theta'(0)},
$$

where $\beta$ is 0.2.

```

<details>
  <summary>Answer</summary>

$$
\pafg{h}{t} &= 0.2 \frac{\overline{w'\theta'}(0)}{\Delta\theta}\\
\overline{w'\theta'}(0) &= 0.15\rm\,K\,m\,s^{-1}\\
\Delta\theta &= 6\rm\,K
$$

Therefore, $\pafg{h}{t} = 0.005\rm\,m\,s^{-1} = 18\,m\,hr^{-1}$

$$
\pafg{\left<{\overline{\theta}}\right>}{t} &=\frac{\overline{w'\theta'}(0)-\overline{w'\theta'}(h)}{h} \\
 &=  \frac{\left(1+\beta\right)\overline{w'\theta'}(0)}{h}\\
h&= 1000\rm\,m
$$

Because of this, $\pafg{\left<{\overline{\theta}}\right>}{t} = 1.8\,10^{-4}\rm\,K\,s^{-1}=0.65\,K\,hr^{-1}$.
</details>

c) Calculate the convective velocity at the same time and estimate how long it takes a parcel to travel from the
surface to the top of the atmospheric boundary layer

<details>
  <summary>Answer</summary>

The convective velocity is defined by 

$$
w_*=\sqrt[3]{\frac{g}{\theta_v}\,\overline{w'\theta_v'}\,h}
$$

In this definition, the buoyancy term of the TKE, $\frac{g}{\theta_v}\,\overline{w'\theta_v'}$, is incorporated. 
In this case, no moisture is considered, so $\overline{w'\theta_v'}=\overline{w'\theta'}$. 
Substituting the known values results in $w_* = 1.72\rm\,m\,s^{-1}$. 

The time it takes for a parcel to travel from the surface to the top of the atmospheric boundary layer due to convection is 

$$
T = \frac{h}{w_*}
$$

This results in $T = 582 s \approx 10\rm\,min$

</details>

##
{numref}`fig:61`, {numref}`fig:62`, and {numref}`fig:63` show the vertical profiles of the potential temperature measured by radiosondes in the USA at 11, 17 and 23 UTC the 20th June 1997 (local time=UTC-6 hours).

```{figure} figures/figset61.png
:name: fig:61
Vertical profile of potential temperature measured by radiosondes at 11 UTC
```

```{figure} figures/figset62.png
:name: fig:62
Vertical profile of potential temperature measured by radiosondes at 17 UTC
```

```{figure} figures/figset63.png
:name: fig:63
Vertical profile of potential temperature measured by radiosondes at 23 UTC
```

a) Describe the radiosoundings by giving the boundary layer height, the mixed layer temperature, the temperature inversion and the laspe rate 
(h (m), $\left<\theta\right>$ (K), $\Delta\theta$ (K), $\gamma_\theta$ (K km$^{-1}$)).

<details>
  <summary>Answer</summary>

|Figure|{numref}`fig:61`|{numref}`fig:62`|{numref}`fig:63`|
|--|--|--|--|
|h (m) | 700 | 1400 | 1400 |
|$\left<\theta\right>$ (K) | 303 | 309.5 | 310|
|$\Delta\theta$ (K) | 9 | 5 | 4|
|$\gamma_\theta$ (K km$^{-1}$) | 2.2 | 2.5 | 2.5|

Note: The upper profile shows a stable boundary layer, while the other two profiles show well-mixed convective boundary layers.

</details>

b) Give the evolution of the boundary layer depth.

<details>
  <summary>Answer</summary>

From 05.30 LT to 11.30 LT: + 700 m, so a growth of approximately 3 $\rm{cm\ s^{-1}}$.

From 11.30 LT to 17.30 LT: the boundary layer height is constant, so a growth of 0 $\rm{cm\ s^{-1}}$.

</details>

c) Assuming an entrainment velocity equal to 0.01 m/s, find the entrainment
flux at 17 UTC.

<details>
  <summary>Answer</summary>

At 17 UTC (11 LT), $\Delta\theta=5\rm\,K$. 

$$
\overline{w'\theta'(z_i)} &= - w_e\,\Delta\theta \\
 &= - \pafg{h}{t}\,\Delta\theta
$$

Substituting the variables results in $\overline{w'\theta'(z_i)} = -0.05\rm\,K\,m\,s^{-1}$.

The flux is negative, since heat is transported downwards.

</details>

##
During the 27th of July 2002, the vertical profile of potential temperature
and heat flux (see {numref}`fig:64` and {numref}`fig:65`) were measured by an aircraft above Cabauw. The heat flux measurements were
taken around 12.45 UTC.

a) Estimate the boundary layer height at 8.15 UTC and 12.45. Calculate the velocity of the growth of the convective boundary layer.

<details>
  <summary>Answer</summary>

Using the location where $\pafg{\theta}{z}$ has its maximum, the boundary layer heights at 8.15 UTC and 12.45 UTC are 375 m and 1025 m, respectively. 
Therefore, the velocity of growth is $\dfrac{650\rm\,m}{4.5\cdot 3600\rm\,s} = 0.04\rm\,m\,s^{-1}$.

</details>

b) Calculate the terms (storage, turbulent flux divergence) of the potential temperature equation.

<details>
  <summary>Answer</summary>

$$
\gemafg{\theta}{t}+\gemafg{w'\theta'}{z} = {\rm Advection} + {\rm Sources/sinks}
$$

Sources correspond with warming and sinks with cooling.

Storage term: $\gemafg{\theta}{t} = \frac{5\rm\,K}{4.5\rm\,hr}=3.1\times 10^{-4}\rm\,K\,s^{-1}$

Turbulent flux divergence: $\gemafg{w'\theta'}{z} = \frac{-0.095\rm\,K\,m\,s^{-1}}{700\rm\,m}= -1.4\times 10^{-4}\rm\,K\,s^{-1}$

</details>

c) Was the advection of potential temperature an important term during the 27th July 2002?

<details>
  <summary>Answer</summary>

Since other sources and sinks are negligible during day, advection should account for the difference between storage and the vertical turbulent flux divergence. 
Therefore, advection should account for $1.7\times 10^{-4}\rm\,K\,s^{-1}$. 
This is of the same order of magnitude as the temperature tendencies of the terms that are related to storage and transport by turbulent fluxes. 
This shows that advection is important for this case. 

</details>

d) According to K-theory, the heat flux can be related to the gradient of the mean potential
temperature as follows

$$
\overline{w'\theta'(z)}=-K_h\pafg{\overline{\theta}}{z}
$$

Using the information from the vertical flux of potential temperature
and heat flux, determine the exchange coefficient $K_h$ at z=500 m (time 12.45). Discuss the result.

<details>
  <summary>Answer</summary>

$$
\overline{w'\theta'(z)}=-K_h\pafg{\overline{\theta}}{z}
$$

Rewritting this equation gives: 

$$
K_h = - \dfrac{\overline{w'\theta'(z)}}{\pafg{\overline{\theta}}{z}}
$$

From the graph, we note that at 500m $\pafg{\overline{\theta}}{z} \approx 0$, this would result in $K_h\ \to\infty$. 
This shows that local K-theory is not applicable in a well mixed boundary layer.

</details>


```{figure} figures/figset64.png
:name: fig:64
Vertical profile of potential temperature measured above Cabauw during the 27th July 2002
```

```{figure} figures/figset65.png
:name: fig:65
Vertical profile of sensible heat flux measured above Cabauw during the 27th July 2002
```

---

##
This exercise is about a convective boundary layer without any background wind. The strength of turbulent convection in such a boundary layer is related to the surface flux of virtual potential temperature $\overline{w^\prime \theta_v^\prime}_0$ and its depth $h$. We assume that the former is 0.1 K m$^{-1}$, and the latter is 1000 m. The kinematic viscosity $\nu$ is $1.5 \cdot 10^{-5}$ m$^2$ s$^{-1}$. The boundary layer is in quasi-steady state, which means that production and destruction by approximation balance. We assume that $g / \overline{\theta}_v$ is 10 / 300.

a) What is the typical velocity $w_*$ of a convective boundary layer, given its surface flux and depth and what is its value in this case?

<details>
  <summary>Answer</summary>

The Deardorff velocity scale is constructed from $\dfrac{g}{\overline{\theta}_v} \overline{w^\prime \theta^\prime}_0$ and $h$. The only way to create a velocity scale is $w_* \equiv \left( \dfrac{g}{\overline{\theta}_v} \overline{w^\prime \theta^\prime}_0 h \right)^\frac{1}{3}$. Its value here is 1.49 m s$^{-1}$.

</details>

b) What is the Reynolds number of this convective boundary layer?

<details>
  <summary>Answer</summary>

The Reynolds number here is $Re = w_* h / \nu$  and its value is very close to $1 \cdot 10^8$.

</details>

c) What is the typical magnitude of the production of turbulence in this system?

<details>
  <summary>Answer</summary>

The production is the buoyancy term from TKE equation: $\dfrac{g}{\overline{\theta}_v} \overline{w^\prime \theta_v^\prime}$. We take the surface value as a reference as this is where the energy enters the system: $\dfrac{g}{\overline{\theta}_v} \overline{w^\prime \theta_v^\prime}_0$. Its value is $3.33 \cdot 10^{-3}$ m$^2$ $s^{-3}$.

</details>

d) What is the magnitude of the dissipation of turbulence in this system?

<details>
  <summary>Answer</summary>

The dissipation is approximately equal to the buoyancy term from TKE equation as there is almost steady state, hence its value is $3.33 \cdot 10^{-3}$ m$^2$ $s^{-3}$.

</details>

e) What is the Kolmogorov scale of this convective boundary layer?

<details>
  <summary>Answer</summary>

Dissipation matches the buoyancy flux, thus the Kolmogorov length $\eta = \left( \nu^3 / \epsilon \right)^\frac{1}{4} = \left( \nu^3 / \dfrac{g}{\overline{\theta}_{v}} \overline{w^\prime \theta_v^\prime}_0 \right)^\frac{1}{4}$. Its value here is $1.0 \cdot 10^{-3}$ m, thus one millimeter.

</details>

f) Show that the Reynolds number is proportional to $\left( h / \eta \right)^\frac{4}{3}$.

<details>
  <summary>Answer</summary>

$$
\dfrac{h}{\eta} &= 
\dfrac{h}{\left( \nu^3 / \dfrac{g}{\overline{\theta}_{v}} \overline{w^\prime \theta_v^\prime}_0 \right)^\frac{1}{4}} \\
&=
\dfrac{h \left( \dfrac{g}{\overline{\theta}_{v}} \overline{w^\prime \theta_v^\prime}_0 \right)^\frac{1}{4}}
{\nu^\frac{3}{4}} \\
&=
\dfrac{h^\frac{3}{4} h^\frac{1}{4} \left( \dfrac{g}{\overline{\theta}_{v}} \overline{w^\prime \theta_v^\prime}_0 \right)^\frac{1}{4}}
{\nu^\frac{3}{4}} \\
&=
\dfrac{h^\frac{3}{4} w_*^\frac{3}{4}}
{\nu^\frac{3}{4}} \\
&=
Re^\frac{3}{4}
$$

</details>
