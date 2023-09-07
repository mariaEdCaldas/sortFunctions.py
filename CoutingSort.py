#implementando o couting sort
def countingSort(vetor, tamanho, maior):
    saida = [0] * tamanho
    contador = [0] * (maior + 1)

    for i in range(tamanho):
        contador[vetor[i]] += 1

    for i in range(1, maior + 1):
        contador[i] += contador[i - 1]

    for i in range(tamanho - 1, -1, -1):
        saida[contador[vetor[i]] - 1] = vetor[i]
        contador[vetor[i]] -= 1

    for i in range(tamanho):
        vetor[i] = saida[i]

