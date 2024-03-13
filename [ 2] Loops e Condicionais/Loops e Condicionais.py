# Loops e Condicionais

# Exercícios:
## 1. Em química, o pH de uma solução aquosa é uma medida da sua acidez. Os Valores de pH variam entre 0 e 14. Soluções ácidas tem pH maior que 7. Soluções básicas tem pH menor que 7. Soluções neutras tem pH igual a 7. Escreva duas funções que recebem um número correspondente ao pH de uma solução aquosa e exibem na tela o tipo de solução (algo como “A solução é ácida”).
pH = float(input("Digite o valor do pH: "))
if pH > 7: 
    print("A solução é ácida.")
elif pH < 7:
    print("A solução é básica.")
else:
    print("A solução é neutra.")


## 2. Crie um programa que calcule o IMC (Índice de Massa Corporal) de uma pessoa e forneça uma classificação com base no resultado.
nome = str(input('Nome: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))

IMC = peso/(altura**2)
print(f'{nome} tem {peso} kilos e altura de {altura} e portanto o IMC é de {IMC:0.1f} (', end ='')

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


## 3. Faça um programa para escrever a contagem regressiva do lançamento de um foguete. O programa deve imprimir 10, 9, 8, ..., 1, 0 e Fogo! na tela.
for i in range(10, -1, -1): # range(inicio, fim - 1, passo)
    print(i)
print("Fogo!")


## 4. Crie um programa que imprima a sequência de Fibonacci até o décimo termo usando um loop for.
a, b = 0, 1
for i in range (0, 10, 1):
    print(a, end = " ")
    a, b = b, a + b


## 5. Em um script, o usuário deve responder à pergunta “Continuar (s/n)?”. Se o usuário digitar ‘s’ ou ‘S’, o script deve retornar a mensagem “OK, continuando...”. Se o usuário digitar ‘n’ ou ‘N’, o script deve retornar a mensagem “OK, parando...”. Por fim, se o usuário digitar qualquer outra coisa,o script deve retornar uma mensagem de erro.
while True:
    resposta = str(input("Continuar (s/n)? "))
    if resposta == 's' or resposta == 'S':
        print("OK, continuando...")
    elif resposta == 'n' or resposta == 'N':
        print("OK, parando...")
        break
    else:
        print("Erro! Digite 's' ou 'n'.")


## 6. Escreva um programa que encontre e imprima todos os números primos entre 1 e 100.
print(2, end = " ")
for i in range(3, 101, 2):
    for j in range(2, i):
        if i % j == 0:
            break
    if j == i - 1:
        print(i, end = " ")

