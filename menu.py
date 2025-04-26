from operacoes import somar, subtrair, multiplicar, dividir

def menu():
    print('Bem vindo a calculadora')
    print('Qual operação deseja executar?')
    print('1 - Soma', '2 - Subtração', '3 - Multilpicação', '4 - Divisão', '5 - Sair', sep='\n')
    oper = input('Escolha a operação: ')

    if oper == '5':
          print('Volte sempre que precisar!')
          return
    
    elif oper not in ['1', '2', '3', '4']:
        print('Não existe essa opção. Digite novamente.')
        return menu()

    a = float(input('Digite o primeiro número: '))
    b = float(input('Digite o segundo número: '))

    if oper == '1':
        print('A soma é', somar(a, b))

    elif oper == '2':
        print('A subtração é', subtrair(a, b))

    elif oper == '3':
        print('A multiplicação é', multiplicar(a, b))

    elif oper == '4':
        print('A divisão é', dividir(a, b))
    
    continuar = input('Deseja continiuar? (s/n): ')
    if continuar == 's':
        return menu()
    else:
        print('Volte sempre que precisar!')

    
      
menu()

# a = input('Digite o primeiro número a ser somado: ')
# b = input('Digite o segundo número a ser somado: ')

# a = input('Digite o minuendo: ')
# b = input('Digite o subtraendo: ')

# a = input('Digite o primeiro número a ser multiplicado: ')
# b = input('Digite o segundo número a ser multiplicado: ')

# a = input('Digite o dividendo: ')
# b = input('Digite o divisor: ')