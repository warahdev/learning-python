# 1. Operadores aritméticos

a, b = 8, 7
print(f'Soma: {a + b}.')
print(f'Sustração: {a - b}.')
print(f'Multiplicação: {a * b}.')
print(f'Divisão: {a / b}.')
print(f'Divisão inteira: {a // b}.')
print(f'Exponenciação: {a ** b}.')
print(f'Módulo: {a % b}.')  # resto da divisão

print("".center(40,'-'))
# 2. Operadores de comparação + Operadores lógicos

limite = 1000
saque = 300
saldo = 20

print(limite > saque and saldo > saque)  # "1000 > 300" AND "20 > 300"? Não

print("".center(40,'-'))
# 4. Operadores de atribuição

saldo = 100
saldo -= 2  # 100 - 2
print(saldo)

saldo *= 2  #98 * 2
print(saldo)

saldo %= 2  # 196 % 2
print(saldo)


print("".center(40,'-'))
# 5. Operadores de identidades 

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # comparação de valor
print(a is b)  # comparação de identidade
print(a is c)  # mesma instância
print(a is not b)