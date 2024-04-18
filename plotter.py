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
        print(indice, "-", opt)
        indice = indice + 1

    print('Digite o indice para o X do seu gráfico:')
    graf1 = int(input())

    print('Digite o indice para o Y do seu gráfico:')
    graf2 = int(input())

valores_graf1 = [float(linha[graf1]) for linha in dados[18:] if linha]
nome_graf1 = [linha[graf1] for linha in dados[14:16] if linha]

valores_graf2 = [float(linha[graf2]) for linha in dados[18:] if linha]
nome_graf2 = [linha[graf2] for linha in dados[14:16] if linha]

# Solicita ao usuário os limites para os valores
print('Digite o valor mínimo para a amostragem:')
limite_minimo = float(input())
print('Digite o valor máximo para a amostragem:')
limite_maximo = float(input())

# Solicita ao usuário o intervalo de amostragem
print('Digite o intervalo para a amostragem:')
intervalo_amostragem = float(input())

# Filtra os dados para estar dentro dos limites especificados e amostra a cada intervalo
valores_graf1_filtrados = []
valores_graf2_filtrados = []
for i in range(len(valores_graf1)):
    if limite_minimo <= valores_graf1[i] <= limite_maximo:
        if i % int(intervalo_amostragem) == 0:
            valores_graf1_filtrados.append(valores_graf1[i])
            valores_graf2_filtrados.append(valores_graf2[i])


plt.figure().set_figwidth(30)
plt.plot(valores_graf1_filtrados, valores_graf2_filtrados)
plt.xlabel(nome_graf1)
plt.ylabel(nome_graf2)
plt.title(nome_graf1[0] + ' x ' + nome_graf2[0])
plt.grid(True)

# Ajusta os ticks do eixo x para mostrar apenas os segundos inteiros
segundos_inteiros = [int(segundo) for segundo in valores_graf1_filtrados]
plt.xticks(valores_graf1_filtrados, segundos_inteiros)

plt.savefig(nome_graf1[0] + ' x ' + nome_graf2[0] + '.pdf', bbox_inches='tight')
plt.tight_layout()
plt.show()
