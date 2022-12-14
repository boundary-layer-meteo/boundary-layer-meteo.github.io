# Kolmogorov scaling

```{admonition} Questions to be answered in this chapter
1. What are the length and time scales of production and dissipation of turbulence?
```


## Length and time scales of turbulence
Production of turbulence happens at large spatial and temporal scales present in the atmospheric boundary layer flow, whereas dissipation of turbulence happens at the smallest scales present.

Production happens due to shear, or due to buoyancy. Dissipation of turbulence happens to processes happening at the scales where viscosity can act. The strict scale separation between production and dissipation allow for some interesting dimensional analysis.

Let us take the neutral surface layer as an example. Here, turbulence is generated at the depth of the surface layer $L$ by a typical wind speed $U$ and is dissipated at the smallest scale with a viscosity $\nu$.
Since at high Reynolds numbers production does not feel viscosity, the production, with units $\mathrm{m}^2\ \mathrm{s}^{-3}$, must be proportional with $U^3 L^{-1}$, and the associated length and time scale are $L$ and $T \equiv L U^{-1}$.
As dissipation is the mechanism to destroy production the amount of dissipation equals the production, but the spatial and temporal scales at which this happen depends strongly on the viscosity $\nu$.
Dimensional reasoning leads us to the Kolomogorov scales: the only length and time scales that we can form from the dissipation and the viscosity

```{admonition} The Kolmogorov scales
The Kolmogorov length scale $\eta$ is

$$
\eta \equiv \left( \dfrac{\nu^3}{\epsilon} \right)^\frac{1}{4}
= \left( \dfrac{\nu^3 L}{U^3} \right)^\frac{1}{4}.
$$

The Kolmogorov time scale $T_\epsilon$ is

$$
T_\epsilon \equiv \left( \dfrac{\nu}{\epsilon} \right)^\frac{1}{2}
= \left( \dfrac{\nu L}{U^3} \right)^\frac{1}{2}.
$$
```

```{admonition} Question
:class: seealso
What is the ratio in length scales, often referred to as scale separation, between production and dissipation in a neutral atmospheric surface layer with wind speed $U$ of $\mathrm{10\ m\ s^{-1}}$, depth $L$ of $100\ \mathrm{m}$, and kinematic viscosity $\nu$ of $1.5 \cdot 10^{-5}\ \mathrm{m\ s^{-1}}$?
```

```{admonition} Answer
:class: important, dropdown

$$
\dfrac{L}{\eta} &= L \left( \dfrac{U^3}{\nu^3 L} \right)^\frac{1}{4} = \left( \dfrac{U L}{\nu} \right)^\frac{3}{4} \\
                &= \left( \dfrac{10 \cdot 100}{1.5 \cdot 10^{-5}} \right)^\frac{3}{4} \approx 7.38 \cdot 10^{5}
$$

```

