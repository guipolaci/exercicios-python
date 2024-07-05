"""
Exercício 3: Manipulação de Strings
Objetivo: Treinar suas habilidades em manipulação de strings.
Descrição: Escreva um programa que conte o número de vogais em uma string fornecida pelo usuário.
Tarefas:
Peça ao usuário para inserir uma string.
Conte o número de vogais na string.
Imprima o total de vogais.

Tempo inicio: 20:24
Tempo: 20:26

"""

frase = str(input("Digite uma frase: "))
vogais = 0
for l in frase:
    if l in 'aeiou':
        vogais += 1
print(f'A frase "{frase}" tem {vogais} vogais')
