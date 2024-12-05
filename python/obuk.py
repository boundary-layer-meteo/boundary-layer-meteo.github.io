import matplotlib.pyplot as plt
import numpy as np

z0 = 0.1
kappa = 0.4
ustar = 0.3

B = 0.03 * (9.81/300)

L = -ustar**3 / (kappa*B)

z = np.arange(0.1, 100.001, 0.001)

def get_u(L):
    if L > 0:
        u = ustar / kappa * (np.log(z / z0) + 4.8 * z/L)
    elif L < 0:
        u = ustar / kappa * (np.log(z / z0) - 3. * np.log( (1 + (1 + 3.6*abs(z/L)**(2/3))**.5 ) / (1 + (1 + 3.6*abs(z0/L)**(2/3))**.5 ) ) )
    else:
        u = ustar / kappa * (np.log(z / z0))
    return u

zL = np.linspace(-1, 1, 10000)

def get_phim(zL):
    phim = np.where(zL < 0, (1 + 3.6*abs(zL)**(2/3))**(-1/2), 1. + 4.8*zL)
    return phim

plt.figure()
plt.plot(zL, get_phim(zL))

plt.figure()
plt.plot(get_u( L), z, label='stable')
plt.plot(get_u(-L), z, label='unstable')
plt.plot(get_u( 0), z, label='neutral')
plt.legend()

plt.show()
