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

````{Admonition} Answer
:class: important, dropdown

```{figure} figures/exercise8_1.png
:name: fig:ans81
Relation between atmospheric stability and plume dispersion
```
````

##
Starting from the Gaussian formula

$$
C=\frac{Q}{2\pi\sigma_y \sigma_zU}
exp\left[-\frac{y^2}{2\sigma_y^2}-\frac{(z-H)^2}{2\sigma_z^2}-\frac{(z+H)^2}{2\sigma_z^2}\right]
$$

where $H=100m$ is the effective source height, find:

a) The concentration at ground in the centerline of the plume $C(x,0,0)U/Q$.
```{Admonition} Answer
:class: important, dropdown

$$
C(x,0,0)\frac{U}{Q} = \frac{1}{2\pi\sigma_y\sigma_z}{\rm e}^{-\frac{H^2}{\sigma_z^2}}
$$

This equation also shows that by normalizing the concentration with $U$ and $Q$, it can be expressed as function of the statistical properties of the Gaussian plume.

```

b) Plot $C(x,0,0)U/Q$ as function of the distance $x$ (from 0 to 3000 m) for the following stability classes:
1. unstable conditions (Pasquill class A): $\sigma_y(x)=0.22x(1+0.0001x)^{-0.5}$, $\sigma_z(x)=0.20x$
2. neutral conditions (Pasquill class D): $\sigma_y(x)=0.08x(1+0.0001x)^{-0.5}$, $\sigma_z(x)=0.06x(1+0.0015x)^{-0.5}$

````{Admonition} Answer
:class: important, dropdown

```{figure} figures/exercise8_2.png
:name: fig:ans82
Normalized particle concentration as a function of horizontal distance from the source
```

$C(x,0,0)\frac{U}{Q}$ is plotted as a function of the distance, $x$, in {numref}`fig:ans82`. 

In the case of neutral conditions, there is less mixing in the boundary layer than in the case of unstable conditions. 
Because of this, the concentration is lower nearby the source. 
Particles are less efficiently mixed in the boundary layer, so they reach the surface at a later time. 
However, at further distances from the source, the concentration is higher due to the fact that the plume then reaches the surface but still is more dense 
(higher concentrations) than the plume under unstable conditions.
 ````


