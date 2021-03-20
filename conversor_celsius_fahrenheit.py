print("#################################################")
print("     conversor de celsius para fahrenheit")
print("#################################################")

celsius = float(input("insira a temperatura em celsius para ser convertida em fahrenheit: "))
fahrenheit = ((celsius * (9/5)) + 32)

print("o resultado é de aproximadamente {:.2f} graus fahrenheit".format(fahrenheit))