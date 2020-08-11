def calcular_permat(p, a):
    return (a**p)% a

if __name__ == '__main__':
    p = int(input('Introduce P: '))
    a = int(input('Introcue A: '))
    if calcular_permat(p,a) == 0:
        print('Divisible')
    else:
        print('No divisible')