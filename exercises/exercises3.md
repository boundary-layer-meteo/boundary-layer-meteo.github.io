# Exercises chapter 3 
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$
$\def\gemafg#1#2{\pafg{\overline{#1}}{#2}}$

##
The Bowen ratio is defined as the ratio of the heat flux to
the moisture flux ($B=H/LE$). Using the first-order closure to
parameterize the fluxes and assuming that $K_h=K_q$, calculate
the Bowen ratio from the following measurements at 10 meters
($\theta=300\ K$, $q = 10\ \rm{g\ kg^{-1}}$) and at 2 m ($\theta=302\ K$, $q = 12\ \rm{g\ kg^{-1}}$).

($L=2.5 \cdot 10^{6}\ \rm{J\ kg^{-1}}$ and $c_p=1004\ \rm{J\ kg^{-1}\ K^{-1}}$)

```{admonition} Answer
:class: important, dropdown

$$
B=\frac{H}{LE}
$$

We know

$$
H &= \rho c_p \overline{w'\theta '}\\
LE &= \rho L \overline{w'q'},
$$

which can be related to gradients using the first-order closure,

$$
\overline{w'\theta '} &= - K_h \pafg{\overline{\theta}}{z} \\
\overline{w'q'} &= - K_q \pafg{\overline{q}}{z} .
$$

Therefore,

$$
B &= \frac{\rho c_p \overline{w'\theta '}}{\rho L \overline{w'q'}} \\
  &= \frac{c_p}{L} \frac{K_h}{K_q} \frac{\pafg{\overline{\theta}}{z}}{\pafg{\overline{q}}{z}} .
$$

All constants are known and from measurements follow $\pafg{\overline{\theta}}{z} = \frac{-2\,{\rm K}}{8\,{\rm m}}$ 
and $\pafg{\overline{q}}{z} = \frac{-2\cdot 10^{-3} \,{\rm kg\ kg^{-1}}}{8\,{\rm m}}$. 

This results in B=0.4.

```

##
The wind profile is given at a measuring site by

$$
\overline{u}~=~\frac{u_*}{\kappa}ln\frac{z}{z_o}
$$

(${\kappa}=0.4$)

with $z_o$= 0.1 m, $u_*=0.3\ \rm{m\ s^{-1}}$, $\overline{w'\theta'} = 0.05\ \rm{K\ m\ s^{-1}}$
and $\overline{T}=25\ \rm{C}$.

a) Calculate the mechanical production term of the TKE at 2 and 10 meters.
Discuss the result.
```{admonition} Answer
:class: important, dropdown

Mechanical production term: $-\overline{u'w'}\pafg{\overline{u}}{z}$; $\overline{u'w'}$ can be related to $u_*$ by using first-order closure ($K$-theory):

$$
\overline{u'w'} &= - \kappa z u_* \pafg{\overline{u}}{z} \\
  &= - \kappa z u_* \pafg{}{z}\left(\frac{u_*}{\kappa}{\rm ln}\frac{z}{z_0}\right)\\
  &= - \kappa z u_* \frac{u_*}{\kappa} \frac{1}{z}\\
  &= - {u_*}^2 .
$$

Therefore, the mechanical production term is

$$
P &= - \overline{u'w'}\pafg{\overline{u}}{z} \\
  &= {u_*}^2 \frac{u_*}{\kappa} \frac{1}{z}
  &= \frac{{u_*}^3}{\kappa z}
$$

Since $\kappa=0.4$ and $u_*=0.3 \rm \, m\ s^{-1}$, P(2 m) = $3.375\cdot 10^{-2}\rm\,m^2\,s^{-3}$ and P(10 m) = $6.75\cdot 10^{-3}\rm\,m^2\,s^{-3}$. 

There is production! Shear does not destroy turbulence.

```


b) Calculate the buoyancy term. Under these conditions, is it a production or destruction term?
```{admonition} Answer
:class: important, dropdown
Buoyancy term: $\frac{g}{\theta_v}\overline{g'\theta_v'}$. 

We assume there's no moist, so $\theta_v=\theta$ and $\theta \approx T + \gamma_d z$. 
$\gamma_d = \frac{g}{c_p} = 9.8 \cdot 10^{-3}\rm\,K\ m^{-1}$. 
Even at 10 $m$ height, $\theta$ and $T$ differ less than $0.1\rm\,K$, so $\theta_v = 298\rm\,K$. 
Therefore, the buoyancy term is $1.64 \cdot 10^{-3}\rm\,m^2\,s^{-3}$ at both heights.

Positive buoyancy flux leads to a production term.
```

