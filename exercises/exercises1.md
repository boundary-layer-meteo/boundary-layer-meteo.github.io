# Exercises chapter 1

```{hint} 
:class: tip
At some exercises we provide hints. These can contains tips to help you find the answer, but they can also contain additional information. 
So, if you managed to answer the question without looking at the tip: great! But please also check the tip, because there might still be valuable information there. 
```

$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$

## 
Calculate the Reynolds number of the following flows $(\nu_{air}=1.5\cdot10^{-5}\ \rm{m^{2}\ s^{-1}},
\nu_{water}=1.0\cdot10^{-6}\ \rm{m^{2}\ s^{-1}}, \nu_{blood}=3.8\cdot10^{-6}\ \rm{m^{2}\ s^{-1}})$. 
Classify if these flows are laminar or turbulent.

```{hint} 
:class: tip, dropdown

The Reynolds number is a dimensionless number, which is used to compare inertial forces with viscous forces. By comparing the magnitudes of those forces we can see how turbulent a flow is. 

$$
{\rm Re} = \frac{U\cdot L}{\nu}
$$

A laminar boundary layer flow becomes turbulent for ${\rm Re} \geq 5\cdot 10^5$.
A pipe flow shows hysteresis:

$$
{\rm Re}_{turbulent \to laminar} = 2300\\
{\rm Re}_{turbulent \to laminar} = 4000
$$

For other configurations, turbulent and laminar regimes are characterized by different regions, but in general, for ${\rm Re} < 10^3$, the flow is laminar and for ${\rm Re} > 10^5$ the flow is turbulent.
```

a) Atmospheric convective boundary layer (W=1 $\mathrm{m\ s^{-1}}$, L=1000 m)
```{admonition} Answer
:class: important, dropdown

$$
\left\lbrace U,L,\nu \right\rbrace &= \left\lbrace 1\,{\rm m\,s^{-1}},1000\,{\rm m},1.5\cdot 10^{-5}\,\rm{m^2\,s^{-1}} \right\rbrace\\
{\rm Re} &= 6.\overline{6}\cdot 10^7
$$
Turbulent
```

b) Oceanic internal waves (U = 0.05 $\rm{m\ s^{-1}}$, L= 10000 m)
```{admonition} Answer
:class: important, dropdown

$$
\left\lbrace U,L,\nu \right\rbrace &= \left\lbrace 0.05\,{\rm m\,s^{-1}},1\cdot 10^4\,{\rm m},1\cdot 10^{-6}\,\rm{m^2\,s^{-1}} \right\rbrace\\
{\rm Re} &= 5\cdot 10^8
$$
Turbulent
```
c) Blood circulation ( U = 0.3 $\rm{m\ s^{-1}}$, L= 0.01 m)
```{admonition} Answer
:class: important, dropdown

$$
\left\lbrace U,L,\nu \right\rbrace &= \left\lbrace 0.30\,{\rm m\,s^{-1}},0.01\,{\rm m},3.8\cdot 10^{-6}\,\rm{m^2\,s^{-1}} \right\rbrace\\
{\rm Re} &= 789
$$
Laminar
```

## 
The velocity and the temperature fields of a flow are given by:

$$
\vec U=(2x^2, xy, \ln(x)+zy)~(\rm{m\ s^{-1}}) ~~~~~~ T = 4x + zy ~(C)
$$

a) Calculate the temperature gradient at the point (0, 1, 1).
```{hint}
:class: tip, dropdown
Gradient of $T = \pafg{}{x_i}T$ 
```

```{admonition} Answer
:class: important, dropdown
$$
\pafg{}{x_i}T\vert_{x=0,y=1,z=1} &= \left(\pafg{T}{x},\pafg{T}{y},\pafg{T}{z}\right)\vert_{x=0,y=1,z=1}\\
&= \left(4,z,y\right) \vert_{x=0,y=1,z=1}\\
&= \left(4,1,1\right)
$$
```

b) Calculate the velocity divergence at the point (-1, 5, 0). Is
it a incompressible or compressible flow at this point?

```{hint}
:class: tip, dropdown
Divergence of $\bf U = \pafg{U_i}{x_i}$
```

```{hint}
:class: tip, dropdown
The flow is incompressible when the divergence is 0. 
```

