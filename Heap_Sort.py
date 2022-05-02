import matplotlib as mpl
import matplotlib.pyplot as plt


import numpy as np
from random import randint
from time import perf_counter, sleep


# ORDENAR AS RAIZES
def heap(lista, n, i):
    root = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and lista[left] > lista[root]:

        root = left

    if right < n and lista[right] > lista[root]:

        root = right

    if root != i:
        lista[root], lista[i] = lista[i], lista[root]
        heap(lista, n, root)


def heapsort(lista):
    n = len(lista)

    # CHAMA A FUNÇÃO DE ORDENAMENTO DE RAIZES COMEÇANDO PELO MEIO DO VETOR
    for i in range(n // 2 - 1, -1, -1):
        heap(lista, n, i)

    # SEGUNDA PARTE DO ALGORITMO ONDE PRGAMOS AS RAIZES(MAIORES ELEMENTOS) E COLOCAMOS PARA O FIM
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heap(lista, i, 0)


# lista 0
inicio0 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 9999)]
heapsort(lista)
print("\n em ordem")
print(lista)
fim0 = perf_counter()
print("Tempo duração em segundos :", fim0 - inicio0)

# pior caso lista 0
lista.sort(reverse=True)

inicio00 = perf_counter()
heapsort(lista)
print("\n em ordem")
print(lista)
fim00 = perf_counter()
print("Tempo duração em segundos :", fim00 - inicio00)

# lista 2
inicio2 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 19999)]
heapsort(lista)
print("\n \n \n \n \n \n \n LISTA 2 em ordem")
print(lista)
fim2 = perf_counter()
print("Tempo duração em segundos :", fim2 - inicio2)

# pior caso lista 2
lista.sort(reverse=True)

inicio22 = perf_counter()
heapsort(lista)
print("\n em ordem")
print(lista)
fim22 = perf_counter()
print("Tempo duração em segundos :", fim22 - inicio22)

# lista 3
inicio3 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 29999)]
heapsort(lista)
print("\n \n \n \n \n \n \n LISTA 3 em ordem")
print(lista)
fim3 = perf_counter()
print("Tempo duração em segundos :", fim3 - inicio3)

# pior caso lista 3
lista.sort(reverse=True)

inicio33 = perf_counter()
heapsort(lista)
print("\n em ordem")
print(lista)
fim33 = perf_counter()
print("Tempo duração em segundos :", fim33 - inicio33)

# lista 4
inicio4 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 39999)]
heapsort(lista)
print("\n \n \n \n \n \n \n LISTA 4 em ordem")
print(lista)
fim4 = perf_counter()
print("Tempo duração em segundos :", fim4 - inicio4)

# pior caso lista 4
lista.sort(reverse=True)

inicio44 = perf_counter()
heapsort(lista)
print("\n em ordem")
print(lista)
fim44 = perf_counter()
print("Tempo duração em segundos :", fim44 - inicio44)

# lista 5
inicio5 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 49999)]
heapsort(lista)
print("\n \n \n \n \n \n \n LISTA 5 em ordem")
print(lista)
fim5 = perf_counter()
print("Tempo duração em segundos :", fim5 - inicio5)

# pior caso lista 5
lista.sort(reverse=True)

inicio55 = perf_counter()
heapsort(lista)
print("\n em ordem")
print(lista)
fim55 = perf_counter()
print("Tempo duração em segundos :", fim55 - inicio55)

# lista 6
inicio6 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 79999)]
heapsort(lista)
print("\n \n \n \n \n \n \n LISTA 6 em ordem")
print(lista)
fim6 = perf_counter()
print("Tempo duração em segundos :", fim6 - inicio6)

# pior caso lista 6
lista.sort(reverse=True)

inicio66 = perf_counter()
heapsort(lista)
print("\n em ordem")
print(lista)
fim66 = perf_counter()
print("Tempo duração em segundos :", fim66 - inicio66)

# lista 7
inicio7 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 99999)]
heapsort(lista)
print("\n \n \n \n \n \n \n LISTA 7 em ordem")
print(lista)
fim7 = perf_counter()
print("Tempo duração em segundos :", fim7 - inicio7)

# pior caso lista 7
lista.sort(reverse=True)

inicio77 = perf_counter()
heapsort(lista)
print("\n em ordem")
print(lista)
fim77 = perf_counter()
print("Tempo duração em segundos :", fim77 - inicio77)


# Plot normal
plt.plot([9999, 19999, 29999, 39999, 49999, 79999, 99999],
         [fim0-inicio0, fim2-inicio2, fim3-inicio3, fim4-inicio4, fim5-inicio5, fim6-inicio6, fim7-inicio7], [9999, 19999, 29999, 39999, 49999, 79999, 99999], [
         fim00-inicio00, fim22-inicio22, fim33-inicio33, fim44-inicio44, fim55-inicio55, fim66-inicio66, fim77-inicio77])
plt.ylabel('TEMPO DE ORDENAMENTO')
plt.xlabel('TAMANHO DA LISTA')
plt.show()











