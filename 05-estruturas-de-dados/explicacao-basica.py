# criando listas
print('Criando listas'.center(40,'-'))
frutas = ['laranja', 'maça', 'uva']
print(frutas)

letras = list('python')
print(letras)

numeros = list(range(10))
print(numeros)

# Operações básicas
print('Operações básicas'.center(40,'-'))

print(letras[1:3])  # saída: index 1 e 2
print(letras[::-1])

# Função enumerate
print('Função enumerate'.center(40,'-'))

flores = ['tulipa','rosa','azaleia','kalanchoe']
for index, flor in enumerate(flores):
    print(f'{index+1} - {flor}')

# Métodos
print('Métodos'.center(40,'-'))

lista = [1,0,209,67,53,90,4876]

lista.append(3)
print(f'Incluindo um novo objeto na lista: {lista}')

lista.extend([1,467,'oi'])
print(f'Incluindo multiplos objetos na lista: {lista}')

print(f'Remove o ultimo objeto da lista: {lista.pop()}')

print(f'Conta quantas vezes aparece o objeto na lista: {lista.count(1)}')

print(f'Limpa a lista: {lista.clear()}')

lista_dois = ['oi','estrela','pijama','casa','paralelepipedo','abelha']
lista_dois.sort()
print(f'Ordena a lista: {lista_dois}')

lista_dois.sort(key=lambda x: len(x), reverse=True)
print(f'Ordena a lista pelo tamanho de cada objto e de trás pra frente: {lista_dois}')
