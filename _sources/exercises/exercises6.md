# Exercises chapter 6
$\def\pafg#1#2{\dfrac{\partial #1}{\partial #2}}$
$\def\afg#1#2{\dfrac{{\rm d} #1}{{\rm d} #2}}$
$\def\gemafg#1#2{\pafg{\overline{#1}}{#2}}$

##
The one-dimensional conservation equation for heat reads:

$$
\pafg{\overline{\theta}}{t}~=~-~\pafg{\overline{w'\theta'}}{z}
$$

a) Discuss which terms have been neglected from this equation

```{admonition} Answer
:class: important, dropdown

The total conservation equation for heat is

$$
\underbrace{\gemafg{\theta}{t}}_{\rm Tendency} + \underbrace{\overline{u_j}\gemafg{\theta}{x_j}}_{\rm Advection} + \underbrace{\gemafg{u_j'\theta'}{x_j}}_{Turbulent\ heat\ flux } = \underbrace{\nu_\theta\pafg{^2\overline{\theta}}{x_j^2}}_{\rm Molecular\ conduction\ \/ dissipation} - \underbrace{\frac{1}{\rho\,c_p}\gemafg{Q_j}{x_j}}_{\rm Radiation} - \underbrace{\frac{{ L_v}\,E}{\rho c_p}}_{\rm Latent\ heat\ release}
$$

The neglected terms are:
* **advection**: No advection is present. This automatically follows from using the assumption of horizontal homogeneity and the absence of subsidence.
* **horizontal turbulent heat flux**: Due to horizontal homogeneity, it is assumed that the horizontal turbulent heat flux is equal for all $x$ and $y$, causing the terms with $i$ equal to 1 or 2 to vanish.
* **dissipation**: The impact of dissipation is relatively small under daytime (convective) conditions.
* **radiation**: The impact of radiation is relatively small under these conditions as well.
* **latent heat release**: In the case of clear skies, there is no condensation/evaporation.

```

b) Explain the mathematical steps and definitions to derive the mixed-layer equation for the bulk potential temperature that reads:

$$
\pafg{ {<\overline{\theta}}>}{t}~=~\frac{\overline{w'\theta'(0)}-\overline{w'\theta'(h)}}{h}.
$$

