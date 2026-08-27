# def busca_sequencial(lista, procurado):
#     for i in range(len(lista)):
#         if lista[i] == procurado:
#             return i
#     return -1

# nome = ["M","j","jj","B","G","A"]

# posicao = busca_sequencial(nome, "jj")

# print(posicao + 1)


def busca_binaria(lista, valor):
    inicio = 0 
    fim = len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2 
        if lista[meio] == valor:
            return meio 
        elif lista[meio] < valor:
            inicio = meio +1
        else:
            fim = meio - 1 
    return -1

numeros = [3, 7, 10, 15, 21, 28, 32, 40, 47, 51, 63]
posicao = busca_binaria(numeros, 51)

print(posicao + 1)


