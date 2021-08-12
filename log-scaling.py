#%%

import numpy as np
import matplotlib.pyplot as plt

# %%

# Generiamo dei dati secondo una distribuzione log-uniforme

rng = np.random.default_rng()

def loguniform(a, b, rng=rng, **kwargs):
    return np.exp(rng.uniform(low=np.log(a), high=np.log(b), **kwargs))

data = loguniform(1, 100, size=10_000)


# %%

with plt.xkcd():
    plt.title('Dati fittizi!')
    plt.hist(data, bins=30, density=True)
    plt.xlabel('Reddito $R$, in migliaia di euro')
    plt.ylabel('Densità di probabilità,\n in 1/(1000 euro)')
    plt.tight_layout()
    plt.savefig('fictitious-income-linear.png', dpi=150)

# %%

with plt.xkcd():
    plt.title('Dati fittizi!')
    plt.hist(data, bins=30, density=True)
    plt.xscale('log')
    plt.xlabel('Reddito $R$, in migliaia di euro')
    plt.ylabel('Densità di probabilità,\n in 1/(1000 euro)')
    plt.tight_layout()
    plt.savefig('fictitious-income-log1.png', dpi=150)
# %%

with plt.xkcd():
    plt.title('Dati fittizi!')
    plt.hist(np.log10(data), bins=30, density=True)
    plt.xlabel('Logaritmo del reddito: $\\log_{10} R$')
    plt.ylabel('Densità di probabilità, in 1/decade')
    plt.tight_layout()
    plt.savefig('fictitious-income-log2.png', dpi=150)
# %%
