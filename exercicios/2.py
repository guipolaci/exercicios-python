"""
Exercício 2: Loops e Listas
Objetivo: Treinar suas habilidades com loops e manipulação de listas.
Descrição: Escreva um programa que some todos os números em uma lista.
Tarefas:
Crie uma lista de números.
Use um loop para somar todos os números na lista.
Imprima o total.

Tempo inicio: 20:22
Tempo: 20:23
"""
numeros = [1, 2, 3, 4, 5]
soma = 0
for n in numeros:
    soma += n

print(f'A soma dos números dessa lista {numeros} é {soma}')

