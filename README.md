 # Caso COH-PIAH
![Botão de Versão](https://img.shields.io/badge/Version-310-blue)   ![CSS](https://img.shields.io/badge/Python-3-blue) 

![Programa COH-PIAH](https://github.com/joao-lucasilva/Caso-COH-PIAH/blob/master/assets/scrennshot.JPG?raw=true)

Tabela de conteúdos
=================
   * [Sobre](#sobre)
   * [Como funciona](#como-funciona)
   * [Como utilizar](#como-utilizar)
   * [Tecnologias](#tecnologias)
   * [Autores](#autores)
 
## Sobre

Este projeto foi desenvolvido como exercício final do curso Introdução a Ciência da Computação com Python, ministrado pela Universidade de São Paulo através da plataforma Coursera.

O COH-PIAH é uma doença rara e altamente contagiosa, ela faz com que indivíduos contaminados produzam, involuntariamente, textos muito semelhantes aos de outras pessoas. Uma epidemia desta doença se espalhou pela Universidade de Pasárgada, e o programa detecta quais alunos estão contaminados através da  Similaridades entre textos.

## Como Funciona
Diferentes pessoas possuem diferentes estilos de escrita, assim é possível identificar aspectos que funcionam como uma “assinatura” do autor  de um texto e,  detectar se dois textos dados foram escritos por uma mesma pessoa. Essa assinatura é utilizada para diagnosticar a grave doença COH-PIAH.

O programa utiliza uma assinatura contaminada padrão e uma lista de textos, calcula os valores dos diferentes traços linguísticos desses textos para compará-los com a assinatura dada. Após isto verifica o grau de similaridade entre a assinatura contaminada e assinatura de cada texto da lista, com base neste calculo o programa detecta qual autor de qual texto está infectado com COH-PIAH.

Os traços linguísticos são:
-   Tamanho médio de palavra: Média simples do número de caracteres por palavra.
-   Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
-   Razão Hapax Legomana: Número de palavras utilizadas uma única vez dividido pelo número total de palavras.
-   Tamanho médio de sentença: Média simples do número de caracteres por sentença.
-   Complexidade de sentença: Média simples do número de frases por sentença.
-   Tamanho médio de frase: Média simples do número de caracteres por frase.

## Como Utilizar
Clone este repositório:
> git clone https://github.com/joao-lucasilva/Caso-COH-PIAH.git

Execute o arquivo COH-PIAH em seu ambiente Python:
> python COH-PIAH.py
## Tecnologias
Neste projeto foi utilizado:
	- [Python 3](https://www.python.org/) 
## Autor
Desenvolvido por João Lucas da Silva.
Entre em contato comigo:
 [![Linkedin Badge](https://img.shields.io/badge/-JoaoLucas-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/tgmarinho/)]([https://www.linkedin.com/in/joaolucassilva-812819165/](https://www.linkedin.com/in/joaolucassilva-812819165/)) | [![Gmail Badge](https://img.shields.io/badge/-joao.lsilva1198@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:tgmarinho@gmail.com)](mailto:joao.lsilva1198@gmail.com)
