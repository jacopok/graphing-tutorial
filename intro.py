#%%

xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

ys = []
for x in xs:
    ys.append(x**2)

print(ys)

# %%
import numpy as np

xs = np.arange(0, 10)

ys = xs ** 2

print(ys)

#%%

import matplotlib.pyplot as plt

plt.plot(xs, ys)

# plt.savefig('figures/parabola-v1.png', dpi=150, facecolor='white', transparent=True)

# %%

### ATTENZIONE

# Segue risultato dell'esercizio:

# - la funzione `np.arange` può essere sostituita da [`np.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace), che genera un array di punti equispaziati fra un minimo e un massimo. Come si può leggere nella documentazione, la si può chiamare, ad esempio, come `np.linspace(0, 9, num=100)`. In questo modo avremo più punti a disposizione e la curva apparirà più liscia. Nella descrizione della funzione della documentazione gli argomenti che appaiono come `argomento=valore` hanno un valore di _default_: possiamo modificarli se ne abbiamo bisogno, se non lo facciamo saranno inizializzati al default.

# - Possiamo aggiungere delle _etichette_ per i nostri assi: il comando è `plt.xlabel` per l'asse x (e rispettivamente `ylabel`), da dare dopo `plt.plot`, e al quale passare una _stringa_ come `'asse $x$'` (testo delimitato da degli apici singoli o doppi, i dollari invece sono i delimitatori di un ambiente "equazione" nel quale possiamo usare simboli matematici).

# - Possiamo aggiungere un _titolo_ con il comando `plt.title('Grafico cartesiano')`.
# - Possiamo aggiungere una _griglia_ con il comando `plt.grid('on')`
# - Possiamo aggiungere una _legenda_ (anche se in questo caso, con una sola curva, è un po' ridondante): per farlo dobbiamo dare un'etichetta alla curva, aggiungendo l'opzione `label = '$y=x^2$'` al comando `plot`, e generare la legenda alla fine con il comando `plt.legend()`. 

#

#

#

### ATTENZIONE

# rimuovere la soluzione? 

xs = np.linspace(0, 9, num=100)
ys = xs**2

plt.plot(xs, ys, label='$y = x^2$')
plt.xlabel('asse x')
plt.ylabel('asse y')
plt.title('Grafico cartesiano')
plt.grid('on')
plt.legend()
plt.savefig('figures/parabola-v2.png', dpi=150, facecolor='white', transparent=True)

# %%
