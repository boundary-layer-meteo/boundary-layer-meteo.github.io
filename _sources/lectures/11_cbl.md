# Convective boundary layer

## Derivation of the mixed-layer model

During daytime, there is a well-mixed convective boundary layer of approximately 1 km in depth.
If we assume horizontal homogeneity, no subsidence and high Reynolds numbers, the conservation of energy in this layer can be described as

$$
\def\pd#1#2{\dfrac{\partial #1}{\partial #2}}
\def\thetabar{\overline{\theta}}
\def\qbar{\overline{q}}
\def\thetabulk{\left< \thetabar \right>}
\def\qbulk{\left< \qbar \right>}
\pd{\overline{\theta}}{t} = - \pd{\overline{w^\prime \theta^\prime}}{z} 
$$

The well-mixed property of this layer allows us to derive a very simple bulk model (thus no spatial derivatives).
We integrate from surface to the depth of the layer.

$$
\int_0^h \pd{\thetabar}{t} \mathrm{d}z  = - \int_0^h \pd{\overline{w^\prime \theta^\prime}}{z} \mathrm{d}z
$$

We rewrite the lefthand side using Leibniz' rule:

$$
\dfrac{\mathrm{d}}{\mathrm{d} t} \int_0^h \thetabar \, \mathrm{d}z
= \int_0^h \pd{\thetabar}{t} \mathrm{d}z
+ \dfrac{\mathrm{d} h}{\mathrm{d} t} \thetabar \left(h\right)
- \dfrac{\mathrm{d} 0}{\mathrm{d} t} \thetabar \left(0\right)
$$

where the last term is equal to zero.

If we define the bulk mean temperature of the convective boundary layer

$$
\thetabulk = \dfrac{1}{h} \int_0^h \thetabar \, \mathrm{d} z
$$

and substitute the lefthand side of the integrated equation with the help of the Leibniz rule to get


$$
\dfrac{\mathrm{d}}{\mathrm{d} t} \left( \thetabulk h \right)
- \dfrac{\mathrm{d} h}{\mathrm{d} t} \thetabar \left(h\right)
= 
- \overline{w^\prime \theta^\prime} \left( h \right)
+ \overline{w^\prime \theta^\prime} \left( 0 \right)
\\
  \dfrac{\mathrm{d} \thetabulk}{\mathrm{d} t} h
+ \dfrac{\mathrm{d} h}{\mathrm{d} t} \thetabulk
- \dfrac{\mathrm{d} h}{\mathrm{d} t} \thetabar \left(h\right)
= 
\overline{w^\prime \theta^\prime} \left( 0 \right)
- \overline{w^\prime \theta^\prime} \left( h \right)
$$

If we assume that the boundary layer is well-mixed, the bulk temperature $\thetabulk$ and the boundary-layer top temperature $\thetabar \left( h \right)$ equal and after division by $h$ the final equation can be written as 

$$
  \dfrac{\mathrm{d} \thetabulk}{\mathrm{d} t}
= 
\dfrac{ \overline{w^\prime \theta^\prime} \left( 0 \right)
- \overline{w^\prime \theta^\prime} \left( h \right) }{h}
$$


Similarly, we can derive a budget around the mixed-layer top

$$
\int_{h-\epsilon}^{h + \epsilon} \pd{\thetabar}{t} \mathrm{d}z  = - \int_{h-\epsilon}^{h + \epsilon} \pd{\overline{w^\prime \theta^\prime}}{z} \mathrm{d}z
$$

Again with application of Leibniz rule, we can write

$$
\dfrac{\mathrm{d}}{\mathrm{d} t} \int_{h - \epsilon}^{h + \epsilon} \thetabar \, \mathrm{d}z
- \dfrac{\mathrm{d} \left( h + \epsilon \right) }{\mathrm{d} t} \thetabar \left(h + \epsilon \right)
+ \dfrac{\mathrm{d} \left( h - \epsilon \right) }{\mathrm{d} t} \thetabar \left(h - \epsilon \right)
= 
- \overline{w^\prime \theta^\prime} \left( h + \epsilon \right)
+ \overline{w^\prime \theta^\prime} \left( h - \epsilon \right)
$$

