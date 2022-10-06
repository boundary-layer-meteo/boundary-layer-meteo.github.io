$\def\cp{c_\textrm{p}}$
$\def\Rd{R_\textrm{d}}$

# Temperature and stability

```{admonition} Questions to be answered in this chapter
1. What is potential temperature and why do we use it?
2. What is the importance of atmospheric stability?
3. What is the dry adiabatic lapse rate?
```

## The ideal gas law
We assume that the air in the atmospheric boundary layer behaves as an ideal gas, in which pressure $p$, density $\rho$ and the gas constant for dry air $\Rd$ are related as:

```{admonition} Ideal gas law
$$
p = \rho \Rd T.
$$ (ideal_gas_law)
```


## Conservation of energy
### The first law of thermodynamics
As a starting point for conservation of energy, we start with the first law of thermodynamics written in a convenient form to describe atmospheric flow:

```{admonition} Conservation of energy
$$
\rho \cp \mathrm{d}T - \mathrm{d}p = Q
$$ (first_law)
```

This equation relates the change in temperature $\mathrm{d}T$ of a parcel of air to its pressure change $\mathrm{d}p$ and the heat $Q$ added to the parcel. We can now describe for any parcel of air how its temperature will change under expansion and compression if it is displaced in the vertical direction by atmospheric motions, or how temperature will change if we add or remove heat, for instance by heating by solar radiation or cooling by thermal radiation.

```{admonition} Question
:class: seealso
Assume no heat is added ($Q = 0$) and use Equation {eq}`first_law` to answer the question. If we move a parcel of air up a mountain, does its temperature increase or decrease?
```

```{admonition} Answer
:class: important, dropdown
If $Q$ equals zero, then $\rho \cp \mathrm{d}T = \mathrm{d}p$. Therefore, if we move up a mountain and pressure decreases ($dp < 0$), temperature change $dT$ must be smaller than 0 as well. Temperature thus decreases.
```

### Potential temperature
One of the disadvantages of temperature is that it is influenced by expansion and compression, as well as heat transfer. This means that an air parcel that is vertically displaced by turbulence experiences a temperature change even if no heat is added or removed. In the analysis of turbulent boundary layer flows it is convenient to have a quantity that is conserved under adiabatic dispacement. Before deriving this quantity, we rewrite Equation {eq}`first_law` in units of temperature, and we remove the density from the pressure term with the help of the ideal gas law (Equation {eq}`ideal_gas_law`).

$$
\cp \mathrm{d}T - \dfrac{1}{\rho} \mathrm{d}p &= \dfrac{Q}{\rho} \\
\cp \mathrm{d}T - \dfrac{\Rd T}{p} \mathrm{d}p &= \dfrac{Q}{\rho} \\
\dfrac{1}{T} \mathrm{d}T - \dfrac{\Rd}{\cp}\dfrac{1}{p} \mathrm{d}p &= \frac{Q}{\rho \cp T} \\
\mathrm{d} \left( \ln T \right) - \dfrac{\Rd}{\cp} \mathrm{d}\left( \ln p \right) &= \frac{Q}{\rho \cp T}
$$

Now we can introduce our new quantity potential temperature $\theta$ as follows.

$$
\mathrm{d} \left( \ln T \right) - \dfrac{\Rd}{\cp} \mathrm{d}\left( \ln p \right) = \mathrm{d} \left( \ln \theta \right).
$$

If we look carefully to the equation, we have chosen potential temperature $\theta$ such that it compensates for changes in pressure $p$ caused by displacement, which is what we intended. We can now work towards a definition of potential temperature $\theta$, where we integrate from some chosen reference pressure $p_0$ to the actual pressure $p$ at which we need to know the potential temperature.

$$
\int_{p_0}^p \mathrm{d} \left( \ln T \right) - \dfrac{\Rd}{\cp} \int_{p_0}^p \mathrm{d}\left( \ln p^\prime \right) &= \int_{p_0}^p \mathrm{d} \left( \ln \theta \right) \\

\left[ \ln T \right]_{p_{0}}^p - \dfrac{\Rd}{\cp} \left[ \ln p \right]_{p_{0}}^p &= \left[ \ln \theta \right]_{p_{0}}^p \\
\ln T - \ln T_0  - \dfrac{\Rd}{\cp} \ln p + \dfrac{\Rd}{\cp} \ln p_0 &= \ln \theta - \ln \theta_0
$$

To be able to provide an actual value of $\theta$ we define $\theta$ to be equal to $T$ at pressure $p_0$, thus mathematically $\theta_0 = T_0$. With this choice we can cancel two terms in the equation:

