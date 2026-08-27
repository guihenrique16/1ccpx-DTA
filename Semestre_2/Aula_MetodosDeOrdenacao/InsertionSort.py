def insertion_sort(lista):
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        print(lista)
        print(f"\nPassagem {i}: Encaixando o número {atual}")

        while j >= 0 and lista[j] > atual:
            print(f"  {lista[j]} é maior que {atual} -> movendo {lista[j]} para a direita")
            lista[j + 1] = lista[j]
            j -= 1
            print(f"  Lista temporária: {lista}")
        
        lista[j + 1] = atual
        print(f"  Encaixou {atual} na posição {j + 1}")
        print(f"Estado da lista após Passagem {i}: {lista}")

    return lista


numeros = [5, 3, 8, 2]
print("\nResultado final:", insertion_sort(numeros))