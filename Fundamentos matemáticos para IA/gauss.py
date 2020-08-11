import numpy as np

matriz1= np.matrix([[2, -1, 3],
                  [2, 2, 3],
                  [-2, 3, 0]])
sol1 = np.array([5, 7, -3])

print("Solución: ")
print(np.linalg.solve(matriz1, sol1))

#Trabaja de la siguiente forma
#Aunque parezca otra cosa al pasar "sol1" como vector fila
# | 2  -13 |    |  5 |
# | 223 | =  |  7 |
# |-230 |    | -3 |