```{admonition} Answer
:class: important, dropdown

To get to the mixed-layer equations, the conservation equation has to be integrated with height over the whole boundary layer. 
Next to that, we calculate the boundary layer averaged value of an arbitrary scalar, $\phi$, as

$$
\left<\phi\right> = \frac{1}{h} \int_{z_0}^h{\phi\,{\rm d}z}
$$

In this equation, $h$ is the boundary layer height. Integrating the 1D conservation equation for heat that was given in this exercise results in

$$
\int_{z_0}^h{\gemafg{\theta}{t}\,{\rm d}z} &= -\int_{z_0}^h{\gemafg{w'\theta'}{z}\,{\rm d}z} \\
\int_{z_0}^h{\gemafg{\theta}{t}\,{\rm d}z} &= -\left(\overline{w'\theta'}\left(h\right)-\overline{w'\theta'}\left(z_0\right)\right) 
$$(for:61main) 

Using the Leibniz integral rule:

$$
\frac{{\rm d}}{{\rm d}\alpha}\int_{a(\alpha)}^{b(\alpha)} f(x,\alpha)\,{\rm d}x = \frac{{\rm d} b(\alpha)}{{\rm d} \alpha}\,f(b(\alpha),\alpha)-\frac{{\rm d} a(\alpha)}{{\rm d} \alpha}\,f(a(\alpha),\alpha)+ \int_{a(\alpha)}^{b(\alpha)}\frac{\partial}{\partial \alpha}\,f(x,\alpha)\,{\rm d}x
$$

It can be seen that

$$
\pafg{}{t}\int_{z_0}^{h} \overline{\theta}\,{\rm d}z = \pafg{h}{t}\,\overline{\theta}\left(h^-\right)-\pafg{z_0}{t}\,\overline{\theta}\left(z_0\right)+ \int_{z_0}^{h}\pafg{\overline{\theta}}{t}\,{\rm d}z
$$

Where $h^-$ is height $h$, but approached from the boundary layer. This is of importance at interfaces. 
Actually, the integral is evaluated until an infinitesimally small distance from the boundary layer top. 
Since $\overline{\theta}\left(h^-\right)$ is equal to the potential temperature in the boundary layer, $\left<\overline{\theta}\right>$, it follows that

$$
\int_{z_0}^{h}\pafg{\overline{\theta}}{t}\,{\rm d}z &= \pafg{}{t}\int_{z_0}^{h} \overline{\theta}\,{\rm d}z - \pafg{h}{t}\left<\overline{\theta}\right>\\
 &= \pafg{}{t}\left(h\,\frac{1}{h}\int_{z_0}^{h} \overline{\theta}\,{\rm d}z\right) - \pafg{h}{t}\left<\overline{\theta}\right>\\
  &= \pafg{}{t}\left(h\left<\overline{\theta}\right>\right) - \pafg{h}{t}\left<\overline{\theta}\right>\\
  &= \pafg{h}{t}\left<\overline{\theta}\right> + h \pafg{\left<\overline{\theta}\right>}{t} - \pafg{h}{t}\left<\overline{\theta}\right>
\\ \int_{z_0}^{h}\pafg{\overline{\theta}}{t}\,{\rm d}z &= h \pafg{\left<\overline{\theta}\right>}{t} 
$$(for:61Leibniz)

Combining Equations {eq}`for:61main` and {eq}`for:61Leibniz` nets

$$
h \pafg{\left<\overline{\theta}\right>}{t} &= -\left(\overline{w'\theta'}\left(h\right)-\overline{w'\theta'}\left(z_0\right)\right) \\
\pafg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}\left(z_0\right)-\overline{w'\theta'}\left(h\right)}{h} 
$$(for:61b)

Notice that by integrating over height, we now have a variable, $\left<\overline{\theta}\right>$, that only depends on $t$.

An alternate way, without the Leibniz integral rule, to derive this equation is by making use of the energy budget in the boundary layer. 

<!--
This is shown in Appendix \ref{app:pottemp}.
-->
```

c) Assuming that we are in an encroachment situation and the sensible heat flux and h are constant on time, find an expression for $<{\overline{\theta}}>$
as a function of time. The assumption of sensible heat flux and h constant on time is reasonable in the afternoon hours
and during a relative short time. Discuss this assumption.

```{admonition} Answer
:class: important, dropdown
In case of encroachment, the vertical turbulent heat flux is 0 near the entrainment zone since there is no inversion, so 

$$
\pafg{\left<\overline{\theta}\right>}{t} = \frac{\overline{w'\theta'}\left(0\right)}{h}
$$

This expression shows that if the boundary lower growth has become minimal, the heating of the boundary layer is proportional to the surface heat flux and inversely proportional to the boundary layer height. All energy (in the form of heat) is equally distributed over the mixed layer.

Near the end of the afternoon, $h$ is approximately constant. This assumption is therefore valid. However, the sensible heat flux changes rapidly in that period. The derived equation is still valid in those situations if the heat flux is considered as a function of time.

```

d) Derive a similar expression but now assuming that the entrainment flux is 20$\%$ of the surface flux. Compare
your formulations and discuss their implications.

