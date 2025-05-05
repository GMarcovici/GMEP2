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

#exercicio 4
def calcula_pontos_regra_simples(rolados):
    pontos = {}
    pontos[1]= 0
    pontos[2]= 0
    pontos[3]= 0
    pontos[4]= 0
    pontos[5]= 0
    pontos[6]= 0
    for num in rolados:
        pontos[num]+=num
    return pontos

#exercicio 5
def calcula_pontos_soma(rolados):
    soma = 0
    for num in rolados:
        soma += num
    return soma