c) For the unstable condition find at which distance $x$ the ground concentration $C(x,0,0)U/Q$ reaches a maximum. 
```{hint}
:class: tip, dropdown
The maximum of the function $f(x)$ is reached at $x$ for which $\pafg{f}{x}=0$.
```
```{Admonition} Answer
:class: important, dropdown
The normalized surface concentration is at its maximum when

$$
\pafg{}{x}\left(C(x,0,0)\frac{U}{Q}\right) &= 0 \\
\pafg{C(x,0,0)}{x} &= 0\\
\pafg{}{x}\left(\frac{1}{2\pi\sigma_y\sigma_z} {\rm e}^{-\frac{H^2}{\sigma_z^2}}\right) &= 0 \\
\pafg{}{x}\left(\frac{1}{\sigma_y}\,\frac{1}{\sigma_z}\,{\rm e}^{-\frac{H^2}{\sigma_z^2}}\right) &= 0
$$

Using the product rule results in

$$
-\frac{1}{\sigma_y^2}\pafg{\sigma_y}{x} \,\frac{1}{\sigma_z}\,{\rm e}^{-\frac{H^2}{\sigma_z^2}}
-\frac{1}{\sigma_y}\, \frac{1}{\sigma_z^2}\pafg{\sigma_z}{x} \,{\rm e}^{-\frac{H^2}{\sigma_z^2}}
+ \frac{1}{\sigma_y}\,\frac{1}{\sigma_z}\,{\rm e}^{-\frac{H^2}{\sigma_z^2}} \left(-\left(-\frac{2 H^2}{\sigma_z^3}\right)\right)\pafg{\sigma_z}{x} = 0
$$

After dividing by $\frac{1}{\sigma_y}\,\frac{1}{\sigma_z}\,{\rm e}^{-\frac{H^2}{\sigma_z^2}}$, the criterion becomes

$$
-\frac{1}{\sigma_y}\pafg{\sigma_y}{x} -\frac{1}{\sigma_z}\pafg{\sigma_z}{x} + \frac{2 H^2}{\sigma_z^3}\pafg{\sigma_z}{x} = 0
$$

Under unstable conditions, $\sigma_z = 0.20 x$ and $\pafg{\sigma_z}{x} = 0.20$. Therefore,

$$
-\frac{1}{\sigma_y}\pafg{\sigma_y}{x} -\frac{1}{x} + \frac{2 H^2}{0.04 x^3} &= 0 \\
-\pafg{{\rm ln}\left(\sigma_y\right)}{x} -\frac{1}{x} + \frac{2 H^2}{0.04 x^3} &= 0 
$$(for:82c)

We first evaluate the term 

$$
\pafg{{\rm ln}\left(\sigma_y\right)}{x} &= \pafg{{\rm ln}\left(0.22 x \left( 1 + 0.0001 x \right)^{-0.5} \right)}{x} \\
&= \pafg{{\rm ln}\left(0.22 x\right)}{x} + \pafg{{\rm ln}\left( 1 + 0.0001 x \right)^{-0.5}}{x} \\
&= \frac{1}{x} + \pafg{\left(-0.5 {\rm ln}\left( 1 + 0.0001 x \right)\right)}{x} \\
&= \frac{1}{x} - 0.5 \pafg{ {\rm ln}\left( 1 + 0.0001 x \right)}{x}\\
&= \frac{1}{x} - 0.5 \frac{1}{1 + 0.0001 x} 0.0001 \\
&= \frac{1}{x} - \frac{0.5\times 10^{-4}}{1 + 0.0001 x}
$$

In the evaluated range of distances, $0 \leq x \leq 3000\rm\,m$ , 
the $2^{\rm nd}$ term on the right hand side is at least an order of magnitude smaller than the $1^{\rm st}$ term. 
We therefore, approximate that 

$$
\pafg{{\rm ln}\left(\sigma_y\right)}{x} \approx \frac{1}{x}
$$

Using this approximation, Equation {eq}`for:82c` becomes

$$
-\frac{1}{x} -\frac{1}{x} + \frac{2 H^2}{0.04 x^3} &\approx 0 \\
\frac{2 H^2}{0.04 x^3} &\approx \frac{2}{x}\\
x^2 &\approx 25 H^2
$$

Therefore, the maximum is reached at $x\approx 5H$

In this case, this is equal to 500 m.

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
```{Admonition} Answer
:class: important, dropdown

Skewness is a measure of what sign and magnitude the extreme values have. 