```{admonition} Answer
:class: important, dropdown
$$
\pafg{U_i}{x_i}\vert_{x=-1,y=5,z=0} &= \pafg{U_x}{x} + \pafg{U_y}{y} + \pafg{U_z}{z}\vert_{x=-1,y=5,z=0} \\
&= 4x + x + y\vert_{x=-1,y=5,z=0} \\
&= 0
$$

Therefore, the flow could be incompressible at this point. However, the general flow field is compressible, since the divergence is only 0 only for $y=-5x$
```

c) Calculate the velocity curl at (1, 1, 1). 
```{hint}
:class: tip, dropdown
Curl of $\bf U = {\bf e}_k \epsilon^{klm} \pafg{}{x_l}{U_m}$
```


```{admonition} Answer
:class: important, dropdown
$$
{\bf e}_k \epsilon^{klm} \pafg{}{x_l}{U_m}\vert_{x=1,y=1,z=1} &= \left(\pafg{U_z}{y}-\pafg{U_y}{z},\pafg{U_x}{z}-\pafg{U_z}{x},\pafg{U_y}{x}-\pafg{U_x}{y}\right)\vert_{x=1,y=1,z=1}\\
&= \left(z-0,0-\frac{1}{x},y-0\right) \vert_{x=1,y=1,z=1}\\
&= \left(1,-1,1\right)
$$
```

d) Given the surface mixing ratio of 15 g/kg at the surface pressure of 1003 hPa, calculate
the potential temperature and the virtual potential temperature at the point
(5, 1, 2) and at the pressure 850 hPa ($R_d=287\ J\ Kg^{-1}\ K^{-1}, c_p=1004\ J\ Kg^{-1}\ K^{-1}$).
```{hint}
:class: tip, dropdown
$$
\theta &= T\left(\frac{P_0}{P}\right)^{\frac{R_d}{c_p}}\\
\theta_v &= \theta \left(1 + 0.61 q \right)
$$
```


```{admonition} Answer
:class: important, dropdown
We know:

$$
T(5,1,2) &= 4\cdot 5+2\cdot 1\,^\circ{\rm C}\\
         &= 295\,{\rm K}\\
P_0 &= 1003\,{\rm hPa}\\
P   &= 850\,{\rm hPa}\\
R_d &= 287\,{\rm J\,kg^{-1}\,K^{-1}}\\
c_p &= 1004\,{\rm J\,kg^{-1}\,K^{-1}}\\
q   &= 15 \cdot 10^{-3}\,kg\,kg^{-1}
$$

Substituting these numbers results in:

$$
\theta &= 309.29\,{\rm K}\\
\theta_v &= 312.12\,{\rm K}\\
$$

```

## 
Let $c$ be a constant, $t$ a function of time and $A$ and $B$ turbulent
variables. Expand the following terms into a mean and turbulent parts and apply
Reynolds rules to simplify the expressions as much as possible.

```{hint} 
:class: tip, dropdown

From {cite}`stull1988introduction` the averaging rules are known. For arbitrary variables, $A$ and $B$, and constants, $c$, it holds that

$$
\overline{c} &= c \\
\overline{c\,A} &= c\,\overline{A} \\
\overline{\overline{A}} &= \overline{A}\\
\overline{\overline{A}\,B} &= \overline{A} \, \overline{B} \\
\overline{A+B} &= \overline{A} + \overline{B}\\
\overline{\afg{A}{t}} &= \afg{\overline{A}}{t} \label{for:Rey6}
$$

The last equation also holds true for derivatives to other coordinates than $t$, like $x$, $y$ and $z$.
```

a) $\overline{cAB}$
```{admonition} Answer
:class: important, dropdown

$$
\overline{cAB} &= c \overline{AB}\\
&=c\overline{\left(\overline{A}+A'\right)\left(\overline{B}+B'\right)}\\
&=c\overline{\left(\overline{A}\,\overline{B}+\overline{A}B'+A'\overline{B}+A'B'\right)}\\
&=c\left(\overline{\overline{A}\,\overline{B}}+\overline{\overline{A}B'}+\overline{A'\overline{B}}+\overline{A'B'}\right)\\
&=c\left(\overline{A}\,\overline{\overline{B}}+\overline{A}\,\overline{B'}+\overline{B}\,\overline{A'}+\overline{A'B'}\right)\\
&=c\left(\overline{A}\,\overline{B}+\overline{A'B'}\right)
$$
```

