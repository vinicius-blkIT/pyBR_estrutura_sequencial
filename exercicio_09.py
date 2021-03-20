print("#################################################")
print("     conversor de fahrenheit para celsius")
print("#################################################")

fahrenheit = float(input("insira a temperatura em fahrenheit para ser convertida em celsius: "))
celsius = 5 * ((fahrenheit-32) / 9)

print("o resultado é de aproximadamente {:.2f} graus celsius".format(celsius))
