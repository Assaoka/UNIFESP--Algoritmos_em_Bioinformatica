<h1 align="center"> Loops e Condicionais <br>
  <a href="../[  1 ] Primeiros Passos em Python/"><img src="https://img.shields.io/badge/Anterior-Primeiros Passos em Python-215a36" alt="Anterior"></a>
  <a href="../[  3 ] Listas e Tuplas/"><img src="https://img.shields.io/badge/Próximo-Listas e Tuplas-215a36" alt="Próximo"></a>
</h1>

# Boleanos:
&emsp;&emsp; Booleanos são um tipo de dado que pode ter um de dois valores: True (Verdadeiro) ou False (Falso). Eles são frequentemente usados em operações de comparação e lógica.

## | Operadores de Comparação:
| `Operador` | `Exemplo` |             `Descrição`              |
| :--------: | :-------: | :----------------------------------: |
|    `==`    |  a == b   |     Verdadeiro se a é igual a b      |
|    `!=`    |  a != b   |   Verdadeiro se a é diferente de b   |
|    `>`     |   a > b   |    Verdadeiro se a é maior que b     |
|    `<`     |   a < b   |    Verdadeiro se a é menor que b     |
|    `>=`    |  a >= b   | Verdadeiro se a é maior ou igual a b |
|    `<=`    |  a <= b   | Verdadeiro se a é menor ou igual a b |

## | Operadores Lógicos:
| `Operador` | `Exemplo` |             `Descrição`              |
| :--------: | :-------: | :----------------------------------: |
|   `and`    |  a and b  | Verdadeiro se a e b são verdadeiros  |
|    `or`    |  a or b   | Verdadeiro se a ou b são verdadeiros |
|   `not`    |   not a   |       Verdadeiro se a é falso        |

# Estruturas Condicionais:
## | If-Elif-Else:
&emsp;&emsp; Estrutura condicional tradicional, que executa um bloco de código se (If) uma condição for verdadeira. Em python, um bloco de código é definido por identação.
~~~python
if condição1:
    print("Condição 1 é verdadeira.")
    # Comandos a serem executados se condição1 for verdadeira
elif condição2:
    print("A condição 1 é falsa e a condição 2 é verdadeira.")
    # Comandos a serem executados se a condição 1 for falsa e a condição 2 for verdadeira
elif condição3:
    print("A condição 1 e 2 são falsas e a condição 3 é verdadeira.")
    # Você pode ter quantos elifs quiser. Esse bloco será executado se todas as condições anteriores forem falsas e a condição_i for verdadeira.
else:
    print("Nenhuma das condições é verdadeira.")
    # Comandos a serem executados se nenhuma das condições for verdadeira

# O bloco de código do if-elif-else termina quando a identação é quebrada.
print("Fim do if-elif-else.")
~~~

## | Operador Ternário:
&emsp;&emsp; O operador ternário é uma forma compacta de escrever uma estrutura condicional. Em python, o operador ternário é escrito como:
~~~python
valor_se_verdadeiro if condição else valor_se_falso
~~~

&emsp;&emsp; O operador ternário acima é equivalente a:
~~~python
if condição:
    valor_se_verdadeiro
else:
    valor_se_falso
~~~

## | Match-Case:
&emsp;&emsp; A estrutura match-case é equivalente ao switch-case de outras linguagens de programação. A estrutura match-case foi introduzida no Python 3.10.
~~~python
match valor:
    case valor1:
        # Comandos a serem executados se valor == valor1. Observe que esse bloco possui duas identações (uma para o match e outra para o case)
    case valor2:
        # Comandos a serem executados se valor == valor2
    case valor3:
        # Comandos a serem executados se valor == valor3
    case _:
        # Comandos a serem executados se valor não for igual a nenhum dos valores anteriores
~~~

&emsp;&emsp; O bloco acima é equivalente a:
~~~python
if valor == valor1:
    # Comandos a serem executados se valor == valor1
elif valor == valor2:
    # Comandos a serem executados se valor == valor2
elif valor == valor3:
    # Comandos a serem executados se valor == valor3
else:
    # Comandos a serem executados se valor não for igual a nenhum dos valores anteriores
~~~

# Estruturas de Repetição:
## | For:
&emsp;&emsp; O loop for é utilizado para iterar um conjunto de instruções um número específico de vezes. São especialmente úteis em python quando queremos percorrer uma variável composta (que veremos mais adiante).
~~~python
for i in repetições:
    # Comandos a serem executados a cada repetição. i vale a i-ésima posição do elemento repetições.
~~~

