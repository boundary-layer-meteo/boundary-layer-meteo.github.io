# Exercises chapter 2
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$

##
The Navier-Stoke equation for the instantaneous velocity is

$$
\pafg{u_i}{t}+u_j\pafg{u_i}{x_j}~=~-\frac{1}{\rho}\pafg{p}{x_i}
-g\delta_{i3}+f_c\epsilon_{ij3}u_j+\nu\pafg{^2 u_i}{x_j^2}
$$

a) Using the scales $\cal U$ and $\cal L$, deduce the dimensionless form of the
Navier Stoke equation.

```{hint}
:class: tip, dropdown

$u_{i}^*= \dfrac{u_i}{\cal U}$

$x_{j}^*= \dfrac{x_j}{\cal L}$ 

$p^*= \dfrac{p}{\rho {\cal U}^2}$
```

```{admonition} Answer
:class: important, dropdown

$\cal L$ and $\cal U$ represent respectively the scaling height and scaling velocity. Variables indicated with a $*$ are dimensionless.

$$
u_i &= u_i^* \, \cal U\\
t &= t^* \, \frac{\cal L}{\cal U}\\
x_i &= x_i^* \, \cal L\\
p &= p^* \rho \, \cal U\rm^2\\
g &= g^* \, \frac{\cal U\rm^2}{\cal L} \\
f_c &= f_c^* \, \frac{\cal U}{\cal L}
$$

This results in

$$
\frac{\cal U\rm^2}{\cal L} \pafg{u_i^*}{t^*} + \frac{\cal U\rm^2}{\cal L} u_j^* \pafg{u_i^*}{x_j^*} &= - \frac{\rho\cal U\rm^2}{\cal L} \frac{1}{\rho} \pafg{p^*}{x_i^*} - \frac{\cal U\rm^2}{\cal L} g^* \delta_{i3} + \frac{\cal U\rm^2}{\cal L} f_c^* \epsilon_{ij3}u_j^* + \frac{\cal U}{\cal L\rm^2} \nu \pafg{u_i^*}{{x_j^*}^2}\\
\pafg{u_i^*}{t^*} + u_j^* \pafg{u_i^*}{x_j^*} &= - \pafg{p^*}{x_i^*} - g^* \delta_{i3} + f_c^* \epsilon_{ij3}u_j^* + \frac{\nu}{\cal U L} \pafg{u_i^*}{{x_j^*}^2}
$$

This can also be expressed with the Reynold's number, ${\rm Re} = \frac{\cal U L}{\nu}$:

$$
\pafg{u_i^*}{t^*} + u_j^* \pafg{u_i^*}{x_j^*} = - \pafg{p^*}{x_i^*} - g^* \delta_{i3} + f_c^* \epsilon_{ij3}u_j^* + \frac{1}{\rm Re} \pafg{u_i^*}{{x_j^*}^2}
$$
```

b) Typical length scales in the ABL are $\cal U$= 1 $\rm{m\ s^{-1}}$ and $\cal L$=1000 m.
Are the Coriolis rotational term and the viscous term relevant in the ABL?

($f_c=10^{-4} s^{-1}$, $\nu_{air}=1.5~10^{-5} \rm{m^2\ s^{-1}}$)

```{admonition} Answer
:class: important, dropdown
Contribution of Coriolis force with respect to the other terms: $f_c^* = f_c \frac{\cal L}{\cal U} = 0.1 = 10~\%$. This contribution is weak, but significant. 
Contribution of viscosity: ${\rm Re} = \frac{\cal U L}{\nu} = 6.7 \cdot 10^7$, so $\frac{1}{\rm Re} \to 0$. This contribution is not significant. Consequently, this term can be neglected.
```

##
Suppose that $\overline{u'w'}=-(u_*+cz)^2$ and $\overline{v'w'}=0$ for all $z$ and
the geostrophic velocities for the x- and y-components are 5 $\rm{m\ s^{-1}}$ and 5 $\rm{m\ s^{-1}}$ at all heights, respectively.
Find the acceleration of air in the x- and y-directions $\left(\pafg{u}{t}, \pafg{v}{t}\right)$ at a height of 100 m in the ABL.
The initial velocities at 100 m are $\overline{u}=\ 4\ \rm{m\ s^{-1}}$ and $\overline{v}=\ 2\ \rm{m\ s^{-1}}$.

