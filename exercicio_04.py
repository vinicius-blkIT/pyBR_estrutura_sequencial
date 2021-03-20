import math
from cria_banner import banner

nome_programa = "calculadora da média anual v1.0"
banner(nome_programa)

print("""Info:
Insira as quatro médias de cada bimestre
Utilize apenas uma casa decimal separando por . "ponto"
A aplicação irá calcular a média anual para você!""")

bimestre1 = float(input("Insira a nota do primeiro bimestre: "))
print("Registrada a nota {:.2} para o primeiro bimestre".format(bimestre1))

bimestre2 = float(input("Insira a nota do segundo bimestre: "))
print("Registrada a nota {:.2} para o segundo bimestre".format(bimestre2))

bimestre3 = float(input("Insira a nota do terceiro bimestre: "))
print("Registrada a nota {:.2} para o terceiro bimestre".format(bimestre3))

bimestre4 = float(input("Insira a nota do quarto bimestre: "))
print("Registrada a nota {:.2} para o quarto bimestre".format(bimestre4))

media_anual = round((bimestre1 + bimestre2 + bimestre3 + bimestre4)/4, 1)
print("A média anual é {}".format(media_anual))

if media_anual < 7:
    print("Aluno deve fazer recuperação final!")
else:
    print("Aluno aprovado!")

print("FIM")
