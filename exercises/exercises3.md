# Exercises chapter 3 
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$

##
The Bowen ratio is defined as the ratio of the heat flux to
the moisture flux ($B=H/LE$). Using the first-order closure to
parameterize the fluxes and assuming that $K_h=K_q$, calculate
the Bowen ratio from the following measurements at 10 meters
($\theta=300\ K$, $q = 10\ \rm{g\ kg^{-1}}$) and at 2 m ($\theta=302\ K$, $q = 12\ \rm{g\ kg^{-1}}$).

($L=2.5~10^{6}\ \rm{J\ kg^{-1}}$ and $c_p=1004\ \rm{J\ kg^{-1}\ K^{-1}}$)

##
The wind profile is given at a measuring site by

$$
\overline{u}~=~\frac{u_*}{\kappa}ln\frac{z}{z_o}
$$

(${\kappa}=0.4$)

with $z_o$= 10 cm, $u_*=0.3\ \rm{m\ s^{-1}}$, $\overline{w'\theta'} = 0.05\ \rm{K\ m\ s^{-1}}$
and $\overline{T}=25\ \rm{C}$.

a) Calculate the mechanical production term of the TKE at 2 and 10 meters.
Discuss the result.

b) Calculate the buoyancy term. Under these conditions, is it a production or destruction term?

##
From steady state and in case one can neglect the turbulent transport and advection terms,
the turbulent kinetic energy (E) equation reduces to

$$
0~=-\overline{u_i'u_j'}\pafg{\overline{u_i}}{x_j}+
\frac{g}{\theta_o}\overline{w'\theta_v'}-\epsilon
$$

We can express (parameterize) the momentum flux, buoyancy flux (virtual temperature flux) as a function of
the mean gradients of wind and virtual potential temperature as:

$$
\overline{u_i'u_j'}~=~-K_m \left (\pafg{\overline u_i}{x_j}+\pafg{\overline u_j}{x_i} \right)\\
\overline{w'\theta_v'}~=~-K_h \pafg{\overline\theta_v}{z},
$$

and the dissipation of TKE as

$$
\epsilon~=~c_\epsilon E^{3/2} l^{-1},
$$

where $c_\epsilon$ is a constant and $l$ is a characteristic length scale.

a) If we assume that the exchange coefficient (K) can be written as the product
of a length and a velocity scale ($K_{m,h}=c_{m,h}lE^{1/2}$). Solve the TKE in terms
of $l$, the deformation tensor and the gradient Richardson number.

b) Find the corresponding expression for $K_{m,h}$

c) What is the value of the critical Richardson number if $c_h/c_m \approx 3$?

##
From the reduced TKE equation (exercise 3)

$$
0~=\underbrace{-\overline{u_i'u_j'}\pafg{\overline{u_i}}{x_j}}_{S}+
\underbrace{\frac{g}{\theta_o}\overline{w'\theta_v'}}_{B}-\epsilon,
$$

and assuming no subsidence and a horizontal wind blowing only in
the x-direction ($v = 0$, assume the vertical profile $u(z)$
similar to that in exercise 2), deduce if the buoyancy (B) and
shear (S) terms are production or loss terms under the following
conditions:

a) unstable condition

b) stable condition

Explain your answer.

##
During the 20th July, the sun set at Cabauw at 20 UTC. The day
was clear (cloudless). 

a) Sketch in a plot the evolution on time (between 18 and 22 UTC) of
the shear, the buoyancy contribution terms and the flux Richardson number. Discuss it.

b) The prognostic equation of the Turbulent Kinetic Energy equation (TKE=$e$) reads:

$$
\pafg{e}{t}=-\overline{u'w'}\pafg{\overline{u}}{z}+
\frac{g}{\overline{\theta_v}}\overline{w'\theta_v'}- \pafg{\overline{w'e}}{z}-\frac{1}{\overline{\rho}}\pafg{\overline{w'p'}}{z}-\epsilon.
$$

At 22 UTC, the only important term in the right hand side of the prognostic Turbulent Kinetic Energy
equation is the dissipation term.
The dissipation term is generally parameterized as:

$$
\epsilon = C \frac{e^{3/2}}{h}
$$

where $C$ is a constant and $h$ is the boundary layer height.

Find an expression of the evolution on time of the turbulent kinetic
energy. Assume that $h$ does not change on time and the initial condition is
$e=e_o$ at $t=0$.

c) Is the turbulent kinetic energy being produced or destroyed?

## 
Given the following draw of the evolution of the atmospheric
Boundary Layer, fill in the table with the most appropriate labels
(some examples have been already inserted) .

```{figure} figures/figset31.png
:name: fig31
```

| **Region** | **Name**    | **Lapse rate** | **Heat Flux** | **Static stability** | **Turbulent?** |
|------------|-------------|----------------|---------------|----------------------|----------------| 
| A          |             | Superadiabatic |               |                      |                |
| B          | Mixed Layer |                |               |                      |                |
| C          |             |                | 0             |                      |                |
| D          |             |                |               |                      | Sporadic       |
| E          |             | Subadiabatic   |               | Stable               |                |
| F          |             |                |               |                      | Unknown        |

