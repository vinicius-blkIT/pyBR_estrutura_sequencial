from cria_banner import banner

nome_programa = "calculadora de salário mensal v1.0"
banner(nome_programa)

colaborador = input("insira o nome do colaborador em questão: ")
valor_da_hora = float(input("insira o valor da hora trabalhada: "))
horas_trabalhadas = float(input("insira a quantidade de horas trabalhadas: "))

salario_mensal = valor_da_hora * horas_trabalhadas

print("o colaborador {} trabalhou {} horas no último mês, sob o valor R${:.2f}/hora e o salário mensal calculado é de R${:.2f}".format(colaborador,horas_trabalhadas,valor_da_hora,salario_mensal))