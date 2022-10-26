# Exercises chapter 4

```{epigraph}
$$
Big\ whirls\ have\ little\ whirls\ that\ feed\ on\ their\ velocity, \\
    and\ little\ whirls\ have\ lesser\ whirls\ and\ so\ on\ to\ viscosity.
$$

-- Lewis Fry Richardson, 1922
```

##
The following figure shows the raw observation of the wind speed.

```{figure} figures/figset51.png
:name: fig51
```

a) Sketch your best guess of the spectrum of the wind velocity as
function of the period (min), the frequency (cycles/min) and the
wave-number (cycles/m).

````{admonition} Answer
:class: important, dropdown
It should be visible in the figure at which frequencies the eddies contain most energy. 
In this exercise, not the angular frequencies, $\left(\omega=\frac{2\pi}{T}\right)$, and wave numbers, $\left(k=\frac{2\pi}{\lambda}\right)$, are used, but the ordinary ones: $f=\frac{1}{T}$ and $\nu=\frac{1}{\lambda}$. 
In these equations $T$ and $\lambda$ denote the corresponding period and length scale.
The periods that seem most important are 1 minute and 0.1 minute (6 s). 
The signal with a time scale of 1 minute contains most energy. 
The corresponding sketch is shown in {numref}`fig411`.

```{figure} figures/exercise4_1_1.png
:name: fig411
Spectrum of the wind velocity as a function of time.
```

The conversion from time period to frequency is straight forward. 
However, the dependency on the wave number is a bit harder. 

$$
\overline{v}&=\lambda f\\
 &= \frac{f}{\nu}\\
\nu &= \frac{f}{\overline{v}} 
$$(for:41a)

Since $\overline{v} = 5\rm\,m\,s^{-1}$ according to the observations, it is known that $\nu = \frac{f}{\overline{v}} = f \frac{1}{5\rm\,m\,s^{-1}} = f \frac{1}{300} \rm\frac{min}{m}$. 
According to Taylor's frozen turbulence assumption, $f$ and $\nu$ are proportional to each other (Equation {eq}`for:41a`). 
Therefore, the sketch for these two variables are combined in {numref}`fig412`.

```{figure} figures/exercise4_1_2.png
:name: fig412
Spectrum of the wind velocity as a function of frequency, $f$, and wave number, $\nu$.
```

````

b) From your estimate of the mean wind velocity indicate the
diameter (in meters) of the most characteristic eddies.

```{admonition} Answer
:class: important, dropdown

Wanted: the size of eddies that transport most. 

The most dominant eddies have a time scale of 1 min (60 s). 
Larger eddies transport a bit more per eddy, but are less common. 
Smaller eddies transport less per eddy, but are more common. 
$\lambda=\overline{v}\,T$, so $\lambda=300\rm\,m$. 
Alternatively, this could be calculated by $\lambda=\frac{1}{\nu}$. 
(This is in accordance with Taylor's frozen turbulence theory.)

```

##
The spectra of the vertical velocity was calculated from sonic measurements
taken under convective conditions
at Cabauw (23 August 2001 at 12 UTC).

```{figure} figures/figset52.png
:name: fig52

Power spectra of the vertical velocity measured by means of a sonic at 2 m
at Cabauw during the 23th August 2001
```

a) Describe the different regions of the power spectra of the vertical velocity

```{admonition} Answer
:class: important, dropdown

1. Energy containing/producing range
2. Inertial subrange: redistribution, transport processes
3. Dissipation range

The border between 1 and 2 lies at the beginning of the relative straight decay of turbulence and the border between 2 and 3 at the end of this straight line. 

```

b) Discuss the validity of the Reynolds decomposition for the vertical velocity $w=
\overline{w}~+~w'$
```{hint}
:class: tip, dropdown
It's often stated that $\overline{w}=0$, but (when) is this valid?
```

