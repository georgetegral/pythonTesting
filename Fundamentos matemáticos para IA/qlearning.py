import numpy as np
#iniciar desde cero los valores de la tabla q
Q = np.zeros((state_size, action_size))

import random
#Establece el porcentaje a explorar
epsilon = 0.2

if random.uniform(0,1) < epsilon:
"""
Explora: Selecciona una acción aleatoria
"""
else:
"""
Explota: Selecciona acción de valor máximo (recompensa)
"""

#Actualiza los valores de q
Q[state, action] = Q[state, action] + lr * (reward + gama * np.max(Q[new_state,:]) - Q[state, action])
