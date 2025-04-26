def somar(a, b):
    return a+b

def subtrair(a, b):
    return a-b

def multiplicar(a, b):
    return a*b

def dividir(a, b):
    if b != 0:
        return a/b
    else:
        print('Não existe divisão por zero.')
        a = float(input('Digite novamente o numerador: '))
        b = float(input('Digite um denominador diferente de zero: '))
        return dividir(a, b)