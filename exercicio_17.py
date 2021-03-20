import math
from cria_banner import banner

nome_programa = "calculadora de utilização de tinta - galões e latas - v1.0"
banner(nome_programa)

area_pintura = float(input("insira a área a ser pintada em m²: "))
cobertura_tinta = 6

valor_lata = 80.0
valor_galao = 25.0

capacidade_lata = 18.0
capacidade_galao = 3.6

cobertura_lata = capacidade_lata * cobertura_tinta
cobertura_galao = capacidade_galao * cobertura_tinta

margem_de_seguranca = 1.1

def imprimir(tipo):
    if tipo == "lata":
        print("serão necessárias {} latas de tinta para pintar {}m² e custará R${:.2f}".format(quantidade, area_pintura,valor_total))
    elif tipo == "galao":
        print("serão necessários {} galoes de tinta para pintar {}m² e custará R${:.2f}".format(quantidade, area_pintura,valor_total))
    else:
        pass

def calcular_litros_a_serem_utilizados():
    global litros_utilizados
    litros_utilizados = (area_pintura / cobertura_tinta) * margem_de_seguranca
    return litros_utilizados

def calcular_quantidade(capacidade, litros_necessarios):
    global quantidade
    quantidade = math.trunc(litros_necessarios / capacidade)
    condicao_excedente = litros_necessarios % capacidade
    if condicao_excedente > 0:
        quantidade = quantidade + 1
        return quantidade
    else:
        return quantidade

def calcular_quantidade_sem_desperdicio():
    global quantidade_latas
    global quantidade_galoes
    if area_pintura >= cobertura_lata:
            quantidade_latas = math.trunc(litros_utilizados / capacidade_lata)
            condicao_excedente = litros_utilizados % capacidade_lata
            if condicao_excedente > 0:
                quantidade_galoes = math.trunc(condicao_excedente / capacidade_galao)
                condicao_excedente2 = condicao_excedente % capacidade_galao
                if condicao_excedente2 > 0:
                    quantidade_galoes = quantidade_galoes + 1
                    return quantidade_latas, quantidade_galoes
                else:
                    return quantidade_latas, quantidade_galoes
            else:
                return quantidade_latas, quantidade_galoes
    else:
        quantidade_galoes = math.trunc(litros_utilizados / capacidade_galao)
        quantidade_latas = 0
        condicao_excedente = litros_utilizados % capacidade_galao
        if condicao_excedente > 0:
            quantidade_galoes = quantidade_galoes + 1
            return quantidade_galoes, quantidade_latas
        else:
            return quantidade_galoes, quantidade_latas

def calcular_valor_sem_desperdicio():
    global valor_total
    valor_total = ((quantidade_latas*valor_lata)+(quantidade_galoes*valor_galao))
    return valor_total

def imprimir_sem_desperdicio():
    if quantidade_latas > 0:
        if quantidade_galoes > 0:
            print("serão necessárias {} latas e {} galões de tinta para pintar {}m² e custará R${:.2f}".format(quantidade_latas, quantidade_galoes, area_pintura,valor_total))
        else:
            print("serão necessárias {} latas de tinta para pintar {}m² e custará R${:.2f}".format(quantidade_latas, area_pintura,valor_total))   
    else:
        if quantidade_galoes < 0:
            print("serão necessários {} galões de tinta para pintar {}m² e custará R${:.2f}".format(quantidade_galoes, area_pintura,valor_total))
        else:
            pass

def calcular_total(quantidade, valor):
    global valor_total
    valor_total = quantidade * valor
    return valor_total

calcular_litros_a_serem_utilizados()
calcular_quantidade(capacidade_lata,litros_utilizados)
calcular_total(quantidade, valor_lata)
imprimir("lata")

calcular_quantidade(capacidade_galao,litros_utilizados)
calcular_total(quantidade, valor_galao)
imprimir("galao")

calcular_quantidade_sem_desperdicio()
calcular_valor_sem_desperdicio()
imprimir_sem_desperdicio()




