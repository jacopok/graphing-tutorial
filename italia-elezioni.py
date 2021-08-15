#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
from tqdm import tqdm
import shapefile as shp
import json

# %%

comuni_df = pd.read_csv('data/camera_geopolitico_italia.csv')
# %%

elezioni_df = pd.read_csv('data/scrutiniCI_cm.csv')

elezioni_df = elezioni_df[elezioni_df.tipo_riga == 'LI']

elezioni_df = elezioni_df.filter(
    items = ['codice', 'descr_lista', 'perc', 'voti'])

#%%

percentuali = defaultdict(dict)
votanti = defaultdict(int)

# bad_vals = ['-', 'NaN,00', 'nan', float('NaN')]

for _, row in tqdm(elezioni_df.iterrows()):
    comune = comuni_df[comuni_df.id == row['codice']].nome.to_numpy()[0]

    perc_str = row['perc']
        
    try:
        perc = float(perc_str.replace(',', '.'))
    except (ValueError, AttributeError):
        perc = 0.
    
    percentuali[comune][row['descr_lista']] = perc

    voti_str = row['voti']
    try:
        voti = int(voti_str)
    except (ValueError, AttributeError):
        voti = 0
        
    votanti[comune] += voti

# %%

partiti = set()

for comune, voti in percentuali.items():
    for partito, perc in voti.items():
        partiti = partiti.union(set([partito]))
# %%

lista_1 = [
 '+EUROPA',
 '10 VOLTE MEGLIO',
 'AUTODETERMINATZIONE',
 "BLOCCO NAZIONALE PER LE LIBERTA'",
 'CIVICA POPOLARE LORENZIN',
 'ITALIA EUROPA INSIEME',
 'ITALIA NEL CUORE',
 'LIBERI E UGUALI',
 'LISTA DEL POPOLO PER LA COSTITUZIONE',
 'PARTITO COMUNISTA',
 'PARTITO DEMOCRATICO',
 'PARTITO REPUBBLICANO ITALIANO - ALA',
 'PARTITO VALORE UMANO',
 "PATTO PER L'AUTONOMIA",
 'PD-UV-UVP-EPAV',
 'PER UNA SINISTRA RIVOLUZIONARIA',
 'POTERE AL POPOLO!',
 'POUR TOUS PER TUTTI PE TCHEUT',
 'RINASCIMENTO MIR',
 'RISPOSTA CIVICA',
 'SIAMO',
 'SVP - PATT'
]
# sx

lista_2 = [
 "NOI CON L'ITALIA - UDC",
 "FI -FRAT. D'IT. -MOV.NUOVA VALLE D'AOSTA",
 'CASAPOUND ITALIA',
 'FORZA ITALIA',
 "FRATELLI D'ITALIA CON GIORGIA MELONI",
 'GRANDE NORD',
 'IL POPOLO DELLA FAMIGLIA',
 'ITALIA AGLI ITALIANI',
 'LEGA',
]
# dx

lista_3 = [
 'MOVIMENTO 5 STELLE',
]
# 5s

def indice_partito(partito):
    if partito in lista_1:
        return 0
    elif partito in lista_2:
        return 1
    elif partito in lista_3:
        return 2
    else:
        raise NotImplementedError

# %%

nomi_comuni, votanti_per_comune = list(votanti.keys()), np.array(list(votanti.values()))

perc_per_lista = np.zeros((len(votanti_per_comune), 3), dtype=float)

for comune, voti in percentuali.items():
    for partito, perc in voti.items():
        perc_per_lista[nomi_comuni.index(comune),indice_partito(partito)] += perc

#%%

with open('data/italy_geo.json') as file:
    italy_geo = json.loads(file.read())

italy_geo.pop()
lat_per_comune = {
    item['comune'].upper(): item['lat']
    for item in italy_geo
}
lon_per_comune = {
    item['comune'].upper(): item['lng']
    for item in italy_geo
}

    
#%%

lats = np.zeros_like(votanti_per_comune, dtype=float)

for i, com in enumerate(nomi_comuni):
    try:
        lats[i] += float(lat_per_comune[com])
    except KeyError:
        try:
            lats[i] += float(lat_per_comune[com.split(' ')[0]])
        except (KeyError, AttributeError):
            print(f'problems with {com}')
            
lats[lats == 0] += 50

lons = np.zeros_like(votanti_per_comune, dtype=float)

for i, com in enumerate(nomi_comuni):
    try:
        lons[i] += float(lon_per_comune[com])
    except KeyError:
        try:
            lons[i] += float(lon_per_comune[com.split(' ')[0]])
        except (KeyError, AttributeError):
            print(f'problems with {com}')
            
lons[lons == 0] += 40



# %%

x = np.sqrt(3/4) * (perc_per_lista[:, 1] - perc_per_lista[:, 0])
y = -perc_per_lista[:, 2] + 1 / 2 * (perc_per_lista[:, 1] + perc_per_lista[:, 0])

from matplotlib.cm import get_cmap, ScalarMappable
colormap = get_cmap('turbo')

rescale_lat = plt.Normalize(vmin = 36, vmax=47)    

plt.scatter(x, y,
    s=votanti_per_comune / 3e3,
    alpha=.3,
    c=colormap(rescale_lat(lats)))

plt.annotate('Sinistra', (-30 * np.sqrt(3) , 50))
plt.annotate('Destra', ( np.sqrt(3) * 30, 50))
plt.annotate('5 stelle', (0, -60))

plt.plot([0, 0], [0, 100], ls=':', c='black')
plt.plot([0, -np.sqrt(3/4) * 100], [0, -50], ls=':', c='black')
plt.plot([0, np.sqrt(3/4) * 100], [0, -50], ls=':', c='black')

plt.colorbar(ScalarMappable(norm=rescale_lat, cmap=colormap), label='Latitudine')

plt.xlim(-70, 70)
plt.ylim(-70, 60)

plt.scatter(0, 0, c='black', s=6)

plt.savefig('partitiecolori.pdf', dpi=150)

# %%


# %%
