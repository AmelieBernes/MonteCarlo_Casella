#Funciones para entender el algoritmo de Box-Muller


from mpl_toolkits import mplot3d
import numpy as np
import math
import pylab
import matplotlib.pyplot as plt

pi=math.pi

fig=plt.figure()
axis = plt.subplot(1,2,1,projection='3d')
ax[0]=plt.axes(projection='3d')
ax[1]=plt.axes(projection='3d')

def g(x, y):
    return  np.sqrt(-2*np.log(x)) * np.cos (2*pi*y)

def h(x, y):
    return np.sqrt(-2*np.log(x)) * np.sin (2*pi*y)

x = np.linspace(0, 1, 30)
y = np.linspace(0, 1, 30)

X, Y = np.meshgrid(x, y)
Z1=0*X
Z = g(X, Y)


ax[0].plot_surface(X, Y, Z)
ax[0].plot_surface(X, Y, Z1)

esquinas=[]
esq_x=[0,1,0,1]
esq_y=[0,0,1,1]
g_esq=[g(esq_x[i], esq_y[i]) for i in range(4)]

#ax.invert_zaxis() #para que la orientación del espacio sea la correcta.
ax[0].scatter(0,0,0, color='black')
ax[0].scatter(1,0,0, color='black')
ax[0].scatter(0,1,0, color='black')

for i in range(4):
    ax[0].plot((esq_x[i], esq_y[i], 0),(esq_x[i], esq_y[i], g_esq[i]))


plt.show()