(chapter3-exercise3)=
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
\overline{u_i'u_j'}~&=~-K_m \left (\pafg{\overline u_i}{x_j}+\pafg{\overline u_j}{x_i} \right)\\
\overline{w'\theta_v'}~&=~-K_h \pafg{\overline\theta_v}{z},
$$

and the dissipation of TKE as

$$
\epsilon~=~c_\epsilon E^{3/2} l^{-1},
$$

where $c_\epsilon$ is a constant and $l$ is a characteristic length scale.

```{hint}
:class: tip, dropdown

First, let's simplify the turbulent kinetic energy equation to the one stated in the exercise.

$$
\underbrace{\gemafg{e}{t}}_{\rm Tendency} = \underbrace{\delta_{i3} \frac{g}{\overline{\theta_v}} \overline{u_i'\theta_v'}}_{\rm Buoyancy} - \underbrace{\overline{u_i'u_j'}\gemafg{u_i}{x_j}}_{\rm Shear}-\underbrace{\pafg{}{x_i}\overline{u_i'e}}_{\rm Turbulent\ transport} - \underbrace{\frac{1}{\rho}\pafg{}{x_i}\overline{u_i'p'}}_{\rm Pressure\ correlation}-\underbrace{\epsilon}_{\rm Viscous\ dissipation} .
$$

$\delta_{i3}$ is 0 for $i \neq 3$, so $\delta_{i3} \overline{u_i'\theta_v'}$ becomes $\overline{w'\theta_v'}$.
Since energy remains conserved by transport, we ignore those terms. Therefore $\frac{1}{\rho}\pafg{}{x_i}\overline{u_i'p'} \to 0$ and $\pafg{}{x_i}\overline{u_i'e} \to 0$. In the steady state $\gemafg{e}{t} = 0$, so

$$
0 = - \overline{u_i'u_j'}\gemafg{u_i}{x_j} + \frac{g}{\overline{\theta_v}} \overline{w'\theta_v'} - \epsilon
$$
```

a) If we assume that the exchange coefficient (K) can be written as the product
of a length and a velocity scale ($K_{m,h}=c_{m,h}lE^{1/2}$). Solve the TKE in terms
of $l$, the deformation tensor and the gradient Richardson number.

```{hint}
:class: tip, dropdown
In other words, the question is: find turbulent kinetic energy, $E$, as a function of constants ($c_m$, $c_h$ and $c_{\epsilon}$), the characteristic length scale, $l$, the gradient Richardson number, $Ri_g$, and the deformation tensor, $\gemafg{u_i}{x_j}+\gemafg{u_j}{x_i}$. 
```

```{admonition} Answer
:class: important, dropdown
To solve, fill up the given relations for $\overline{u_i'u_j'}$, $\overline{w'\theta_v'}$, $\epsilon$, $K_m$ and $K_h$.

$$
0 &= \left(c_m l E^{\frac{1}{2}}\right) \left(\gemafg{u_i}{x_j}+\gemafg{u_j}{x_i}\right) \gemafg{u_i}{x_j} - \frac{g}{\theta_v} \left(c_h l E^{\frac{1}{2}}\right) \gemafg{\theta_v}{z} - c_{\epsilon} E^{\frac{3}{2} l^{-1}}\\
\frac{c_{\epsilon}}{l^2} E &= c_m \left(\gemafg{u_i}{x_j}+\gemafg{u_j}{x_i}\right) \gemafg{u_i}{x_j} - \frac{g}{\theta_v} c_h \gemafg{\theta_v}{z} \\
&= c_m \left(\gemafg{u_i}{x_j}+\gemafg{u_j}{x_i}\right) \gemafg{u_i}{x_j} \left(1-\frac{\frac{g}{\theta_v}c_h \gemafg{\theta_v}{z}}{c_m \left(\gemafg{u_i}{x_j}+\gemafg{u_j}{x_i}\right) \gemafg{u_i}{x_j}}\right) .
$$

The gradient Richardson number is given by 

$$
Ri_g = \frac{\frac{g}{\overline{\theta_v}}\gemafg{\theta_v}{z}}{\left(\gemafg{U}{z}\right)^2+\left(\gemafg{V}{z}\right)^2} .
$$

Now, we again make the assumption of horizontal homogeneity and absence of subsidence, which means that for every arbitrary scalar, $\chi$, it holds that $\gemafg{\chi}{x} = \gemafg{\chi}{y} = 0$ and $\overline{w}=0$. 

Because of the multiplication by $\gemafg{u_i}{x_j}$, all terms with $j=1$ or $j=2$, can be ignored. The total TKE equation becomes 

$$
\frac{c_{\epsilon}}{l^2} E &= c_m \left(\gemafg{u_i}{z}+\gemafg{w}{x_i}\right) \gemafg{u_i}{z} \left(1-\frac{\frac{g}{\theta_v}c_h \gemafg{\theta_v}{z}}{c_m \left(\gemafg{u_i}{z}+\gemafg{w}{x_i}\right) \gemafg{u_i}{z}}\right)\\
 &= c_m \gemafg{u_i}{z} \gemafg{u_i}{z} \left(1-\frac{\frac{g}{\theta_v}c_h \gemafg{\theta_v}{z}}{c_m \gemafg{u_i}{z} \gemafg{u_i}{z}}\right) . 
$$

So, in the end $E = \frac{c_m}{c_{\epsilon}} l^2 \left(\gemafg{u_i}{z}\right)^2 \left(1-\frac{c_h}{c_m} Ri_g\right)$.

Note that, since $j=3$ for the whole equation, the corresponding deformation tensor is $\gemafg{u_i}{z}$.

```

