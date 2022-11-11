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
$$

## The ideal gas law for a moist atmosphere

$$
p &= p_\mathrm{d} + p_\mathrm{v} \\
p &= \rho_\mathrm{d} \Rd T + \rho_\mathrm{v} \Rv T \\
p &= \left( 1 - q \right) \rho \Rd T + q \rho \Rv T \\
p &= \rho \Rd T \left( 1 + q \left( \dfrac{\Rv}{\Rd} - 1 \right) \right)
$$

We can now define the virtual temperature $\Tv$ as

```{admonition} Virtual temperature
$$
\Tv \equiv T \left( 1 + q \left( \dfrac{\Rv}{\Rd} - 1 \right) \right)
$$ (virtual_temp)
```

In an intuitive definition, the virtual temperature is temperature that an equivalent dry parcel would need to have in order to have the same density as a moist parcel. The fact that the virtual temperature is larger than the absolute temperature for a moist atmosphere is related to the low weight of water molecules compared to those in a dry atmosphere (primarily $O_2$ and $N_2$).