&emsp;&emsp; Uma função muito útil para ser utilizada com o loop for é a função range(). A função range() gera uma sequência de números, que é utilizada para iterar sobre um bloco de código um número específico de vezes. A função range() deve ser utilizada da seguinte forma:
~~~python
range(fim) # Começa em 0, termina em fim - 1 andando 1 elemento por vez
~~~

&emsp;&emsp; Caso você queira uma sequência mais complexa, você pode utilizar a função range() da seguinte forma:
~~~python
range(início, fim, passo) # Começa em início, termina em fim - 1 andando passo elementos por vez
~~~

&emsp;&emsp; O code abaixo imprime os números pares de 0 a 88 (inclusive):
~~~python
for i in range(0, 89, 2):
    print(i)
~~~

## | While:
&emsp;&emsp; O loop while é utilizado para repetir um bloco de código enquanto uma condição for verdadeira.
~~~python
while condição:
    # Comandos a serem executados enquanto a condição for verdadeira.
    # É importante que a condição seja alterada dentro do bloco de código para que o loop não seja infinito.
~~~

## | While-True:
&emsp;&emsp; Python não possui a estrutura do-while, quando queremos que um bloco de código seja executado pelo menos uma vez, podemos utilizar o loop while-true.
~~~python
while True:
    # Comandos a serem executados pelo menos uma vez.
    if condição:
        break # Sai imediatamente do loop. Observe que esse bloco tem duas identações (uma para o while e outra para o if) 
    # Comandos a serem executados enquanto a condição for verdadeira.
~~~

&emsp;&emsp; Outro comando útil para esse tipo de loop é o comando continue, que pula o restante do bloco de código e vai para a próxima iteração do loop.
~~~python
while True:
    # Comandos a serem executados pelo menos uma vez.
    if condição:
        break # Sai imediatamente do loop
    if outra_condição:
        continue # Pula o restante do bloco de código e vai para a próxima iteração do loop
    # Comandos a serem executados enquanto a condição for verdadeira e a outra_condição for falsa.
~~~

&emsp;&emsp; Não é muito recomendado, mas é possível utilizar o break e o continue nas outras estruturas de repetição.


# Exercícios:
## 1. Em química, o pH de uma solução aquosa é uma medida da sua acidez. Os Valores de pH variam entre 0 e 14. Soluções ácidas tem pH maior que 7. Soluções básicas tem pH menor que 7. Soluções neutras tem pH igual a 7. Escreva duas funções que recebem um número correspondente ao pH de uma solução aquosa e exibem na tela o tipo de solução (algo como “A solução é ácida”).
~~~python
pH = float(input("Digite o valor do pH: "))

if pH > 7: 
    print("A solução é ácida.")
elif pH < 7:
    print("A solução é básica.")
else:
    print("A solução é neutra.")
~~~

## 2. Crie um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa e forneça uma classificação com base no resultado.
~~~python
altura = float(input('Altura: '))
peso = float(input('Peso: '))

IMC = peso/(altura**2)
if IMC < 18.5:  
    print("Abaixo do Peso)")
elif IMC < 24.9: 
    print("Peso Normal)")
elif IMC < 29.9: 
    print("Sobrepeso)")
elif IMC < 34.9: 
    print("Obesidade Grau I)")
elif IMC < 39.9: 
    print("Obesidade Grau II)")
else:            
    print("Obesidade Grau III)")
~~~

## 3. Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
~~~python
for i in range(10, -1, -1): # range(inicio, fim - 1, passo)
    print(i)
print("Fogo!")
~~~

## 4. Crie um programa que imprima a sequência de Fibonacci até o décimo termo usando um loop for.
~~~python
a, b = 0, 1
for i in range (0, 10, 1):
    print(a, end = " ")
    a, b = b, a + b
~~~

## 5. Em um script, o usuário deve responder à pergunta “Continuar (s/n)?”. Se o usuário digitar ‘s’ ou ‘S’, o script deve retornar a mensagem “OK, continuando...”. Se o usuário digitar ‘n’ ou ‘N’, o script deve retornar a mensagem “OK, parando...”. Por fim, se o usuário digitar qualquer outra coisa,o script deve retornar uma mensagem de erro.
~~~python
while True:
    resposta = str(input("Continuar (s/n)? "))
    if resposta == 's' or resposta == 'S':
        print("OK, continuando...")
    elif resposta == 'n' or resposta == 'N':
        print("OK, parando...")
        break
    else:
        print("Erro! Digite 's' ou 'n'.")
~~~

## 6. Escreva um programa que encontre e imprima todos os números primos entre 1 e 100.
~~~python
print(2, end = " ")
for i in range(3, 101, 2):
    primo = True
    for j in range(2, i):
        if i % j == 0:
            primo = False
            break
    if primo:
        print(i, end = " ")
~~~
