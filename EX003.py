# Função metragem_limpeza

def metragem_limpeza():
    print('-------- Menu 1 de 3 - Metragem --------')
    while True:
        try:
            metrageml = int(input('Entre com a metragem da casa:'))
            if (30 <= metrageml  < 300):
                return 60 + metrageml * 0.3
            elif (300 <= metrageml < 700):
                return 120 + metrageml * 0.5
            else:
                print('Não aceitamos casas menores que 30m² ou maior que 700m²')
                continue
        except ValueError:
            print('Pare de digitar valores não inteiros')




# Função tipo_limpeza

def tipo_limpeza():
    print('-------- Menu 2 de 3 - Tipo de Limpeza --------')
    while True:
        tipol = input('Entre com o tipo de limpeza: \n'+
                      'B - Básica - Indicada para sujeiras semanais ou quinzenais\n'+
                      'C - Completa (30% a mais) - Indicada para sujeiras antigas e/ou não rotineiras \n'
                      '>>')
        tipol = tipol.upper()
        tipol = tipol.strip()
        if tipol == 'B':
            return 1.00
        elif tipol == 'C':
            return 1.30
        else:
            print('Opção inválida !')
            continue


# Função adicional_limpeza

def adicional_limpeza():
    print('-------- Menu 3 de 3 - Adicional --------')
    acumulador = 0
    while True:
        adicionall = input('Deseja algum adicional ? \n'+
                           '0 - Não desejo mais nada(encerrar)\n'+
                           '1 - Passar 10 peças de roupas - R$ 10,00\n'+
                           '2 - Limpeza de 1 Forno/Micro-ondas - R$ 12,00\n'+
                           '3 - Limpeza de 1 Geladeira/Freezer - R$ 20,00\n'+
                           '>>')
        if adicionall == '0':
            return acumulador
        elif adicionall == '1':
            acumulador = acumulador + 10
            continue
        elif adicionall == '2':
            acumulador = acumulador + 12
            continue
        elif adicionall == '3':
            acumulador = acumulador + 20
            continue
        else:
            print('Adicional invalido')




# Main
print('-------- Bem-vindo ao Programa de Serviços de Limpeza do Luis Felipe --------')
metragem = metragem_limpeza()
tipo = tipo_limpeza()
adicional = adicional_limpeza()
total = metragem * tipo + adicional
print('TOTAL: R$ {:.2f} (metragem: {:.2f} * tipo: {:.2f} + adicional: {:.2f})'.format(total,metragem,tipo,adicional))