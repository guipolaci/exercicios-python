"""
Exercício 1: Condicionais Simples
Objetivo: Treinar suas habilidades com condicionais básicas.
Descrição: Escreva um programa que verifique se um número é positivo, negativo ou zero.
Tarefas:
Peça ao usuário para inserir um número.
Use condicionais para verificar se o número é positivo, negativo ou zero.
Imprima uma mensagem correspondente.

Tempo inicio: 20:19
Tempo: 20:21

"""

num = int(input("Digite um número: "))

if num > 0:
    print(f'{num} é positivo')
elif num == 0:
    print(f'Seu número é 0')
else:
    print(f'{num} é negativo')
