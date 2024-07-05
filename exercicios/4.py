"""
Exercício 4: Leitura de Arquivo e Filtragem
Objetivo: Treinar suas habilidades em leitura de arquivos e filtragem de dados.
Descrição: Escreva um programa que leia um arquivo txt e remova todos os caracteres específicos
(ex.: '!'), salvando o resultado em um novo arquivo.

Tempo inicio: 20:30
Tempo: 20:38

Dificuldades:

Tive que pesquisar como manipular arquivos em Python

"""
caracteres = ["?", "!"]
arquivo = open("arquivoAntigo.txt")
txt = arquivo.read()
arquivo.close()
for c in caracteres:
    txt = txt.replace(c, '')
novoArquivo = open("arquivoNovo.txt", 'w')
novoArquivo.write(txt)
novoArquivo.close()

