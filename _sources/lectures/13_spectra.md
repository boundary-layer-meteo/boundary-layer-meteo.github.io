# Turbulence spectra

```{admonition} Questions to be answered in this chapter
1. What is an energy spectra and how it is derived?
1. How does a turbulence kinetic energy spectra look?
2. What is the explanation for the famous $-5/3$ slope of the turbulence kinetic energy spectra?
```

## Fourier transform and energy spectrum
Fourier transforming data allows us to transform data from physical to spectral space. Fourier transformation goes as following

$$
\hat{f}(k) = \int_{-\infty}^\infty f(x) \exp \left( - i 2 \pi k x \right)\,\mathrm{d} x
$$

although since we generally work with time series or spatial series with equal sampling interval we use the discrete Fourier transform

$$
\hat{f}(k) = \sum_{n = 0}^{N - 1} f(x) \exp \left(-i 2 \pi k \frac{n}{N} \right)\ \ \ \ k = 0, \dots, N-1
$$

By doing so, we can write a time or spatial series as a sum of waves with varying phase and amplitude. This Equation describes a signal of any variable (e.g., velocity, temperature, humidity) and an example for the potential temperature is given below. The red line in the second plot shows the signal described by 5 waves: that are the waves with wavenumbers 0, 1, 2, 3 and 4; the red line in the third plot shows the result of 10 waves, which have wavenumbers 0 to 9; and so on. The wavelength ($\lambda$ [m]) is related to the wavenumber via: $k = \frac{2\pi}{\lambda}$. $k$ is the angular wave number and $\nu$ the linear, with $k = 2 \pi \nu$. This will become more clear in exercise 21.1. These spatial quantities can be converted to temporal quantities using Taylor's hypothesis of frozen turbulence: $U = \lambda f$, with $U$ the velocity [m/s] and $f$ the frequency [1/s].

```{figure} figs/spectra_waves.png
---
width: 500px
name: spectra_waves
---
Potential temperature near the surface of the convective boundary layer captures in waves.
```

Based on the waves we can calculate the contribution of each wave to the variance by taking the square of its absolute value. 

$$
E \left( k \right) = \left| \hat{f} \right|^2 =  \mathrm{Re} \left( \hat{f} \right)^2 + \mathrm{Im} \left( \hat{f} \right)^2
$$

This spectral energy ($E(k)$) is shown in the second Figure of Fig. 13.2. It shows that most variance arises from small k, i.e. big waves.

## The spectral structure of the inertial subrange of turbulence
The turbulence kinetic energy $e$ can be constructed from the spectral energy $E(k)$ (energy per wave number $k$) of the velocity fluctuations following

$$
e = \int_0^\infty E\,\mathrm{d}k.
$$

```{figure} figs/spectra_energy.png
---
width: 500px
name: spectra_energy
---
Spectral energy of the potential temperature near the surface of the convective boundary layer. Note: the y-axis is confusing and the units are wrong. The y-axis above should be k E(k) [$m^2/s^2$] and below E(k) [$m^3/s^2$].
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

Above, the spectral energy is plotted. That is the red line in Figure 13.1. The spectral function can also be calculated for other properties, such as the vertical velocity. As plotted below. $S_\chi(f)$ is the density of the $\chi$ spectrum, in this case $\chi = w$. The integral gives the variance of $\chi$, in this case: $\int S_w df = \sigma^2_w = \overline{w'^2}$. However, the x-labels is logaritmic and $\int S_w d(ln(f)) = \int \frac{1}{f} S_w df$. Therefore the y-axis is multiplied by f to get $\int f S_w d(ln(f)) = \int S_w df = \sigma^2_w$, such that the area under the curve is equal to the variance of w.

```{figure} ../exercises/figures/exercise4_1_1.png
:name: fig411
Spectrum of the wind velocity as a function of time.
```
