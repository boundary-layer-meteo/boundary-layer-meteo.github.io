# Exercises chapter 7
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$
$\def\gemafg#1#2{\pafg{\overline{#1}}{#2}}$

##
The figures below show the vertical profiles of potential temperature and wind speed
observed at the Southern Great Plains in USA during the night of 20th June 1997. By analyzing them
we can determine some of the main characteristics of the nocturnal boundary layer.

```{figure} figures/figset73.png
:name: fig:73
```

```{figure} figures/figset74.png
:name: fig:74
```

a) Describe both vertical profiles.

b) Determine the boundary layer height according the potential temperature profile
and the wind speed. Discuss your criteria and the estimation of the height.

c) Calculate the Brunt-Väisälä frequency. By inverting
this frequency, one obtains the period of the oscillation of a parcel in a statically stable
environment related to the presence of gravity (buoyancy) waves.
Discuss the dependence of this oscillation period as a function of the potential
temperature gradient.

d) During the night, the friction velocity and the sensible heat flux were almost constant on time with
the values 0.6 $ms^{-1}$ and -50 $Wm^{-2}$, respectively. Calculate the flux Richardson number. Could
we characterize this nocturnal boundary layer as weakly or strongly stable?
What is the role of buoyancy and shear in this nocturnal boundary layer?

##
These vertical profiles for potential temperature were measured in USA
at 24.07 and 04.02 local time during the field experiment CASES-99.
Focusing mainly on the sounding observations:

```{figure} figures/figset71.png
:name: fig:71
```

```{figure} figures/figset72.png
:name: fig:72
```

a) Describe both profiles of the potential temperature. Estimate the
evolution of the boundary layer height and the gradient of the potential
temperature from the surface to the top of the boundary layer.

##
The one-dimensional equation that governs the heat budget during stable
conditions reads

$$
\pafg{\overline{\theta}}{t}~=~-~\pafg{\overline{w'\theta'}}{z}~-~\frac{1}{\rho c_p}\pafg{Q^*}{z}
$$

The longwave radiative term $\frac{1}{\rho c_p}\pafg{Q^*}{z}$ can be calculated using
a bulk approach. $Q^*$ is the the new upward longwave radiative flux.
In short, we can define three layers: surface (s), middle (m) and top (t)
that are radiatively active according to the Stefan-Boltzmann expression:

$$
L &= \epsilon_{IR}\sigma_{SB} T^4
\sigma_{SB}&=5.67~10^{-8}~\frac{W}{m^2K^4},
$$

where L is the generic expression for the longwave radiative cooling.
a) Derive a bulk expression of the longwave radiative divergence for these three layers.

b) Assuming that the emissivity at these layers is equal ($\epsilon_{IR}=0.78$) and neglecting the divergence of the
turbulent flux term, calculate the tendency term $\pafg{\overline{\theta}}{t}$, calculate the long wave
radiative term if the potential temperature profile is linear and follows:

$$
\theta (z)~=~\theta (z_o)~+~0.2z.
$$

You can consider that the surface layer is at z$_o$ m and $\theta (z_o)$ K.
The other layers middle and top are at 5 and 10 meters respectively. In consequence,
the interfaces are approximately at 2.55 and 7.5 meters.

c) Repeat now the calculation but assuming a logarithmic profile for the potential temperature that reads:

$$
\theta (z)~=~\theta (z_o)~+~\frac{\theta_*}{\kappa}ln\left(\frac{z}{z_o}\right).
$$

Use the following values to complete the expression: $\overline{w'\theta'}$ = - 24 Wm$^{-2}$,
u$_*$=0.1 m, z$_o$=0.1 m and von Karman constant equal to 0.4.
Similar to (b), assume the surface layer at z$_o$=0.1 m and $\theta (z_o)$=292 K; and layers middle
and top at 5 and 10 meters respectively.

d) Discuss your results from a perspective of the tendency of the temperature $\pafg{\overline{\theta}}{t}$.
Calculate in K h$^{-1}$.
Based on the results of (b) and (c), discuss the most probable profile observed during stable conditions.


##
The momentum equation for the $\overline{U}$ and $\overline{V}$-component
during diurnal and nocturnal conditions reads:

