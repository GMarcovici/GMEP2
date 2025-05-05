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

#exercicio 7
def calcula_pontos_sequencia_alta(dados):
    for num in dados:
        if num == 1 or num ==2:
            if num+1 in dados:
                if num + 2 in dados:
                    if num + 3 in dados:
                        if num+4 in dados:
                            return 30
    return 0

#exercicio 8
def calcula_pontos_full_house(rolados):
    dic = {}
    for num in rolados:
        if num not in dic:
            dic[num]=1
        else:
            dic[num]+=1
    
    pontuacao3 = 0
    pontuacao2 = 0
    for dado, qnt in dic.items():
        if qnt==3:
            pontuacao3 = int(dado)*3
        if qnt==2:
            pontuacao2 = int(dado)*2
    
    if pontuacao3 != 0 and pontuacao2!=0:
        return pontuacao3+pontuacao2
    else:
        return 0
    
#exercicio 9
def calcula_pontos_quadra(rolados):
    dic = {}
    for num in rolados:
        if num not in dic:
            dic[num]=1
        else:
            dic[num]+=1
        
    resultado = 0
    for dado in dic:
        if dic[dado]>=4:
            for dice, qnt in dic.items():
                resultado += dice*qnt
            return resultado
    return 0

#exercicio 10
def calcula_pontos_quina(rolados):
    dic = {}
    for num in rolados:
        if num not in dic:
            dic[num]=1
        else:
            dic[num]+=1
        
    resultado = 0
    for dado in dic:
        if dic[dado]>=5:
            return 50
    return 0

#exercicio 11
def calcula_pontos_regra_avancada(rolados):
    dic = {}
    dic['cinco_iguais'] = calcula_pontos_quina(rolados)
    dic['full_house']= calcula_pontos_full_house(rolados)
    dic['quadra']= calcula_pontos_quadra(rolados)
    dic['sem_combinacao']=calcula_pontos_soma(rolados)
    dic['sequencia_alta']= calcula_pontos_sequencia_alta(rolados)
    dic['sequencia_baixa']= calcula_pontos_sequencia_baixa(rolados)
    return dic

#exercicio 12
def faz_jogada(dados, categoria, cartela):
    simples=calcula_pontos_regra_simples(dados)
    avancado=calcula_pontos_regra_avancada(dados)
    
    for type, points in avancado.items():
        if type==categoria:
            cartela['regra_avancada'][type]=points
    
    for tipo, pontos in simples.items():
        if str(tipo)==categoria:
            cartela['regra_simples'][tipo]=pontos
    return cartela

#exercicio 13
def imprime_cartela(cartela):
    print("Cartela de Pontos:")
    print("-"*25)    
    for i in range(1, 7):
        filler = " " * (15 - len(str(i)))
        if cartela['regra_simples'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_simples'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    for i in cartela['regra_avancada'].keys():
        filler = " " * (15 - len(str(i)))
        if cartela['regra_avancada'][i] != -1:
            print(f"| {i}: {filler}| {cartela['regra_avancada'][i]:02} |")
        else:
            print(f"| {i}: {filler}|    |")
    print("-"*25)