Positive skewness in the boundary layer corresponds to large regions with slowly descending air and small regions with quickly rising air. 
An example is a set with 3 samples of $w$: $\rm\left(-1\,m\,s^{-1},-1\,m\,s^{-1},2\,m\,s^{-1}\right)$. 
This results in $\overline{w'^3} = 2\rm\,m^3\,s^{-3}$ and $S_w = \frac{1}{\sqrt{2}}\rm\,m\,s^{-1}$. 
In the convective boundary layer we have few thermals with high velocities, surrounded by large areas with (compensating) descending air.

Negative skewness would correspond to large regions with slowly rising air and small regions with quickly descending air. 
During transport the smoke plume gradually widens. 
In the meanwhile, the smoke is occasionally quickly transported downward after which it slowly rises again. 
This transport is exactly opposite in a normal CBL (which has positive skewness).

```


##
Starting from the Gaussian formula for an instantaneous release written in in two-dimensional form:

$$
C=\frac{Q}{2\pi\sigma_x
\sigma_z}exp\left[-\frac{(x-Ut)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}\right]
$$

prove that

$K_x=\frac{1}{2}\pafg{\sigma_x^2}{t}$ and $K_z=\frac{1}{2}\pafg{\sigma_z^2}{t}$

```{hint}
:class: tip, dropdown
Hint: calculate

$$
\pafg{C}{t} + U\pafg{C}{x}, \\
\pafg{^2 C}{x^2}, \\
\pafg{^2 C}{z^2}
$$

and show that

$$
\pafg{C}{t} + U\pafg{C}{x}=K_x\pafg{^2 C}{x^2}+K_z\pafg{^2 C}{z^2}
$$
```

```{Admonition} Answer
:class: important, dropdown
In general,

$$
\pafg{c}{t} + u_i\pafg{c}{x_i} = S
$$

$S$ are the sources and sinks in the boundary layer. 
Since chemistry is not considered and there is no emission or deposition except for the original emission source, 
$S=0$ as long as the emission source is not evaluated. 
Reynold's averaging results in

$$
\gemafg{c}{t} + \overline{u_i\pafg{c}{x_i}} = 0\\
\gemafg{c}{t} + \overline{u_i}\overline{\pafg{c}{x_i}} + \overline{u_i'\left(\pafg{c}{x_i}\right)'} = 0\\
\gemafg{c}{t} + \overline{u_i}{\gemafg{c}{x_i}} + \overline{u_i'\pafg{c'}{x_i}} = 0
$$

Considering incompressibility, $\pafg{u_i}{x_i}=\gemafg{u_i}{x_i}=\pafg{u_i'}{x_i}=0$, this results in 

$$
\gemafg{c}{t} + \overline{u_i}{\gemafg{c}{x_i}} + \overline{u_i'\pafg{c'}{x_i}} + \overline{c'\pafg{u_i'}{x_i}} = 0\\
\gemafg{c}{t} + \overline{u_i}{\gemafg{c}{x_i}} + \overline{\pafg{u_i'c'}{x_i}}  = 0 \\
\gemafg{c}{t} + \overline{u_i}{\gemafg{c}{x_i}} + {\gemafg{u_i'c'}{x_i}}  = 0
$$

In this case no horizontal homogeneity can be assumed, since the $x$-position clearly influences the evaluated concentration.
In cases without subsidence, $w=0$. Considering $C=\overline{c}$ and $U\overline{u}$, 

$$
\pafg{C}{t} + {U}{\gemafg{C}{x}} = - {\gemafg{u'c'}{x}} - {\gemafg{w'c'}{z}} 
$$

Since the situation under evaluation is 2D. 
To determine the turbulent fluxes, one can use the flux-gradient relationships and the exchange coefficients. 
The closure expression reads

$$
\overline{u'c'} &= - K_x \gemafg{c}{x}\\
\overline{w'c'} &= - K_z \gemafg{c}{z}
$$

Therefore,

$$
\pafg{C}{t} + {U}{\gemafg{C}{x}} &= - {\gemafg{}{x}\left(- K_x \gemafg{c}{x}\right)} - {\gemafg{}{z}\left(- K_z \gemafg{c}{z}\right)} \\
\pafg{C}{t} + {U}{\gemafg{C}{x}} &= K_x \pafg{^2 C}{x^2} + K_z \pafg{^2 C}{z^2} 
$$(for:finalex_temp)

Assuming that $K_x$ and $K_z$ are not dependent on $x$ or $z$.

Now, start from the expression for $C$:

$$
{C} = \frac{Q}{2\pi\sigma_x\sigma_z}{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}}
$$

Representing the left hand side of Equation {eq}`for:finalex_temp`, results in 

