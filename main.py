# Informações dos alunos
#Pedro Loureiro Morone Branco Volpe           TIA:42131936
#Oliver Kieran Galvão McCormack               TIA:42122058
#Turma: 02D

dados = []
idade = []
vazio = ''
arquivo = open('SUS-Covid19.txt','r')
pessoas = -1

while True: 
    linha = arquivo.readline()
    if linha == vazio:
        break
    else:
        linha = linha.rstrip()
        dados.append(linha)
    pessoas += 1

def sexo():
    global homi
    global muie
    homi = 0
    muie = 0
    for i in range(len(dados)):
        info = dados[i].split(';')
        if "Masculino" in info[5]:
            homi += 1
        elif "Feminino" in info[5]:
            muie += 1
    return homi, muie
    
def testePositivo():
    global positivos
    global positivos_h
    global positivos_m
    positivos = 0
    positivos_h = 0
    positivos_m = 0
    for p in range(len(dados)):
        info = dados[p].split(';')
        if "Positivo" in info:
            positivos += 1
            if "Masculino" in info:
                positivos_h += 1
            elif "Feminino" in info:
                positivos_m += 1
    return positivos, positivos_h, positivos_m

def tipoToeste():
    rt = 0
    tr = 0
    for i in range(len(dados)):
        info = dados[i].split(';')
        if 'RT-PCR' == info[3]:
            rt += 1
        elif 'TESTE RÁPIDO - ANTICORPO' == info[3]:
            tr += 1
    return rt , tr

def sintomaTotal():
    assin = 0
    febre = 0
    cabeça = 0
    garganta = 0
    for i in range(len(dados)):
        info = dados[i].split(';')
        if 'Assintomático' == info[0]:
            assin += 1
        elif 'Febre' == info[0]:
            febre +=1 
        elif 'Dor de Cabeça' == info[0]:
            cabeça += 1
        elif 'Dor de Garganta' == info[0]:
            garganta += 1
    return assin, febre, cabeça, garganta

def acima_50():
    m = 0
    h = 0 
    for j in range(51,101):
        idade.append(str(j))
    for i in range(1, len(dados)):
        info = dados[i].split(';')
        if 'Assintomático' == info[0]:
            if info[8] in idade:
                if "Masculino" in info[5]:
                    h += 1
                elif "Feminino" in info[5]:
                    m += 1
    return m,h
    
def jovens():
    jo = 0 
    for j in range(1,20):
        idade.append(str(j))
    for i in range(len(dados)):
        info = dados[i].split(';')
        if info[8] in idade and info[0] != "Assintomático":
            jo += 1 
    return jo 

def cidade():
    sp = 0
    drac = 0
    bau = 0 
    for j in range(51,101):
        idade.append(str(j))

    for i in range(len(dados)):
        info = dados[i].split(';')
        if info[0] != "Assintomático":
            if info[7] == 'São Paulo':
                sp += 1
            elif info[7] == 'Dracena':
                if info[5] == 'Feminino':
                    drac += 1
            elif info[7] == 'Bauru':
                if info[5] == "Masculino" and info[8] in idade:
                    bau += 1
    return sp, drac, bau


def main(): 

    genero_m, genero_h = sexo()
    positivo, positivo_h, positivo_m = testePositivo()
    rt_pcr, teste_rapido = tipoToeste()
    assin, febre, cabeça, garganta = sintomaTotal()
    m, h = acima_50()
    
    jo = jovens()
    sp, drac, bau = cidade()

    print(f'A quantidade de pessoas que fizeram o teste foi de: {pessoas}')
    print(f'Quantidade de pessoas do sexo masculino: {genero_h} ({((genero_h*100)/pessoas):.2f})%')
    print(f'Quantidade de pessoas do sexo masculino: {genero_m} ({((genero_m*100)/pessoas):.2f}%)')
    print(f'A quantidade de pessoas que testaram positivo: {positivo}')
    print(f'A quantidade de homens que testaream positivo foi de: {positivo_h} ({((positivo_h*100)/pessoas):.2f}%)')
    print(f'A quantidade de homens que testaream positivo foi de: {positivo_m} ({((positivo_m*100)/pessoas):.2f}%)')
    print(f'Quantidade de pessoas que fizeram o teste do tipo “RT-PCR”: {rt_pcr} ({((rt_pcr*100)/pessoas):.2f}%)')
    print(f'Quantidade de pessoas que fizeram o teste do “teste rápido – anticorpo”: {teste_rapido} ({((teste_rapido*100)/pessoas):.2f}%)')
    print(f'Quantidade de pessoas assintomáticas: {assin} ({((assin*100)/pessoas):.2f}%)')
    print(f'Quantidade de pessoas que relataram ter sentido febre: {febre} ({((febre*100)/pessoas):.2f}%)')
    print(f'Quantidade de pessoas que relataram ter sentido dor de cabeça:{cabeça} ({((cabeça*100)/pessoas):.2f}%)')
    print(f'Quantidade de pessoas que relataram ter sentido dor de garganta: {garganta} ({((garganta*100)/pessoas):.2f}%)')
    print(f'Quantidade de mulheres, acima de 50 anos, assintomáticas: {m} ({((m*100)/pessoas):.2f}%)')
    print(f'Quantidade de homens, acima de 50 anos, assintomáticos:{h} ({((h*100)/pessoas):.2f}%)')
    print(f'Quantidade de pessoas com menos de 20 anos sintomáticos: {jo} ({((jo*100)/pessoas):.2f}%)')
    print(f'Quantidade de sintomáticos na cidade de São Paulo: {sp} ({((sp*100)//pessoas):.2f}%)')
    print(f'Quantidade de mulheres sintomáticas na cidade de Dracena: {drac} ({((drac*100)/pessoas):.2f}%)')
    print(f'Quantidade de sintomáticos na cidade de São Paulo: {bau} ({((bau*100)/pessoas):.2f}%)')

main()

arquivo.close()