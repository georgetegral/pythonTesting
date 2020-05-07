from aproximacion import aproximacion
from busqueda_binaria import busqueda_binaria
from enumeracion import enumeracion

print('1. Aproximacion')
print('2. Busqueda binaria')
print('3. Enumeracion')
algo = int(input('Escoge un algoritmo: '))

if algo == 1:
    aproximacion()
elif algo == 2:
    busqueda_binaria()
elif algo == 3:
    enumeracion()
else:
    print('Por favor selecciona un algoritmo válido')