```{admonition} Answer
:class: important, dropdown
In this case $\overline{w'\theta'}(h) = -\beta \overline{w'\theta'}(0)$ with $\beta=0.2$ (the downward heat flux at the boundary layer top is equal to 20~\% of the upward heat flux at the surface), so Equation {eq}`for:61b` changes into

$$
\pafg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}\left(0\right)+ 0.2\,\overline{w'\theta'}\left(0\right)}{h} \\
\pafg{\left<\overline{\theta}\right>}{t} &= \frac{1.2\,\overline{w'\theta'}\left(0\right)}{h}
$$

The difference is that the influx of energy (in the form of heat) is enhanced by 20~\% due to entrainment of warm air that originates from the free troposphere. Therefore, for equal boundary layer heights, the boundary layer would heat up 1.2 times as fast for the same surface heat flux. However, note that due to entrainment the boundary layer grows faster and therefore, the heat has to be spread over a larger volume. 

```

e) Discuss the additional equations that we need to include in order to have a more physical description of the entrainment flux.

```{admonition} Answer
:class: important, dropdown
The entrainment flux has to be related to the boundary layer growth rate:

$$
\overline{w'\theta'}(h) &= - w_e \,\Delta\theta\\
 &= - \afg{h}t \,\Delta\theta
$$

In this equation $w_e$ is the entrainment velocity in m~s$^{-1}$ and $\Delta\theta$ is the potential temperature jump at the inversion. In order to evaluate this equation, the time evolution of $\Delta\theta$ has to be known. This is given by:

$$
\afg{\Delta\theta}{t} = \gamma_{\theta}\afg{h}{t}- \afg{\left<\overline{\theta}\right>}{t}
$$

($\partial$ can be replaced by d, since all variables in this equation are only dependent on time.) 

In the end, the system of governing equations is 

$$
\pafg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}\left(z_0\right)-\overline{w'\theta'}\left(h\right)}{h}\\
\overline{w'\theta'}(h) &= - \afg{h}t \,\Delta\theta = -w_e \Delta\theta \\
\afg{\Delta\theta}{t} &= \gamma_{\theta}\afg{h}{t}- \afg{\left<\overline{\theta}\right>}{t}
$$

$w_e$ is the entrainment velocity.

```

##
The atmospheric boundary layer height is 300 m at 0600 UTC, the temperature
lapse rate is 5 K/km and the initial temperature is $\theta$ is 285 K . Assuming that the sensible heat flux varies with time over this land
according to (t is given in hours):

$$
\overline{w'\theta'(0)}&=c_1 \sin \left( \frac{\pi(t-t_0)}{c_2} \right ) \\ 
c_1&=0.2\ Km\ s{-1} \\
c_2&=12\ hours
$$

a) Under encroachment conditions, find the boundary layer height at 14 UTC, if the entrainment flux and subsidence are neglectable.

