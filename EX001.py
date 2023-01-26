print('Bem vindo a loja do Luis Felipe !')
valor = float(input('Entre com o valor do produto:'))
qtd = int(input('Entre com a quantidade desejada:'))
subtotal = valor * qtd #subtotal(valor sem frete)
print('O valor sem frete foi: R$ %.2f'%(subtotal))
if qtd < 11:
    embalagem = 30
    preco = subtotal+embalagem
elif (11 <= qtd < 101):
    embalagem = 60
    preco = subtotal+embalagem
elif (101 <= qtd < 1001):
    embalagem = 120
    preco = subtotal+embalagem
elif (1001 <= qtd):
    embalagem = 240
    preco = subtotal+embalagem
else:
    print('Você digitou algo errado, revise os dados !')

print('O valor com frete foi: R$ %.2f (Frete de R$ %.2f)'%(preco,embalagem))
