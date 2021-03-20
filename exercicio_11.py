from cria_banner import banner

nome_programa = "cálculos diversos v1.0"
banner(nome_programa)

n1 = int(input("insira um número inteiro: "))
n2 = int(input("insira outro número inteiro: "))
n3 = float(input("insira um número real: "))

resolucao1 = (2 * n1) * (n2 / 2)
resolucao2 = (3 * n1) + n3
resolucao3 = n3**3

print("segue abaixo os cálculos realizados: ")
print("produto do dobro de {} com metade de {} é igual a {}".format(n1,n2,resolucao1))
print("soma do triplo de {} com {} é igual a {}".format(n1,n3,resolucao2))
print("{} elevado ao cubo é igual a {}".format(n3,resolucao3))
