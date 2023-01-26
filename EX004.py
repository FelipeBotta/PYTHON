#Variavéis Globais
lista_funcionario = []
codigo_funcionario = 0

#Função Cadastrar Funcionários
def cadastrar_funcionario(codigo):
    print('Bem-vindo ao Menu de cadastrar funcionarios')
    print('Código do Funcionário {}'.format(codigo))
    nome = input('Por favor entre com o NOME:')
    setor = input('Por favor entre com o SETOR:')
    salario = int(input('Por favor entre com o SALÁRIO (R$):'))
    dicionario_funcionario = {'codigo' : codigo,
                              'nome' : nome,
                              'setor' : setor,
                              'salario' : salario}
    lista_funcionario.append(dicionario_funcionario.copy())




#Função Consultar Funcionários
def consultar_funcionario():
    print('Bem-vindo ao Menu de consultar funcionarios')
    while True:
        menu_consultar = input('\n Escolha a opção desejada: \n'+
                           '1 - Consultar todos os funcionários \n'+
                           '2 - Consultar funcionários por ID \n'+
                           '3 - Consultar funcionários por SETOR \n'+
                           '4 - Retornar \n'+
                           '>>>')
        if menu_consultar == '1':
            print('Você escolheu a opção consultar todos os funcionários')
            for funcionario in lista_funcionario:
                for key, value in funcionario.items():
                    print('{}: {}'.format(key,value))

        elif menu_consultar == '2':
            print('Você escolheu a opção consultar funcionários por ID')
            consulta_codigo = int(input('Digite o ID do funcionário:'))
            for funcionario in lista_funcionario:
                if funcionario['codigo'] == consulta_codigo:
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))


        elif menu_consultar == '3':
            print('Você escolheu a opção consultar funcionários por SETOR')
            consulta_setor = input('Digite o SETOR do(s) funcionário(s):')
            for funcionario in lista_funcionario:
                if funcionario['setor'] == consulta_setor:
                    for key, value in funcionario.items():
                        print('{}: {}'.format(key, value))

        elif menu_consultar == '4':
            return

        else:
            print('Opção inválida !')
            continue




#Função Remover Funcionários
def remover_funcionario():
    print('Bem-vindo ao Menu de remover funcionarios')
    valor_desejado = int(input('Digite o ID do funcionário a ser removido:'))
    for funcionario in lista_funcionario:
        if funcionario['codigo'] == valor_desejado:
            lista_funcionario.remove(funcionario)
            print('Funcionário removido !')


#Inicio do Programa
print('Bem-vindo ao Controle de Funcionários do Luis Felipe')
while True:
    menu_principal = input('\nEscolha a opção desejada:\n'+
                           '1 - Cadastrar Funcionário \n'+
                           '2 - Consultar Funcionário(s) \n'+
                           '3 - Remover Funcionário \n'+
                           '4 - Sair \n'+
                           '>>>')
    if menu_principal == '1':
        codigo_funcionario = codigo_funcionario + 1
        cadastrar_funcionario(codigo_funcionario)
    elif menu_principal == '2':
        consultar_funcionario()
    elif menu_principal == '3':
        remover_funcionario()
    elif menu_principal == '4':
        break
    else:
        print('Opção inválida !')
        continue