```{admonition} Answer
:class: important, dropdown
In case of encroachment:

$$
\afg{\Delta\theta}{t} &= 0 \\
\gamma_{\theta}\afg{h}{t}- \afg{\left<\overline{\theta}\right>}{t} &= 0\\
\afg{h}{t} &= \frac{1}{\gamma_{\theta}}\afg{\left<\overline{\theta}\right>}{t}
$$

Since in the case of encroachment, $\overline{w'\theta'}(h)=0$, Equation {eq}`for:61b` becomes

$$
\afg{\left<\overline{\theta}\right>}{t} = \frac{\overline{w'\theta'}\left(0\right)}{h}
$$

Therefore, denoting $\overline{w'\theta'}\left(0\right)$ as $\overline{w'\theta'}_S$, 

$$
\afg{h}{t} = \frac{1}{\gamma_{\theta}}\frac{\overline{w'\theta'}_S}{h} 
$$(for:62a)

$$
2\,h\,\afg{h}{t} &= 2 \frac{\overline{w'\theta'}_S}{\gamma_{\theta}}\\
\afg{h^2}{t} &= 2 \frac{\overline{w'\theta'}_S}{\gamma_{\theta}}\\
\int_{t1}^{t2}{h^2{\rm d}t} &= \int_{t1}^{t2}{2 \frac{\overline{w'\theta'}_S}{\gamma_{\theta}}{\rm d}t}\\
h_2^2-h_1^2 &=  \frac{2}{\gamma_\theta} \int_{t1}^{t2}{\overline{w'\theta'}_S{\rm\,d}t}
$$

Finally,

$$
h_2 = \sqrt{h_1^2 + \frac{2}{\gamma_\theta} \int_{t1}^{t2}{\overline{w'\theta'}_S{\rm\,d}t}}
$$

Substituting the heat flux results in

$$
h_2 = \sqrt{h_1^2 + \frac{2}{\gamma_\theta} \int_{t1}^{t2}{c_1 \sin\left(\frac{\pi\left(t-t_0\right)}{c_2}\right){\rm\,d}t}}
$$

In this equation, the integral is given by 

$$
\int_{t1}^{t2}{c_1 \sin\left(\frac{\pi\left(t-t_0\right)}{c_2}\right){\rm\,d}t} &= c_1 \left[{-\frac{c_2}{\pi}\cos\left(\frac{\pi\left(t-t_0\right)}{c_2}\right)}\right]_{t_1}^{t_2}\\
 &= \frac{c_1\,c_2}{\pi} \left({\cos\left(\frac{\pi\left(t_1-t_0\right)}{c_2}\right)-\cos\left(\frac{\pi\left(t_2-t_0\right)}{c_2}\right)}\right)_{t_1}^{t_2}\\
 &\approx 4125 {\rm\,K\,m}
$$

for $t_1=t_0=0600\rm\,UTC$ and $t_2=1400\rm\,UTC$. Substituting this value, $h_1$, $c_1$ and $c_2$ nets $h\left(1400\rm\,UTC\right)\approx 1319\rm\,m$

```

b) Calculate the boundary layer height at 14 UTC assuming that there is a closure assumption between the
heat flux at the surface and at the entrainment zone:

$$
\overline{w'\theta'(z_i)}~=~-\beta \overline{w'\theta'(0)},
$$

where $\beta$ is 0.2.

```{admonition} Answer
:class: important, dropdown
This exercise is solved under the assumption that the boundary layer growth is still only due to encroachment, so $\Delta\theta=0$. In this case, the boundary layer height development is not related to the entrainment flux. The governing equations are:

$$
\afg{h}{t} &= \frac{1}{\gamma_{\theta}}\afg{\left<\overline{\theta}\right>}{t}\\
\afg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}\left(0\right)-\overline{w'\theta'}\left(h\right)}{h} \\
 &= \left(1+\beta\right) \frac{\overline{w'\theta'}\left(0\right)}{h} \\
 &= \left(1+\beta\right) \frac{\overline{w'\theta'}_S}{h}
$$

This results in 

$$
\afg{h}{t} = \frac{1+\beta}{\gamma_{\theta}}\frac{\overline{w'\theta'}_S}{h}
$$

Due to the analogy with Equation {eq}`for:62a`, this results in 

$$
h_2 &= \sqrt{h_1^2 + \frac{2}{\gamma_\theta} \int_{t1}^{t2}{\left(1+\beta\right)\overline{w'\theta'}_S{\rm\,d}t}}\\
 &= \sqrt{h_1^2 + \frac{2\,\left(1+\beta\right)}{\gamma_\theta} \int_{t1}^{t2}{\overline{w'\theta'}_S{\rm\,d}t}}
$$

Since the solution to the integral and the values of $h_1$, $\beta$ and $\gamma_\theta$ are known, the answer can be found: $h_2 \approx 1439\rm\,m$

```

c) Calculate the mixed-layer potential temperature in the Convective Boundary Layer
at 14.00 for both cases. Discuss the results.