($u_* = 0.3\ \rm{m\ s^{-1}}$,
$f_c = 10^{-4} s^{-1}$ and $c = 10^{-3} s^{-1}$).

```{admonition} Answer
:class: important, dropdown

First we derive the general momentum equations.

$$
\begin{cases}
    \pafg{u}{t} + u_j \pafg{u}{x_j} = f_c v - \frac{1}{\rho}\pafg{p}{x}+ \nu \pafg{^2u}{{x_j}^2} \\
    \pafg{v}{t} + u_j \pafg{v}{x_j} = - f_c u - \frac{1}{\rho}\pafg{p}{y}+ \nu \pafg{^2v}{{x_j}^2}
\end{cases}
$$

Reynold's averaging results in

$$
\begin{cases}
    \pafg{\overline{u}}{t} + \overline{u_j} \pafg{\overline{u}}{x_j} + \overline{u_j'\pafg{{u'}}{x_j}} = 
        f_c \overline{v} - \frac{1}{\rho}\pafg{\overline{p}}{x}+ \nu \pafg{^2\overline{u}}{{x_j}^2} \\
    \pafg{\overline{v}}{t} + \overline{u_j} \pafg{\overline{v}}{x_j} + \overline{u_j'\pafg{{v'}}{x_j}} = 
        - f_c \overline{u} - \frac{1}{\rho}\pafg{\overline{p}}{y}+ \nu \pafg{^2\overline{v}}{{x_j}^2} 
\end{cases}
$$

Considering $\overline{w} = 0$, 

horizontal homogeneity ($\pafg{\chi}{x}=\pafg{\chi}{y}=0$ with $\chi$ as an arbitrary variable), 

incompressibility ($\pafg{u_i'}{x_i}=0$), 

and the chain rule ($\pafg{u_i\chi}{x_i}$=$u_i\pafg{\chi}{x_i}+\pafg{u_i}{x_i}\chi$), 

this results in

$$
\begin{cases}
    \pafg{\overline{u}}{t} + \pafg{\overline{u_j'u'}}{x_j} = 
        f_c \overline{v} - \frac{1}{\rho}\pafg{\overline{p}}{x}+ \nu \pafg{^2\overline{u}}{{x_j}^2} \\
    \pafg{\overline{v}}{t} + \pafg{\overline{u_j'v'}}{x_j} = 
        - f_c \overline{u} - \frac{1}{\rho}\pafg{\overline{p}}{y}+ \nu \pafg{^2\overline{v}}{{x_j}^2}
\end{cases}
$$

Neglecting the small viscosity term (for high Reynolds numbers) and assuming that at larger scales the Coriolis force 
and horizontal pressure gradients balance to reach a geostrophic wind, 
$\frac{1}{\rho}\pafg{\overline{p}}{x} = f_c v_g$ and $\frac{1}{\rho}\pafg{\overline{p}}{y} = -f_c u_g$, the momentum equations are:

> $\pafg{\overline{u}}{t} + \pafg{\overline{u'w'}}{z}$ = $f_c \left(\overline{v}-v_g\right) $

> $\pafg{\overline{v}}{t} + \pafg{\overline{v'w'}}{z}$ = $-f_c \left(\overline{u}-u_g\right) $

In this representation, $u_g$ and $v_g$ are components of the geostrophic wind, 
which is the steady state wind considering the horizontal pressure gradients and the Coriolis force.
In this specific case, filling up the momentum fluxes, the governing equations for the acceleration are:

$$
\pafg{\overline{u}}{t} &= 2 c \left(u_*+c z\right) + f_c \left(\overline{v}-v_g\right) \\
\pafg{\overline{v}}{t} &= -f_c \left(\overline{u}-u_g\right) 
$$

Substituting the values, results in:

$\pafg{\overline{u}}{t}$ = $5 \cdot 10^{-4}\,\rm m\,s^{-1}$

$\pafg{\overline{v}}{t}$ = $1 \cdot 10^{-4}\,\rm m\,s^{-1}$

```


##
The thermodynamic equation reads

$$
\pafg{\theta}{t}+u_j\pafg{\theta}{x_j} = \nu_{\theta}\pafg{^2\theta}{x_j^2}
-\frac{1}{\rho c_p}\pafg{Q_j}{x_j}-\frac{L_vE}{\rho c_p}
$$

