def heapify(vetor, tam, i):
    maior = i
    q = 2 * i + 1
    r = 2 * i + 2

    if q < tam and vetor[q] > vetor[i] :
        maior = q
    if r < tam and  vetor[r] > vetor[maior]:
        maior = r
    if maior != i:
        vetor[i], vetor[maior] = vetor[maior], vetor[i]
        heapify(vetor, tam, maior)

def heapSort(vetor):
    tam = len(vetor)

    for i in range(tam // 2, -1, -1):
        heapify(vetor, tam, i)
    for i in range(tam - 1, 0, -1):
        vetor[i], vetor[0] = vetor[0], vetor[i]
        heapify(vetor, i, 0)
