# Bloco 2 — Trace manual (dry run)

numeros = [9, 1, 6, 3]

# Q3. Dado [9, 1, 6, 3]
# escreva o estado completo da lista após cada passagem externa (não cada comparação) do Bubble Sort clássico (sem otimização de flag).

def bubble_sort(lista):
    n = len(lista)

    print(lista)

    for i in range(n):
        for j in range(n - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

            print(lista)
        print(f'passagem {i + 1}')
    return(lista)

print(bubble_sort(numeros.copy()))


# Q4. Dado [9, 1, 6, 3]
# faça o mesmo para o Selection Sort — mostre o estado da lista após cada iteração de i, e diga qual foi o índice menor escolhido em cada uma.

# def selection(lista):


# Q5. Dado [9, 1, 6, 3]
# faça o trace do Insertion Sort mostrando o valor de atual e o estado da lista a cada iteração de i.


