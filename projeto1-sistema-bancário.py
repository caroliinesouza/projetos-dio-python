menu = ''' Menu:
[1] Depósito
[2] Saque
[3] Extrato
[4] Sair

'''
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    escolha = input(menu)

    if escolha == '1':
        valor = float(input('Valor a ser depositado: '))
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'

    elif escolha == '2':
        valor_saque = float(input('Valor a ser sacado: '))
        
        if valor_saque > saldo:
          print('Não foi possível sacar o valor por falta de saldo.')

        elif numero_saques >= LIMITE_SAQUES:
          print('Numero de saques excedido')

        elif valor_saque > limite:
          print('Limite de saque excedido')

        elif valor_saque > 0:
          saldo -= valor_saque
          extrato += f' Saque: R$ {valor_saque:.2f}\n'
          numero_saques += 1

    elif escolha == '3':
        print('Extrato:\n')
        print(extrato)
        print(f'Saldo: {saldo}')

    elif escolha == '4':
        break

    else:
        print('Operação inválida! Selecione um valor do menu')