$$
\pafg{C}{t} + {U}{\gemafg{C}{x}} &=  
\left(\frac{Q}{2\pi\sigma_z}\pafg{\frac{1}{\sigma_x}}{t}+\frac{Q}{2\pi\sigma_x}\pafg{\frac{1}{\sigma_z}}{t}\right)
{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}} + 
\frac{Q}{2\pi\sigma_x\sigma_z}{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}} 
\pafg{}{t} \left(-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}\right) + 
U \frac{Q}{2\pi\sigma_x\sigma_z}{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}} 
\pafg{}{x}\left(-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}\right) \\
       
&= \left(\frac{Q}{2\pi\sigma_z}{\frac{-1}{\sigma_x^2}}\pafg{\sigma_x}{t}+\frac{Q}{2\pi\sigma_x}{\frac{-1}{\sigma_z^2}}\pafg{\sigma_z}{t}\right)
{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}} + 
C \left( \pafg{}{t} \left(-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}\right) 
+ U \pafg{}{x}\left(-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}-\frac{z^2}{2\sigma_z^2}\right) \right) \\
    
&= \left(\frac{-1}{\sigma_x}\pafg{\sigma_x}{t} + \frac{-1}{\sigma_z}\pafg{\sigma_z}{t}\right) C 
+ C \Bigg( -2 \frac{\left(x-Ut\right)}{2\sigma_x^2} \pafg{\left(x-U t\right)}{t} 
+ \frac{\left(x-Ut\right)^2}{2\left(\sigma_x^2\right)^2} \pafg{\sigma_x^2}{t} 
+ \frac{z^2}{2\left(\sigma_z^2\right)^2} \pafg{\sigma_z^2}{t} 
+ U \left(-2 \frac{\left(x-Ut\right)}{2\sigma_x^2} \pafg{\left(x-U t\right)}{x}\right) \Bigg) 
$$

This is derived, assuming that $\sigma_x$ and $\sigma_z$ are only dependent on time and not on $x$ or $z$. 

This equation is further solved as

$$
\pafg{C}{t} + {U}{\gemafg{C}{x}} &= 
C \Bigg( 
\frac{-1}{\sigma_x}\pafg{\sigma_x}{t} 
+ \frac{-1}{\sigma_z}\pafg{\sigma_z}{t} 
+ 2 U \frac{\left(x-Ut\right)}{2\sigma_x^2} 
+ \frac{\left(x-Ut\right)^2}{2\left(\sigma_x^2\right)^2} \pafg{\sigma_x^2}{t} 
+ \frac{z^2}{2\left(\sigma_z^2\right)^2} \pafg{\sigma_z^2}{t} 
- 2 U \frac{\left(x-Ut\right)}{2\sigma_x^2} 
\Bigg)\\

&= C \Bigg(
\frac{-1}{2\sigma_x^2}\left(2\sigma_x\pafg{\sigma_x}{t}\right) 
+ \frac{-1}{2\sigma_z^2}\left(2\sigma_z\pafg{\sigma_z}{t}\right) 
+ \frac{\left(x-Ut\right)^2}{2\left(\sigma_x^2\right)^2} \pafg{\sigma_x^2}{t} 
+ \frac{z^2}{2\left(\sigma_z^2\right)^2} \pafg{\sigma_z^2}{t} 
\Bigg) \\
 
\pafg{C}{t} + {U}{\gemafg{C}{x}} &= 
\frac{1}{2} \pafg{\sigma_x^2}{t} \left(\frac{\left(x-Ut\right)^2}{\sigma_x^4}-\frac{1}{\sigma_x^2}\right) C  
+ \frac{1}{2}\pafg{\sigma_z^2}{t} \left(\frac{z^2}{\sigma_z^4} - \frac{1}{\sigma_z^2}\right) C 
$$(for:totaleq84)

Now we evaluate $\pafg{^2 C}{x^2}$ and $\pafg{^2 C}{z^2}$.

