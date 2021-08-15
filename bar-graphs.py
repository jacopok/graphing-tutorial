#%%

import numpy as np
import matplotlib.pyplot as plt

labels = ['a', 'b', 'c']
data = np.array([1, 2, 3])

plt.bar(labels, data, yerr=np.sqrt(data))
plt.savefig('bars.pdf', dpi=150)
# %%
