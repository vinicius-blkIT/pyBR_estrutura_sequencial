from cria_banner import banner

nome_programa = "soma dois números v1.0"
banner(nome_programa)

n1 = int(input("insira o primeiro número para realizar a soma: "))
print("o número inserido foi {}".format(n1))

n2 = int(input("insira o segundo número para realizar a soma: "))
print("o número inserido foi {}".format(n2))

soma = n1 + n2
print("o resultado da soma entre o número {} e o número {} é igual à {}".format(n1,n2,soma))