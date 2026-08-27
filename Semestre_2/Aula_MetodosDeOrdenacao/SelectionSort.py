def selection_sort(lista):
    n = len(lista)

    for i in range(n-1):
        menor = i
        print(f"\nPassagem {i + 1} (buscando o menor elemento para o índice {i})")
        print(lista)

        for j in range(i + 1, n):
            print(f"  Comparando {lista[j]} com o menor atual ({lista[menor]})")

            if lista[j] < lista[menor]:
                menor = j
                print(f"  --> Novo menor encontrado: {lista[menor]} (no índice {j})")
        
        print('ordenando a lista')        
        lista[i], lista[menor] = lista[menor], lista[i]        
        print(lista)
                
    return lista


numeros = [5, 3, 8, 2]
selection_sort(numeros)