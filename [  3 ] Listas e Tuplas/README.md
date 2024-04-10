<h1 align="center"> Listas e Tuplas <br>
  <a href="../[  2 ] Loops e Condicionais/"><img src="https://img.shields.io/badge/Anterior-Loops e Condicionais-215a36" alt="Anterior"></a>
  <a href="../[  4 ] Strings/"><img src="https://img.shields.io/badge/Próximo-Strings-215a36" alt="Próximo"></a>
</h1>

# Listas:
## | Características:
- São estruturas de dados que permitem armazenar vários valores (sem necessariamente serem do mesmo tipo) em uma única variável.
- São mutáveis, ou seja, é possível alterar, adicionar e remover elementos.
- São representadas por colchetes `[]`.

## | Criação e Acesso:
&emsp;&emsp; Para criar uma lista, basta colocar os valores entre colchetes e separá-los por vírgula.
~~~python
a = 5
lista = [1, '2', 3.0, 2*2, a] # [1, '2', 3.0, 4, 5]
~~~

&emsp;&emsp; Para acessar um elemento da lista, basta informar o índice do elemento desejado entre colchetes.
~~~python
lista = [1, 2, 3, 4, 5]
print(lista[0]) # 1, a contagem começa em 0
print(lista[-1]) # 5
~~~

&emsp;&emsp; Para alterar um elemento da lista, basta informar o índice do elemento desejado entre colchetes e atribuir um novo valor.
~~~python
lista = [1, 2, 3, 4, 5]
lista[0] = 10
print(lista) # [10, 2, 3, 4, 5]
~~~

&emsp;&emsp; Para acessar um intervalo de elementos, basta informar o índice inicial, final e o passo entre colchetes e separados por `:`.
~~~python
lista = [1, 2, 3, 4, 5]
print(lista[1:4]) # [2, 3, 4], exclui o elemento de índice fim (semelhante ao range)
print(lista[::2]) # [1, 3, 5], pega do início ao fim com passo 2
print(lista[::-1]) # [5, 4, 3, 2, 1], inverte a lista
print(lista[-1:1:-1]) # [5, 4, 3] , elementos entre o ultimo e o segundo (excluindo o segundo).
~~~

&emsp;&emsp; Para copiar uma lista, não basta atribuir a lista a ser copiada a uma nova variável.
~~~python
lista1 = [1, 2, 3]
lista2 = lista1 # Dessa forma, ambas as listas apontam para o mesmo endereço de memória. Existe apenas uma lista, mas duas variáveis que apontam para ela (se alterar uma, altera a outra).
lista2 = lista1[:] # Dessa forma, criamos uma cópia com os mesmos valores, mas em endereços de memória diferentes. Se alterar uma, não altera a outra.
~~~

## | Métodos Úteis:
- `.append(x)`: Adiciona o elemento `x` ao final da lista.
- `.insert(i, x)`: Adiciona o elemento `x` na posição `i`.
- `.count(x)`: Conta quantas vezes o elemento `x` aparece na lista.
- `.pop(i)`: Remove o elemento de índice `i` da lista e o retorna.
- `.remove(x)`: Remove a primeira ocorrência do elemento `x` da lista.

## | Funções Úteis:
- `len(lista)`: Retorna o tamanho da lista.
- `sum(lista)`: Retorna a soma dos elementos da lista.
- `enumerate(lista)`: Retorna uma tupla com o índice e o valor de cada elemento da lista. Utilizado em laços de repetição.
- `zip(lista1, lista2)`: Retorna uma lista de tuplas, onde cada tupla contém um elemento de `lista1` e um de `lista2`. Utilizado em laços de repetição.

## | List Comprehension:
&emsp;&emsp; List Comprehension é uma forma concisa de criar listas de uma forma compacta. A sintaxe é semelhante a um operador ternário, porém com um loop for.
~~~python
lista = [x for x in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lista = [x**2 for x in lista] # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
lista = [x for x in lista if x % 2 == 0] # [0, 4, 16, 36, 64]
~~~

# Tuplas:
## | Características:
- São estruturas de dados que permitem armazenar vários valores (sem necessariamente serem do mesmo tipo) em uma única variável.
- São imutáveis, ou seja, não é possível alterar, adicionar ou remover elementos. Frequentemente utilizadas para armazenar coleções de itens que não devem ser alterados.
- São representadas por parênteses `()`.

## | Criação e Acesso:
&emsp;&emsp; Para criar uma tupla, basta colocar os valores entre parênteses e separá-los por vírgula.
~~~python
a = 5
tupla = (1, '2', 3.0, 2*2, a) # (1, '2', 3.0, 4, 5)
~~~

&emsp;&emsp; Para acessar um elemento da tupla, basta informar o índice do elemento desejado entre colchetes.
~~~python
tupla = (1, 2, 3, 4, 5)
print(tupla[0]) # 1, a contagem começa em 0
~~~

# Exercícios:
## 1. Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
~~~python
lista = []
for i in range(10):
    lista.append(float(input(f'Digite o {i+1}º número: ')))
print(lista[::-1])
~~~

## 2. Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
~~~python
lista1, lista2 = [1, 2, 3], [4, 5, 6]

lista3 = lista1 + lista2 # Concatenação
print(lista3)
~~~

## 3. A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
~~~python
T = [ -10, -8, 0, 1, 2, 5, -2, -4]
print(f'Menor: {min(T)}\nMaior: {max(T)}, Média: {sum(T)/len(T)}')
~~~

## 4. Faça um Programa que leia 20 números inteiros e armazene-os num lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima os três vetores.
~~~python
lista = []
for i in range (20):
    lista.append(int(input(f'Digite o {i+1}º número: ')))

par = [x for x in lista if x % 2 == 0]
impar = [x for x in lista if x % 2 != 0]

print(f'Lista: {lista}\nPar: {par}\nImpar: {impar}')
~~~

## 5. Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima quais alunos estão com média maior ou igual a 7.0.
~~~python
alunos = []
for i in range(5):
    notas = []
    for j in range(4):
        notas.append(float(input(f'Digite a {j+1}ª nota do {i+1}º aluno: ')))
    alunos.append(sum(notas)/4)

aprovados = [i+1 for i, j in enumerate(alunos) if j >= 7]
print(f'Aprovados: {aprovados}')
~~~
    
## 6. Escreva uma rotina que recebe uma lista de números e retorna a soma dos quadrados dos números.
~~~python
lista = []
for i in range(5):
    lista.append(float(input(f'Digite o {i+1}º número: ')))

soma = sum([x**2 for x in lista])
print(soma)
~~~

## 7. Escreva uma função que recebe uma lista de strings e retorna a string mais longa.
~~~python
lista = []
for i in range(5):
    lista.append(input(f'Digite a {i+1}ª palavra: '))

tamanhos = [len(x) for x in lista]
maior = lista[tamanhos.index(max(tamanhos))]
print(maior)
~~~

