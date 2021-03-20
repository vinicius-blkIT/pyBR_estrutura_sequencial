from cria_banner import banner

nome_programa = "calcula o dobro da área de um quadrado v1.0"
banner(nome_programa)

lado = float(input("insira o tamanho dos lados, em centímetros, do quadrado para ser calculado: "))

area = lado**2

dobro = area*2

print("o valor inserido foi de {}cm, a área calculada é de {}cm² e o dobro da área é de {}cm²".format(lado,area,dobro))