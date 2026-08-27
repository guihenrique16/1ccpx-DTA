def bubble_sort(lista):
    n = len(lista)

    for i in range(n):
        trocou = False
        print(f"\nPassagem {i + 1}")
        print(lista)

        for j in range(n - 1 - i):
            print(f"Comparando {lista[j]} com {lista[j + 1]}")

            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

                trocou = True
                print("Troca realizada!")
                print(lista)
            else:
                print("Ja ordenado")
                
        if not trocou:
            print("Nenhuma troca realizada nesta passagem. Lista já ordenada!")
            break
        
    return lista

numeros = [5, 3, 8, 2]
bubble_sort(numeros)


