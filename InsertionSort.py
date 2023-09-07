#implementando o insertion sort
def insertionSort(vetor):

    for i in range(0, len(vetor)): #1
        chave = vetor[i]

        j = i-1
        while j >= 0 and chave < vetor[j] :
            vetor[j + 1] = vetor[j]
            j -= 1

        vetor[j + 1] = chave
