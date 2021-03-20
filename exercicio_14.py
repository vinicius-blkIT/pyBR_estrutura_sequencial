from cria_banner import banner

nome_programa = "calculadora de multas sobre peso excedente v1.0"
banner(nome_programa)

multa_excesso = 4
limite_peso = 50


print("______________________________________________________________________________")
print("                                 DISCLAIMER")
print("o estado de sp multa em R${:.2f} para cada kg excedente do limite de {:.2f}kg".format(multa_excesso,limite_peso))
print("______________________________________________________________________________")

peso_peixes = float(input("insira o peso dos peixes que foram pescados hoje: "))

if peso_peixes > limite_peso:
    peso_excedido = peso_peixes - limite_peso
    multa_aplicada = peso_excedido * multa_excesso
    print("como o limite diário de {:.2f}kg foi excedido em {:.2f}kg, o estado de sp gerou uma multa no valor de R${:.2f}!".format(limite_peso,peso_excedido,multa_aplicada))
else:
    print("o limite diário de {:2}kg não foi excedido, portanto não haverá multa!".format(limite_peso))

print("fim do programa.")