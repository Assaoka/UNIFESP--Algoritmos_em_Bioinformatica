<h1 align="center"> Primeiros Passos em Python <br>
  <a href="../"><img src="https://img.shields.io/badge/Anterior-Home-215a36" alt="Anterior"></a>
  <a href="../[  2 ] Loops e Condicionais/"><img src="https://img.shields.io/badge/Próximo-Loops e Condicionais-215a36" alt="Próximo"></a>
</h1>


# Variáveis:
## | O que são Variáveis?
1. Variáveis são espaços de memória que armazenam valores. 
2. Em Python, as variáveis são criadas automaticamente quando um valor é atribuído a ela (através do operador de atribuição `=`).
3. Diferente de outras linguagens de programação, não é necessário declarar o tipo da variável.
4. As variáveis são case-sensitive, ou seja, diferenciam letras maiúsculas de minúsculas.
5. O nome de uma variável deve começar com uma letra ou um sublinhado (_) e não pode ser uma palavra reservada (if, else, for, etc).

## | Tipos de Variáveis Primitivas:
| `Tipo`  |                             `Descrição`                             |  `Exemplo`  |
| :-----: | :-----------------------------------------------------------------: | :---------: |
|  `int`  |                          Números Inteiros                           |     10      |
| `float` | Números de Ponto Flutuante (utiliza o ponto como separador decimal) |    10.5     |
|  `str`  |                        Cadeia de Caracteres                         | 'Olá Mundo' |
| `bool`  |                      Booleano (True ou False)                       |    True     |

# Leitura de Dados:
&emsp;&emsp; Podemos ler dados do teclado utilizando a função `input()`. Essa função sempre retorna uma string, então é necessário converter o valor para o tipo desejado. Para converter um tipo de variável em outro, basta utilizar o nome do tipo desejado como uma função. Exemplo:
~~~python
n = int(input('Digite um número: '))
~~~

&emsp;&emsp; Essa linha de código imprime a mensagem "Digite um número: " e lê uma entrada do teclado. Em seguida, tenta converter a entrada para um número inteiro e armazenar na variável `n`. Se a entrada não for um número inteiro, o programa irá gerar um erro.

# Impressão de Dados:
&emsp;&emsp; Para imprimir dados na tela, utilizamos a função `print()`. Existem várias formas de formatar a saída de dados, aqui vamos utilizar a função `f-string` para formatar a saída. Exemplo:
~~~python
print(f'A Variável X tem o valor {x}') # Imprime o valor da variável x, idependente do tipo (identificado automaticamente)
print(f'A Soma de {a} e {b} é igual a {a+b}') # Realiza a soma de a e b e imprime o resultado
print(f'O Resultado é {resultado:.2f}') # Limita o número de casas decimais
# ... e assim por diante
~~~

# Operadores Aritméticos:
| `Operador` |   `Descrição`    | `Exemplo` |
| :--------: | :--------------: | :-------: |
|    `+`     |      Adição      |   a + b   |
|    `-`     |    Subtração     |   a - b   |
|    `*`     |  Multiplicação   |   a * b   |
|    `/`     |     Divisão      |   a / b   |
|    `//`    | Divisão Inteira  |  a // b   |
|    `%`     | Resto da Divisão |   a % b   |
|    `**`    |  Exponenciação   |  a ** b   |

## | Precedência de Operadores:
&emsp;&emsp; A precedência de operadores em Python segue a mesma ordem da matemática:
1. Parênteses
2. Exponenciação
3. Multiplicação, Divisão, Divisão Inteira e Resto da Divisão (Na ordem que aparecem)
4. Adição e Subtração (Na ordem que aparecem)

