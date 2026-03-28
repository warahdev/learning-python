menu = '''
Escolha qual exercicio deseja executar:

1 - Reajuste salarial
2 - Média de aprovação
3 - Divisão de conta e gorjeta
4 - Conversor de temperatura
5 - Intervalo numérico

==> '''


while True:
    opcao = input(menu)

    if opcao =='1':
        salario = float(input('Informe seu salario em R$: '))
        ajuste = 0.1

        ajuste_salarial = salario * (1+ajuste)
        print(f'Seu ajuste salarial será de: R${ajuste_salarial:.2f}')

    elif opcao == '2':
        nota1 = float(input('Informe sua primeira nota: '))
        nota2 = float(input('Informe sua segunda nota: '))
        frequencia = float(input('Informe sua frequência no curso (%): '))
        media = (nota1 + nota2) / 2

        aprovado = (media >= 7.0) and (frequencia >= 75)
        print(f'Aprovado? {aprovado}')

    elif opcao == '3':
        conta = float(input('Informe o valor da conta (R$): '))
        adicional_atendimento = 0.10  # 10%
        pessoas = int(input('Será divido a conta para quantas pessoas? '))
        valor_final = (conta * (1 + adicional_atendimento)) / pessoas

        print(f'O valor da conta dividido para {pessoas} pessoa(s) será de R$ {valor_final:.2f}.')

    elif opcao == '4':
        celsius = float(input('Informe a temperatura em Celsus: '))
        fahrenheit = (celsius * 1.8) + 32
        
        print(f'A temperatura em Fahrenheit é de {fahrenheit:.2f} F.')

    elif opcao == '5':
        numero = float(input('Informe um número: '))
        esta_no_intervalo = 10 <= numero <= 50  # (numero >= 10) and (numero <= 50)

        print(f'O número {numero} está entre 10 e 50? {esta_no_intervalo}.')

    else:
        print('Saindo...')
        break