b) Find the corresponding expression for $K_{m,h}$
```{admonition} Answer
:class: important, dropdown
Since $K_{m,h} = c_{m,h} l E^{\frac{1}{2}}$, 

$K_{m,h} = c_{m,h} l^2 \left|\gemafg{u_i}{z}\right|\sqrt{\frac{c_m}{c_{\epsilon}}\left(1-\frac{c_h}{c_m} Ri_g\right)}$

```

c) What is the value of the critical Richardson number if $c_h/c_m \approx 3$?
```{admonition} Answer
:class: important, dropdown

At the critical Richardson number, the generation of TKE by shear is at least equal to destruction by buoyancy. Since there is dissipation, the corresponding steady state TKE is equal to 0.

$$
 \frac{c_m}{c_{\epsilon}} l^2 \left(\gemafg{u_i}{z}\right)^2 \left(1-\frac{c_h}{c_m} Ri_c\right) &= 0\\
 1-\frac{c_h}{c_m} Ri_c &= 0\\
 Ri_c &= \frac{c_m}{c_h}
$$

Therefore, $Ri_c = \frac{1}{3}$
```

(chapter3-exercise4)=
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

```{hint}
:class: tip, dropdown

$$
0 = \underbrace{- \overline{u_i'u_j'}\gemafg{u_i}{x_j}}_{\rm S} + \underbrace{\frac{g}{\overline{\theta_v}} \overline{w'\theta_v'}}_{\rm B} - \epsilon
$$

With horizontal homogeneity and no subsidence, $\overline{w}=0$. Also $\overline v=0$, so $i=1$. Due to horizontal homogeneity $\gemafg{u}{x}=\gemafg{u}{y}=0$, so $j=3$ and

$$
0 = \underbrace{- \overline{u'w'}\gemafg{u}{z}}_{\rm S} + \underbrace{\frac{g}{\overline{\theta_v}} \overline{w'\theta_v'}}_{\rm B} - \epsilon
$$

In this exercise, specific humidity is ignored, so $\theta_v = \theta$.

```


````{admonition} Answer
:class: important, dropdown

```{figure} figures/exercise3_4_a.png
:name: fig3a
Vertical profiles of $\theta$ (a) and $U$ (b) under unstable conditions
```

The unstable condition is depicted in {numref}`fig3a`. 
It is shown that $\overline{w'\theta'}>0$ and $\overline{u'w'}<0$. 
Since $\frac{g}{\overline{\theta}} > 0$ and $\gemafg{u}{z} > 0$, this leads to $B>0$ and $S>0$. 
Both contributions are production terms.


```{figure} figures/exercise3_4_b.png
:name: fig3b
Vertical profiles of $\theta$ (a) and $U$ (b) under stable conditions
```

The stable condition is depicted in {numref}`fig3b`. 
It is shown that $\overline{w'\theta'}<0$ and $\overline{u'w'}<0$. 
Since $\frac{g}{\theta} > 0$ and $\gemafg{u}{z} > 0$, this leads to $B<0$ and $S>0$. 
Shear remains a production terms, but buoyancy leads to destruction of TKE.

