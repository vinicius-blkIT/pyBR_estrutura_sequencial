from cria_banner import banner

nome_programa = "calculadora de peso ideal v1.0"
banner(nome_programa)

nome = input("insira o seu nome para iniciarmos: ")
print("olá {}, tudo bem? vamos prosseguir.".format(nome))

print("___________________________________________________")

altura = float(input("agora insira a sua altura em metros para realizarmos o cálculo: "))

print("___________________________________________________")

peso_ideal = (72.7 * altura) - 58
print ("{}, com base na sua altura, seu peso ideal é {:.1f} kg!".format(nome,peso_ideal))

print("fim do programa")