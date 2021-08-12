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
plt.savefig('figures/parabola-v1.png', dpi=150, facecolor='white', transparent=True)

# %%

### ATTENZIONE

# Segue risultato dell'esercizio

#

#

### ATTENZIONE

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
