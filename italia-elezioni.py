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
 'CIVICA POPOLARE LORENZIN',
 'ITALIA EUROPA INSIEME',
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
 'RINASCIMENTO MIR',
 'RISPOSTA CIVICA',
 'SIAMO',
 'SVP - PATT'
]
# sx

lista_2 = [
 "NOI CON L'ITALIA - UDC",
 'ITALIA NEL CUORE',
 "BLOCCO NAZIONALE PER LE LIBERTA'",
 "FI -FRAT. D'IT. -MOV.NUOVA VALLE D'AOSTA",
 'CASAPOUND ITALIA',
 'FORZA ITALIA',
 "FRATELLI D'ITALIA CON GIORGIA MELONI",
 'GRANDE NORD',
 'IL POPOLO DELLA FAMIGLIA',
 'ITALIA AGLI ITALIANI',
 'LEGA',
 'AUTODETERMINATZIONE',
]
# dx

lista_3 = [
 'MOVIMENTO 5 STELLE',
 '10 VOLTE MEGLIO',
]
# 5s

uncategorized = [
 'POUR TOUS PER TUTTI PE TCHEUT',
]

class PartitoNonTrovato(NotImplementedError):
    pass

def indice_partito(partito):
    if partito in lista_1:
        return 0
    elif partito in lista_2:
        return 1
    elif partito in lista_3:
        return 2
    else:
        raise PartitoNonTrovato

# %%

nomi_comuni, votanti_per_comune = list(votanti.keys()), np.array(list(votanti.values()))

perc_per_lista = np.zeros((len(votanti_per_comune), 3), dtype=float)

for comune, voti in percentuali.items():
    for partito, perc in voti.items():
        try:
            perc_per_lista[nomi_comuni.index(comune), indice_partito(partito)] += perc
        except PartitoNonTrovato:
            continue

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
lons = np.zeros_like(votanti_per_comune, dtype=float)

accents = [
    ("A'", "À"),
    ("E'", "È"),
    ("I'", "Ì"),
    ("O'", "Ò"),
    ("U'", "Ù"),
]

def replace_accents(s):
    for a in accents:
        s = s.replace(*a)
    return s

replacements = [
    lambda com: com,
    lambda com: com.split(' - ')[0],
    replace_accents,
    lambda com: com.split('/')[0],
    lambda com: com.split(' ')[0],
]

for i, com in enumerate(nomi_comuni):
    for rep in replacements:
        try:
            com = rep(com)
            lats[i] += float(lat_per_comune[com])
            lons[i] += float(lon_per_comune[com])
            break
        except KeyError:
            continue
        except AttributeError:
            print(com)
            continue
    if lats[i] == 0:
        print(f'Did not find {com}')

#%%

comuni_grandi_idx = votanti_per_comune.argsort()[-40:]

comuni_grandi_legend = {
    nomi_comuni[idx].split(' ')[0]: lats[idx]
    for idx in comuni_grandi_idx
}

comuni_grandi_legend.pop('VERONA')
comuni_grandi_legend.pop('GENOVA')
comuni_grandi_legend.pop('BARI')
comuni_grandi_legend.pop('TORINO')
comuni_grandi_legend.pop('VENEZIA')
comuni_grandi_legend.pop('MESSINA')
comuni_grandi_legend.pop('TRIESTE')
comuni_grandi_legend.pop('PADOVA')
comuni_grandi_legend.pop('MODENA')
comuni_grandi_legend.pop('BRESCIA')


comuni_grandi_labels = list(comuni_grandi_legend.keys())
comuni_grandi_lats = list(comuni_grandi_legend.values())

# %%

x = np.sqrt(3/4) * (perc_per_lista[:, 1] - perc_per_lista[:, 0])
y = -perc_per_lista[:, 2] + 1 / 2 * (perc_per_lista[:, 1] + perc_per_lista[:, 0])

from matplotlib.cm import get_cmap, ScalarMappable
colormap = get_cmap('turbo')

rescale_lat = plt.Normalize(vmin = 36, vmax=47)    

plt.scatter(x, y,
    s=votanti_per_comune / 4e2,
    alpha=.3,
    c=colormap(rescale_lat(lats)),
    marker='.',
    edgecolors='none'
    )

plt.annotate('Centre-left', (-40 , 43))
plt.annotate('Centre-right', (  20, 43))
plt.annotate('5 stelle', (-10, -70))

plt.plot([0, 0], [0, 50], ls=':', c='black')
plt.plot([0, -np.sqrt(3/4) * 50], [0, -25], ls=':', c='black')
plt.plot([0, np.sqrt(3/4) * 50], [0, -25], ls=':', c='black')

x_triangle = np.array([0, -np.sqrt(3 / 4), np.sqrt(3 / 4), 0]) * 100
y_triangle = np.array([-1, 1/2, 1/2, -1]) * 100
plt.plot(x_triangle, y_triangle, c='black', lw=.5)

from matplotlib.ticker import FixedFormatter

colorbar = plt.colorbar(
    ScalarMappable(norm=rescale_lat, cmap=colormap),
    label='Latitude',
    format = FixedFormatter(comuni_grandi_labels),
    ticks = comuni_grandi_lats
)

plt.gca().axes.get_xaxis().set_visible(False)
plt.gca().axes.get_yaxis().set_visible(False)
for spine in plt.gca().spines.values():
    spine.set_visible(False)

plt.xlim(-np.sqrt(3) * 50, np.sqrt(3) * 50)
plt.ylim(-100, 50.01)

plt.scatter(0, 0, c='black', s=6)
plt.title('2018 Election in Italy')

plt.tight_layout()
plt.savefig('figures/partitiecolori.png', dpi=500, transparency=False, facecolor='white')
plt.savefig('figures/partitiecolori.pdf', dpi=500, transparency=False, facecolor='white')

# %%

plt.scatter(lons, lats)
plt.xlim(6, 19)
plt.ylim(34, 48)

# %%
