while True:
    print('Olá, seja bem-vindo a sua calculadora!')
    print('[ 1 ] Adição')
    print('[ 2 ] Subtração')
    print('[ 3 ] Multiplicação')
    print('[ 4 ] Divisão')
    print('[ 0 ] Sair')

    opcao = input('Escolha uma opção: ')

    if(opcao == '1'):
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        sum = (n1 + n2)

        print('{:.1f} + {:.1f} = {:.1f} '.format(n1, n2, sum))
    
    elif(opcao == '2'):
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        sub = (n1 - n2)

        print('{:.1f} - {:.1f} = {:.1f} '.format(n1, n2, sub))

    elif(opcao == '3'):
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        mult = (n1 * n2)

        print('{:.1f} x {:.1f} = {:.1f} '.format(n1, n2, mult))

    elif(opcao == '4'):
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))

        div = (n1 / n2)

        print('{:.1f} ÷ {:.1f} = {:.1f} '.format(n1, n2, div))

    
    elif(opcao == '0'):
        print('Até logo!')
        break

    else:
        print('Opção inválida. Tente novamente')
