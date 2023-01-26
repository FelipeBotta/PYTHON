print('Bem-vindo a Sorveteria do Luis Felipe')
print('------------------------------CARDÁPIO------------------------------')
print('|CÓDIGO | DESCRIÇÃO            | TAMANHO P | TAMANHO M | TAMANHO G | ')
print('|TR     | Sabores Tradicionais | R$ 6,00   | R$ 10,00  | R$ 18,00  |')
print('|ES     | Sabores Especiais    | R$ 7,00   | R$ 12,00  | R$ 21,00  |')
print('|PR     | Sabores Premium      | R$ 8,00   | R$ 14,00  | R$ 24,00  |')
print('--------------------------------------------------------------------')

acumulador = 0
while True:
    tamanho = input('Entre com o tamanho do sorvete desejado (P/M/G):')
    if tamanho != 'P' and tamanho != 'M' and tamanho != 'G':
        print('Opção Inválida !')
        continue

    codigo = input('Entre com o código do sorvete desejado (TR/ES/PR):')
    if codigo != 'TR' and codigo != 'ES' and codigo != 'PR':
        print('Opção Inválida !')
        continue

    elif codigo == 'TR' and tamanho == 'P':
        print('Você escolheu um Sorvete Tradicional de R$ 6,00.')
        acumulador = acumulador + 6
        print(acumulador)

    elif codigo == 'TR' and tamanho == 'M':
        print('Você escolheu um Sorvete Tradicional de R$ 10,00.')
        acumulador = acumulador + 10
        print(acumulador)

    elif codigo == 'TR' and tamanho == 'G':
        print('Você escolheu um Sorvete Tradicional de R$ 18,00.')
        acumulador = acumulador + 18
        print(acumulador)

    elif codigo == 'ES' and tamanho == 'P':
        print('Você escolheu um Sorvete Especial de R$ 7,00.')
        acumulador = acumulador + 7
        print(acumulador)

    elif codigo == 'ES' and tamanho == 'M':
        print('Você escolheu um Sorvete Especial de R$ 12,00.')
        acumulador = acumulador + 12
        print(acumulador)

    elif codigo == 'ES' and tamanho == 'G':
        print('Você escolheu um Sorvete Especial de R$ 18,00.')
        acumulador = acumulador + 18
        print(acumulador)

    elif codigo == 'PR' and tamanho == 'P':
        print('Você escolheu um Sorvete Premium de R$ 8,00.')
        acumulador = acumulador + 8
        print(acumulador)

    elif codigo == 'PR' and tamanho == 'M':
        print('Você escolheu um Sorvete Premium de R$ 14,00.')
        acumulador = acumulador + 14
        print(acumulador)

    elif codigo == 'PR' and tamanho == 'G':
        print('Você escolheu um Sorvete Premium de R$ 24,00.')
        acumulador = acumulador + 24
        print(acumulador)

    continuar_pedido = input('Deseja pedir algo mais (S/N) ?:')
    if continuar_pedido == 'S':
        continue
    else:
        print('O valor total a ser pago: R${:.2f}'.format(acumulador))
        break