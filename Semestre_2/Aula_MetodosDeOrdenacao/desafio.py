# 9. Desafio rápido
# ordenada = [1, 2, 3, 4, 5, 6, 7, 8]
# invertida = [8, 7, 6, 5, 4, 3, 2, 1]
# quase_ordenada = [1, 2, 3, 5, 4, 6, 7, 8]
# Execute os três algoritmos e compare as operações. Questão: o estado inicial dos dados interfere igualmente
# nos três algoritmos?
# A discussão introduz melhor caso, caso médio, pior caso, adaptabilidade, estabilidade, custo de comparações e
# custo de movimentações.

def testar_algoritmos():
    # Definição dos cenários
    cenarios = {
        "1. Ordenada": [1, 2, 3, 4, 5, 6, 7, 8],
        "2. Invertida": [8, 7, 6, 5, 4, 3, 2, 1],
        "3. Quase Ordenada": [1, 2, 3, 5, 4, 6, 7, 8],
    }

    print(
        f"{'Cenario':<18} | {'Algoritmo':<15} | {'Comparacoes':<12} | {'Trocas/Mov':<10}"
    )
    print("-" * 65)

    for nome_cenario, dados in cenarios.items():
        # 1. Bubble Sort (Otimizado com flag)
        lista = dados.copy()
        n = len(lista)
        comp_b, trocas_b = 0, 0
        for i in range(n):
            trocou = False
            for j in range(n - 1 - i):
                comp_b += 1
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocas_b += 1
                    trocou = True
            if not trocou:
                break
        print(
            f"{nome_cenario:<18} | {'Bubble (Otim.)':<15} | {comp_b:<12} | {trocas_b:<10}"
        )

        # 2. Selection Sort
        lista = dados.copy()
        comp_s, trocas_s = 0, 0
        for i in range(n):
            menor = i
            for j in range(i + 1, n):
                comp_s += 1
                if lista[j] < lista[menor]:
                    menor = j
            if menor != i:
                lista[i], lista[menor] = lista[menor], lista[i]
                trocas_s += 1
        print(
            f"{'':<18} | {'Selection':<15} | {comp_s:<12} | {trocas_s:<10}"
        )

        # 3. Insertion Sort
        lista = dados.copy()
        comp_i, mov_i = 0, 0
        for i in range(1, n):
            atual = lista[i]
            j = i - 1
            while j >= 0:
                comp_i += 1
                if lista[j] > atual:
                    lista[j + 1] = lista[j]
                    mov_i += 1
                    j -= 1
                else:
                    break
            lista[j + 1] = atual
            mov_i += 1
        print(
            f"{'':<18} | {'Insertion':<15} | {comp_i:<12} | {mov_i:<10}"
        )
        print("-" * 65)


testar_algoritmos()