$$
\pafg{\overline{U}}{t}~=~f \overline{V}- \pafg{\overline{w'u'}}{z}
$$

$$
\pafg{\overline{V}}{t}~=~f (\overline{U_g}-\overline{U})- \pafg{\overline{w'v'}}{z}
$$

where $\overline{U_g}$ is the geostrophic wind in the U direction and f
is the Coriolis parameter. We assume that $\overline{V_g}$=0.

a) Calculate the $\overline{U}$ and $\overline{V}$-component during day conditions.
In diurnal conditions, one can assume that the wind is in steady-state.
Discuss the role of the momentum flux divergence.

b) Calculate the $\overline{U}$ and $\overline{V}$-components during the night. Under
nocturnal conditions, the friction suddenly disappears above the surface
layer. Discuss the validity of this assumption.

```{hint}
:class: tip, dropdown
First derive a second-order differential equation for the $\overline{U}-\overline{U_g}$ component. 

Second, prove that the solution

$$
\overline{U}-\overline{U_g}=A sin(ft) + B cos (ft)
$$

is a correct solution.

Third, the constants A and B are determined from
the initial conditions for $\overline{U}(t=0)$ and $\overline{V}(t=0)$-components are:

$$
\overline{U}(t=0)~=~\overline{U_d}=\overline{U_g}-F_{v}(t=0)
$$

$$
\overline{V}(t=0)~=~\overline{V_d}=F_{u}(t=0)
$$

where $\pafg{\overline{w'u'}}{z}=fF_{u}(t=0)$ and $\pafg{\overline{w'v'}}{z}=fF_{v}(t=0)$.

```

c) Calculate and plot the $\overline{U}$ and $\overline{V}$-components for every hour over a full period
T=2$\pi$/f, using the following values: f=10$^{-4}$s$^{-1}$, F$_{u}(t=0)$=F$_{v}(t=0)$=3ms$^{-1}$ and
$\overline{U_g}$=10 ms$^{-1}$ and $\overline{V_g}$=0.

##
The conservation equation for the potential temperature in a Stable Boundary Layer reads (neglecting phase changes)

$$
\pafg{\overline{\theta}}{t}~=~- \pafg{\overline{w'\theta'}}{z}-\frac{1}{\rho c_p}\pafg{Q^*}{z}
$$

a)By using a bulk approach, calculate the divergence of the net upward longwave radiation
($Q^*=F_{up}-F_{down}$). Remember that the longwave radiation follows the
Stefan-Boltzmann law:

$$
L&=\epsilon_{IR}\sigma_{SB} T^4
\sigma_{SB}&=5.67~10^{-8}~\frac{W}{m^2K^4}
$$

The following values in the three-layer model of the stable
boundary layer are suggested. At the surface, $T_s=290~K$ and $\epsilon_s=0.78$. 

In the layer that represents the SBL, $T_m=296~K$ and $\epsilon_m=0.78$.

Finally, at the top of the SBL $T_t=298~K$ and $\epsilon_t=0.78$.

The boundary layer height is equal to 25 m.
Additional data to calculate the divergence of
the net longwave radiation are: $\rho=1.292 Kg/m^3$, $c_p=1004 J/KgK$.

b) Assuming that the turbulent flux is constant with height, calculate the
variation of potential temperature per hour.

c) The sensible heat flux has the following vertical profile

$$
\overline{w'\theta'}(z)~=~\overline{w'\theta'}_o~(1-z/h)~~~~\overline{w'\theta'}_o= -14~W/m^2
$$

where $\overline{w'\theta'}_o$ is the sensible heat flux at
the surface and $h=25~m$ is the depth of the SBL.

Plot this profile. Discuss the role of the turbulent flux under this conditions.

d) By using the values found in a) and taking now into account the turbulent divergence
term, calculate the temperature change per hour.

e) If now we consider in the budget equation for the temperature, the
horizontal advection term $U~\pafg{\overline{\theta}}{x}$. If $U=10~m/s$, calculate
the horizontal gradient of temperature ($\pafg{\overline{\theta}}{x}$) in order to
reach a steady-state.
