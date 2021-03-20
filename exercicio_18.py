from cria_banner import banner

nome_programa = "calculadora de tempo de download v1.0"
banner(nome_programa)

tamanho_arquivo = float(input("insira o tamanho do arquivo em MB: "))
velocidade_internet = float(input("insira a velocidade do seu link de internet em Mbps: "))

tempo_download = (tamanho_arquivo / (velocidade_internet/8))/60

print("com um link de velocidade {}Mbps, o tempo aproximado para fazer o download de um arquivo de {}MB é de {:.2f} minutos".format(velocidade_internet, tamanho_arquivo, tempo_download))