```{admonition} Answer
:class: important, dropdown
Due to the relation 

$$
\afg{h}{t} = \frac{1}{\gamma_{\theta}}\afg{\left<\overline{\theta}\right>}{t}
$$

It is known that

$$
\afg{\left<\overline{\theta}\right>}{t} &= \gamma_\theta \afg{h}{t}\\
\Delta{\left<\overline{\theta}\right>} &= \gamma_\theta \Delta{h}\\
\left<\overline{\theta}\right>_2 &= \left<\overline{\theta}\right>_1 + \gamma_\theta \left(h_2-h_1\right)
$$

The resulting mixed layer potential temperatures are $290.1\rm\,K$ in the case of encroachment 
and $290.7\rm\,K$ in the case of entrainment flux without the associated boundary layer growth. 

Note that the solution presented here is not the complete analytical solution, since we neglected the growth of the boundary layer that is associated to the entrainment flux. In case this is taken into account, a factor 2 appears before $\beta$ in the final equation for $h_2$ as well as some extra terms that deal with the initial inversion conditions.

```

##
Given an arbitrary mixed layer, we can assume that the mixed layer potential temperature
($\left<\overline{\theta}\right>$ and the potential temperature jump ($\Delta\theta$)) evolve with time according to

$$
\pafg{\left<{\overline{\theta}}\right>}{t} &=\frac{\overline{w'\theta'}(0)-\overline{w'\theta'}(h)}{h} \\
        \pafg{\Delta\theta}{t} &= \gamma_\theta\pafg{h}{t} - \pafg{\left<\overline{\theta}\right>}{t}\\
        \overline{w'\theta'}(h) &= - \pafg{h}{t}\Delta\theta
$$

At 12 UTC, the mixed layer temperature is 290 K. At the top of the mixed layer, there is an inversion
with an initial temperature above equal to 296 K.
Above the inversion the temperature increases 0.05 K every 10 m.
The surface flux $\overline{w'\theta'}(0)$ is 185 $W/m^2$.

a) Draw the vertical profile of the potential temperature and the heat flux.
Describe the different regions in the CBL.

```{hint}
:class: tip, dropdown
In this exercise it is <u>assumed</u> that $\afg{\Delta\theta}{t}=0$. Due to this, it follows from the governing equation

$$
\afg{\Delta\theta}{t}=\gamma_\theta\afg{h}{t}-\afg{\left<\overline{\theta}\right>}{t}
$$

that $\gamma_\theta\afg{h}{t}=\afg{\left<\overline{\theta}\right>}{t}$.
```


````{admonition} Answer
:class: important, dropdown

```{figure} figures/exercise6_3.png
:name: fig:6

Boundary layer profiles of potential temperature **a** and sensible heat flux **b** at 12 UTC. The dashed lines denote the idealized profiles.
```

The profiles are drawn in {numref}`fig:6`. From bottom to top, the layers are:
* the surface layer
* the mixed layer
* the entrainment zone
* the free troposphere
````

b) Find an expression for the time evolution of $h$ without evaluating it. Do this

1. assuming no entrainment and no potential temperature inversion (encroachment).
    ```{admonition} Answer
    :class: important, dropdown
    If no entrainment is present, $\overline{w'\theta'}(h)=0$. 
    Since it is assumed that no potential temperature inversion is present at the top of the boundary layer, both the left hand side and the right hand side of the 3$^{\rm rd}$ governing equation are 0. 
    Also $\pafg{\Delta\theta}{t}=0$. Combining these relations results in
    
    $$
    \gamma_\theta \pafg{h}{t} &= \pafg{\left<\overline{\theta}\right>}{t}\\
    \pafg{\left<\overline{\theta}\right>}{t} &= \frac{\overline{w'\theta'}(0)}{h}
    $$
    
    Therefore,
    
    $$
    \pafg{h}{t} = \frac{\overline{w'\theta'}(0)}{\gamma_\theta\,h}
    $$
    
    This could be further solved by  rewriting it to 
    
    $$
    2h\pafg{h}{t} &= 2 \frac{\overline{w'\theta'}(0)}{\gamma_\theta}\\
    \pafg{h^2}{t} &= 2 \frac{\overline{w'\theta'}(0)}{\gamma_\theta}\\
    \int_{t_0}^t{\pafg{h^2}{t}{\rm d}t} &= \int_{t_0}^t{2 \frac{\overline{w'\theta'}(0)}{\gamma_\theta}{\rm d}t} \\
    h^2 - h_0^2 &= \frac{2}{\gamma_\theta} \int_{t_0}^t{{\overline{w'\theta'}(0)}{\rm d}t} \\
    $$
    
    This results in
    
    $$
    h = \sqrt{h_0^2 + \frac{2}{\gamma_\theta} \int_{t_0}^t{\overline{w'\theta'}(0){\rm d}t}}\\
    $$
    ```
