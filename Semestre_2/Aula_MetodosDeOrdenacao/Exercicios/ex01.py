# Bloco 1 — Encontre o bug (debug de código)
# Q1. O código abaixo tenta implementar Insertion Sort contando comparações corretamente. 
# Encontre e corrija o erro de contagem:
# def insertion(lista):
#     n = len(lista)
#     comparacoes = 0
#     for i in range(1, n):
#         atual = lista[i]
#         j = i - 1
#         if j >= 0:
#             comparacoes += 1
#         while j >= 0 and lista[j] > atual:
#             lista[j + 1] = lista[j]
#             j -= 1
#         lista[j + 1] = atual
#     return lista

def insertion(lista):
    n = len(lista)
    comparacoes = 0
    for i in range(1, n):
        atual = lista[i]
        j = i - 1
        print(f'\n {lista}')
        print(f"\nPassagem {i}: Encaixando o número {atual}")
        
        if j >= 0:
            comparacoes += 1
        while j >= 0 and lista[j] > atual:
            comparacoes += 1
            print(f"  {lista[j]} é maior que {atual} -> movendo {lista[j]} para a direita")
            lista[j + 1] = lista[j]
            # print(f"  {lista[j + 1]} é maior que {} -> nao")
            j -= 1
            print(f"  Lista temporária: {lista}")


        lista[j + 1] = atual
        print(f"    Encaixou {atual} na posição {j + 1}")
        print(f"Estado da lista após Passagem {i}: {lista}")

    print(comparacoes)
    return lista

# Q2. O trecho abaixo pretende ser um Selection Sort, mas tem um bug sutil que faz ele nunca ordenar nada. 
# Ache o erro:
# def selection_bug(lista):
#     n = len(lista)
#     for i in range(n):
#         menor = lista[i]          # <-- suspeito
#         for j in range(i + 1, n):
#             if lista[j] < menor:
#                 menor = lista[j]
#         lista[i], menor = menor, lista[i]
#     return lista

def selection_bug(lista):
    n = len(lista)
    for i in range(n):
        menor = i          
        for j in range(i + 1, n):
            if lista[j] < lista[menor]:
                menor = j
        lista[i], lista[menor] = lista[menor], lista[i]
    return lista

numeros = [11, 8, 51, 12, 22, 17]
# print(insertion(numeros.copy()))
print(selection_bug(numeros.copy()))


