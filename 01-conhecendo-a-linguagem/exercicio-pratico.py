menu = '''
Escolha qual exercicio deseja executar:

1 - Contador de vogais e consoantes
2 - Remove Caractere
3 - Palíndromo
4 - Par ou ímpar
5 - Ano bissexto
6 - Sair

==> '''


while True:
    opcao = input(menu)

    # 1 - Contador de vogais e consoantes:
    if opcao == '1':
        vogais = 'aeiou'  # Determinando quais são as vogais
        qtd_vogais = 0  # quantidade inicial de vogais
        qtd_consoantes = 0  # quantidade inicial de consoantes
        palavra = input('Informe uma palavra para contar as vogais e consoantes: ')

        for caractere in palavra:
            if caractere in vogais:
                qtd_vogais += 1
            if caractere not in vogais:
                qtd_consoantes += 1
            
        print(f'Quantidade de vogais: {qtd_vogais}.')
        print(f'Quantidade de consoantes: {qtd_consoantes}.')

    # 2 - Remove Caractere:
    elif opcao == '2':
        texto = input('Informe uma palavra: ')
        caracter = input('Informe o caracter que deseja remover: ')

        print(f'{texto.replace(caracter, '')}')

    # 3 - Palíndromo:
    elif opcao == '3':
        verificar = input('Informe uma palavra: ')
        palindromo = True
        if verificar != verificar[::-1]:
            palindromo = False
        
        if palindromo:
            print('A palavra é um palíndromo.')
        else:
            print('A palavra não é um palíndromo.')
    
    # 4 - Par ou ímpar:
    elif opcao == '4':
        numero = int(input('Informe um número inteiro: '))
        if (numero % 2) == 0:
            print('O número é par.')
        else:
            print('O número é ímpar.')
    
    # 5 - Ano bissexto:
    elif opcao == '5':
        ano = int(input('Informe um ano: '))
        bissexto = True
        if (ano % 4) != 0:  # se for não for divisível por 4, não é ano bissexto
            bissexto = False

        if (ano % 400 != 0) and (ano % 100 == 0):  # se for não for divisível por 400 AND for divisível por 100, não é ano bissexto
            bissexto = False

        if bissexto:
            print(F'O ano {ano} é bissexto.')
        else:
            print(f'O ano {ano} não é bissexto.')

    # 6 - Sair:
    else:
        print('Saindo...')
        break
            
    