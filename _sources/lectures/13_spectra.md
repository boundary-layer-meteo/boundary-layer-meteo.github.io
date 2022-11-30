# Turbulence spectra

```{admonition} Questions to be answered in this chapter
1. What is an energy spectra and how it is derived?
1. How does a turbulence kinetic energy spectra look?
2. What is the explanation for the famous $-5/3$ slope of the turbulence kinetic energy spectra?
```

## Fourier transform and energy spectrum
Fourier transforming data allows us to transform data from physical to spectral space. Fourier transformation goes as following

$$
\hat{f}(k) = -\int_\infty^\infty f(x) \exp \left( - i 2 \pi k x \right)\,\mathrm{d} x
$$

although since we generally work with time series of spatial series with equal sampling interval we use the discrete Fourier transform

$$
\hat{f}(k) = \sum_{n = 0}^{N - 1} f(x) \exp \left(-i 2 \pi k \frac{n}{N} \right)\ \ \ \ k = 0, \dots, N-1
$$

By doing so, we can write a time or spatial series as a sum of waves with varying phase and amplitude.

```{figure} figs/spectra_waves.png
---
width: 500px
name: spectra_waves
---
Potential temperature near the surface of the convective boundary layer captures in waves.
```

Based on the waves we can calculate its contribution to the variance by taking the square of its absolute value.

$$
E \left( k \right) = \left| \hat{f} \right|^2 =  \mathrm{Re} \left( \hat{f} \right)^2 + \mathrm{Im} \left( \hat{f} \right)^2
$$


## The spectral structure of the inertial subrange of turbulence
The turbulence kinetic energy $e$ can be constructed from its spectral energy $E(k)$ (energy per wave number $k$) following

$$
e = \int_0^\infty E\,\mathrm{d}k.
$$

```{figure} figs/spectra_energy.png
---
width: 600px
name: spectra_energy
---
Spectral energy of the potential temperature near the surface of the convective boundary layer.
```

If we assume a strict separation between production and dissipation in terms of length and time scales, there must exist a region that only transfers energy from the largest to the smallest scales.
We call this region the **inertial subrange**, and the only parameter relevant there is $\epsilon$.
Note that viscosity $\nu$ does not play a role here yet.

Following the same dimensional reasoning as before, and noting that only $\epsilon$ matters, the spectral energy $E$ must be related to wave number $k$ and dissipiation $\epsilon$ as

```{admonition} Kolmogorov scaling of the intertial subrange
$$
E \sim \epsilon^\frac{2}{3} \kappa^{-\frac{5}{3}}.
$$
```

The result that the spectral energy $E$ for a certain wave number is proportional to wave number $k$ to the power $-5/3$ is one of the most fundamental properties of high-Reynolds number turbulent flows.