```{admonition} Answer
:class: important, dropdown
If the spectrum is high, there is still a lot of energy associated with fluctuations of that frequency. 
It is visible that for $f>0.005\rm\,Hz$, the energy is still high, so there are many fluctuations of that frequency. 
To be able to average out all fluctuations for $\overline{w}$, one should measure long enough.

$$
T=\frac{1}{f} ,
$$

so $T_{\rm Av.}>200\rm\,s$.

```

c) If $U=5~m/s$, find the characteristic length scale for this convective boundary layer.

```{admonition} Answer
:class: important, dropdown
The characteristic length scale is the scale that contains most energy. 
From the figure, the corresponding frequency, $f$, is 0.05 Hz.

$$
U &= \lambda f\\
\lambda_{\rm char.} &= \frac{U}{f_{\rm char.}}
$$

Therefore, $\lambda_{\rm char.} = 100\rm\,m$.

```

d) What is the frequency response of the sonic anemometer.

```{admonition} Answer
:class: important, dropdown
Frequency response: the frequency with which is measured.
This frequency corresponds to the highest frequency that's present in the corresponding Fourier spectrum. However, to prevent aliasing, spectra are evaluated until the Nyquist frequency, $f_{Nyquist}$. Since $f_{Nyquist} = \frac{f_{max}}{2}$ and $f_{nyquist}=10\rm\,Hz$, we know that $f_{max}=20\rm\,Hz$.

```

e) In the inertial subrange $S(k) \cong \alpha \epsilon^{\frac{2}{3}} \kappa^{-\frac{5}{3}}$. Using Taylor's hypothesis of frozen turbulence
that relates frequencies and wave numbers with the mean wind ($f = U K$), we can derive that in the inertial subrange, the region which separates the
energy-containing region from the dissipation region, the density of the energy spectrum follows

$$
S_w(f)~=~\alpha~U^{5/3}~\epsilon^{2/3}~f^{-5/3}
$$

where $\alpha$ is a constant equal to 0.6; $\epsilon$ is the dissipation of the turbulent kinetic energy and $f$ is the frequency.
Using the values of the figure, calculate the characteristic length scale at the dissipation
range which is given by

$$
\eta~=~\left(\frac{\nu^3}{\epsilon}\right)^{1/4}
$$

where $\nu$ is the kinematic viscosity of air ($1.5~10^{-5} m^2/s)$.
(and $U=5~m/s$ as in question c)

```{admonition} Answer
:class: important, dropdown

Calculate the length scale of dissipation (Kolmogorov length scale): the length scale for which motions are dissipated by molecular processes. 
This is the lower bound of the length scales that can be evaluated using the governing equations without losing their physical meaning.

$$
\eta = \left(\frac{\nu^3}{\epsilon}\right)^\frac{1}{4}
$$

$\nu=1.5\,10^{-5}\rm\,m^2\,s^{-1}$, but $\epsilon$ has to be calculated. In the inertial subrange 

$$
S_w\left(f\right) &= \alpha\ U^\frac{5}{3}\epsilon^\frac{2}{3}f^{-\frac{5}{3}} , \\
\alpha&=0.6 .
$$

Since $f=1\rm\,Hz$ lies in this range, we can evaluate this equation for this value and 

$$
0.01&=0.6\ 5^\frac{5}{3}\epsilon^\frac{2}{3}1^{-\frac{5}{3}} , \\
\epsilon^\frac{2}{3} &= \frac{1}{60}\cdot 5^\frac{5}{3} , \\
\epsilon &=  0.12.
$$

This is in SI units ($\rm\,m^2\,s^{-3}$). Filling it up results in $\eta = 4.1\,10^{-4}\rm\,m$, so $\eta=0.4\rm\,mm$

```

f) Calculate the ratio between the characteristic length scale of the
boundary layer (question c) and the dissipation length scale (question e).
Discuss the result.


```{admonition} Answer
:class: important, dropdown

This ratio shows how many times the smallest scale involved has to be resolved in order to also resolve the characteristic process for at least one period. 
The ratio is $R=\frac{100\rm\,m}{0.4\rm\,mm}$, so $R=2.5 \cdot 10^5$. 
A normal PC (or even standard super computer) can not perform these calculations within reasonable time.
```
