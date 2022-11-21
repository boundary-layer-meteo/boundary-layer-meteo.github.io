# Richardson numbers

```{admonition} Questions to be answered
1. What does the Richardson number describe?
1. What is the difference between the flux-, gradient- and bulk-Richardson number?
1. At which Richardson numbers is the boundary layer statically unstable?
1. At which Richardson numbers is the boundary layer statically stable?
1. At which Richardson numbers is the boundary layer dynamically unstable?
1. At which Richardson numbers is the boundary layer dynamically stable?
```


$$
\def\ubar{\overline{u}}
\def\vbar{\overline{v}}
\def\wbar{\overline{w}}
\def\ebar{\overline{e}}
\def\uprime{u^\prime}
\def\vprime{v^\prime}
\def\wprime{w^\prime}
\def\uvar{\overline{u^{\prime 2}}}
\def\vvar{\overline{v^{\prime 2}}}
\def\wvar{\overline{w^{\prime 2}}}
\def\pd#1#2{\dfrac{\partial #1}{\partial #2}}
\def\fd#1#2{\dfrac{\Delta #1}{\Delta #2}}
\def\rhobar{\overline{\rho}}
\def\pdd#1#2{\dfrac{\partial^2 #1}{\partial#2^2}}
\def\uibar{\overline{u}_i}
\def\ujbar{\overline{u}_j}
\def\uiprime{u_i^\prime}
\def\uiprimesq{u_i^{\prime 2}}
\def\uiprimesqbar{\overline{u_i^{\prime 2}}}
\def\ujprime{u_j^\prime}
  \underbrace{\pd{\ebar}{t}}_\textrm{storage}
=
\underbrace{ - \pd{\overline{e  w^\prime}}{z} }_\textrm{turbulent transport}
\underbrace{ - \overline{u^\prime w^\prime} \pd{\ubar}{z}
             - \overline{v^\prime w^\prime} \pd{\vbar}{z} }_\textrm{shear}
\underbrace{ - \dfrac{1}{\rhobar} \pd{\overline{w^\prime p^\prime}}{z}}_\textrm{pressure transport}
\underbrace{ + \dfrac{g}{\overline{\theta}_\mathrm{v}} \overline{ w^\prime \theta_\mathrm{v}^\prime} }_\textrm{buoyancy}
\underbrace{ - \epsilon }_\textrm{dissipation}
$$

Turbulence generation is done by shear and, depending on its sign, buoyancy, while dissipation destroys turbulence at the smallest scales.
The Richardson numbers relates the magnitude of buoyancy and shear production to each other.

The flux-Richardson number is defined as

```{admonition} Flux-Richardson number
$$
Ri_\mathrm{f} \equiv
\dfrac{\dfrac{g}{\overline{\theta}_\mathrm{v}} \overline{ w^\prime \theta_\mathrm{v}^\prime}}
{\overline{u^\prime w^\prime} \pd{\ubar}{z} + \overline{v^\prime w^\prime} \pd{\vbar}{z}}
$$
```

The value of $Ri_\mathrm{f}$ can teach us something about the nature of the flow
* If $Ri_\mathrm{f} < 0$ the flow is statically and dynamically unstable
* If $0 < Ri_\mathrm{f} < 1$ the flow is statically stable and dynamically unstable
* If $Ri_\mathrm{f} > 1$ the flow is statically and dynamically stable


Via K-theory, fluxes can be related to gradients. Consequently, we can rewrite the flux-Richardson number as:

$$
Ri_\mathrm{f} =
\dfrac{  -K_\theta \dfrac{g}{\overline{\theta}_\mathrm{v}} \pd{\overline{\theta}_\mathrm{v}}{z}}
{ -K_\mathrm{m} \pd{\ubar}{z} \pd{\ubar}{z} - K_\mathrm{m} \pd{\vbar}{z} \pd{\vbar}{z}}
$$

If we assume that the turbulent diffusion coefficients $K_\mathrm{m}$ and $K_\theta$ are equal, we arrive at the definition of the gradient Richardson number

```{admonition} Gradient-Richardson number
$$
Ri_\mathrm{g} \equiv
\dfrac{\dfrac{g}{\overline{\theta}_\mathrm{v}} \pd{\overline{\theta}_\mathrm{v}}{z}}
{\left( \pd{\ubar}{z} \right)^2 + \left( \pd{\vbar}{z} \right)^2}
$$
```

Field observations have shown that laminar flow can become turbulent if $Ri_\mathrm{g}$ is below 0.25.

We can also define a finite difference approximation of the gradient Richardson number called the Bulk Richardson number

$$
Ri_\mathrm{g} \approx
\dfrac{\dfrac{g}{\overline{\theta}_\mathrm{v}} \fd{\overline{\theta}_\mathrm{v}}{z}}
{\left( \fd{\ubar}{z} \right)^2 + \left( \fd{\vbar}{z} \right)^2}
$$

which can be simplified to

```{admonition} Bulk-Richardson number
$$
Ri_\mathrm{B} \equiv
\dfrac{g \Delta \overline{\theta}_\mathrm{v} \Delta z}
{\overline{\theta}_\mathrm{v} \left( \left( \Delta \ubar \right)^2 + \left( \Delta \vbar \right)^2 \right)}
$$
```

