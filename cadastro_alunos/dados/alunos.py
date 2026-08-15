"""
Módulo responsável por guardar os alunos cadastrados.

Como é apenas uma lista Python comum, os dados existem enquanto o
programa estiver rodando (em memória). Se quiser que os dados
sobrevivam ao fechar o app, dá pra trocar isso depois por um arquivo
JSON ou um banco de dados — mas para o exercício da aula, uma lista
já resolve e deixa o foco no Flet.
"""

# Cada aluno é um dicionário: {"nome": ..., "idade": ..., "curso": ...}
lista_alunos = []


def adicionar_aluno(nome: str, idade: str, curso: str):
    lista_alunos.append({"nome": nome, "idade": idade, "curso": curso})


def remover_aluno(indice: int):
    if 0 <= indice < len(lista_alunos):
        lista_alunos.pop(indice)