a) Find the equation for the averaged potential temperature $\overline{\theta}$.
```{admonition} Answer
:class: important, dropdown
$$
\underbrace{\pafg{\theta}{t}}_{\rm Tendency} + \underbrace{u_j \pafg{\theta}{x_j}}_{\rm Advection} = \underbrace{\nu_{\theta}\pafg{^2\theta}{{x_j}^2}}_{\rm Viscosity} - \underbrace{\frac{1}{\rho c_p} \pafg{Q_j}{x_j}}_{\rm Radiation} - \underbrace{\frac{L_v E}{\rho c_p}}_{\rm Phase\,changes} \\
\pafg{\overline{\theta}}{t} + \overline{u_j \pafg{\theta}{x_j}} = \overline{\nu_{\theta}\pafg{^2\theta}{{x_j}^2}} - \overline{\frac{1}{\rho c_p} \pafg{Q_j}{x_j}} - \overline{\frac{L_v E}{\rho c_p}} \\
\pafg{\overline{\theta}}{t} + \overline{u_j}\,\overline{\pafg{\theta}{x_j}} + \overline{u_j' \pafg{\theta'}{x_j}} = \nu_{\theta}\pafg{^2\overline{\theta}}{{x_j}^2} - \frac{1}{\rho c_p} \pafg{\overline{Q_j}}{x_j} - \frac{L_v \overline{E}}{\rho c_p}
$$
Because of incompressibility, $\pafg{u_j}{x_j}=0$, and therefore also $\pafg{\overline{u_j}}{x_j}=\pafg{u_j'}{x_j} =0$. Therefore

$$
u_j'\pafg{\theta'}{x_j} &= u_j'\pafg{\theta'}{x_j} + \pafg{u_j'}{x_j} \theta' \\
&= \pafg{u_j'\theta'}{x_j}
$$(for:23b)

This is the flux form; after Reynolds averaging Equation {eq}`for:23b`, the divergence of a turbulent flux is obtained. Using this relation, the total thermodynamic equation reads

$$
\pafg{\theta}{t} + \overline{u_j}\pafg{\overline{\theta}}{x_j} + \pafg{\overline{u_j'\theta'}}{x_j} = \nu_{\theta}\pafg{^2\overline{\theta}}{{x_j}^2}-\frac{1}{\rho c_p} \pafg{\overline{Q_j}}{x_j} - \frac{L_v \overline{E}}{\rho c_p}
$$
```


b) Suppose that $\overline{w'\theta'}~=~a - bz$ where $a=0.3\ K\ m\ s^{-1}$ and $b=3 \cdot 10^{-4} K\ s^{-1}$.
How long will it take the ABL to warm up 0.54 K?

```{hint}
:class: tip, dropdown
From the $\overline{\theta}$ equation neglect subsidence, radiation
and latent heat releases and assume horizontal homogeneity.
```
```{admonition} Answer
:class: important, dropdown
Since there are no clouds, **no latent heat release** is present: $\overline{E}=0$.

The impact of **radiation** is relatively **small** during day: $\frac{1}{\rho c_p} \pafg{\overline{Q_j}}{x_j} \approx 0$.

Due to the **high turbulent nature** of the atmospheric boundary layer, the viscous term can be neglected as well: $\nu_{\theta}\pafg{^2\overline{\theta}}{{x_j}^2} \approx 0$.

We assume **horizontal homogeneity**, so $x$ and $y$ derivatives of Reynold's averaged variables are equal to 0. 

Without subsidence, the mean vertical wind velocity, $\overline{w}$, is equal to 0 as well.

Finally, the equation results in

$$
\pafg{\overline{\theta}}{t} = - \pafg{\overline{w'\theta'}}{z}
$$

Since $\pafg{\overline{w'\theta'}}{z} = - b$, $\pafg{\overline{\theta}}{t} = 3 \cdot 10^{-4}\rm\,K\,s^{-1}$. The time needed is equal to $\frac{0.54\rm\,K}{3 \cdot 10^{-4}\rm\,K\,s^{-1}} = 1800\,{\rm s} = \frac{1}{2}\,{\rm hr}$.

```

