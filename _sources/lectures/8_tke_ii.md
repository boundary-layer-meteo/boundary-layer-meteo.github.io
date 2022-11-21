# Turbulence kinetic energy (ii)

```{admonition} Questions to be answered
1. What is the meaning of each of the terms in the conservation equations in this lecture?
1. Which terms do always produce turbulence?
1. Which terms do always destroy turbulence?
1. Which terms can both produce and destroy turbulence?
1. Which terms only transport turbulence?
1. Why are there no pressure redistribution term and the Coriolis term in the conservation equation for $\overline{e}$?
```

## Definition

In the previous lecture, we derived the equation that describes the conservation of mean turbulence variances.

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
\def\rhobar{\overline{\rho}}
\def\pdd#1#2{\dfrac{\partial^2 #1}{\partial#2^2}}
\def\uibar{\overline{u}_i}
\def\ujbar{\overline{u}_j}
\def\uiprime{u_i^\prime}
\def\uiprimesq{u_i^{\prime 2}}
\def\uiprimesqbar{\overline{u_i^{\prime 2}}}
\def\ujprime{u_j^\prime}
  \pd{\uiprimesqbar}{t}
+ \pd{\uiprimesqbar \ujbar}{x_j}
=
- \pd{\overline{\uiprimesq \ujprime}}{x_j}
- 2 \overline{\uiprime \ujprime} \pd{\uibar}{x_j}
- \dfrac{2}{\rhobar} \pd{\overline{\uiprime p^\prime}}{x_i}
+ \dfrac{2}{\rhobar} \overline{ p^\prime \pd{\uiprime}{x_i} }
+ 2 f \epsilon_{ij3} \overline{ \uiprime \ujprime }
+ 2 \delta_{i3} \dfrac{g}{\overline{\theta}_\mathrm{v}} \overline{ \uiprime \theta_\mathrm{v}^\prime}
+ \nu \pdd{\uiprimesqbar}{x_j}
- 2 \nu \overline{ \left( \pd{\uiprime}{x_j} \right)^2}
$$

If we define $e \equiv \frac{1}{2} \uiprimesq$, and assume the viscous transport is small, we can write the general equation for TKE conservation as


```{admonition} Conservation of turbulence kinetic energy (TKE)
$$
  \pd{\ebar}{t}
+ \pd{\ebar\,\ujbar}{x_j}
=
- \pd{\overline{e\ujprime}}{x_j}
- \overline{\uiprime \ujprime} \pd{\uibar}{x_j}
- \dfrac{1}{\rhobar} \pd{\overline{\uiprime p^\prime}}{x_i}
+ \delta_{i3} \dfrac{g}{\overline{\theta}_\mathrm{v}} \overline{ \uiprime \theta_\mathrm{v}^\prime}
- \nu \overline{ \left( \pd{\uiprime}{x_j} \right)^2}
$$
```

If we now assume horizontal homogeneity and no subsidence, and define the dissipation as $\epsilon \equiv \nu \overline{ \left( \pd{\uiprime}{x_j} \right)^2}$, we can write

```{admonition} Conservation of turbulence kinetic energy (TKE) under horizontal homogeneity
$$
  \pd{\ebar}{t}
=
- \pd{\overline{e  w^\prime}}{z}
- \overline{u^\prime w^\prime} \pd{\ubar}{z}
- \overline{v^\prime w^\prime} \pd{\vbar}{z}
- \dfrac{1}{\rhobar} \pd{\overline{w^\prime p^\prime}}{z}
+ \dfrac{g}{\overline{\theta}_\mathrm{v}} \overline{ w^\prime \theta_\mathrm{v}^\prime}
- \epsilon
$$
```
