# Simulação de Caixa Eletrônico.

saldo = 1000

print('=== Caixa Eletrônico ===')
print(f'Saldo Inicial: {saldo:.2f}')

try: 
    saque = float(input('Valor que deseja sacar: R$ '))

    
except ValueError:
    print('Valor Inválido.')
except KeyboardInterrupt:
    print('Programa encerrado pelo o usuário.')
else:
    if saque > saldo:
        print('Saldo Insuficiente.')
    elif saque <= 0:
        print('Saque precisa ser maior que 0')
    else:
        saldo = saque 
        print('\nSaque realizado com sucesso')
        print(f'Saldo em conta R$ {saldo:.2}')
finally:
    print('Operação realizada')

print('Programa encerrado.')