import math

print("###################################################")
print("               cálculo tintas")
print("###################################################")

area_pintura = float(input("insira a área a ser pintada em m²: "))
litros_utilizados = area_pintura / 3

valor_galao = 80.0
capacidade_galao = 18

quantidade_latas = math.trunc(litros_utilizados / capacidade_galao)
condicao_excedente = litros_utilizados % capacidade_galao

if condicao_excedente > 0:
    quantidade_latas = quantidade_latas + 1
    valor_total = quantidade_latas * valor_galao

else:
    valor_total = quantidade_latas * valor_galao

print("serão necessárias {} latas de tinta para pintar {}m² e custará R${:.2f}".format(quantidade_latas, area_pintura,valor_total))