2. assuming $\overline{w'\theta'}(h) = -\beta \,\overline{w'\theta'}(0)$. In this case, consider a situation in which $\Delta\theta$ is relatively constant in time $\left(\pafg{\Delta\theta}t\right)\approx 0$ and unknown (negating the use of eq. 6.45).

    ```{admonition} Answer
    :class: important, dropdown
    In this case $\overline{w'\theta'}(h)=-\beta \overline{w'\theta'}(0)$. 
    Also, the time derivative of the potential temperature jump is 0, $\pafg{\Delta\theta}{t}=0$, and the 3$^{\rm rd}$ governing equation has to be ignored. 
    Therefore, the governing equations are 
    
    $$
    \pafg{\left<{\overline{\theta}}\right>}{t} &=\frac{\overline{w'\theta'}(0)-\left(-\beta \overline{w'\theta'}(0)\right)}{h} \\
    0 &= \gamma_\theta \pafg{h}{t} - \pafg{\left<\overline{\theta}\right>}{t}
    $$
    
    These can be combined to
    
    $$
    \pafg{h}{t} = \frac{\left(1+\beta\right)\overline{w'\theta'}(0)}{\gamma_\theta\,h}$
    $$
    
    This can be solved, similar to the previous exercise, with the exception of taking $\left(1+\beta\right)\overline{w'\theta'}(0)$ instead of $\overline{w'\theta'}(0)$. Therefore, the resulting expression for $h$ is
    
    $$
    h &= \sqrt{h_0^2 + \frac{2+2\beta}{\gamma_\theta} \int_{t_0}^t{\overline{w'\theta'}(0){\rm d}t}}\\
    $$
    ```
3. making no assumptions, except that $\overline{w'\theta'}(h) = -\beta \,\overline{w'\theta'}(0)$. 
   In this case, can you determine $\pafg{h}{t}$ without knowing $\Delta\theta$?
    ```{admonition} Answer
    :class: important, dropdown
    In this case, no assumptions are made, except for $\overline{w'\theta'}(h)=-\beta \overline{w'\theta'}(0)$. Since we're allowed to use the value of $\Delta\theta$ (which changes in time as well), we can use the 3$^{\rm rd}$ governing equation. 
    
    $$
    \pafg{h}{t} &= -\frac{\overline{w'\theta'}(h)}{\Delta\theta}\\
    $$
    
    Therefore,
    
    $$
    $\pafg{h}{t} = \beta \frac{\overline{w'\theta'}(0)}{\Delta\theta}
    $$
    
    Since the boundary layer growth is governed by the potential temperature jump (faster growth in the case of a weaker jump), $\pafg{h}{t}$ cannot be determined without knowing $\Delta\theta$. 
   
    As a note: It is not straightforward to solve $h$ as a function of time. However, it can be done, with as result
    
    $$
    &h^2\left[1 - \frac{2+4\beta}{\gamma_{\theta}}\left(\Delta\theta_0 h_0^{\frac{1+\beta}{\beta}} - \frac{\beta}{1+2\beta} \gamma_{\theta} h_0^{\frac{1+2\beta}{\beta}}  \right) h^{-\frac{1+2\beta}{\beta}}\right] = \nonumber \\
    &\qquad \qquad \qquad h_0^2 - \frac{2+4\beta}{\gamma_{\theta}}\left(\Delta\theta_0 h_0 - \frac{\beta}{1+2\beta} \gamma_{\theta} h_0^2 \right) + \frac{2+4\beta}{\gamma_{\theta}}\int_{t_0}^t{\overline{w'\theta'}_0\mathrm{d}t} \label{for:implicitdecomposed}
    $$
    ```

