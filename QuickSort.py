#implementando o Quick Sort
def partition(vet, p, r):
    x = vet[r]
    i = p - 1
    for j in range(p, r):
        if vet[j] <= x:
            i = i + 1
            vet[i], vet[j] = vet[j], vet[i]
    vet[i + 1], vet[r] = vet[r], vet[i + 1]
    return i + 1

def quicksort(vet, p, r):
    stack = [(p, r)]
    while stack:
        p, r = stack.pop()
        if p < r:
            q = partition(vet, p, r)
            if q > p + 1:
                stack.append((p, q - 1))
            if q < r - 1:
                stack.append((q + 1, r))
