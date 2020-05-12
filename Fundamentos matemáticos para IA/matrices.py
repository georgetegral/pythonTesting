import numpy as np
# No sólo muestra los datos, también imprime el tipo de objeto a diferencia deprint()
from IPython.display import display 

m1 = np.matrix([[1, 0, 3],
              [-4, 3, 7],
              [2, -2, -5]])
m2 = np.array([[2, 1, 0],
               [3, 1, -2],
              [0, -1, -2]])
display(m1)
display(m2)

print(m1*m2)