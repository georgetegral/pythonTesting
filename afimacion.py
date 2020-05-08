# assert <expresion boleana>, <mensaje de error>

lista_palabras = []
lista_primeras_letras = []

for i in range(5):
    word=input('Escribe una palabra: ')
    lista_palabras.append(word)
    

for palabra in lista_palabras:
    assert type(palabra) == str, f'{palabra} no es str'
    assert len(palabra) > 0, 'No se permiten palabras vacios'

    lista_primeras_letras.append(palabra[0])

print(lista_palabras,lista_primeras_letras)