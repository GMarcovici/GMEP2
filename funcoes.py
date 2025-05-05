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

#exercicio 6
def calcula_pontos_sequencia_baixa(dados):
    for num in dados:
        if num == 1 or num ==2:
            if num+1 in dados:
                if num + 2 in dados:
                    if num + 3 in dados:
                        return 15
        if num == 5 or num==6:
            if num-1 in dados:
                if num - 2 in dados:
                    if num - 3 in dados:
                        return 15
    return 0