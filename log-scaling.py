#%%

import numpy as np
import matplotlib.pyplot as plt

#%%

# Esempio di dati esponenziali con un asse lineare -
# grafici che abbiamo purtroppo visto spesso l'anno scorso

xs = np.linspace(0, 10)
ys = np.exp(xs) * np.random.normal(loc=1., scale=.1, size=xs.shape)

with plt.xkcd():
    plt.plot(xs, ys)
    plt.savefig('figures/exponential-linear.png', dpi=150)

#%%

# gli stessi dati con un asse logaritmico

with plt.xkcd():
    plt.semilogy(xs, ys)
    plt.savefig('figures/exponential-log.png', dpi=150)

# %%

# Generiamo dei dati secondo una distribuzione log-uniforme

rng = np.random.default_rng()

def loguniform(a, b, rng=rng, **kwargs):
    return np.exp(rng.uniform(low=np.log(a), high=np.log(b), **kwargs))

data = loguniform(1, 100, size=10_000)

avg = np.average(data)
std = np.std(data)
med = np.median(data)

# %%

with plt.xkcd():
    plt.title('Dati fittizi!')
    plt.hist(data, bins=50, density=True)
    plt.axvline(avg, label='Media', c='green')
    plt.axvline(med, label='Mediana', c='orange')
    plt.xlabel('Reddito $R$, in migliaia di euro')
    plt.ylabel('Densità di probabilità,\n in 1/(1000 euro)')
    plt.legend()
    plt.tight_layout()
    plt.savefig('figures/fictitious-income-linear.png', dpi=150)

# %%

with plt.xkcd():
    plt.title('Dati fittizi!')
    v = plt.hist(data, bins=30, density=True)
    plt.xscale('log')
    plt.xlabel('Reddito $R$, in migliaia di euro')
    plt.ylabel('Densità di probabilità,\n in 1/(1000 euro)')
    plt.tight_layout()
    plt.savefig('figures/fictitious-income-log1.png', dpi=150)

#%%

# Se invece non mettiamo i bins! 
with plt.xkcd():
    v = plt.hist(data, bins=30, density=True)
    plt.plot( (v[1][1:] + v[1][:-1] ) / 2, v[0])
    plt.xscale('log')

# %%

with plt.xkcd():
    plt.title('Dati fittizi!')
    plt.hist(np.log10(data), bins=30, density=True)
    plt.xlabel('Logaritmo del reddito: $\\log_{10} R$')
    plt.ylabel('Densità di probabilità, in 1/decade')
    plt.tight_layout()
    plt.savefig('figures/fictitious-income-log2.png', dpi=150)
# %%