c) If $h$ is 1000 m at 12 UTC, what is the boundary layer growth rate and the temperature change per hour in the CBL?
```{admonition} Answer
:class: important, dropdown

$$
\pafg{h}{t} &= 0.2 \frac{\overline{w'\theta'}(0)}{\Delta\theta}\\
\overline{w'\theta'}(0) &= 185 {\rm\,W\,m^{-2}} = 0.15\rm\,K\,m\,s^{-1}\\
\Delta\theta &= 6\rm\,K
$$

Therefore, $\pafg{h}{t} = 0.005\rm\,m\,s^{-1} = 18\,m\,hr^{-1}$

$$
\pafg{\left<{\overline{\theta}}\right>}{t} &=\frac{\overline{w'\theta'}(0)-\overline{w'\theta'}(h)}{h} \\
 &=  \frac{\left(1+\beta\right)\overline{w'\theta'}(0)}{h}\\
h&= 1000\rm\,m
$$

Because of this, $\pafg{\left<{\overline{\theta}}\right>}{t} = 1.8\,10^{-4}\rm\,K\,s^{-1}=0.65\,K\,hr^{-1}$.
```

d) Calculate the convective velocity at the same time and estimate how long it takes a parcel to travel from the
    surface to the top of the atmospheric boundary layer
```{admonition} Answer
:class: important, dropdown
The convective velocity is defined by 

$$
w_*=\sqrt[3]{\frac{g}{\theta_v}\,\overline{w'\theta_v'}\,h}
$$

In this definition, the buoyancy term of the TKE, $\frac{g}{\theta_v}\,\overline{w'\theta_v'}$, is incorporated. In this case, no moisture is considered, so $\overline{w'\theta_v'}=\overline{w'\theta'}$. Substituting the known values results in \boxin{$w_* = 1.72\rm\,m\,s^{-1}$}

The time it takes for a parcel to travel from the surface to the top of the atmospheric boundary layer due to convection is 

$$
T = \frac{h}{w_*}
$$

This results in $T = 582 s \approx 10\rm\,min$

```

##
{numref}`fig:61`, {numref}`fig:62`, and {numref}`fig:63` show the vertical profiles of the potential temperature measured by radiosondes in the USA at 11, 17 and 23 UTC the 20th June 1997 (local time=UTC-6 hours).

```{figure} figures/figset61.png
:name: fig:61
Vertical profile of potential temperature and specific humidity measured by radiosondes at 11 UTC
```

```{figure} figures/figset62.png
:name: fig:62
Vertical profile of potential temperature and specific humidity measured by radiosondes at 17 UTC
```

```{figure} figures/figset63.png
:name: fig:63
Vertical profile of potential temperature and specific humidity measured by radiosondes at 23 UTC
```

a) Describe the main characteristics of the radiosoundings.
```{admonition} Answer
:class: important, dropdown
The upper left profile shows a stable boundary layer, while the other two profiles show well-mixed convective boundary layers.

|Figure|{numref}`fig:61`|{numref}`fig:62`|{numref}`fig:63`|
|--|--|--|--|
|h (m) | 700 | 1400 | 1400 |
|$\left<\theta\right>$ (K) | 303 | 309.5 | 310|
|$\Delta\theta$ (K) | 9 | 5 | 4|
|$\gamma_\theta$ (K km$^{-1}$) | 2.2 | 2.5 | 2.5|
```

