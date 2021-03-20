print("###################################################")
print("  cálculo de peso ideal - para homens e mulheres")
print("###################################################")

nome = input("insira o seu nome para iniciarmos: ")
print("olá {}, tudo bem? vamos prosseguir.".format(nome))

print("___________________________________________________")

altura = float(input("agora insira a sua altura em metros para realizarmos o cálculo: "))

print("___________________________________________________")

peso_ideal_homem = (72.7 * altura) - 58
peso_ideal_mulher = (62.1 * altura) - 44.7
print ("{}, com base na sua altura, se você for homem, seu peso ideal é {:.1f} kg e se for mulher o peso ideal é {:.1f}!".format(nome,peso_ideal_homem,peso_ideal_mulher))

print("fim do programa")