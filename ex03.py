# 3) Desenvolva um programa que receba como entrada do usuário a população de uma cidade
# e a taxa de crescimento anual da população. Apresentar como resultado qual será a população
# da cidade em 15 anos.

populacao = int(input('Informe a quantidade de habitantes: '))
taxa_crescimento = float(input('Informe a taxa de crescimento: '))

for i in range(1, 16):
    populacao += int(populacao * taxa_crescimento / 100)
    print(f"Ápos{i}º ano -> {populacao}")