$$
\ln T - \ln T_0  - \dfrac{\Rd}{\cp} \ln p + \dfrac{\Rd}{\cp} \ln p_0 &= \ln \theta - \ln \theta_0 \\
\ln T - \dfrac{\Rd}{\cp} \ln p + \dfrac{\Rd}{\cp} \ln p_0 &= \ln \theta \\
\ln T - \ln \left( \dfrac{p}{p_0}\right)^\frac{\Rd}{\cp} &= \ln \theta \\
\ln T + \ln \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp} &= \ln \theta \\
\ln \left( T \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp} \right) &= \ln \theta
$$

This brings us to the definition of the potential temperature:

```{admonition} Potential temperature
$$
\theta \equiv T \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp}
$$ (pot_temp)
```

The last question to answer is what to chose for the value of $p_0$. Generally, we use the $1 \cdot 10^5~\mathrm{Pa}$ as its value, which means that at sea level pressure the absolute temperature $T$ and potential temperaure $\theta$ are very close together. Following this logics, an intuitive way of defining potential temperature is:

> _Potential temperature $\theta$ is the temperature of an air parcel if it is adiabatically (thus no heat added or removed) transported back to sea level._

### Atmospheric stability
The atmospheric static stability defines whether the temperature stratification support or suppresses the generation of turbulent motions. If $\dfrac{\partial \theta}{\partial z} \gt 0$, the atmosphere is statically stable, if $\dfrac{\partial \theta}{\partial z} \approx 0$, the atmosphere is neutral, and if $\dfrac{\partial \theta}{\partial z} \lt 0$ the atmosphere is unstable.

If a layer of air is vertically well-mixed, then the stratification is neutral and the actual temperature $T$ follows the **dry adiabatic lapse rate**. This is for instance the case in the daytime convective boundary layer, in which surface driven plumes constantly mix the layer vertically through.


```{admonition} Question
:class: seealso
What is the value of the dry adiabatic lapse rate?
```

```{admonition} Answer
:class: important, dropdown
The dry adiabatic lapse rate is found under neutral conditions. First, we substitute the potential temperature $\theta$ by its definition Eq. X, and apply the product role to split the derivative into two terms.

$$
\dfrac{\partial \theta}{\partial z} &= 0 \\
\dfrac{\partial}{\partial z} \left( T \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp} \right) &= 0 \\
\dfrac{\partial T}{\partial z} \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp} + T \dfrac{\partial}{\partial z} \left( \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp} \right) &= 0
$$


First, we work out the second term. We replace the partial derivative by hydrostatic balance, and subsequently use the ideal gas law to simplify the equation:

$$
T \dfrac{\partial}{\partial z} \left( \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp} \right)
&= T \dfrac{\Rd}{\cp} \left( \dfrac{\partial}{\partial z}\left( \dfrac{p_0}{p} \right) \right) ^{\frac{\Rd}{\cp} - 1} \\
&= T \dfrac{\Rd}{\cp} \left( \dfrac{p_0}{p} \right)^{\frac{\Rd}{\cp} - 1} \cdot \dfrac{\partial}{\partial z}\left( \dfrac{p_0}{p} \right) \\
&= T \dfrac{\Rd}{\cp} \left( \dfrac{p_0}{p} \right)^{\frac{\Rd}{\cp}} \left( \dfrac{p}{p_0} \right) \cdot - \left( \dfrac{p_0}{p^2} \right) \dfrac{\partial p}{\partial z} \\
&= T \dfrac{\Rd}{\cp} \left( \dfrac{p_0}{p} \right)^{\frac{\Rd}{\cp}} \cdot - \left( \dfrac{1}{p} \right) \dfrac{\partial p}{\partial z} \\
&= \left( \dfrac{p_0}{p} \right)^{\frac{\Rd}{\cp}} \cdot - \left( \dfrac{\Rd T}{p \cp} \right) \dfrac{\partial p}{\partial z} \\
&= \left( \dfrac{p_0}{p} \right)^{\frac{\Rd}{\cp}} \cdot \left( \dfrac{\rho \Rd T g}{p \cp} \right) \\
&= \left( \dfrac{p_0}{p} \right)^{\frac{\Rd}{\cp}} \cdot \left( \dfrac{g}{\cp} \right) 
$$

Substitution back into the original term and moving the second term to the right hand side gives

$$
\dfrac{\partial T}{\partial z} \left( \dfrac{p_0}{p}\right)^\frac{\Rd}{\cp} &= - \left( \dfrac{p_0}{p} \right)^{\frac{\Rd}{\cp}} \left( \dfrac{g}{\cp} \right) \\
\dfrac{\partial T}{\partial z} &= - \dfrac{g}{\cp}
$$

The drop of temperature with height is thus approximately $1\ \mathrm{K}$ per $100\ \mathrm{m}$.
```