If we take the limit of $\epsilon$ going to zero, then the first term goes to zero.
The second and third term can be combined, taking into account that temperature at $h$ approached from below is $\thetabar$, while from above $\thetabar + \Delta \theta$.
The first term on the righthand side is zero, as the flux at $h$ approached from above equals zero.
All these assumptions give

$$
- \dfrac{\mathrm{d} h}{\mathrm{d} t} \Delta \theta
= 
  \overline{w^\prime \theta^\prime} \left( h \right)
$$

which can be rewritten into

$$
\dfrac{\mathrm{d} h}{\mathrm{d} t} = 
- \dfrac{\overline{w^\prime \theta^\prime} \left( h \right)}{\Delta \theta}
$$

As a last step, we need an evolution equation for the jump $\Delta \theta$.
This evolution is a competition of boundary layer growth that makes the jump larger, and boundary-layer heating that makes the jump smaller.

$$
\dfrac{\mathrm{d} \Delta \theta}{\mathrm{d} t} = 
  \gamma_{\theta} \dfrac{\mathrm{d} h}{\mathrm{d} t}
- \dfrac{\mathrm{d} \thetabulk}{\mathrm{d} t}
$$

These three equations combined provide the set of mixed-layer equations. We have, however, a new closure problem, because we do not know the entrainment flux.
Analysis of field measurements have revealed that the total entrainment of virtual potential temperature is a fixed fraction $\beta$ of its surface flux

$$
\dfrac{\mathrm{d} h}{\mathrm{d} t} = 
\beta \dfrac{\overline{w^\prime \theta_v^\prime} \left( 0 \right)}{\Delta \theta_v}
$$

The growth rate of the boundary layer due to entrainment is often also called the entrainment velocity $w_e$, such that in absense of subsidence $\mathrm{d}h / \mathrm{d}t = w_e$

We can now write down the total set

```{admonition} Mixed-layer equations for potential temperature
$$
  \dfrac{\mathrm{d} \thetabulk}{\mathrm{d} t}
&= 
\dfrac{ \overline{w^\prime \theta^\prime} \left( 0 \right)
- \overline{w^\prime \theta^\prime} \left( h \right) }{h}
\\
\overline{w^\prime \theta^\prime} \left( h \right) &= - w_e {\Delta \theta}
\\
\dfrac{\mathrm{d} \Delta \theta}{\mathrm{d} t}
&= 
  \gamma_{\theta} \dfrac{\mathrm{d} h}{\mathrm{d} t}
- \dfrac{\mathrm{d} \thetabulk}{\mathrm{d} t}
\\
w_e &= \beta \dfrac{\overline{w^\prime \theta_v^\prime} \left( 0 \right)}{\Delta \theta_v}
$$
```

In a similar fashion, we can construct the set for $q$

```{admonition} Mixed-layer equations for specific humidity
$$
  \dfrac{\mathrm{d} \qbulk}{\mathrm{d} t}
&= 
\dfrac{ \overline{w^\prime q^\prime} \left( 0 \right)
- \overline{w^\prime q^\prime} \left( h \right) }{h}
\\
\overline{w^\prime q^\prime} \left( h \right) &= - w_e {\Delta q}
\\
\dfrac{\mathrm{d} \Delta q}{\mathrm{d} t}
&= 
  \gamma_{q} \dfrac{\mathrm{d} h}{\mathrm{d} t}
- \dfrac{\mathrm{d} \qbulk}{\mathrm{d} t}
$$
```

where make use of the same entrainment velocity defined earlier.


## The Deardorff velocity scale
The velocities in the convective boundary layer in its most basic form are governed by two variables: the surface buoyancy flux $\dfrac{g}{\overline{\theta}_\mathrm{v}} \overline{ w^\prime \theta_\mathrm{v}^\prime}_0$ and the boundary layer depth $h$. From these two variables a velocity scale $w_*$ can be derived.

```{admonition} The Deardorff velocity scale
$$
w_* \equiv \left( \dfrac{g}{\overline{\theta}_\mathrm{v}} \overline{ w^\prime \theta_\mathrm{v}^\prime}_0 h \right)^\frac{1}{3}
$$
```

The Deardorff velocity scale $w_*$ is an estimate of the velocity of a typical plume in the convective boundary layer, and can be used to normalize the velocity variances to universal profiles, as shown in the lecture. A typical value for $w_*$ in a daytime boundary layer is ~1 m s$^{-1}$
