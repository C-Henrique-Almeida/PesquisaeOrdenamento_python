import matplotlib as mpl
import matplotlib.pyplot as plt


import numpy as np
from random import randint
from time import perf_counter, sleep
from functools import reduce





  
#pegar o numero maior de digitos
def get_num_digits(lista):
    return len(str(max(lista)))


#achatar lista
def flatten(lista):
  return reduce(lambda x, y: x + y, lista)

#radixsort
def radixsort(lista):
  num_digits = get_num_digits(lista)
  for digit in range(0, num_digits): 
    #vetor zerado
    c = [[] for i in  range(10)]
    for item in lista:
      #colocar os itens em seu devido espaço no veto c
      num = item // 10 ** (digit) % 10 #pega o digito escolhido
      c[num].append(item)
    lista = flatten(c)
  return lista




# lista 0
inicio0 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 9999)]
b = radixsort(lista)
print("\n em ordem")
print(b)
fim0 = perf_counter()
print("Tempo duração em segundos :", fim0 - inicio0)

# pior caso lista 0
b.sort(reverse=True)

inicio00 = perf_counter()
b = radixsort(b)
print("\n em ordem")
print(b)
fim00 = perf_counter()
print("Tempo duração em segundos :", fim00 - inicio00)

# lista 2
inicio2 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 19999)]
b = radixsort(lista)
print("\n \n \n \n \n \n \n LISTA 2 em ordem")
print(b)
fim2 = perf_counter()
print("Tempo duração em segundos :", fim2 - inicio2)

# pior caso lista 2
b.sort(reverse=True)

inicio22 = perf_counter()
b = radixsort(b)
print("\n em ordem")
print(b)
fim22 = perf_counter()
print("Tempo duração em segundos :", fim22 - inicio22)

# lista 3
inicio3 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 29999)]
b = radixsort(lista)
print("\n \n \n \n \n \n \n LISTA 2 em ordem")
print(b)
fim3 = perf_counter()
print("Tempo duração em segundos :", fim3 - inicio3)

# pior caso lista 3
b.sort(reverse=True)

inicio33 = perf_counter()
b = radixsort(b)
print("\n em ordem")
print(b)
fim33 = perf_counter()
print("Tempo duração em segundos :", fim33 - inicio33)

# lista 4
inicio4 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 39999)]
b = radixsort(lista)
print("\n \n \n \n \n \n \n LISTA 2 em ordem")
print(b)
fim4 = perf_counter()
print("Tempo duração em segundos :", fim4 - inicio4)

# pior caso lista 4
b.sort(reverse=True)

inicio44 = perf_counter()
b = radixsort(b)
print("\n em ordem")
print(b)
fim44 = perf_counter()
print("Tempo duração em segundos :", fim44 - inicio44)

# lista 5
inicio5 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 49999)]
b = radixsort(lista)
print("\n \n \n \n \n \n \n LISTA 2 em ordem")
print(b)
fim5 = perf_counter()
print("Tempo duração em segundos :", fim5 - inicio5)

# pior caso lista 5
b.sort(reverse=True)

inicio55 = perf_counter()
b = radixsort(b)
print("\n em ordem")
print(b)
fim55 = perf_counter()
print("Tempo duração em segundos :", fim55 - inicio55)

# lista 6
inicio6 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 79999)]
b = radixsort(lista)
print("\n \n \n \n \n \n \n LISTA 2 em ordem")
print(b)
fim6 = perf_counter()
print("Tempo duração em segundos :", fim6 - inicio6)

# pior caso lista 6
b.sort(reverse=True)

inicio66 = perf_counter()
b = radixsort(b)
print("\n em ordem")
print(b)
fim66 = perf_counter()
print("Tempo duração em segundos :", fim66 - inicio66)

# lista 7
inicio7 = perf_counter()
lista = [randint(0, 100000) for p in range(0, 99999)]
b = radixsort(lista)
print("\n \n \n \n \n \n \n LISTA 2 em ordem")
print(b)
fim7 = perf_counter()
print("Tempo duração em segundos :", fim7 - inicio7)

# pior caso lista 7
b.sort(reverse=True)

inicio77 = perf_counter()
b = radixsort(b)
print("\n em ordem")
print(b)
fim77 = perf_counter()
print("Tempo duração em segundos :", fim77 - inicio77)


# Plot normal
plt.plot([9999, 19999, 29999, 39999, 49999, 79999, 99999],
         [fim0-inicio0, fim2-inicio2, fim3-inicio3, fim4-inicio4, fim5-inicio5, fim6-inicio6, fim7-inicio7], [9999, 19999, 29999, 39999, 49999, 79999, 99999], [
         fim00-inicio00, fim22-inicio22, fim33-inicio33, fim44-inicio44, fim55-inicio55, fim66-inicio66, fim77-inicio77])
plt.ylabel('TEMPO DE ORDENAMENTO')
plt.xlabel('TAMANHO DA LISTA')
plt.show()





