<h1 align="center"> Strings <br>
  <a href="../[  3 ] Listas e Tuplas/"><img src="https://img.shields.io/badge/Anterior-Listas e Tuplas-215a36" alt="Anterior"></a>
  <a href="../[  5 ] Dicionários/"><img src="https://img.shields.io/badge/Próximo-Dicionários-215a36" alt="Próximo"></a>
</h1>

# Exercícios
## 1. Escreva um programa que leia duas strings. Verifique se a segunda ocorre dentro da primeira e imprima a posição de início.
~~~python
string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')

if string2 in string1:
    print(f'A segunda string ocorre na primeira string na posição {string1.find(string2)}')
else:
    print('A segunda string não ocorre na primeira string.')
~~~

## 2. Escreva um programa que leia duas strings e gere uma terceira com os caracteres comuns às duas strings lidas.
~~~python
string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')

a = set(string1)
b = set(string2)
c = [i for i in a if i in b]

print(''.join(c))
~~~

## 3. Escreva um programa que leia uma string e imprima quantas vezes cada caractere aparece nessa string. 
~~~python
string = input('Digite uma string: ')

for i in set(string):
    print(f'{i}: {string.count(i)}')
~~~

## 4. Escreva um programa que leia três strings. Imprima o resultado da substituição na primeira, dos caracteres da segunda pelos da terceira.
~~~python
string1 = input('Digite a primeira string: ')
string2 = input('Digite a segunda string: ')
string3 = input('Digite a terceira string: ')

for i in range(len(string2)):
    string1 = string1.replace(string2[i], string3[i])

print(string1)
~~~

## 5. Escreva uma função em Python que receba uma string como entrada e verifique se ela é um palíndromo.
~~~python
string = input('Digite uma string: ')
invertida = string[::-1]

if string == invertida:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
~~~

## 6. Escreva uma função em Python que receba uma string como entrada e retorne a string com cada palavra em ordem inversa.
~~~python
string = input('Digite uma string: ')
resp = ' '.join([i[::-1] for i in string.split()])
print(resp)
~~~

## 7. Escreva um programa que receba uma string e retorne apenas as palavras que possuem mais de três caracteres.
~~~python
string = input('Digite uma string: ')
resp = ' '.join([i for i in string.split() if len(i) > 3])
print(resp)
~~~