$$
\pafg{^2 C}{x^2} &= 
\pafg{}{x} \pafg{}{x} \left(\frac{Q}{2\pi\sigma_x\sigma_z}{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}}{\rm e}^{-\frac{z^2}{2\sigma_z^2}}\right)\\

 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} \pafg{}{x} \pafg{}{x} 
 \left({\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}}\right)\\
 
 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} \pafg{}{x} 
 \left( {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} \pafg{\left({-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}}\right)}{x}\right) \\
 
 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} \pafg{}{x} 
 \left( {-\frac{2\left(x-Ut\right)}{2\sigma_x^2}} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} \right)\\
 
 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} 
 \left( {-\frac{1}{\sigma_x^2}} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} + 
 \left({-\frac{\left(x-Ut\right)}{\sigma_x^2}}\right)\pafg{}{x}{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} \right)\\
 
 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} 
 \left( {-\frac{1}{\sigma_x^2}} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} + 
 \left({-\frac{\left(x-Ut\right)}{\sigma_x^2}}\right)^2 {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} \right) \\
 
\pafg{^2 C}{x^2} &= C \left({-\frac{1}{\sigma_x^2}} + \frac{\left(x-Ut\right)^2}{\sigma_x^4} \right) 
$$(for:84derx)

And

$$
\pafg{^2 C}{z^2} &= 
\pafg{}{z} \pafg{}{z} \left(\frac{Q}{2\pi\sigma_x\sigma_z}{\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}}{\rm e}^{-\frac{z^2}{2\sigma_z^2}}\right)\\

 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} \pafg{}{z} \pafg{}{z} \left({\rm e}^{-\frac{z^2}{2\sigma_z^2}}\right)\\

 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} \pafg{}{z} 
 \left({\rm e}^{-\frac{z^2}{2\sigma_z^2}} \pafg{\left(-\frac{z^2}{2\sigma_z^2}\right)}{z}\right) \\

 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} \pafg{}{z} 
 \left(-\frac{2 z}{2\sigma_z^2} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} \right) \\

 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} 
 \left(-\frac{1}{\sigma_z^2} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} -\frac{z}{\sigma_z^2} \pafg{}{z} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} \right) \\

 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} 
 \left(-\frac{1}{\sigma_z^2} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} -\frac{z}{\sigma_z^2} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} 
 \pafg{\left(-\frac{z^2}{2\sigma_z^2}\right)}{z} \right) \\

 &= \frac{Q}{2\pi\sigma_x\sigma_z} {\rm e}^{-\frac{\left(x-Ut\right)^2}{2\sigma_x^2}} 
 \left(-\frac{1}{\sigma_z^2} {\rm e}^{-\frac{z^2}{2\sigma_z^2}} + \left(-\frac{z}{\sigma_z^2}\right)^2 {\rm e}^{-\frac{z^2}{2\sigma_z^2}} \right) \\

 \pafg{^2 C}{z^2} &= C \left(-\frac{1}{\sigma_z^2} + \frac{z^2}{\sigma_z^4} \right) 
$$(for:84derz)

Combining Equations {eq}`for:totaleq84`, {eq}`for:84derx` and {eq}`for:84derz` results in

$$
\pafg{C}{t} + {U}{\gemafg{C}{x}} = \frac{1}{2} \pafg{\sigma_x^2}{t} \pafg{^2 C}{x^2} + \frac{1}{2}\pafg{\sigma_z^2}{t} \pafg{^2 C}{z^2}
$$

Since Equation {eq}`for:finalex_temp` stated that

$$
\pafg{C}{t} + {U}{\gemafg{C}{x}} = K_x \pafg{^2 C}{x^2} + K_z \pafg{^2 C}{z^2} 
$$

(and $\pafg{^2 C}{x^2}$ is independent of $\pafg{^2 C}{z^2}$), it can be seen that

$$
K_x &= \frac{1}{2} \pafg{\sigma_x^2}{t}\\
K_z &= \frac{1}{2} \pafg{\sigma_z^2}{t}
$$

```
