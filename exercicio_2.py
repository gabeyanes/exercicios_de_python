### 1- Desenvolva um programa em Python que solicite ao usuário os valores dos lados de um retângulo e calcule e mostre seu perímetro e sua área.

print("Me passe os valores dos lados de um retângulo")
alturaRetangulo = int(input("Envie a altura do retângulo:"))
baseRetangulo = int(input("Envie a base do retângulo:"))
areaDoRetangulo = alturaRetangulo*baseRetangulo
print("Essa é a area do retângulo:",areaDoRetangulo)
perimetroDoRetangulo = 2 * (alturaRetangulo + baseRetangulo)
print("Essa é o perímetro do retângulo:",perimetroDoRetangulo)

# 2- Escreva um programa em Python que solicite ao usuário o salário atual e mostre o salário acrescido de 5% de comissão.

meuSalario = int(input("Qual é o seu salário:"))
comissao = meuSalario * (5/100)
print("Sua comissão é:",comissao)
acrescimoDoSalario = comissao + meuSalario
print("Seu salario + a sua comissão fica:", acrescimoDoSalario)

# 3- Escreva um programa em Python que solicite ao usuário a distância entre duas cidades e o tempo de viagem. O programa deverá calcular e exibir a velocidade média de um carro que vai de uma cidade para outra. Utilize a fórmula:  vide Apresentação

distancia = int(input("Digite a distancia entre a cidade A e B em Km:"))
tempo = int(input("Diga o tempo que leva para chegar da cidade A a B em horas:"))
velocidadeMedia = distancia/tempo
print("A velocidade média é:", velocidadeMedia,"Km/h")

# 4- Escreva um programa em Python que calcule as duas
# raízes de uma equação de 2º grau ax²+bx+c, conhecendo os
# valores dos coeficientes da mesma (a, b, c). Suponha que as
# raízes são reais. Lembre-se que para calcular as duas raízes:

coeficienteA = int(input("Passe o valor do coeficiente A:"))
coeficienteB = int(input("Passe o valor do coeficiente B:"))
coeficienteC = int(input("Passe o valor do coeficiente C:"))
delta = coeficienteB ** 2 - 4*coeficienteA*coeficienteC
print("Este é seu delta",delta)
umX = (-coeficienteB - delta**0.5) / (2*coeficienteA)
doisX = (-coeficienteB + delta**0.5) / (2*coeficienteA)
print("O valor de x1 é:", umX)
print("O valor de x2 é:", doisX)

# 5- Escreva um programa em Python que leia a cotação do
# dólar (taxa de conversão), leia um valor em dólares e converta
# e mostre o valor equivalente em Reais.

dolar = float(input("insira o valor em dolar:"))
conversao = dolar * 5.83
print("o valor convertido em reais fica:", conversao)

# 6- Escreva um programa em Python que leia um valor
# representando o gasto realizado por um cliente do restaurante
# ComaBem e visualize o valor total a ser pago, considerando
# os 10% do garçom.

valorGasto = float(input("Quanto você gastou no restaurante?"))
gorjeta = valorGasto * (10/100)
valorTotal = gorjeta + valorGasto
print("o valor total que você gastou contanto com a gorjeta foi:",valorTotal)

# 7- Escreva um programa em Python que obtenha uma
# temperatura em graus Celsius, calcule e mostre a respectiva
# temperatura nas escalas Fahrenheit e Kelvin. Utilize as
# fórmulas abaixo:

celsius = float(input("Qual a temperatura agora?"))
fahrenheit = (1.8 * celsius) + 32
kelvin = celsius + 273
print("A temperatura em fahrenheit é:", fahrenheit)
print("A temperatura em kelvin é:", kelvin)