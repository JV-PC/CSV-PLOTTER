import csv
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

print('nome do arquivo csv na pasta (sem a extensão):')
arq = input()

with open(arq + '.csv', 'r', encoding='utf8', newline='') as arquivo:
    leitor = csv.reader(arquivo)
    dados = list(leitor)


    print('opções para grafico:')
    indice = 0
    for opt in dados[14]:
        print (indice,"-",opt)
        indice = indice + 1

    print('Digite o indice para o X do seu gráfico:')
    graf1 = int(input())

    print('Digite o indice para o Y do seu gráfico:')
    graf2 = int(input())
    


valores_graf1 = [float(linha[graf1]) for linha in dados[18:] if linha]  # Ignora as primeiras 18 linhas
nome_graf1 = [linha[graf1] for linha in dados[14:16] if linha]

valores_graf2 = [float(linha[graf2]) for linha in dados[18:] if linha]  # Extrai os valores da coluna escolhida
nome_graf2 = [linha[graf2] for linha in dados[14:16] if linha]  # Extrai o nome e tipo da coluna escolhida


# Ajustar os dados para pegar apenas valores a cada x segundos
valores_graf1_amostrados = []
valores_graf2_amostrados = []
ultimo_tempo_amostrado = None
intervalo_amostragem = 1  # Intervalo de amostragem

for tempo, velocidade in zip(valores_graf1, valores_graf2):
    if ultimo_tempo_amostrado is None or tempo - ultimo_tempo_amostrado >= intervalo_amostragem:
        valores_graf1_amostrados.append(tempo)
        valores_graf2_amostrados.append(velocidade)
        ultimo_tempo_amostrado = tempo

plt.plot(valores_graf1_amostrados, valores_graf2_amostrados)
plt.xlabel(nome_graf1)
plt.ylabel(nome_graf2)
plt.title(nome_graf1[0] + ' x ' + nome_graf2[0])
plt.grid(True)

segundos_inteiros = [int(segundo) for segundo in valores_graf1_amostrados]
plt.xticks(valores_graf1_amostrados, segundos_inteiros)
    
plt.savefig(nome_graf1[0] + ' x ' + nome_graf2[0] + '.pdf', bbox_inches='tight')
plt.show()
