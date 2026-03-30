# Fatiamento de String
# - Utilizada para retornar substrings.
print('Fatiamento de String'.center(40,'-'))

texto = '123456'
print(f'Caracter de index 1 do texto {texto} é: {texto[1]}') 
print(f'Caracter de index 2 até 5 de 2 em 2 do texto {texto} é: {texto[2:5:2]}')

log = "ERRO: Falha no MAC. ERRO: Conexão perdida."
print(f"Total de erros encontrados: {log.count('ERRO')}")

posicao = log.find("MAC")
print(f"A palavra MAC começa na posição: {posicao}")

# Métodos de verificação
# - Sempre retornam um valor Booleano.
senha_fraca = 'abcd1234'
print(f'Possui apenas algarismos? {senha_fraca.isdigit()}.\nPossui apenas letras? {senha_fraca.isalpha()}.\nPossui algarismos ou letras? {senha_fraca.isalnum()}')

# Verificação de início e fim
celular = '11 - 555555555.'

print(f'O celular começa com DD 11? {celular.startswith('11')}. Termina com 99? {celular.endswith('99')}')

# Contagem e localização
trava_lingua = 'A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha.'

print(f'No trava lingua "{trava_lingua}".\nQuantas vezes aparece a palavra "râ"? {trava_lingua.count('rã')} vez(es).\nE onde ela aparece pela primeira vez? No index de número {trava_lingua.find('rã')}.')