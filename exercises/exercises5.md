# Exercises chapter 5
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$

##
Assuming that the potential temperature increases with height,
find the potential temperature at the top of a turbulent layer which becomes laminar at a height of 20 m. The wind profile is given by:

$$
\overline{u}(z) &= \frac{u_*}{k}ln\left (\frac {z}{z_o}\right)\\
\overline{v}(z) &= 4
$$

The friction velocity is 0.45 m s$^{-1}$ and the potential temperature at the height of the roughness lenght z$_o$ is 295 K.
($\kappa$ = 0.4, g = 9.8 m $\rm{s^{-2}}$, z$_o$ = 1 m)

```{admonition} Answer
:class: important, dropdown

At the height of 20 meters the flow becomes laminar, meaning:

$$
Ri_g (z=20 \ m.)=\frac{\frac{g}{\theta_0}\frac{\partial \overline{\theta}}{\partial z}}{\left(\frac{\partial u}{\partial z}\right) ^2 +\left(\frac{\partial v}{\partial z}\right) ^2} =0.25\equiv Ri_g^{crit}
$$

Rearranging the equation above:

$$
\frac{\partial \overline{\theta}}{\partial z}= Ri_g^{crit} \frac{\theta_0}{g} \left[\left(\frac{\partial u}{\partial z}\right) ^2 +\left(\frac{\partial v}{\partial z}\right) ^2 \right]
$$(ex5.1eq1)

We now calculate $\frac{\partial u}{\partial z}$ and $\frac{\partial v}{\partial z}$:

$$
\frac{\partial u}{\partial z} &= \frac{u_*}{\kappa}\frac{\partial (ln \frac{z}{z_0})}{\partial z}  = \frac{u_*}{\kappa}\frac{1}{z}\\
\frac{\partial v}{\partial z} &= 0
$$

Introducing this in Eq. {eq}`ex5.1eq1` we obtain:

$$
\frac{\partial \overline{\theta}}{\partial z}= Ri_g^{crit} \frac{\theta_0}{g} \frac{u_*^2}{\kappa^2}\frac{1}{z^2}
$$

We now rearrange and integrate on both sides:

$$
\int_{\theta(z_0)}^{\theta(z)}\partial \overline{\theta}=\int_{z=z_0}^{z}Ri_g^{crit} \frac{\theta_0}{g} \frac{u_*^2}{\kappa^2}\frac{1}{z^2}\partial z
$$

Integrating first and then rearranging the terms yields:

$$
\overline{\theta}(z)=\overline{\theta}(z_0) + Ri_g^{crit} \frac{\theta_0}{g} \frac{u_*^2}{\kappa^2} \left( \frac{1}{z_0}-\frac{1}{z}\right)
$$

Substituting 
$u_*=0.45$, 
$\theta_0=295  \ \rm K$, 
$\overline{\theta}(z_0)=295 \  \rm K$, 
$\kappa=0.4$, 
$g=9.8\ \rm{m\ s^{-2}}$, 
$z_0=1 \ \rm m$, 
$z=20 \ \rm m$,
and $Ri_g^{crit}=0.25$ we obtain

$$
\overline{\theta}(z=20 m)= 304.05   \ \rm K
$$

```

##
Given the following vertical profile of wind:

| z (m)         | 1     | 4 | 10    | 20    | 50    | 100   | 300   | 500   | 1000  | 2000  | 
| --            |--     |-- | --    | --    | --    | --    | --    | --    | --    | --    |  
| U (m s$^{-1}$)| 3.7   |5.0|5.8    |6.5    |7.4    |8.0    |9.0    |9.5    |10.0   |10.0   |

assuming that the potential temperature increases with height at
the constant rate of $6\ \rm{K\ km^{-1}}$,

a) Calculate the bulk Richardson number for each layer (assume $g/\theta_v=0.0333 \rm{m\ s^{-2}\ K^{-1}}$)
```{admonition} Answer
:class: important, dropdown

```

b) Indicate the static and dynamic stability of each layer
```{admonition} Answer
:class: important, dropdown

```

c) Indicate which layer is expected to be turbulent in these
condition.
```{admonition} Answer
:class: important, dropdown

```

##
The frequency of vertical oscillations for an atmospheric flow is given by
the Brunt-Väisälä frequency

$$
N^2=\left(\frac{g}{\overline{\theta_v}}\right)~\pafg{\overline{\theta_v}}{z}~~~(s^{-2})
$$

a) Find an expression of the velocity gradient as a function of
the Richardson Number and the Brunt-Väisälä frequency. Assume that $\overline{v}(z)=0$.
```{admonition} Answer
:class: important, dropdown

```

b) Find the velocity at z=30 m for $N=0.05~s^{-1}$ and Ri=0.2. The surface velocity is 0.
```{admonition} Answer
:class: important, dropdown

```


##
From steady state and in case one can neglects the turbulent transport and advection terms,
the TKE equation reduces under horizontally homogeneous conditions to

