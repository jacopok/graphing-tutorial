#%%

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

CODE = 'USA'

# creiamo un "dataframe" che contenga i dati
deaths_df = pd.read_csv('data/lung-cancer-deaths-per-100000-by-sex-1950-2002.csv')

# selezioniamo solo quelli corrispondenti alla nazione selezionata
# "setacciare"
deaths_df = deaths_df[deaths_df.Code == CODE]

# i dati sono presentati divisi per sesso, noi guarderemo un aggregato: 
# facciamo una media per semplicità, anche se ciò non è molto preciso 
deaths = (
    deaths_df['Female lung cancer deaths (per 100,000) (WHO (IARC) (2016))'] +
    deaths_df['Male lung cancer deaths per 100,000 (WHO (IARC) (2016))']
).to_numpy() / 2

# definiamo anche un array con gli anni corrispondenti a questi
# tassi di mortalità

years_deaths = deaths_df['Year'].to_numpy()

# facciamo operazioni analoghe per le vendite di sigarette

sales_df = pd.read_csv('data/sales-of-cigarettes-per-adult-per-day.csv')
sales_df = sales_df[sales_df.Code == CODE]
sales = sales_df['Sales of cigarettes per adult per day (International Smoking Statistics (2017)) '].to_numpy()
years_sales = sales_df['Year'].to_numpy()

# %%

# Version 1A

plt.plot(years_deaths, deaths)
plt.savefig('figures/cigarettes_cancer_v1a.png', format = 'png', bbox_inches='tight')


#%%

# 1B

plt.plot(years_sales, sales)
plt.savefig('figures/cigarettes_cancer_v1b.png', format = 'png', bbox_inches='tight')


# %%

# Version 2

# ci stiamo inoltrando in territorio più avanzato
# e dobbiamo creare l'oggetto "figura"
fig = plt.figure()

# "gca" sta per "get current axes", che nel linguaggio
# di matplotlib sono la "carta millimetrata" sulla quale mettere i dati
ax = plt.gca()

# twinx permette di ottenere un altro "foglio" di carta millimetrata
# corrispondente però agli stessi valori sulle x (ovvero, per noi, anni)
# e si possono allungare separatamente sulle y
ax2 = ax.twinx()

# ora quando diamo il comando "plot" dobbiamo specificare a quali 
# axes ci stiamo riferendo
ax.plot(years_deaths, deaths, label='deaths', c='red')
ax2.plot(years_sales, sales, label='sales', c='blue')

# fare una legenda quando ci sono più axes è leggermente più complicato
# il codice seguente prende le due legende e le mette insieme in una
handles, labels = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()
ax.legend(handles+handles2, labels+labels2)

# alternativa:
# fig.legend(loc='upper left', bbox_to_anchor=(0,1), bbox_transform=ax.transAxes)

fig.savefig('figures/cigarettes_cancer_v2.png', format = 'png', bbox_inches='tight')


# %%

# Version 3

# ci serviranno questi colori più volte, quindi li definiamo qui
# così, cambiarli sarà più semplice se ne avremo bisogno
death_color = 'red'
sales_color = 'blue'

fig = plt.figure()
ax = plt.gca()
ax2 = ax.twinx()

ax.plot(years_deaths, deaths, label='deaths', c=death_color)

# diamo lo stesso colore della curva all'asse y, in modo che
# sia chiaro a cosa si riferisce
# e aggiungiamo un'etichetta più estesa sull'asse stesso
ax.set_ylabel('Morti per cancro al polmone ogni 100000', c=death_color)
ax.tick_params(axis='y', colors=death_color)

ax2.plot(years_sales, sales, label='sales', c=sales_color)
ax2.set_ylabel('Sigarette vendute per adulto ogni giorno', c=sales_color)
ax2.tick_params(axis='y', colors=sales_color)

# diamo un titolo alla figura
ax.set_title('Morti per cancro e vendite di sigarette')

# facciamo partire entrambi gli assi da 0;
# lo dobbiamo fare manualmente definendo l'estensione delle y
# quindi andiamo da 0 a poco sopra il massimo per entrambe
ax.set_ylim(0, max(deaths)*1.1)
ax2.set_ylim(0, max(sales)*1.1)


# ora la legenda di prima diventa ridondante: possiamo rimuoverla.
# handles, labels = ax.get_legend_handles_labels()
# handles2, labels2 = ax2.get_legend_handles_labels()
# ax.legend(handles+handles2, labels+labels2)

# aumentiamo leggermente la dimensione dell'immagine
fig.set_dpi(150)

fig.savefig('figures/cigarettes_cancer_v3.png', format = 'png', bbox_inches='tight')
fig.show()

# %%

# Version 4

# invece dei colori di default possiamo sceglierne uno 
# personalizzato con una stringa RGB, che troviamo con un
# color picker: https://g.co/kgs/v8tjCs
death_color = '#b82727'
sales_color = '#1c21b0'

fig = plt.figure()
ax = plt.gca()

ax2 = ax.twinx()

ax.plot(years_sales, sales, label='sales', c=sales_color)

# mettiamo il testo in orizzontale
ax.set_ylabel(
    'Sigarette vendute \nper adulto ogni giorno',
    c=sales_color,
    rotation='horizontal',
    size=8,
    ha='left') # horizontal alignment
ax.yaxis.set_label_coords(0.,1.03) # selezione della posizione
ax.tick_params(axis='y', colors=sales_color)

ax2.plot(years_deaths, deaths, label='deaths', c=death_color)
ax2.set_ylabel(
    'Morti per cancro al\npolmone ogni 100000',
    c=death_color,
    rotation='horizontal',
    size=8,
    ha='right')
ax2.yaxis.set_label_coords(1., 1.1)
ax2.tick_params(axis='y', colors=death_color)

# un dettaglio estetico: coloriamo il testo del titolo! 
# per farlo, dobbiamo dividerlo in pezzi
# e colorarli individualmente
fig.text(.22, 1., 'Vendita di sigarette', fontsize='large', color=sales_color)
fig.text(.5, 1., 'e', fontsize='large')
fig.text(.528, 1., 'morti per cancro', fontsize='large', color=death_color)

# possiamo includere il codice del paese di riferimento
fig.text(.77, 1., f'({CODE})', fontsize='large')

# per avere una griglia coerente fra i due assi y, 
# dobbiamo scegliere un rapporto fra di essi che sia un numero intero
deaths_by_sales = round(max(deaths) / max(sales))

# ora possiamo creare degli assi con lo stesso numero di ticks
ax_ticks = list(np.arange(0, max(sales) + 2))
ax2_ticks = list(np.arange(0, max(sales) + 2) * deaths_by_sales)

ax.set_yticks(ax_ticks)
ax2.set_yticks(ax2_ticks)

# e attivare la griglia, rendendola tratteggiata
ax.grid('on', ls='--') # ls sta per "linestyle"

# mentre disabilitiamo il rettangolo nero attorno alla figura
for spine in ax.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

# i limiti degli assi y devono corrispondere a quelli 
ax.set_ylim(ax_ticks[0], ax_ticks[-1])
ax2.set_ylim(ax2_ticks[0], ax2_ticks[-1])

# infine, il grafico ha l'aria più pulita se lo chiudiamo su un numero tondo come 2000
ax.set_xlim(1900, 2000)

fig.set_dpi(150)
fig.savefig('figures/cigarettes_cancer_v4.png', format = 'png', bbox_inches='tight')
fig.show()

# %%