b) $\overline{A\pafg{B}{t}}$
```{admonition} Answer
:class: important, dropdown

Consider $C \equiv \pafg{B}{t}$, so according to the averaging rules: $\overline{C} = \overline{\pafg{B}{t}} = \pafg{\overline{B}}{t}$ and $C' = C - \overline{C} = \pafg{B}{t} - \pafg{\overline{B}}{t} = \pafg{B-\overline{B}}{t} = \pafg{B'}{t}$

$$
\overline{A\pafg{B}{t}} &= \overline{AC}\\
 &= \overline{\left(\overline{A}+A'\right)\left(\overline{C}+C'\right)}\\
 &=\overline{\left(\overline{A}\,\overline{C}+\overline{A}C'+A'\overline{C}+A'C'\right)}\\
 &=\left(\overline{\overline{A}\,\overline{C}}+\overline{\overline{A}C'}+\overline{A'\overline{C}}+\overline{A'C'}\right)\\
 &=\left(\overline{A}\,\overline{\overline{C}}+\overline{A}\,\overline{C'}+\overline{C}\,\overline{A'}+\overline{A'C'}\right)\\
 &= \overline{A}\,\overline{C}+\overline{A'C'}\\
 &= \overline{A}\pafg{\overline{B}}{t}+\overline{A'\pafg{B'}{t}}
$$
```

c) $\overline{\pafg{A}{t}\pafg{B}{t}}$
```{admonition} Answer
:class: important, dropdown

Same strategy as the one in solution **b**, only now also consider $D \equiv \pafg{A}{t}$ with the same rules. ($\overline{D} = \pafg{\overline{A}}{t}$ and $D' = \pafg{A'}{t}$).

$$
\overline{\pafg{A}{t}\pafg{B}{t}} &= \overline{DC}\\
 &= \overline{\left(\overline{D}+D'\right)\left(\overline{C}+C'\right)}\\
 &=\overline{\left(\overline{D}\,\overline{C}+\overline{D}C'+D'\overline{C}+D'C'\right)}\\
 &=\left(\overline{\overline{D}\,\overline{C}}+\overline{\overline{D}C'}+\overline{D'\overline{C}}+\overline{D'C'}\right)\\
 &=\left(\overline{D}\,\overline{\overline{C}}+\overline{D}\,\overline{C'}+\overline{C}\,\overline{D'}+\overline{D'C'}\right)\\
 &= \overline{D}\,\overline{C}+\overline{D'C'}\\
 &= \pafg{\overline{A}}{t}\pafg{\overline{B}}{t}+\overline{\pafg{A'}{t}\pafg{B'}{t}}
$$
```

<!---
d) $\overline{c \nabla^2 A}$
```{admonition} Answer
:class: important, dropdown

$$
\overline{c\nabla^2 A} &= c \overline{\nabla \nabla A}\\
 &= c \nabla \cdot \overline{\nabla A}\\
 &= c \nabla \cdot \nabla \overline{A}\\
 &= c \nabla^2 \overline{A}
$$
```
--> 

## 
The following terms are given in summation notation. Expand them (that is, write
out each term of the indicated sums).

a) $\pafg{\overline{u_i'u_j'}}{x_j}$
```{admonition} Answer
:class: important, dropdown

$$
\pafg{\overline{u_i'u_j'}}{x_j}=\pafg{\overline{u_i'u'}}{x}+\pafg{\overline{u_i'v'}}{y}+\pafg{\overline{u_i'w'}}{z}
$$

This can be further expanded to:

$$
\pafg{\overline{u_i'u_j'}}{x_j}=\left( \pafg{\overline{u'u'}}{x}+\pafg{\overline{u'v'}}{y}+\pafg{\overline{u'w'}}{z} , \pafg{\overline{v'u'}}{x}+\pafg{\overline{v'v'}}{y}+\pafg{\overline{v'w'}}{z} , \pafg{\overline{w'u'}}{x}+\pafg{\overline{w'v'}}{y}+\pafg{\overline{w'w'}}{z} \right)
$$

```