````

##
During the 20th July, the sun set at Cabauw at 20 UTC. The day
was clear (cloudless). 

a) Sketch in a plot the evolution on time (between 18 and 22 UTC) of
the shear, the buoyancy contribution terms and the flux Richardson number. Discuss it.
````{admonition} Answer
:class: important, dropdown

```{figure} figures/exercise3_5.png
:name: fig5
Buoyancy (B), shear (S), and the Richardson number (Ri) as a function of time.
```

{numref}`fig5` contains the sketch. 
The buoyancy decreases until sunset. 
After sunset, the earth's surface is still warmed up, but begins to cool, which causes a delay in the moment that buoyancy is zero. 
After this point, the earth's surface keeps cooling by longwave radiation. 
Consequently, stratification of the flow sets in, $\gemafg{\theta}{z}>0$, and the heat flux becomes negative, corresponding to negative buoyancy.

When the flow becomes more laminar / less turbulent, the shear decreases.

During day (and the start of the afternoon), the Richardson number is negative, which corresponds to a turbulent flow. 
After sunset, the Richardson number increases. When  ${\rm Ri > Ri}_T$, the flow becomes laminar.

````

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
```{admonition} Answer
:class: important, dropdown

If only dissipation is important, the total equation becomes

$$
\pafg{e}{t} &= -\epsilon\\
 &= -C\frac{e^\frac{3}{2}}{h}\\
e^{-\frac{3}{2}} \partial e &= -\frac{C}{h}\partial t
$$

Since $e$ is only dependent on $t$, this can be written as

$$
e^{-\frac{3}{2}} {\rm d}e &= -\frac{C}{h}{\rm d}t \\
\int_{e\left(t_1\right)}^{e\left(t_2\right)}{e^{-\frac{3}{2}} {\rm d}e} &= -\int_{t_1}^{t_2}{\frac{C}{h}{\rm d}t} \\
\left[-2 e^{-\frac{1}{2}}\right]_{e\left(t_1\right)}^{e\left(t_2\right)} &= -\frac{C}{h} \left[t\right]_{t_1}^{t_2}
$$

Now, substituting $t_1=0$, $t_2=t$, $e\left(t_1\right)=e_0$ and $e\left(t_2\right)=e$.

$$
-2\left(e^{-\frac{1}{2}} - e_0^{-\frac{1}{2}}\right) &= -\frac{C}{h}t\\
e^{-\frac{1}{2}} &= e_0^{-\frac{1}{2}} + \frac{C\,t}{2h}\\
e^{\frac{1}{2}} &= \frac{1}{e_0^{-\frac{1}{2}} + \frac{C\,t}{2h}}
$$

This results in $e=\left(\dfrac{1}{\dfrac{1}{\sqrt{e_0}}+\dfrac{C\,t}{2 h}}\right)^2$

```

c) Is the turbulent kinetic energy being produced or destroyed?
```{admonition} Answer
:class: important, dropdown
If the only relevant term is dissipation, the turbulent kinetic energy is being destroyed.
```

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

```{admonition} Answer
:class: important, dropdown

| **Region** | **Name**                 | **Lapse rate** | **Heat Flux**                          | **Static stability** | **Turbulent?** |
|------------|--------------------------|----------------|----------------------------------------|----------------------|----------------| 
| A          | Surface Layer            | Superadiabatic | >0                                     | Unstable             | Yes            |
| B          | Mixed Layer              | Adiabatic      | $\begin{cases} >0 \\ <0 \end{cases} $ | Neutral              | Yes            |
| C          | Residual layer           | Adiabatic      | 0                                      | Neutral              | Sporadic       |
| D          | Nocturnal boundary layer | Subadiabatic   | <0                                     | Stable               | Sporadic       |
| E          | Capping inversion        | Subadiabatic   | <0                                     | Stable               | Yes            |
| F          | Free atmosphere          | Subadiabatic   | 0                                      | Stable               | Unknown        |

Superadiabatic: The temperature decreases more with height compared to the case of adiabatic cooling.

Subadiabatic: The temperature decreases less with height compared to the case of adiabatic cooling.

In the mixed layer, the heat flux decreases with height. 
It's positive in the lower $\frac{5}{6}$ part of the boundary layer and negative in the rest.

In the residual layer and in the nocturnal boundary layer, turbulence is generated by shear. 
In the free troposphere as well, but less frequent due to the stronger stability.
```

