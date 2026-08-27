# 8. Atividade prática — Comparando os algoritmos
# numeros = [
#     38, 12, 45, 7, 29,
#     18, 41, 3, 25, 10
# ]
# Execute manualmente bubble_sort(), selection_sort() e insertion_sort(). Todos devem produzir:
# [3, 7, 10, 12, 18, 25, 29, 38, 41, 45]
# Depois, modifique cada algoritmo para contar comparações e trocas/movimentações.
# comparacoes = 0
# trocas = 0
# # a cada comparação:
# comparacoes += 1
# # quando houver troca:
# trocas += 1
# O objetivo é perceber que algoritmos pertencentes à mesma classe assintótica podem apresentar comportamentos
# concretos diferentes.


numeros = [
    38, 12, 45, 7, 29,
    18, 41, 3, 25, 10
]


# 1. Bubble Sort Otimizado (com flag 'trocou')
def bubble_otimizado(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        trocou = False
        for j in range(n - 1 - i):
            comparacoes += 1
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                trocou = True
        if not trocou:
            break

    print(f"Bubble Sort    -> Comparacoes: {comparacoes} | Trocas: {trocas}")
    return(lista)

# 2. Selection Sort
def selection(lista):
    n = len(lista)
    comparacoes = 0
    trocas = 0

    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if lista[j] < lista[menor]:
                menor = j

        # Só conta troca se o elemento mudar de lugar
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1

    print(f"Selection Sort -> Comparacoes: {comparacoes} | Trocas: {trocas}")
    return(lista)

# 3. Insertion Sort
def insertion(lista):
    n = len(lista)
    comparacoes = 0
    movimentacoes = 0

    for i in range(1, n):
        atual = lista[i]
        j = i - 1

        # Avaliação da comparação inicial
        if j >= 0:
            comparacoes += 1

        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            movimentacoes += 1
            j -= 1

        lista[j + 1] = atual
        movimentacoes += 1  # Reatribuição do elemento

    print(
        f"Insertion Sort -> Comparacoes: {comparacoes} | Movimentacoes: {movimentacoes}"
    )
    return[lista]

print(bubble_otimizado(numeros.copy()))
print(selection(numeros.copy()))
print(insertion(numeros.copy()))