from borracho import BorrachoTradicional
from campo import Campo 
from coordenada import Coordenada 

from bokeh.plotting import figure, show

def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)

    for _ in range(pasos):
        campo.mover_borracho(borracho)

    return inicio.distancia(campo.obtener_coordenada(borracho))


def ejecutar_caminata(campo, borracho, distancia):
    x_arreglo = []
    y_arreglo = []
    x_arreglo.append(campo.obtener_coordenada(borracho).x)
    y_arreglo.append(campo.obtener_coordenada(borracho).y)
    for _ in range(distancia):
        campo.mover_borracho(borracho) #se actualiza las coordenadas del borracho
        x_arreglo.append(campo.obtener_coordenada(borracho).x)
        y_arreglo.append(campo.obtener_coordenada(borracho).y)

    graficar(x_arreglo, y_arreglo)

def graficar(x, y):
    figura = figure()
    figura.line(x, y)
    show(figura)

def main(distancia, inicio, tipo_de_borracho):
    campo = Campo()
    campo.anadir_borracho(borracho,inicio)
    ejecutar_caminata(campo, borracho, distancia)

if __name__ == '__main__':
    distancia = 100000
    inicio = Coordenada(0,0)
    borracho = BorrachoTradicional('Yorch')

    main(distancia, inicio, BorrachoTradicional)