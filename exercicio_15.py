print("########################################################")
print("calculadora de salário com descontos - IR/INSS/sindicato")
print("########################################################")

horas_trabalhadas = float(input("insira a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("insira o valor por hora trabalhada: R$"))

salario_bruto = horas_trabalhadas * valor_por_hora
ir = (salario_bruto * 11) / 100
inss = (salario_bruto * 8) / 100
sindicato = (salario_bruto * 5) / 100
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print("########################################################")
print("abaixo seguem os rendimentos e descontos detalhados")
print("+ Salário Bruto : R${:.2f}".format(salario_bruto))
print("- IR (11%) : R${:.2f}".format(ir))
print("- INSS (8%) : R${:.2f}".format(inss))
print("- Sindicato ( 5%) : R${:.2f}".format(sindicato))
print("= Salário Liquido : R${:.2f}".format(salario_liquido))