b) Give the evolution of the boundary layer depth.
```{admonition} Answer
:class: important, dropdown
From 05.30 LT to 11.30 LT: + 700 m, so a growth of approximately 3~cm~s$^{-1}$.

From 11.30 LT to 17.30 LT: the boundary layer height is constant, so a growth of 0~cm~s$^{-1}$.
```

c) Assuming an entrainment velocity equal to 0.01 m/s, find the entrainment
flux at 17 UTC.
```{admonition} Answer
:class: important, dropdown
At 17 UTC (11 LT), $\Delta\theta=5\rm\,K$ (since it's not that different from the jump at 17.30 UTC) and $\pafg{h}{t}=0.01\rm\,m\,s^{-1}$. 

$$
F_e &= - w_e\,\Delta\theta \\
 &= \pafg{h}{t}\,\Delta\theta
$$

Substituting the variables results in $F_e = -0.05\rm\,K\,m\,s^{-1}$.

The flux is negative, since heat is transported downwards.

```

##
During the 27th of July 2002, the vertical profile of potential temperature
and heat flux (see {numref}`fig:64` and {numref}`fig:65`) were measured by an aircraft above Cabauw. The heat flux measurements were
taken around 12.45 UTC.

a) Estimate the boundary layer height at 8.15 UTC and 12.45. Calculate the velocity of the growth of the convective boundary layer.
```{admonition} Answer
:class: important, dropdown
Using the location where $\pafg{\theta}{z}$ has its maximum, the boundary layer heights at 8.15 UTC and 12.45 UTC are 375 m and 1025 m, respectively. 
Therefore, the velocity of growth is $\pafg{650\rm\,m}{4.5\cdot 3600\rm\,s} = 0.04\rm\,m\,s^{-1}$.

```

b) Calculate the terms (storage, turbulent flux divergence) of the potential temperature equation in the mixed layer.
```{admonition} Answer
:class: important, dropdown

$$
\gemafg{\theta}{t}+\gemafg{w'\theta'}{z} = {\rm Advection} + {\rm Sources/sinks}
$$

Sources correspond with warming and sinks with cooling.

Storage term: $\gemafg{\theta}{t} = \frac{5\rm\,K}{4.5\rm\,hr}=3.1\times 10^{-4}\rm\,K\,s^{-1}$

Turbulent flux divergence: $\gemafg{w'\theta'}{z} = \frac{0.095\rm\,K\,m\,s^{-1}}{700\rm\,m}= 1.4\times 10^{-4}\rm\,K\,s^{-1}$

```

c) Was the advection of potential temperature an important term during the 27th July 2002?
```{admonition} Answer
:class: important, dropdown
Since other sources and sinks are negligible during day, advection should account for the difference between storage and the vertical turbulent flux divergence. 
Therefore, advection should account for $1.7\times 10^{-4}\rm\,K\,s^{-1}$. 
This is of the same order of magnitude as the temperature tendencies of the terms that are related to storage and transport by turbulent fluxes. 
This shows that advection is important for this case. 
```

d) The heat flux can be related to the gradient of the mean potential
temperature as follows

$$
\overline{w'\theta'(z)}=-K_h\pafg{\overline{\theta}}{z}
$$

Using the information from the vertical flux of potential temperature
                                                          and heat flux, calculate the exchange coefficient $K_h$ at z=500 m (time 12.45).
This coefficient can also be calculated using convective scaling. The expression reads:

$$
    K_h=\kappa w_*z\left(1-\frac{z}{h}\right )^2
$$

Calculate $K_h$ at 500 m and at 12.45 using this expression and compare it with the previous calculation.

```{admonition} Answer
:class: important, dropdown
*THERE IS NO ANSWER IN THE ANSWER MODEL*
```

```{figure} figures/figset64.png
:name: fig:64
Vertical profile of potential temperature measured above Cabauw during the 27th July 2002
```

```{figure} figures/figset65.png
:name: fig:65
Vertical profile of sensible heat flux measured above Cabauw during the 27th July 2002
```
