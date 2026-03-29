# Estrutura condicional
    # Decisões
    # - Executa o bloco de código, se a condição for verdadeira, o bloco de código dentro da instrução 'if' será executado, se a condição for falsa, o bloco de código será ignorado.
temperatura = float(input('Qual é a temperatura atual em Celsius? '))

if temperatura <= 10:
    print('Nossa! Está muito frio, cuidado para não se congelar.')

elif temperatura <= 24:
    print('Bem relativo se está um clima bom, seria meio termo, não?')

elif temperatura <= 30:
    print('Hora de usar roupas leves e se hidratar bastante.')

else:
    print('Está bastante quente, não esqueça o protetor solar ao sair de casa.') 


    # Para casos multiplos
	# - Usada para executar diferentes ações com base em diferentes condições.
print('Estrutura condicional - MATCH'.center(40,'-'))
mes = input('Informe o número do mês atual: ')

match mes:
    case '12' | '1' | '2':
        print("É Verão! (Mas em Curitiba pode chover a qualquer hora 🌦️)")
        
    case '6' | '7' | '8':
        print("É Inverno! Hora de tirar o pinhão e o casaco de lã do armário ❄️")
        
    case '3' | '4' | '5':
        print("Outono: As folhas caem e o clima esfria.")
        
    case _:
        print("Primavera: A cidade fica cheia de flores! 🌸")


# Estrutura de repetição
#   For: Utilizada para iterar sobre sequências (listas, tuplas, strings, etc).
print('Estrutura de repetição - FOR'.center(40,'-'))

frutas = ['maçã', 'banana', 'morango', 'limão']
for fruta in frutas:
	print(fruta)

#   While: Utilizada para repetir um bloco de código enquanto uma condição for verdadeira.
print('Estrutura de repetição - WHILE'.center(40,'-'))

numero = 7
chute = int(input('Estou pensando em um número inteiro entre 0 e 10, tente adivinhar qual é o número: '))

while chute != numero:
    chute = int(input('Errou! Tente de novo: '))

print(f'Isso mesmo! Estava pensando no número {numero}.')


# Função range()
print('Função range()'.center(40,'-'))

for x in range(3,9,2):  # ou seja, o range será de 3,4,5,6,7,8 (3,9) de 2 em 2 (step 2)
    print(x)


# Operadpr tenário
#   - Útil para decisões simples e rápidas dentro de atribuições ou expressões.
print('Operadpr tenário'.center(40,'-'))

a, b = 5, 7
if a > b: print(f'{a} é maior do que {b}.')

valor_da_compra = 150
frete = 0 if valor_da_compra >= 100 else 15.00

print(f'O valor do frete será de R$ {frete:.2f}.')


# Break e continue
#   - Com a declaração "break" podemos parar o loop mesmo que a condição no while seja verdadeira.
#   - Com a declaração "continue" podemos parar a iteração atual e continuar com a próxima.
print('Break e continue'.center(40,'-'))

tentativa, limite = 0, 5

while tentativa <= limite:
    senha = input('Digite sua senha: ')
    tentativa += 1

    if senha == '':
        print('Campo vazio.')
        continue

    if senha == 'Python123':
        print('Senha correta! Seja bem-vindo(a).')
        break
    print(f'Senha incorreta! Você possui {limite - tentativa} tentativa(s) restates.') 
else:
    print('Limite de tentativas excedido. Acesso bloqueado.')
