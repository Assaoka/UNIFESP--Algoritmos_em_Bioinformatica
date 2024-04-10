# Primeiros Passos em Python

# Exercícios:
## 1. Crie um script em Python que solicite o nome, altura e peso de uma pessoa e mostre a seguinte mensagem: “João tem 90 kilos e altura de 1.78 e portanto o IMC é de 28.4”.
nome = str(input('Nome: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))

IMC = peso/(altura**2)
print(f'{nome} tem {peso} kilos e altura de {altura} e portanto o IMC é de {IMC:0.1f}')


## 2. Escreva um script que leia um valor em metros e o exiba convertido em milímetros
valor = float(input('Valor em Metros: '))
print(f'Valor em Milímetros: {valor*1000}')


## 3. Escreva um script que leia a quantidade de dias, horas, minutos e segundos para o usuário. Calcule o total em segundos.
tempo = int(input('Dias: '))
tempo = tempo*24 + int(input('Horas: '))
tempo = tempo*60 + int(input('Minutos: '))
tempo = tempo*60 + int(input('Segundos: '))

print(f'\nTotal: {tempo} s')


## 4. Faça um script que calcule o aumento de salário. Ele deve solicitar o valor do salário e a porcentagem de aumento. Exiba o valor do aumento e do novo salário.
salário = float(input('Salário: '))
aumento = float(input('Aumento (%): '))

aumento = (aumento/100)*salário
print(f'Valor do Aumento: {aumento}')
print(f'Total: {salário + aumento}')


## 5. Leia a temperatura em graus Celsius e converta para Fahrenheit.
Temp_C = float(input('Temperatura em C°: '))
Temp_F = (Temp_C * 9/5) + 32

print(f'Temperatura em F°: {Temp_F:.2f} F°')


## 6. Leia o valor de um produto e calcule o valor final com 10% de desconto.
valor = float(input('Preço: R$ '))
print(f'Valor Final: R$ {valor*0.9:.2f}')


## 7. Crie um programa que calcule o tempo de viagem, pedindo ao usuário a distância e a velocidade.
d = float(input('Distância em Metros: '))
v = float(input('Velocidade em Metros por Segundo: '))

print(f'Tempo de Viagem: {d/v:.2f} s')


## 8. Escreva um script que pergunte a quantidade de km percorridos por um carro alugado pelo usuário e a quantidade de dias pelo qual o carro foi alugado. Calcule o preço a pagar sabendo que o carro custa 60 reais por dia e 15 centavos por Km rodado.
dist = float(input('Quilômetros Percorridos: '))
dias = int(input('Número de Dias: '))
carro = str(input('Qual o Carro ALugado: '))

preço = dist*0.15 + dias*60
print(f'Preço: R$ {preço:.2f}')


## 9. Calcule a resistência resultante de de três resistores R1, R2 e R3 em paralelo.
R1 = float(input('R1: '))
R2 = float(input('R2: '))
R3 = float(input('R3: '))

R = 1/(1/R1 + 1/R2 + 1/R3)
print(f'R: {R} Ω')
