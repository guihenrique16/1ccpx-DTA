# Sorteie um vetor aleatório de 200 elementos, faça as ordenações no mesmo vetor e imprima a quantidade de trocas de cada um dos casos no final do código, conforme explicado em aula.

import random

vetor_original = [random.randint(1, 1000) for _ in range(200)]

# Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    trocas = 0
    for i in range(n):
        trocou = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocas += 1
                trocou = True
        if not trocou:
            break
    return trocas


# Selection Sort
def selection_sort(lista):
    n = len(lista)
    trocas = 0
    for i in range(n):
        menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        if menor != i:
            lista[i], lista[menor] = lista[menor], lista[i]
            trocas += 1
    return trocas


# Insertion Sort
def insertion_sort(lista):
    n = len(lista)
    movimentacoes = 0
    for i in range(1, n):
        atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > atual:
            lista[j + 1] = lista[j]
            movimentacoes += 1
            j -= 1
        lista[j + 1] = atual
        movimentacoes += 1
    return movimentacoes

trocas_bubble = bubble_sort(vetor_original.copy())
trocas_selection = selection_sort(vetor_original.copy())
mov_insertion = insertion_sort(vetor_original.copy())


print("=== RESULTADO DA ORDENACAO (200 ELEMENTOS) ===")
print(f"Bubble Sort    -> Quantidade de Trocas: {trocas_bubble}")
print(f"Selection Sort -> Quantidade de Trocas: {trocas_selection}")
print(f"Insertion Sort -> Quantidade de Movimentacoes: {mov_insertion}")