containers_C = [ 
    98, 655, 603, 667, 986, 719, 531, 568, 716, 335, 301, 257, 690, 790, 427, 557, 307, 187, 167, 684, 
    194, 705, 549, 457, 759, 697, 284, 699, 902, 525, 349, 318, 606, 286, 341, 149, 205, 609, 547, 583, 
    271, 375, 632, 861, 648, 973, 917, 235, 876, 733, 781, 921, 126, 644, 347, 576, 128, 799, 631, 176, 
    793, 820, 146, 83, 201, 958, 225, 830, 171, 936, 214, 229, 730, 591, 764, 999, 433, 119, 651, 622, 
    173, 620, 804, 944, 92, 253, 841, 312, 867, 825, 121, 401, 594, 598, 111, 475, 154, 590, 526, 518, 
    947, 461, 409, 539, 563, 714, 183, 14, 870, 392, 358, 447, 905, 278, 742, 449, 504, 482, 438, 384, 
    132, 72, 808, 888, 160, 615, 406, 246, 396, 934, 470, 672, 663, 754, 274, 586, 913, 678, 270, 455, 
    332, 691, 116, 296, 414, 454, 352, 155, 491, 910, 361, 932, 287, 788, 756, 105, 137, 571, 845, 198, 
    889, 261, 862, 681, 552, 536, 241, 874, 339, 512, 773, 365, 293, 704, 739, 443, 960, 266, 323, 995, 
    712, 856, 978, 725, 208, 245, 928, 981, 517, 319, 139, 835, 240, 748, 64, 812, 420, 381, 203, 823 
]

# Missão 1
def analisar_carga(lista):
    quantidade = len(lista)

    menor = lista[0]
    maior = lista[0]

    for valor in lista:
        if valor < menor:
            menor = valor

        if valor > maior:
            maior = valor

    return quantidade, menor, maior

# CHAMANDO A FUNCAO
quantidade, menor_codigo, maior_codigo = analisar_carga(containers_C)
    

# Missão 2
def busca_linear(lista, codigo):
    comparacoes = 0

    for i in range(len(lista)):

        comparacoes += 1

        if lista[i] == codigo:
            return i, comparacoes

    return -1, comparacoes

# CHAMANDO A FUNCAO
# TESTE COM CODIGO EXISTENTE
codigo_existente = 823

posicao_linear, comparacoes_linear = busca_linear(
    containers_C,
    codigo_existente
)

# TESTE COM CODIGO INEXISTENTE
codigo_inexistente = 1001

posicao_linear_inexistente, comparacoes_linear_inexistente = busca_linear(
    containers_C,
    codigo_inexistente
)


#MISSAO 03
def ordenar(lista):
    comparacoes = 0
    movimentacoes = 0
    n = len(lista)

    for i in range(n - 1):
        menor = i

        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            movimentacoes += 1

    return lista, comparacoes, movimentacoes

# CHAMANDO A FUNCAO
ordenada, comparacoes_ordenacao, movimentacoes = ordenar(
    containers_C[:]
)

#MISSAO 04
def busca_binaria(lista, codigo):
    inicio = 0
    fim = len(lista) - 1

    comparacoes = 0

    while inicio <= fim:

        meio = (inicio + fim) // 2
        #Critério de contagem
        #Consideramos 1 comparação a cada elemento central
        #Analisado pela busca binária
        comparacoes += 1

        if lista[meio] == codigo:
            return meio, comparacoes

        elif lista[meio] < codigo:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1, comparacoes

# CHAMANDO A FUNCAO
# TESTE COM CODIGO EXISTENTE
posicao_binaria, comparacoes_binaria = busca_binaria(
    ordenada,
    codigo_existente
)

# TESTE COM CODIGO INEXISTENTE
posicao_binaria_inexistente, comparacoes_binaria_inexistente = busca_binaria(
    ordenada,
    codigo_inexistente
)


print("========== CENTRAL DE TRIAGEM ==========")

print(f"Quantidade de contêineres: {quantidade}")
print(f"Menor código: {menor_codigo}")
print(f"Maior código: {maior_codigo}")

print()

print("--------- ORDENAÇÃO ----------")
print("Algoritmo: Selection Sort")
print(f"Comparações: {comparacoes_ordenacao}")
print(f"Movimentações: {movimentacoes}")

print()

print("---------- BUSCAS -----------")
print(f"Código procurado: {codigo_existente}")

print(
    f"Busca Linear - Posição: {posicao_linear} "
    f"| Comparações: {comparacoes_linear}"
)

print(
    f"Busca Binária - Posição: {posicao_binaria} "
    f"| Comparações: {comparacoes_binaria}"
)

print("=================================")

# TESTE CODIGOS INEXISTENTES
print()
print("----- TESTES COM CÓDIGO INEXISTENTE -----")

print(f"Código procurado: {codigo_inexistente}")

print(
    f"Busca Linear - Posição: {posicao_linear_inexistente} "
    f"| Comparações: {comparacoes_linear_inexistente}"
)

print(
    f"Busca Binária - Posição: {posicao_binaria_inexistente} "
    f"| Comparações: {comparacoes_binaria_inexistente}"
)


