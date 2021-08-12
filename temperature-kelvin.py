#%%

import numpy as np
import matplotlib.pyplot as plt


mean_monthly_temperature_rome_celsius = np.array([7.5,
    8.2,
    10.2,
    12.6,
    17.2,
    21.1,
    24.1,
    24.5,
    20.8,
    16.4,
    11.4,
    8.4])
    
months = ['Gennaio',
'Febbraio',
'Marzo',
'Aprile',
'Maggio',
'Giugno',
'Luglio',
'Agosto',
'Settembre',
'Ottobre',
'Novembre',
'Dicembre']

mean_monthly_temperature_rome_kelvin = mean_monthly_temperature_rome_celsius + 273.15

plt.bar(months, mean_monthly_temperature_rome_kelvin)
plt.ylabel('Temperatura media a Roma (gradi Kelvin)')
plt.ylim(0, 300)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature-kelvin.png', dpi=150, facecolor='white', transparent=False)

# %%
