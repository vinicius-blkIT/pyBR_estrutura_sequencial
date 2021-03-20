from cria_banner import banner

nome_programa = "conversor de metros para centímetros v1.0"
banner(nome_programa)

metros = (float(input("insira a medida a ser convertida de metros para centímetros: ")))

ople = (metros*100)

print("a medida inserida foi {} metros e é representada por {} centímetros".format(metros,ople))