b) $ u_i'\pafg{\theta'}{x_i}    $
```{admonition} Answer
:class: important, dropdown

$$
u_i'\pafg{\theta'}{x_i} = u'\pafg{\theta'}{x} + v'\pafg{\theta'}{y} + w'\pafg{\theta'}{z}
$$
```

c) $ \overline{U_j} \pafg{\overline{u_i'u_k'}}{x_j} $
```{admonition} Answer
:class: important, dropdown

$$
\overline{U_j}\pafg{\overline{u_i'u_k'}}{x_j} = \overline{U}\pafg{\overline{u_i'u_k'}}{x} + \overline{V}\pafg{\overline{u_i'u_k'}}{y} + \overline{W}\pafg{\overline{u_i'u_k'}}{z}
$$

This can be further expanded to:

$$
\overline{U_j}\pafg{\overline{u_i'u_k'}}{x_j} &= \left(\overline{U}\pafg{}{x}+\overline{V}\pafg{}{y}+\overline{W}\pafg{}{z}\right)\overline{u_i'u_k'}\\
 &= \left(\overline{U}\pafg{}{x}+\overline{V}\pafg{}{y}+\overline{W}\pafg{}{z}\right)\left
 [\begin{matrix}
 \overline{uu} & \overline{uv} & \overline{uw} \\
 \overline{vu} & \overline{vv} & \overline{vw} \\
 \overline{wu} & \overline{wv} & \overline{ww}\\
 \end{matrix}\right]
$$
```

<!---
d) $ \overline{u_i'u_j'} \pafg{\overline{U_k}}{x_j}  $
```{admonition} Answer
:class: important, dropdown

$$
\overline{u_i'u_j'}\pafg{\overline{U_k}}{x_j} = \overline{u_i'u'}\pafg{\overline{U_k}}{x}+\overline{u_i'v'}\pafg{\overline{U_k}}{y}+\overline{u_i'w'}\pafg{\overline{U_k}}{z}
$$

This can be further expanded to a 3x3-matrix:

$$
&\overline{u_i'u_j'}\pafg{\overline{U_k}}{x_j} = \nonumber \\ &\left[
\begin{matrix} 
 \overline{u'u'}\pafg{\overline{U}}{x}+\overline{u'v'}\pafg{\overline{U}}{y}+\overline{u'w'}\pafg{\overline{U}}{z} &
 \overline{u'u'}\pafg{\overline{V}}{x}+\overline{u'v'}\pafg{\overline{V}}{y}+\overline{u'w'}\pafg{\overline{V}}{z} & 
 \overline{u'u'}\pafg{\overline{W}}{x}+\overline{u'v'}\pafg{\overline{W}}{y}+\overline{u'w'}\pafg{\overline{W}}{z} \\
 \overline{v'u'}\pafg{\overline{U}}{x}+\overline{v'v'}\pafg{\overline{U}}{y}+\overline{v'w'}\pafg{\overline{U}}{z} &
 \overline{v'u'}\pafg{\overline{V}}{x}+\overline{v'v'}\pafg{\overline{V}}{y}+\overline{v'w'}\pafg{\overline{V}}{z} & 
 \overline{v'u'}\pafg{\overline{W}}{x}+\overline{v'v'}\pafg{\overline{W}}{y}+\overline{v'w'}\pafg{\overline{W}}{z} \\
 \overline{w'u'}\pafg{\overline{U}}{x}+\overline{w'v'}\pafg{\overline{U}}{y}+\overline{w'w'}\pafg{\overline{U}}{z} &
 \overline{w'u'}\pafg{\overline{V}}{x}+\overline{w'v'}\pafg{\overline{V}}{y}+\overline{w'w'}\pafg{\overline{V}}{z} & 
 \overline{w'u'}\pafg{\overline{W}}{x}+\overline{w'v'}\pafg{\overline{W}}{y}+\overline{w'w'}\pafg{\overline{W}}{z} \\
\end{matrix}\right]
$$
```
-->

d) $ \delta_{i3}g $
```{admonition} Answer
:class: important, dropdown

No double indicators, so the summation cannot be performed. However, it can be further expanded to:

$$
\delta_{i3}g = \left(0,0,g\right)
$$

This term is present in the Navier-Stokes equation. It tells us that only the 3$^{\rm rd}$ dimension of the vector (usually $w$) is affected by gravity and, consequently, buoyancy. 
```

