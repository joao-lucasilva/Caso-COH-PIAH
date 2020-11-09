import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = diferenca_total = 0
    while i < len(as_a):
        diferenca = as_a[i] - as_b[i]
        diferenca_total += abs(diferenca)
        i += 1
    grau_similaridade = diferenca_total / 6
    return grau_similaridade

def calcula_assinatura(texto):
    sentencas = separa_sentencas(texto)
    frases = lista_frases(texto)
    palavras = lista_palavras(texto)

    qtd_caracteres = conta_caracteres(texto)

    tam_sentencas = tamanho_palavras =  0
    num_sentencas = num_palavras = 0
    
    for i in palavras:
         tamanho_palavras += len(i)
         num_palavras += 1
    tam_medio = tamanho_palavras/num_palavras
    
    n_dif_palavras = n_palavras_diferentes(palavras)
    type_token = n_dif_palavras/num_palavras

    palavras_unicas = n_palavras_unicas(palavras)
    hapax_legomana = palavras_unicas/num_palavras

    for i in sentencas:
         tam_sentencas += len(i)
         num_sentencas += 1
    tam_medio_sentencas = tam_sentencas/num_sentencas

    
    complexidade_sentenca  = len(frases)/num_sentencas

    num_caracteres = 0
    frases = lista_frases(texto)
    for i in frases:
        for j in i:
            if j != '.' or j != ',' or j != '-':
                num_caracteres += 1
    tam_medio_frases = num_caracteres/len(frases)
    
    assinatura = [tam_medio, type_token, hapax_legomana, tam_medio_sentencas,complexidade_sentenca,tam_medio_frases]
    return assinatura

def avalia_textos(textos, ass_cp):
    '''Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_sab = []
    for texto in textos:
        assinatura = calcula_assinatura(texto)
        comparacao = compara_assinatura(ass_cp, assinatura)
        lista_sab.append(comparacao)
    maior = max(lista_sab)
    return lista_sab.index(maior)

#Essas funções foram desenvolvidas por mim
def conta_caracteres(texto):
    '''Essa função recebe um texto  e retorna o número de caracteres que o mesmo possui (sem contar os caracteres qeu separam as palavras)'''
    num_caracteres = 0
    lista_palavras = separa_palavras(texto)
    for i in lista_palavras:
        for j in i:
            if j != '.' or j != ',' or j != '-':
                num_caracteres += 1
    return num_caracteres

def lista_frases(texto):
    '''Essa função recebe um texto e retorna uma lista contendo as todas as frases deste texto'''
    sentencas = separa_sentencas(texto)
    lista_frases = []
    frases = []
    for i in sentencas:
        frase = separa_frases(i)
        frases.append(frase)
    for i in frases:
      for j in i:
        lista_frases.append(j)
    return lista_frases

def lista_palavras(texto):
    '''Esta função recebe um texto e retorna uma lista contendo todas as palavras deste texto'''
    sentencas = separa_sentencas(texto)
    lista_frases = []
    palavras = []
    lista_palavras = []
    for i in sentencas:
        frases = separa_frases(i)
        lista_frases.append(frases)

    for i in lista_frases:
        for j in i:
            palavra = separa_palavras(j)
            palavras.append(palavra)
    for i in palavras:
        for j in i:
            lista_palavras.append(j)
    return lista_palavras
#Funcao principal
def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    possivel_contaminado = avalia_textos(textos, ass_cp)
    print('O autor do texto {} está infectado com COH-PIAH'.format(possivel_contaminado))

main()