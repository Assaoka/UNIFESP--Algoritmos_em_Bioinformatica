# Listas e Tuplas

# Exercícios:
## 1. Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
lista = []
for i in range(10):
    lista.append(float(input(f'Digite o {i+1}º número: ')))
print(lista[::-1])


## 2. Faça um programa que leia duas listas e que gere uma terceira com os elementos das duas primeiras.
lista1, lista2 = [1, 2, 3], [4, 5, 6]

lista3 = lista1 + lista2 # Concatenação
print(lista3)


## 3. A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista T = [ -10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor e a maior temperatura, assim como a temperatura média.
T = [ -10, -8, 0, 1, 2, 5, -2, -4]
print(f'Menor: {min(T)}\nMaior: {max(T)}, Média: {sum(T)/len(T)}')


## 4. Faça um Programa que leia 20 números inteiros e armazene-os num lista. Armazene os números pares na lista PAR e os números IMPARES na lista impar. Imprima os três vetores.
lista = []
for i in range (20):
    lista.append(int(input(f'Digite o {i+1}º número: ')))

par = [x for x in lista if x % 2 == 0]
impar = [x for x in lista if x % 2 != 0]

print(f'Lista: {lista}\nPar: {par}\nImpar: {impar}')


## 5. Faça um Programa que peça as quatro notas de 5 alunos, calcule e armazene numa lista a média de cada aluno, imprima quais alunos estão com média maior ou igual a 7.0.
alunos = []
for i in range(5):
    notas = []
    for j in range(4):
        notas.append(float(input(f'Digite a {j+1}ª nota do {i+1}º aluno: ')))
    alunos.append(sum(notas)/4)

aprovados = [i+1 for i, j in enumerate(alunos) if j >= 7]
print(f'Aprovados: {aprovados}')

    
## 6. Escreva uma rotina que recebe uma lista de números e retorna a soma dos quadrados dos números.
lista = []
for i in range(5):
    lista.append(float(input(f'Digite o {i+1}º número: ')))

soma = sum([x**2 for x in lista])
print(soma)


## 7. Escreva uma função que recebe uma lista de strings e retorna a string mais longa.
lista = []
for i in range(5):
    lista.append(input(f'Digite a {i+1}ª palavra: '))

tamanhos = [len(x) for x in lista]
maior = lista[tamanhos.index(max(tamanhos))]
print(maior)


