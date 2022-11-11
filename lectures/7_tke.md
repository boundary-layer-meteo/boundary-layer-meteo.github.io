# Turbulence Kinetic Energy (TKE)

$$
\def\ubar{\overline{u}}
\def\vbar{\overline{v}}
\def\wbar{\overline{w}}
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
\def\ujprime{u_j^\prime}
\def\ubar{\overline{u}}
\def\vbar{\overline{v}}
\def\wbar{\overline{w}}
$$

## Definition

The kinetic energy is defined as $\frac{1}{2} \left( u^2 + v^2 + w^2 \right)$. If we apply Reynolds decomposition to this and take the mean we find that we can split the kinetic energy into the mean kinetic energy $\frac{1}{2} \left( \ubar^2 + \vbar^2 + \wbar^2 \right)$ and the **turbulence kinetic energy (TKE)** $e$

$$
e \equiv \frac{1}{2} \left( \uvar + \vvar + \wvar \right)
$$

The TKE $e$ can be interpreted as the mean variations induced by turbulence.
The evolution of the TKE is essential to understand in the understanding of atmospheric boundary layer turbulence. So our ultimate goals is a conservation equation for $\overline{e}$.
The starting point is the conservation equation for $\uiprime$, which we can acquire from subtracting the mean conservation of momentum equation from the full equation

$$
  \pd{\uibar}{t}
+ \pd{\uiprime}{t}
+ \pd{\uibar\ujbar}{x_j}
+ \pd{\uiprime \ujbar}{x_j}
+ \pd{\uibar \ujprime}{x_j}
+ \pd{\uiprime \ujprime}{x_j}
&=
- \dfrac{1}{\rhobar} \pd{p^\prime}{x_i}
+ f \epsilon_{ij3} \left( \ujbar + \ujprime - u_{g,j} \right)
+ \delta_{i3} \dfrac{\theta_\mathrm{v}^\prime}{\overline{\theta}_\mathrm{v}} g
+ \nu \pdd{\uibar}{x_j}
+ \nu \pdd{\uiprime}{x_j}
\\
  \pd{\uibar}{t}
+ \pd{\uibar \ujbar}{x_j}
+ \pd{\overline{ \uiprime \ujprime }}{x_j}
&=
  f \epsilon_{ij3} \left( \ujbar - u_{g,j} \right)
+ \nu \pdd{\uibar}{x_j}
$$

Subtraction gives

$$
  \pd{\uiprime}{t}
+ \pd{\uiprime \ujbar}{x_j}
+ \pd{\uibar \ujprime}{x_j}
+ \pd{\uiprime \ujprime}{x_j}
- \pd{\overline{ \uiprime \ujprime }}{x_j}
=
- \dfrac{1}{\rhobar} \pd{p^\prime}{x_i}
- f \epsilon_{ij3} \ujprime
+ \delta_{i3} \dfrac{\theta_\mathrm{v}^\prime}{\overline{\theta}_\mathrm{v}} g
+ \nu \pdd{\uiprime}{x_j}
$$

Multiplication with $\uiprime$ gives

$$
  2 \uiprime \pd{\uiprime}{t}
+ 2 \uiprime \pd{\uiprime \ujbar}{x_j}
+ 2 \uiprime \pd{\uibar \ujprime}{x_j}
+ 2 \uiprime \pd{\uiprime \ujprime}{x_j}
- 2 \uiprime \pd{\overline{ \uiprime \ujprime }}{x_j}
=
- 2 \uiprime \dfrac{1}{\rhobar} \pd{p^\prime}{x_i}
- 2 \uiprime f \epsilon_{ij3} \ujprime
+ 2 \uiprime \delta_{i3} \dfrac{\theta_\mathrm{v}^\prime}{\overline{\theta}_\mathrm{v}} g
+ 2 \uiprime \nu \pdd{\uiprime}{x_j}
$$

$$
  \pd{\uiprimesq}{t}
+ \pd{\uiprimesq \ujbar}{x_j}
+ 2 \uiprime \pd{\uibar \ujprime}{x_j}
+ \pd{\uiprimesq \ujprime}{x_j}
- 2 \uiprime \pd{\overline{ \uiprime \ujprime }}{x_j}
=
- \dfrac{2}{\rhobar} \pd{\uiprime p^\prime}{x_i}
+ p^\prime \dfrac{2}{\rhobar} \pd{\uiprime}{x_i}
- 2 f \epsilon_{ij3} \uiprime \ujprime
+ 2 \delta_{i3} \dfrac{\uiprime \theta_\mathrm{v}^\prime}{\overline{\theta}_\mathrm{v}} g
+ 2 \uiprime \nu \pdd{\uiprime}{x_j}
$$

