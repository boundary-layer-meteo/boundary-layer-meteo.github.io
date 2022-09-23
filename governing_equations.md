# The governing equations

## Conservation of energy
### The first law of thermodynamics
The first law of thermodynamics {eq}`first_law`.

$$
c_p \mathrm{d}T - \dfrac{1}{\rho} \mathrm{d}p = J \\
c_p \mathrm{d}T - \dfrac{R_d T}{p} \mathrm{d}p = J \\
\dfrac{1}{T} \mathrm{d}T - \dfrac{R_d}{c_p}\dfrac{1}{p} \mathrm{d}p = \frac{J}{c_p T} \\
\mathrm{d} \left( \ln T \right) - \dfrac{R_d}{c_p} \mathrm{d}\left( \ln p \right) = \frac{J}{c_p T}
$$ (first_law)

### Potential temperature
One of the disadvantages of temperature is that it is influenced by expansion and compression, as well as heat transfer. This means that an air parcel that is vertically displaced by turbulence experiences a temperature change even if no heat is added or removed. In the analysis of turbulent boundary layer flows it is convenient to have a quantity that is conserved under adiabatic dispacement. Therefore, we introduce potential temperature $\theta$ as follows:

$$
\mathrm{d} \left( \ln T \right) - \dfrac{R_d}{c_p} \mathrm{d}\left( \ln p \right) = \mathrm{d} \left( \ln \theta \right).
$$

If we look carefully to the equation, we see that potential temperature compensates for changes in pressure $p$ caused by reversible work in the form of expansion and compression.

$$
\int_{p_0}^p \mathrm{d} \left( \ln T \right) - \dfrac{R_d}{c_p} \int_{p_0}^p \mathrm{d}\left( \ln p^\prime \right) &= \int_{p_0}^p \mathrm{d} \left( \ln \theta \right) \\

\left[ \ln T \right]_{p_{0}}^p - \dfrac{R_d}{c_p} \left[ \ln p \right]_{p_{0}}^p &= \left[ \ln \theta \right]_{p_{0}}^p \\
\ln T - \ln T_0  - \dfrac{R_d}{c_p} \ln p + \dfrac{R_d}{c_p} \ln p_0 &= \ln \theta - \ln \theta_0
$$

To be able to provide an actual value of $\theta$ we define $\theta$ as equal to $T$ at a chosen pressure $p_0$.

$$
\ln T - \ln T_0  - \dfrac{R_d}{c_p} \ln p + \dfrac{R_d}{c_p} \ln p_0 &= \ln \theta - \ln \theta_0 \\
\ln T - \dfrac{R_d}{c_p} \ln p + \dfrac{R_d}{c_p} \ln p_0 &= \ln \theta \\
\ln T - \ln \left( \dfrac{p}{p_0}\right)^\frac{R_d}{c_p} &= \ln \theta \\
\ln T + \ln \left( \dfrac{p_0}{p}\right)^\frac{R_d}{c_p} &= \ln \theta \\
\ln \left( T \left( \dfrac{p_0}{p}\right)^\frac{R_d}{c_p} \right) &= \ln \theta
$$

This brings us to the definition of the potential temperature:

$$
\theta \equiv T \left( \dfrac{p_0}{p}\right)^\frac{R_d}{c_p}
$$ (pot_temp)

