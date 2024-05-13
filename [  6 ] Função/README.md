<h1 align="center"> Função <br>
  <a href="../[  5 ] Dicionários/"><img src="https://img.shields.io/badge/Anterior-Dicionários-215a36" alt="Anterior"></a>
  <a href="../[  7 ] Seminário - Banco de Dados de Sequências de Proteínas/"><img src="https://img.shields.io/badge/Próximo-Seminário-215a36" alt="Próximo"></a>
</h1> 

# Exercícios:
## 1. Escreva uma função chamada fatorial para calcular o fatorial de um número inteiro.
~~~python
def fatorial (n):
    if (n == 0): return 1
    elif (n > 0): return n * fatorial(n-1)
~~~

## 2. Escreva uma função chamada maxnum que retorne o maior número de um conjunto de números. Utilize empacotamento para fazer a função.
~~~python
def maxnum (*a):
    maior = a[0]
    for i in a[1:]:
        if (maior < i): maior = i
    return maior
~~~

## 3. Escreva uma função que receba dois números e retorne True se o primeiro número for múltiplo do segundo.
~~~python
def multiplo (a, b):
    if (a % b == 0): True
    else: False
~~~

## 4. Crie uma função chamada "calculadora" que recebe três parâmetros: dois números e uma operação matemática (+, -, *, /). A função deve retornar o resultado da operação.
~~~python
def calculadora (a, b, op):
    if (op ='+'): return a + b
    elif (op ='-'): return a - b
    elif (op ='*'): return a * b
    elif (op ='/'): return a / b
~~~

## 5. Crie uma função chamada "maior_palavra" que recebe uma lista de palavras como parâmetro e retorna a maior palavra dessa lista.
~~~python
def maior_palavra (lista):
    maior_palavra = lista[0]
    for i in lista[1:]:
        if (len(i) > len(maior_palavra)): maior_palavra = i
    return maior_palavra
~~~

## 6. Implemente uma função chamada "soma_recursiva" que recebe um número inteiro positivo como parâmetro e retorna a soma de todos os números inteiros de 1 até esse número, utilizando recursividade.
~~~python
def soma_recursiva (a):
    if (a == 1): 
        print('1 ', sep='')
        return 1
    else: 
        return 1 + soma_recursiva(a - 1)
        print('+ 1', sep='')
~~~

## 7. Crie uma função na qual calcula o valor do seno a partir da série de Taylor (50 primeiros termos) e cosseno a partir da seguinte identidade a baixo. Obs: Fazer a serie utilizando for e utilizar a função fatorial desenvolvida no exercício 1.
~~~
def seno_coseno (x):
    seno = 0
    for i in range (50)
        impar = 2i + 1
        seno += (x**impar)/fatorial(impar)
    cosseno = (1 - seno**2)**(1/2)
    return seno, cosseno
~~~