e) $ \pafg{\tau_{mn}}{x_n} $
```{admonition} Answer
:class: important, dropdown

$$
\pafg{\tau_{mn}}{x_n} = \pafg{\tau_{m1}}{x} + \pafg{\tau_{m2}}{y} + \pafg{\tau_{m3}}{z}
$$

since indices 1, 2 and 3 correspond to the $x$, $y$ and $z$ coordinates, respectively. This can be further expanded to:

$$
\pafg{\tau_{mn}}{x_n} = \left( \pafg{\tau_{11}}{x} + \pafg{\tau_{12}}{y} + \pafg{\tau_{13}}{z} , \pafg{\tau_{21}}{x} + \pafg{\tau_{22}}{y} + \pafg{\tau_{23}}{z} , \pafg{\tau_{31}}{x} + \pafg{\tau_{32}}{y} + \pafg{\tau_{33}}{z} \right)
$$
```

## 
With a frequency of 1 Hz and during 8 seconds we have measured the following values of the
vertical velocity and specific humidity

| t [s] | 0 | 1 | 2|3|4|5|6|7|
| --- | -- | --- | --- | --- | --- | --- | --- | --- |
| $w\ \rm(m\ s^{-1})$| 0| -2 | -1 | 1 | -2 | 2 | 1 | 1 |
| $q\ \rm(g\ kg^{-1})$| 8 | 9 | 9 | 6 | 10 | 3 | 5 | 6 |


a) Calculate the time average of $w$ and $q$
```{admonition} Answer
:class: important, dropdown

$\overline{w} = 0\rm\,m\,s^{-1}$ and $\overline{q} = 7 \rm\,g\,kg^{-1}$.

```

b) Calculate the moisture flux. What is the direction of the flux?
````{admonition} Answer
:class: important, dropdown

```{list-table}
:header-rows: 1
* - t [s] 
  - 0 
  - 1 
  - 2
  - 3
  - 4
  - 5
  - 6
  - 7
* - $q'\ \mathrm{[g\ kg^{-1}]}$ 
  - 1 
  - 2 
  - 2 
  - -1
  - 3 
  - -4 
  - -2 
  - -1 
* - $w'\ \mathrm{[m\ s^{-1}]}$
  - 0 
  - -2 
  - -1 
  - 1 
  - -2 
  - 2 
  - 1 
  - 1 
* - $w'q'\ \mathrm{[g\ kg^{-1}\ m\ s^{-1}]}$ 
  - 0 
  - -4 
  - -2 
  - -1 
  - -6 
  - -8 
  - -2 
  - -1 
```

Therefore, $\overline{w'q'} = -3 \rm \,g\,kg^{-1}\,m\,s^{-1}$. The moisture flux is directed downward.
````

c) Calculate the vertical velocity and specific humidity variances
```{admonition} Answer
:class: important, dropdown

| t [s] | 0 | 1 | 2|3|4|5|6|7|
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $q'^2\ \mathrm{[g^2\,kg^{-2}]}$ | 1 | 4 | 4 | 1 | 9 | 16 | 4 | 1|
| $w'^2\ \rm \,[m^2\,s^{-2}]$ | 0 | 4 | 1 | 1 | 4 | 4 | 1 | 1|

So, $\sigma_w^2 \equiv \overline{w'^2} = 2 \rm\,m^2\,s^{-2}$ and $\sigma_q^2 \equiv \overline{q'^2} = 5 \rm\,g^2\,kg^{-2}$.
```

## 
We have measured in a meteorological mast the following values
for the wind: U(2 m)= 2.8 $\rm{m\ s^{-1}}$ and U(20 m) = 5.75 $\rm{m\ s^{-1}}$.

a) Calculating using linear interpolation the value of the
wind at 9 m.
```{admonition} Answer
:class: important, dropdown

$$
U(z) = \frac{z-z_1}{z_2-z_1}\left(U(z_2)-U(z_1)\right) + U(z_1)
$$

$z_1=2\,\rm m$, $z_2=20\,\rm m$, $U(z_1)=2.8\,\rm m\,s^{-1}$ and $U(z_2)=5.75\,\rm m\,s^{-1}$.
Therefore $U\rm\left(9\, m\right) = 3.95\,m\,s^{-1}$.
```

b) If the wind velocity gradient reads:

$$
\pafg{U}{z}=\frac{u_*}{\kappa~z}.
$$

Assuming the following values for the friction velocity (=0.5 $\rm{m\ s^{-1}}$),
the roughness length (= 0.2 m) and the Von Karman constant (=0.4),
calculate the wind speed at 9 m.
```{admonition} Answer
:class: important, dropdown

According to this equation, we get a logarithmic wind profile. This can be used in two ways: starting from $z=z_0$ or from $z=z_1=2\,\rm m$. Both will be explored here.

$$
\pafg{U}{z} &= \frac{u_*}{\kappa z} \\
\partial U &= \frac{u_*}{\kappa} \frac{\partial z}{z}
$$

This can be integrated:

$$
\int_{U\left({z_1}\right)}^{U\left({z_2}\right)} {\rm d} U &= \int_{z_1}^{z_2} \frac{u_*}{\kappa} \frac{{\rm d} z}{z}\\
&= \frac{u_*}{\kappa} \int_{z_1}^{z_2}  \frac{1}{z} {\rm d} z
$$

This results in:

$$
U|_{U\left({z_2}\right)} - U|_{U\left({z_1}\right)} &= \frac{u_*}{\kappa} \left(\log z|_{z_2} - \log z|_{z_1}\right)\\
U(z'_2) &= U(z'_1) + \frac{u_*}{\kappa} \log \left(\frac{z'_2}{z'_1}\right)
$$

in which $z'_1$ and $z'_2$ are two arbitrary heights. In both cases $z'_2 = 9\,\rm m$ and also $U_* = 0.5\,\rm m\,s^{-1}$ and $\kappa=0.4$.

In the first situation, $z'_1=z_0=0.2\,\rm m$ with the corresponding wind velocity $U(z'_1) = 0\,\rm m\,s^{-1}$. In this case $U(9\,\rm m) = 4.76\,\rm m\,s^{-1}$.

In the second situation,$z'_1=z_1=2\,\rm m$ with the corresponding wind velocity $U(z'_1) = 2.8\,\rm m\,s^{-1}$. In this case $U(9\,\rm m) = 4.68\,\rm m\,s^{-1}$.
```



c) Estimate the error associated to the calculation of the wind speed using the linear interpolation.
````{admonition} Answer
:class: important, dropdown

```{figure} figures/Exercise16b.png
:name: fig1.6
```
The figure shows the linear approximation from question a in blue and the logarithmic wind profile from question b in red. 
The error made with the linear interpolation is the difference between these lines. 

At 9 m the estimation with the linear interpolation is $U\rm\left(9\, m\right) = 3.95\,m\,s^{-1}$. 

Comparing the linear interpolation with the logarithmic profile in the first situation results in an error of $0.81\,\rm m\,s^{-1}$. 

Comparing the linear interpolation method with the logarithmic profile in the second situation results in an error of $0.73\,\rm m\,s^{-1}$. 
````

## 
During a measurement campaign the following vertical profile
of potential temperature was measured at 14 UTC (see {numref}`fig1`).

a) Name each of the layers indicated in the figures with the letters A, B, C and D

```{admonition} Answer
:class: important, dropdown

* A. Surface layer              
* B. Mixed layer                
* C. Entrainment zone/layer     
* D. Free troposphere       
```

b) Find the vertical gradient of temperature

$$\pafg{\theta}{z}\sim\frac{\Delta \theta}{\Delta z}$$

for each of the layers above mentioned.
```{admonition} Answer
:class: important, dropdown
It depends on how you draw the schematic lines. 
* A. $\rm \frac{-1.5 K}{300 m} = -5 K km^{-1}$
* B. $\rm \frac{0 K}{1100 m} = 0 K km^{-1}$ 
* C. $\rm \frac{8 K}{350 m} = 23 K km^{-1}$
* D. $\rm \frac{0.75 K}{400 m} = 1.9 K km^{-1}$
```

c) Indicate for each layer whether it is stable, neutral or unstable and whether it is turbulent or laminar. 
```{admonition} Answer
:class: important, dropdown
* A. Unstable and turbulent
* B. Neutral and turbulent
* C. Stable, but turbulent
* D. Stable and laminar
```

```{figure} figures/figset11.png
:name: fig1

Vertical profile of potential temperature measured by a
radiosonde at 14 UTC.
```
