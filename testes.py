# 7- Escreva um programa em Python que obtenha uma
# temperatura em graus Celsius, calcule e mostre a respectiva
# temperatura nas escalas Fahrenheit e Kelvin. Utilize as
# fórmulas abaixo:

celsius = float(input("Qual a temperatura agora?"))
fahrenheit = (1.8 * celsius) + 32
kelvin = celsius + 273
print("A temperatura em fahrenheit é:", fahrenheit)
print("A temperatura em kelvin é:", kelvin)