# Conservation of energy (ii)

```{admonition} Questions to be answered in this lecture
1. What is the gas law for an atmosphere with water vapor?
1. What is virtual temperature and why do we use it?
1. What is the gas law under the assumption of small perturbations?
1. What is buoyancy?
```

$$
\def\cp{c_{\mathrm{p}}}
\def\Rd{R_{\mathrm{d}}}
\def\Rv{R_{\mathrm{v}}}
\def\Tv{T_{\mathrm{v}}}
\def\pbar{\overline{p}}
\def\pprime{p^\prime}
\def\rhobar{\overline{\rho}}
\def\rhoprime{\rho^\prime}
\def\Tvbar{\overline{\Tv}}
\def\Tvprime{\Tv^\prime}
\def\pd#1#2{\dfrac{\partial #1}{\partial #2}}
\def\pdd#1#2{\dfrac{\partial^2 #1}{\partial#2^2}}
\def\uibar{\overline{u}_i}
\def\ujbar{\overline{u}_j}
\def\uiprime{u_i^\prime}
\def\ujprime{u_j^\prime}
\def\ubar{\overline{u}}
\def\vbar{\overline{v}}
\def\wbar{\overline{w}}
$$

## The ideal gas law for a moist atmosphere

The pressure $p$ of the atmosphere can be decomposed into the partial pressure of dry air $p_\mathrm{d}$ and that of vapor $p_\mathrm{v}$. With the help of the gas law, and the specific humidity $q$, we can work this towards a notation that introduces virtual temperature

$$
p &= p_\mathrm{d} + p_\mathrm{v} \\
p &= \rho_\mathrm{d} \Rd T + \rho_\mathrm{v} \Rv T \\
p &= \left( 1 - q \right) \rho \Rd T + q \rho \Rv T \\
p &= \rho \Rd T \left( 1 + q \left( \dfrac{\Rv}{\Rd} - 1 \right) \right)
$$

We can now define the virtual temperature $\Tv$ as

```{admonition} Virtual temperature
$$
\Tv &\equiv T \left( 1 + q \left( \dfrac{\Rv}{\Rd} - 1 \right) \right) \\
    &\approx T \left( 1 + 0.61 q \right)
$$ (virtual_temp)
```

and the gas law becomes $p = \rho \Rd \Tv$

In an intuitive definition, the virtual temperature is temperature that an equivalent dry parcel would need to have in order to have the same density as a moist parcel. The fact that the virtual temperature is larger than the absolute temperature for a moist atmosphere is related to the low weight of water molecules compared to those in a dry atmosphere (primarily $O_2$ and $N_2$).

Similar as the virtual temperature, we can also define the virtual potential temperature

$$
\theta_\mathrm{v} \equiv \theta \left( 1 + q \left( \dfrac{\Rv}{\Rd} - 1 \right) \right)
$$

We can assume that in an atmospheric boundary layer $\rhoprime \ll \rhobar$, $\pprime \ll \pbar$, and $\Tvprime \ll \Tvbar$. Hence we can rewrite the gas law.

$$
\pbar + \pprime = \left( \rhobar + \rhoprime \right) \Rd \left( \Tvbar + \Tvprime \right) \\
\pbar + \pprime = \rhobar \Rd \Tvbar + \rhobar \Rd \Tvprime + \rhoprime \Rd \Tvbar + \rhoprime \Rd \Tvprime
$$

Given that all perturbations are small, the mean gas law is $\pbar = \rhobar \Rd \Tvbar$, and we can neglect all terms that have multiplications of perturbations. This gives:

$$
\pprime = \rhobar \Rd \Tvprime + \rhoprime \Rd \Tvbar
$$

If we then divide the equation by $\pbar$ and substitute the gas law for mean quantities we get the gas law for small perturbations

$$
\dfrac{\pprime}{\pbar} = \dfrac{\Tvprime}{\Tvbar} + \dfrac{\rhoprime}{\rhobar}
$$

In the atmospheric boundary layer, we can compare the typical magnitude of pressure perturbations to those of density and virtual temperature and find that those of pressure are (at least) two orders of magnitude smaller. Hence, the gas law that we use in the atmospheric boundary under the Boussinesq approximation simplifies to

```{admonition} Ideal gas law under Boussinesq approximation
$$
\dfrac{\rhoprime}{\rhobar} = - \dfrac{\Tvprime}{\Tvbar}
$$ (gas_law)
```

We can also assume that $\dfrac{\Tvprime}{\Tvbar} \approx \dfrac{\theta_\mathrm{v}^\prime}{\overline{\theta}_\mathrm{v}}$.
This we can substitute into the momentum equation and redefine the buoyancy term and get

$$
\pd{u_i}{t} + \pd{u_i u_j}{x_j} = - \dfrac{1}{\rhobar} \pd{p^\prime}{x_i} + f \epsilon_{ij3} \left( u_j - u_{g,j} \right) + \delta_{i3} \dfrac{\theta_\mathrm{v}^\prime}{\overline{\theta}_\mathrm{v}} g + \nu \pdd{u_i}{x_j}
$$

In a moist atmosphere, we will now also define stability based on vertical gradient of the virtual potential temperature $\theta_\mathrm{v}$, rather than the potential temperature $\theta$ that does not take into account the effects of moisture.
