#implementando o Merge Sort
def merge(vetor, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    left = [0] * (n1 + 1)
    right = [0] * (n2 + 1)

    for i in range(n1):#(0, n1)//(1, n1)
        left[i] = vetor[p + i]
    
    for i in range(0, n2):
        right[i] = vetor[q + i + 1]

    left[n1] = float("inf")
    right[n2] = float("inf")
    i = 0
    j = 0

    for k in range(p, r + 1):
        if left[i] <= right[j]:
            vetor[k] = left[i]
            i += 1
        else:
            vetor[k] = right[j]
            j += 1

def mergeSort(vetor, p, r):
    if p < r:
        q = (p + r) // 2 
        mergeSort(vetor, p, q)
        mergeSort(vetor, q + 1, r)
        merge(vetor, p, q, r)
