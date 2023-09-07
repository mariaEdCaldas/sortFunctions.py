#implementando o Selection sort
def selectionSort(vet):
    n = len(vet)
    for i in range(0, n-1):
        minVal = vet[i]
        minInd = i
        for j in range(i+1, n):
            if(vet[j] < minVal):
                minVal = vet[j]
                minInd = j
        (vet[i], vet[minInd]) = (vet[minInd], vet[i])
