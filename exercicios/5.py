"""
Exercício 5: Funções e Modularização
Objetivo: Treinar suas habilidades em criar e usar funções.
Descrição: Escreva um programa que calcule o fatorial de um número usando uma função.

Tempo inicio: 20:40
Tempo: 20:46
"""

def calcular_fatorial(num):
    f = 1 # começa do 1
    i = 2 # itera do 2 pois fatorial de 1 é 1, e do 2 é 2
    while i <= num:
        f *= i
        i += 1
    return f
print(calcular_fatorial(7))