## | Operadores de Atribuição:
| `Operador` |   `Descrição`    | `Exemplo` | `Equivalente` |
| :--------: | :--------------: | :-------: | :-----------: |
|    `=`     |    Atribuição    |   a = b   |     a = b     |
|    `+=`    |      Adição      |  a += b   |   a = a + b   |
|    `-=`    |    Subtração     |  a -= b   |   a = a - b   |
|    `*=`    |  Multiplicação   |  a *= b   |   a = a * b   |
|    `/=`    |     Divisão      |  a /= b   |   a = a / b   |
|   `//=`    | Divisão Inteira  |  a //= b  |  a = a // b   |
|    `%=`    | Resto da Divisão |  a %= b   |   a = a % b   |
|   `**=`    |  Exponenciação   |  a **= b  |  a = a ** b   |

&emsp;&emsp; O operador de atribuição `=` permite que você atribua valor a múltiplas variáveis ao mesmo tempo. Exemplo:
~~~python
a, b = b, a # Podemos, por exemplo, trocar o valor de duas variáveis sem a necessidade de uma variável auxiliar
~~~ 


# Exercícios:
## 1. Crie um script em Python que solicite o nome, altura e peso de uma pessoa e mostre a seguinte mensagem: “João tem 90 kilos e altura de 1.78 e portanto o IMC é de 28.4”.
~~~python
nome = str(input('Nome: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))

IMC = peso/(altura**2)
print(f'{nome} tem {peso} kilos e altura de {altura} e portanto o IMC é de {IMC:0.1f}')
~~~

## 2. Escreva um script que leia um valor em metros e o exiba convertido em milímetros
~~~python
valor = float(input('Valor em Metros: '))
print(f'Valor em Milímetros: {valor*1000}')
~~~

## 3. Escreva um script que leia a quantidade de dias, horas, minutos e segundos para o usuário. Calcule o total em segundos.
~~~python
tempo = int(input('Dias: '))
tempo = tempo*24 + int(input('Horas: '))
tempo = tempo*60 + int(input('Minutos: '))
tempo = tempo*60 + int(input('Segundos: '))

print(f'\nTotal: {tempo} s')
~~~

## 4. Faça um script que calcule o aumento de salário. Ele deve solicitar o valor do salário e a porcentagem de aumento. Exiba o valor do aumento e do novo salário.
~~~python
salário = float(input('Salário: '))
aumento = float(input('Aumento (%): '))

aumento = (aumento/100)*salário
print(f'Valor do Aumento: {aumento}')
print(f'Total: {salário + aumento}')
~~~

## 5. Leia a temperatura em graus Celsius e converta para Fahrenheit.
~~~python
Temp_C = float(input('Temperatura em C°: '))
Temp_F = (Temp_C * 9/5) + 32

print(f'Temperatura em F°: {Temp_F:.2f} F°')
~~~

## 6. Leia o valor de um produto e calcule o valor final com 10% de desconto.
~~~python
valor = float(input('Preço: R$ '))
print(f'Valor Final: R$ {valor*0.9:.2f}')
~~~

## 7. Crie um programa que calcule o tempo de viagem, pedindo ao usuário a distância e a velocidade.
~~~python
d = float(input('Distância (km): '))
v = float(input('Velocidade (km/h): '))
print(f'Tempo de Viagem: {d/v:.2f} horas')
~~~

## 8. Escreva um script que pergunte a quantidade de km percorridos por um carro alugado pelo usuário e a quantidade de dias pelo qual o carro foi alugado. Calcule o preço a pagar sabendo que o carro custa 60 reais por dia e 15 centavos por Km rodado.
~~~python
km_percorridos = float(input('Quantidade de km percorridos: '))
dias_alugados = int(input('Quantidade de dias alugados: '))

preço = (dias_alugados * 60) + (km_percorridos * 0.15)
print(f'Preço: R$ {preço:.2f}')
~~~

## 9. Calcule a resistência resultante de de três resistores R1, R2 e R3 em paralelo.
~~~python
R1 = float(input('R1: '))
R2 = float(input('R2: '))
R3 = float(input('R3: '))

R = 1/(1/R1 + 1/R2 + 1/R3)
print(f'R: {R} Ω')
~~~


---
