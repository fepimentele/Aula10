print('=== Cálculo de Produtividade ===')

try: 
    total_produzido = float(input('Valor total da venda: '))
    funcionarios = int(input('total de Funcinários: '))

    media_por_funcionario = total_produzido / funcionarios
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
#except (ValueError, TypeError):
except ValueError:
    print('Informe um número.')
except ZeroDivisionError:
    print('Funcionário não pode ser zero.')
# Se não der erro, executa o else.
else: 
    print(f'Média por funcionário: {media_por_funcionario:.2f}')
finally:
    print('Programa finalizado.')