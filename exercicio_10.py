from cria_banner import banner

nome_programa = "conversor de temperatura - celsius para fahrenheit - v1.0"
banner(nome_programa)

celsius = float(input("insira a temperatura em celsius para ser convertida em fahrenheit: "))
fahrenheit = ((celsius * (9/5)) + 32)

print("o resultado é de aproximadamente {:.2f} graus fahrenheit".format(fahrenheit))