$$
0~=-\overline{u'w'}\pafg{\overline{u}}{z}+
\left(\frac{g}{\overline{\theta_v}}\right)\overline{w'\theta_v'}-\epsilon
$$

By using the following dimensionless parameters one can derive a dimensionless
equation for the TKE equation

$$
\Phi_M~=~\frac{\kappa z}{u_*}\pafg{\overline{u}}{z}~~~~~~~~
\Phi_\epsilon~=~\frac{\kappa z}{u_*^3}\epsilon
$$

a) Find the non-dimensional equation for TKE at the surface layer in terms of $\Phi_M$, $\Phi_\epsilon$
and $z/L$. 

```{hint}
:class: tip, dropdown
multiply the dimension TKE equation by the factor $\kappa~z/u_*^3$ and make use of $u_*^2=-\overline{u'w'}$
```
```{admonition} Answer
:class: important, dropdown

```

b) Discuss what occur under neutral stratifying conditions.
```{admonition} Answer
:class: important, dropdown

```

##
Using the previous definition of $\Phi_M$ and the following temperature scaling parameters

$$
\theta_*~=~-~\frac{\overline{w'\theta'}}{u_*}~~~~~~\Phi_H~=~\frac{\kappa z}{\theta_*}\pafg{\overline{\theta}}{z}
$$

a) and assuming that $\overline{V(z)}=0$, find a relation between the gradient Richardson number and $z/L$, $\Phi_M$ and $\Phi_H$.
```{admonition} Answer
:class: important, dropdown

```

b) Under very stable conditions $\Phi_M~=~ \alpha_M\frac{z}{L}$ and $\Phi_H~=~ \alpha_H\frac{z}{L}$ where ($\alpha_M=\alpha_H \approx 5$).
Discuss the value of the Richardson number under this condition.
```{admonition} Answer
:class: important, dropdown

```


##
The flux-gradient relationships for momentum and heat ($\Phi_M$ and $\Phi_H$)
are related to the exchange coefficients ($K_M$ and $K_H$).

a) Using the first-order closure assumption to parameterize the
fluxes and surface layer similarity, find the relationship between
$\Phi_M$,  $\Phi_H$ and $K_M$, $K_H$.
```{admonition} Answer
:class: important, dropdown

```

b)  The moisture flux can be written as

$$
\overline{w'q'}~=~-K_q \pafg{\overline{q}}{z}
$$

Knowing that
$\Phi_Q~=~\frac{\kappa z}{q_*} \pafg{\overline{q}}{z}$,
find a relation between the exchange coefficient and
the flux-gradient relationship for moisture.
```{admonition} Answer
:class: important, dropdown

```

c) For an unstable surface layer, the flux-gradient relationship for $q$ is

$$
\Phi_Q~=~\left (1-16\frac{z}{L}\right)^{-\frac{1}{2}}
$$

Calculate the exchange coefficient at z=300 cm and for a Monin-Obukhov length scale
equal to -2 m. Calculate the exchange coefficient at the same height but now under neutral
conditions. Discuss the results in terms of mixing-length theory.

($u_*=0.3~m/s,\kappa=0.4$)
```{admonition} Answer
:class: important, dropdown

```

##
In a fertilized field a constant flux of nitric oxide ($NO$) has been measured
($\overline{w'NO'}=0.1~ppb~m/s$) with a concentration of NO at ground level equal to 5 ppb.
Additional measurements showed that $(z/L) \approx 0$ and the friction velocity was 0.3 m/s.
($z_o=10~cm$) 

a) Find the concentration of NO at 10 m. Plot the profile of NO(z).
```{admonition} Answer
:class: important, dropdown

```

b) At which height the NO concentration is lower than $70\%$ with respect the ground value.
```{admonition} Answer
:class: important, dropdown

```

##
Assuming that the radiative divergence and the phase changes are neglectable, the equation
for temperature reads

$$
\pafg{\theta}{t}+{u_j}\pafg{\theta}{x_j}~=~\nu_{\theta}\pafg{^2\theta}{x_j^2}
$$

a) Derive from this equation the governing equation of the temperature fluctuations $\overline{\theta'^{~2}}$.
```{admonition} Answer
:class: important, dropdown

```

b) From the general expression, write the simplify equation if one assumes: steady-state, no advection, horizontal
homogeneity and the turbulent transport of $\overline{\theta'^{~2}}$ is neglectable.
```{admonition} Answer
:class: important, dropdown

```

c) By using the similarity theory scaling functions

$$
\Phi_H~=~\frac{\kappa z}{\theta_*} \pafg{\overline{\theta}}{z}~~~~~~~~
\Phi_{\epsilon\theta}~=~\frac{\kappa z}{u_*\theta_*^2} \epsilon_{\theta},
$$

find the dimensionless equation for $\overline{\theta'^{~2}}$. Discuss the result. What is the
value of $\Phi_{\epsilon\theta}$ under neutral conditions?

```{admonition} Answer
:class: important, dropdown

```
