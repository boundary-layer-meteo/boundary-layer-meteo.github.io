import matplotlib.pyplot as plt
import numpy as np

kappa = 0.4
dz = 1
L = 100

z = np.arange(dz/2, L, dz)

def make_lotw(z, ustar, z0):
    dudz = ustar / (kappa * z)
    u = ustar / kappa * np.log(z / z0)

    return dudz, u

ustar = 0.3; z0 = 0.1
dudz, u = make_lotw(z, ustar, z0)

plt.figure(figsize=(8,3.5), constrained_layout=True)
plt.subplot(131)
plt.plot(dudz, z)
plt.xlabel('du/dz (s$^{-1}$)')
plt.ylabel('z (m)')
plt.subplot(132)
plt.plot(u, z)
plt.xlabel('u (m s$^{-1}$)')
plt.ylabel('z (m)')
plt.subplot(133)
plt.plot(kappa*z/ustar*dudz, z)
plt.xlabel('$\phi_m$ (-)')
plt.ylabel('z (m)')
plt.savefig('lotw.png', dpi=300)
plt.show()
