#exercicio 1
from random import randint
def rolar_dados(n):
    i = 0
    rolagem = []
    for i in range(n):
        rolagem.append(randint(1,6))
    return rolagem

#exercicio 2
def guardar_dado(rolados, guardados, indice):
    guardados.append(rolados[indice])
    rolados.pop(indice)
    return [rolados, guardados]

#exercicio 3
def remover_dado(rolados, guardados, indice_remover):
    rolados.append(guardados[indice_remover])
    guardados.pop(indice_remover)
    return [rolados, guardados]