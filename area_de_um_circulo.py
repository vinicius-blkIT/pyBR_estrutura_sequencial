print("##################################################")
print("calcule a área de um círculo informando o seu raio")
print("##################################################")

pi = 3.14
raio = float(input("insira o raio do círculo, em centímetros, ao qual deseja calcular a área: "))

area = pi*(raio**2)

print("o raio informado é de {} centímetros e a área cálculada é de {} centímetros".format(raio,area))