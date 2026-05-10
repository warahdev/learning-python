# Recursos para criar funções que aceitam um número dinâmico (indefinido) de argumentos, não é necessário fixar quantos parâmetros a função irá receber.

# args: recebe multiplos argumentos sem nome e agrupados em uma tupla ()
# kwargs: recebe muliplos argumentos nomeados e os agrupa em um dicionário {}

# Exemplo:
def montar_buque_personalizado(tamanho, *args, **kwargs):
    print(f'Criando buquê de tamanho: {tamanho}')
    print('\nFlores escolhidas:')
    for flor in args:
        print(f'  -> {flor}')
        
    print('\nEspecificações de acabamento:')
    # Se o cliente não definir uma embalagem, usamos um padrão seguro
    embalagem = kwargs.get("embalagem", "Papel Kraft clássico")
    fita = kwargs.get("fita", "Barbante rústico")
    print(f'  * Embalagem: {embalagem}')
    print(f'  * Fita/Laço: {fita}')
    
    # Se houver um cartão de mensagem, nós exibimos
    if "mensagem" in kwargs:
        print(f'  * Cartão de presente: "{kwargs["mensagem"]}"')

# Chamando a função com tudo junto:
montar_buque_personalizado(
    "Grande",  # Parâmetro posicional comum (tamanho)
    "Mini Rosas", "Gipsófilas", "Azaleias", # *args (múltiplas flores)
    # **kwargs (detalhes opcionais)
    embalagem="Papel Celofane",
    fita= "Fita de Cetim Vermelha",
    mensagem="Feliz aniversário!"
)