import matplotlib.pyplot as plt
import numpy as np

time = np.arange(0, 43201, 1)
f = 1e-4
u0 = 3
v0 = 2
ug = 5

c2 = u0-ug
c1 = v0

u = ug + c1*np.sin(f*time) + c2*np.cos(f*time)
v = c1*np.cos(f*time) - c2*np.sin(f*time)
U = (u**2 + v**2)**.5

plt.figure(figsize=(7, 3.8), constrained_layout=True)
plt.subplot(121)
plt.plot(time/3600, u, 'C0-', label='u')
plt.plot(time/3600, v, 'C1-', label='v')
plt.plot(time/3600, U, 'k-', label='U')
plt.plot(time/3600, ug*np.ones_like(time), 'k:', label=r'u$_g$')
plt.xlabel(r'hours after sunset')
plt.ylabel(r'velocity (m s$^{-1}$)')
plt.legend()
plt.title('a)', loc='left')
plt.subplot(122)
plt.scatter(u[::3600], v[::3600], c=time[::3600], cmap=plt.cm.Blues)
plt.plot(u, v, 'C0-')
plt.xlabel(r'u (m s$^{-1}$)')
plt.ylabel(r'v (m s$^{-1}$)')
plt.savefig('llj.png', dpi=200)
plt.title('b)', loc='left')
plt.show()
