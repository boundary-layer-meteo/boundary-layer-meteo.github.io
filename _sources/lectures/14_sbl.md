# The stable boundary layer

```{admonition} Questions to be answered in this chapter
1. What is a stable boundary layer?
1. What is the low level jet and how does it originate?
1. What happens to the logarithmic profile in the surface layer as an effect of stability?
```

A *stable boundary layer* occurs when the atmosphere is statically stable ($\partial \overline{\theta}_v / \partial z > 0$).
In such a boundary layer, if we study TKE evolution we find that buoyancy is suppressing the generation of turbulence by shear, and if the Richardson number exceeds 1, then turbulence will collapse.

Since stable boundary layers are shear-driven with buoyancy working against turbulence generation, its depth is far less than that of a convective boundary layer, generally (at most) a few 100 meter. Above the stable boundary layer, we find the *residual layer* which is the well-mixed region that remained of the convective boundary layer from daytime.

## The low-level jet
One of the unique features of the stable boundary layer is the low-level jet, a peak in wind speed at the top of the stable boundary layer. This peak can exceed geostrophic wind. We repeat here the governing equations for the conservation of momentum, under the assumption of high Reynolds numbers, horizontal homogeneity, and no subsidence.

$$
\def\ubar{\overline{u}}
\def\vbar{\overline{v}}
\def\uwflux{\overline{u^\prime w^\prime}}
\def\vwflux{\overline{v^\prime w^\prime}}
\def\pd#1#2{\dfrac{\partial #1}{\partial #2}}
\pd{\ubar}{t} &= - \pd{\uwflux}{z} + f \left( \vbar - v_g \right) \\
\pd{\vbar}{t} &= - \pd{\vwflux}{z} - f \left( \ubar - u_g \right)
$$

In a convective boundary layer, there is often an approximate balance between the coriolis force and the flux divergence. If we assume the geostropic wind to be only in the $u$-direction, thus $v_g = 0$, then the following balance holds

$$
0 &\approx - \pd{\uwflux}{z} + f \vbar \\
0 &\approx - \pd{\vwflux}{z} - f \left( \ubar - u_g \right)
$$

In this balance, the mixed-layer value of the wind is subgeostrophic.
If then at sunset convection stops and the convective boundary layer splits in a stable boundary layer close to the surface, and a residual layer above.
The residual layer is no longer turbulent and no longer connected to the surface.
Therefore, the wind just above the stable boundary layer starts evolving following

$$
\pd{\ubar}{t} &=   f \vbar \\
\pd{\vbar}{t} &= - f \left( \ubar - u_g \right)
$$

*...more to come...*
