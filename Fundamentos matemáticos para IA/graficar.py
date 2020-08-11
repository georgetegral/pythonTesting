import numpy as np
from matplotlib import pyplot as plt 

deffuncion(x):
    return4*x**3 - 260*x**2 + 4000*x

x = np.linspace(-40, 100, 10000)

#Nombre de los ejes y límites de los ejes
plt.xlabel("Alto [m]")
plt.ylabel("Volumen [m3]")
plt.xlim(left=-20, right=60)
plt.ylim(bottom=-60000, top=60000)

#Se crean las líneas de los ejes X=0, Y=0 y X=10
plt.axhline(0, color='black', linestyle = 'dotted')
plt.axvline(0, color='black', linestyle = 'dotted')
plt.axvline(10, color='red', linestyle = 'dotted')

plt.text(10, funcion(10),'MÁX: ({}, {})'.format(10, funcion(10)))
plt.plot(x, [funcion(i) for i in x])
plt.show()