menu = '''
Escolha qual exercicio deseja executar:

1 - Reajuste salarial
2 - Média de aprovação
3 - 
4 - 
5 - 
6 - 

==> '''


while True:
    opcao = input(menu)

    if opcao =='1':
        salario = int(input('Informe seu salario em R$: '))
        ajuste = 0.1

        ajuste_salarial = salario * (1+ajuste)
        print(f'Seu ajuste salarial será de: R${ajuste_salarial:.2f}')

    elif opcao == '2':
        nota1 = float(input('informe sua primeira nota: '))
        nota2 = float(input('informe sua segunda nota: '))
        frequencia = float(input('Informe sua frequência no curso (%): '))
        media = (nota1 + nota2) / 2

        aprovado = (media >= 7.0) and (frequencia >= 0.75)
        print(f'Aprovado? {aprovado}')

    else:
        print('Saindo...')
        break