c) In a pseudo-stationary state, the vertical profile of the averaged potential
temperature is constant with time, i.e. $\left(\pafg{}{t}\right)\ \left(\pafg{\overline \theta}{z}\right) \approx 0$. Calculate
the heat flux profile $\overline {w'\theta'}(z)$ for the following boundary condition values of the heat flux
at $z=0~~$ $\overline {w'\theta'}(0)$ and at $z=h~~$ $\overline {w'\theta'}(h)$.

```{hint}
:class: tip, dropdown
Use the same assumptions as in 3b.
```
````{admonition} Answer
:class: important, dropdown
The governing equation is

$$
\pafg{\overline{\theta}}{t} = - \pafg{\overline{w'\theta'}}{z}
$$

By taking the derivative to $z$ of this equation, we obtain

$$
\pafg{}{z}\left(\pafg{\overline{\theta}}{t}\right) = - \pafg{^2\overline{w'\theta'}}{z^2} 
$$(for:23c1)

The left hand side can be rewritten:

$$
\pafg{}{z}\left(\pafg{\overline{\theta}}{t}\right) = \pafg{}{t}\left(\pafg{\overline{\theta}}{z}\right) \approx 0 
$$(for:23c2)

This is known as the quasi-steady approximation. It holds true under convective conditions and states that the gradient of potential temperature does not change on time.

Equations {eq}`for:23c1` and {eq}`for:23c2` show that

$$
\pafg{^2\overline{w'\theta'}}{z^2} &\approx 0\\
$$

This results in 

$$
\pafg{\overline{w'\theta'}}{z} &= C_1 \\
\overline{w'\theta'} &= C_1 z + C_2
$$ 

Using the boundary conditions:  

$\overline{w'\theta'} = \overline{w'\theta'}(0) + \left( \overline{w'\theta'}(h) - \overline{w'\theta'}(0) \right)\frac{z}{h}$  

In the figure, a visual representation is shown.

```{figure} figures/Exercise23c.png
:name: fig2.3
```

````

##
The conservation equation for a scalar (c) in the air can be
written as follows:

$$
\pafg{c}{t}+u_i\pafg{c}{x_i} = S
$$

where $S$ is a generic source/sink term.

Assume $S$ to have the form

$$
S=acT
$$

where a is a constant and T the absolute temperature.

Find the conservation equation for the mean concentration
$\overline{c}$ in a turbulent environment and put it in the "flux
form" (assume horizontal homogeneity and no subsidence).

```{admonition} Answer
:class: important, dropdown
$$
\pafg{c}{t} + u_i \pafg{c}{x_i} &= S \\
\pafg{\overline{c}}{t} + \overline{u_i \pafg{c}{x_i}} &= \overline{S} \\
\pafg{\overline{c}}{t} + \overline{u_i} \pafg{\overline{c}}{x_i} + \overline{u_i'\pafg{c'}{x_i}} &= \overline{a c T} 
$$

Now we assume horizontal homogeneity: $\pafg{\overline{\chi}}{x}=\pafg{\overline{\chi}}{y}=0$ for any arbitrary variable $\chi$. 
In the absence of subsidence, $\overline{w}=0$. This results in

$$
\pafg{\overline{c}}{t} + \overline{u_i'\pafg{c'}{x_i}} = \overline{a c T}
$$

Using incompressibility ($\pafg{u_i'}{x_i}=0$) and the chain rule

$$
\pafg{\overline{c}}{t} + \pafg{\overline{u_i'c'}}{x_i} = \overline{a c T} \\ 
\pafg{\overline{c}}{t} + \pafg{\overline{w'c'}}{z} = \overline{a c T} 
$$

So

$$ 
\pafg{\overline{c}}{t} &= -\pafg{\overline{w'c'}}{z} + \overline{a c T} \\ 
 &= -\pafg{\overline{w'c'}}{z} + a \overline{c T} \\
 &= -\pafg{\overline{w'c'}}{z} + a \overline{\left(\overline{c}+c'\right) \left(\overline{T}+T'\right)} \\
 &= -\pafg{\overline{w'c'}}{z} + a \overline{\left(\overline{c}{\overline{T}}+{c'}\overline{T}+\overline{c}{T'} + {c'}{T'} \right)}\\
$$

$$
\pafg{\overline{c}}{t} = -\pafg{\overline{w'c'}}{z} + a \left(\overline{cT}+\overline{c'T}+\overline{cT'} + \overline{c'T'} \right)\\
$$
```
