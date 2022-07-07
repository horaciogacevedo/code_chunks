import matplotlib.pyplot as plt
import numpy as np

A = 2
a = 0.3
hlam = 0.5
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
r = 0.05
u, v = np.mgrid[0:2 * np.pi:30j, 0:np.pi:20j]
x = ((A+a)*np.cos(u) - hlam*a*np.cos((A+a)*u/a))*np.sin(v)
y = (A+a)*np.sin(u) - hlam*a*np.sin((A+a)*u/a)*np.sin(v)
z = np.cos(v)
ax.axis('off')
ax.plot_surface(x, y, z, cmap=plt.cm.Spectral_r)
plt.show()