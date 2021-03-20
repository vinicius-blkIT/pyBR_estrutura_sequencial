from cria_banner import banner

nome_programa = "conversor de temperatura - fahrenheit para celsius - v1.0"
banner(nome_programa)

fahrenheit = float(input("insira a temperatura em fahrenheit para ser convertida em celsius: "))
celsius = 5 * ((fahrenheit-32) / 9)

print("o resultado é de aproximadamente {:.2f} graus celsius".format(celsius))
