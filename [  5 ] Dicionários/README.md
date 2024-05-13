<h1 align="center"> Dicionários <br>
    <a href="../[  4 ] Strings/"><img src="https://img.shields.io/badge/Anterior-Strings-215a36" alt="Anterior"></a>
    <a href="../[  6 ] Função/"><img src="https://img.shields.io/badge/Próximo-Função-215a36" alt="Próximo"></a>
</h1>

# Exercícios
## 1. Escreva um programa que gere um dicionário, onde cada chave seja um caractere, e seu valor seja o número desse caractere encontrado em uma frase lida. Exemplo: O rato -> { “O”:1, “r”:1, “a”:1, “t”:1, “o”:1}
~~~python
string = input('Digite uma string: ')
dicionario = {i: string.count(i) for i in set(string)}
print(dicionario)
~~~

## 2. Crie um dicionário, chamado frutas, de frutas e seus preços. a) Crie um segundo dicionário chamado compras na qual as chaves são as frutas e valores é a quantidade a ser comprada. b) Calcule o preço total de um carrinho de compras de frutas usando o dicionário criado no exercício anterior. c) Remova todas as frutas do dicionário de frutas que custam mais de R$ 5,00.
~~~python
frutas = {'banana': 2.00, 'maçã': 3.00, 'uva': 4.00, 'melancia': 5.00, 'morango': 6.00}
print(frutas)

# Parte a
compras = {}
for i in frutas.keys():
    quantidade = int(input(f'Quantas {i}s você deseja comprar? '))
    if quantidade > 0: compras[i] = quantidade
print(compras)

# Parte b
total = 0
for i in compras.keys():
    total += compras[i] * frutas[i]
print(f'O total da compra é R$ {total:.2f}')

# Parte c
for i in frutas.keys():
    if frutas[i] > 5.00: frutas.pop(i)
print(frutas)
~~~

## 3. Faça um programa que leia o nome RA e média final de uma aluno. Armazene todas as informações num dicionário. No final programa deve imprimir as informações do dicionário e situação do aluno (reprovado, exame ou aprovado). Utilize as regras da UNIFESP para definir a situação do aluno.
~~~python
aluno = {}
aluno['RA'] = int(input('Digite o RA do aluno: '))
aluno['Média'] = float(input('Digite a média final do aluno: '))
aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 6.0 else 'Reprovado' if aluno['Média'] < 3.0 else 'Exame'

print(aluno)
~~~

## 4. Crie um programa que leia nome, sexo, peso e altura de várias pessoas. guarde os dados de cada pessoa num dicionário individual e acrescente o IMC da pessoa. Organize todos os dicionários em uma lista. No final mostre: a) Quantas pessoas foram cadastradas. b) Qual é o peso médio das pessoas.
~~~python
pessoas = []
for i in range(3): # Altere o valor para a quantidade de pessoas que deseja cadastrar
    pessoa = {}
    pessoa['Nome'] = input('Digite o nome da pessoa: ')
    pessoa['Sexo'] = input('Digite o sexo da pessoa: ')
    pessoa['Peso'] = float(input('Digite o peso da pessoa: '))
    pessoa['Altura'] = float(input('Digite a altura da pessoa: '))
    pessoa['IMC'] = pessoa['Peso'] / pessoa['Altura'] ** 2
    pessoas.append(pessoa)

# Parte a
print(f'Foram cadastradas {len(pessoas)} pessoas.')

# Parte b
pesos = [i['Peso'] for i in pessoas]
peso_medio = sum(pesos) / len(pesos)
print(f'O peso médio das pessoas é {peso_medio:.2f} kg.')
~~~

## 5. Escreva um programa para agrupar uma lista de dicionários por uma chave específica.
~~~python
lista = [{'chave1': 1, 'chave2': 2}, {'chave2': 3, 'chave7': 4}, {'chave1': 1, 'chave4': 5}]
chave = 'chave1'

lista_agrupada = []
for i in lista:
    if chave in i.keys():
        lista_agrupada.append(i)

print(lista_agrupada)
~~~

## 7. Escreva um programa para verificar se uma chave específica existe no dicionário ou não.
~~~python
dicionario = {'chave1': 1, 'chave2': 2, 'chave3': 3}
chave = input('Digite a chave que deseja verificar: ')

if chave in dicionario.keys(): print('A chave existe no dicionário.')
else: print('A chave não existe no dicionário.')
~~~

## 8. Escreva um programa para criar um set de todos os caracteres únicos em uma string.
~~~python
string = input('Digite uma string: ')
caracteres_unicos = set(string)
print(caracteres_unicos)
~~~

## 9. Crie um programa que gerencia o aproveitamento de um jogador de futebol. o programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário incluindo o total de gols realizados durante o campeonato.
~~~python
jogador = {}
jogador['Nome'] = input('Digite o nome do jogador: ')
jogador['Partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
jogador['Gols'] = []
for i in range(jogador['Partidas']):
    jogador['Gols'].append(int(input(f'Digite a quantidade de gols feitos na partida {i+1}: '))
jogador['Total de gols'] = sum(jogador['Gols'])

print(jogador)
~~~