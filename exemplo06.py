# Calcula média de notas
# Não sabemos quantos alunos, mas todos terão 4 notas sempre

def calcula_media(lista_notas):
    tot = sum(lista_notas)
    med = tot / len(lista_notas)
    return tot, med 


contador = 1
#resposta = "S"
while True:
    print(f'Aluno {contador}')
    aluno = input('Nome do aluno: ')

    notas = []
    try:
        for i in range(4):
            nota = float(input('Informe a nota: '))
            notas.append(nota)

    except ValueError:
        print('Erro: Informe apenas valores válidos!')
    else:
        total, media = calcula_media(notas)

        print('\nResultado')
        print(f'Aluno: {aluno}')
        print(f'Total de Pontos: {total}')
        print(f'Média: {media:.2}')
    
    finally:
        print('Processo encerrado para o aluno')

    opcao = input('Deseja calcular a nota de outro aluno ?').strip().upper()
    if opcao != 'S':
        break