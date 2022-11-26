# Convective boundary layer

During daytime, there is a well-mixed convective boundary layer of approximately 1 km in depth.
If we assume horizontal homogeneity, no subsidence and high Reynolds numbers, the conservation of energy in this layer can be described as

$$
\def\pd#1#2{\dfrac{\partial #1}{\partial #2}}
\def\thetabar{\overline{\theta}}
\def\thetabulk{\left< \thetabar \right>}
\pd{\overline{\theta}}{t} = - \pd{\overline{w^\prime \theta^\prime}}{z} 
$$

The well-mixed property of this layer allows us to derive a very simple bulk model (thus no spatial derivatives).
We integrate from surface to the depth of the layer.

$$
\int_0^h \pd{\thetabar}{t} \mathrm{d}z  = - \int_0^h \pd{\overline{w^\prime \theta^\prime}}{z} \mathrm{d}z
$$

We rewrite the lefthand side using Leibniz' rule:

$$
\dfrac{\mathrm{d}}{\mathrm{d} t} \int_0^h \thetabar \, \mathrm{d}z
= \int_0^h \pd{\thetabar}{t} \mathrm{d}z
+ \dfrac{\mathrm{d} h}{\mathrm{d} t} \thetabar \left(h\right)
- \dfrac{\mathrm{d} 0}{\mathrm{d} t} \thetabar \left(0\right)
$$

where the last term is equal to zero.

If we define the bulk mean temperature of the convective boundary layer

$$
\thetabulk = \dfrac{1}{h} \int_0^h \thetabar \, \mathrm{d} z
$$

and substitute the lefthand side of the integrated equation with the help of the Leibniz rule to get


$$
\dfrac{\mathrm{d}}{\mathrm{d} t} \left( \thetabulk h \right)
- \dfrac{\mathrm{d} h}{\mathrm{d} t} \thetabar \left(h\right)
= 
- \overline{w^\prime \theta^\prime} \left( h \right)
+ \overline{w^\prime \theta^\prime} \left( 0 \right)
$$
