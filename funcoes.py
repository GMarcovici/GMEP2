#exercicio 1
from random import randint
def rolar_dados(n):
    i = 0
    rolagem = []
    for i in range(n):
        rolagem.append(randint(1,6))
    return rolagem