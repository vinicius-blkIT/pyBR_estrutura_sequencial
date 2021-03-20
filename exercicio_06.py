from cria_banner import banner

nome_programa = "calculadora da área de um círculo v1.0"
banner(nome_programa)

pi = 3.14
raio = float(input("insira o raio do círculo, em centímetros, ao qual deseja calcular a área: "))

area = pi*(raio**2)

print("o raio informado é de {} centímetros e a área cálculada é de {} centímetros".format(raio,area))