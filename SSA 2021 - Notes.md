## Prima sessione

### Principi di design

Parliamo di grafici, che permettono di rendere visualmente comprensibile dei dati quantitativi. 
Ci concentreremo su grafici statici, immagini bidimensionali: possono essere molto utili anche animazioni e grafici interattivi; non ne parleremo molto per semplicità, ma anch'essi sono di grande interesse. 

Prima di iniziare con il codice e gli aspetti tecnici, parliamo un poco di cosa vogliamo fare e perché.
Qual'è l'utilità di un grafico? Quali sono gli obiettivi che raggiunge, nel migliore dei casi? 

Per quanto questo modulo si collochi all'interno di una summer school sulle materie STEM, creare e criticare grafici è più arte che scienza, ma tutte le scienze necessitano del buon uso di quest'arte.

Come punto di partenza per la discussione della qualità di un grafico possiamo usare il [triangolo](https://junkcharts.typepad.com/junk_charts/junk-charts-trifecta-checkup-the-definitive-guide.html) sviluppato da Kaiser Fung del blog [junkcharts](https://junkcharts.typepad.com/junk_charts/2014/08/welcome.html): un grafico è definito dalle tre domande
- Qual'è la *domanda* (Q) alla quale dà una risposta? 
- Cosa dice la *visualizzazione* (V)?
- Cosa dicono i *dati* (D)?

I consigli che si possono dare sul design di grafici ricadono generalmente in una di queste categorie, dunque è bene tenerle a mente. 

Prima di discutere nel dettaglio questi tre punti, guardiamo un esempio: discutiamo insieme di cosa va e cosa non va in questo [grafico](https://junkcharts.typepad.com/junk_charts/2021/06/start-at-zero-improves-this-chart-but-only-slightly.html) (di cui non menzionamo l'autore, "si dice il peccato ma non il peccatore").

![altezza donne](https://junkcharts.typepad.com/.a/6a00d8341e992c53ef0282e10aabee200b-pi)

(*Discussione collaborativa*, cerchiamo poi di classificare le idee nelle tre categorie QVD)

Alcune idee che potrebbero venire fuori nella discussione, ma che altrimenti menzionerò io:
- dal lato della domanda (Q) non è ben chiaro quale sia l'oggetto dell'investigazione: perché siamo interessati all'altezza delle donne in questa selezione apparentemente casuale di nazioni? Cosa dovremmo trarre come conseguenza?
- Dal lato visuale (V), il colore è eccessivo nel suo desiderio di comunicare che si parla di *donne*! Le sfumature di rosa sembrano scelte in maniera casuale - se hanno un significato, non è esplicitato.
- Di nuovo dal lato visuale (V), le proporzioni fra le altezze medie delle donne nelle varie nazioni sono falsate in ben due modi! 
	- l'asse y parte da poco meno di 5 piedi (circa 150cm), mentre gli ideogrammi danno l'idea di avere i "piedi" a zero;
	- gli ideogrammi sono scalati sia in verticale che in orizzontale: l'importanza visuale di uno di essi, dunque, scala con il *quadrato* dell'altezza.

Diamo invece un'occhiata a un grafico fatto bene: questo grafico, dovuto a Charles Joseph Minard, visualizza il terribile destino dell'armata di Napoleone durante l'invasione della Russia nell'inverno 1812-13.
Tufte, nel suo "The Visual Display of Quantitative Information" (base di buona parte di questo modulo), scrive che potrebbe essere il grafico migliore mai creato. 

![Napoleon](https://upload.wikimedia.org/wikipedia/commons/2/29/Minard.png)

La tipologia di grafico è un "Sankey Diagram", un diagramma di flusso.
Riesce a mostrare molti dati contemporaneamente, 6 variabili in totale:
- Posizione dell'esercito (x e y, due variabili)
- Direzione degli spostamenti
- Dimensione dell'esercito
- Temperatura durante la ritirata (in gradi Réamur, una scala in uso al tempo, per la quale l'acqua congela a 0°R e bolle a 80°R)
- Date della ritirata

Questo grafico illustra chiaramente quelli che Tufte definisce come i principali dettami del buon design grafico:
- porta chi guarda a pensare alla sostanza invece che a metodologia, design grafico o altro: la *storia* che racconta il grafico è immediatamente chiara (Q)
- è strettamente integrato con la descrizione statistica e verbale del dataset: la didascalia è immediatamente sopra l'immagine, e chiarisce i possibili dubbi sul significato dei colori o dei numeri (Q)
- rende coerente un grande dataset: sono integrati tutti i dati menzionati sopra, peraltro relativi ad un esercito che talvolta si andava a dividere in diverse sezioni (V)
- rivela i dati a diversi livelli di dettaglio (V)
- non contiene elementi superflui (V)
- presentare molti numeri in poco spazio (D, V)
- non distorce quello che dicono i dati (D)

Come aggiornare questi dettami al giorno d'oggi:
- il grafico deve essere appropriato per il mezzo con cui è visualizzato (V): quello di Minard è perfetto se abbiamo a disposizione un libro da guardare da vicino e una lente d'ingrandimento, mostrato su una slide come stiamo facendo d'ora funziona meno
- possiamo usare il colore a nostro vantaggio (V)! Se non ha un particolare significato è meglio lasciare tutto nero, ma spesso scegliere una *colormap* adeguata può essere illuminante
- il grafico dovrebbe essere generato programmaticamente (tecnico): in questo modo
	- sarà esattamente riproducibile a partire dai dati, specie se forniamo il codice
	- sarà facile da sistemare se dovremo modificare i dati per qualche motivo (ad esempio, se troviamo un errore o dei dati migliori) 

Un esempio di cattivo uso dei colori:
![steel-production-donut](https://junkcharts.typepad.com/.a/6a00d8341e992c53ef0263e99e1fe6200b-pi)

È molto più chiara, in questo caso, una visualizzazione che fa uso minimo del colore:
![steel-production-arrows](https://junkcharts.typepad.com/.a/6a00d8341e992c53ef027880235910200d-pi)

### Il primo grafico

Partiamo da un semplice esempio di grafico in python come riscaldamento. 

Conoscete i grafici del tipo $y = f(x)$, in cui si traccia una linea nel piano cartesiano che unisce tutti i punti $(x,y)$ che corrispondono ad input e output della funzione $f$. 

Per la nostra rappresentazione digitale della funzione dovremo discretizzare lo spazio. Ipotizziamo, ad esempio, di voler mostrare il grafico di $y = x^2$. 
Per farlo, possiamo scegliere come $x$ i punti che corrispondono ai numeri naturali da 1 a 9: il codice per generare i due array che ci servono è 
```python
xs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 

# inizializzazione di una lista vuota
ys = []
for x in xs:
	# 'append' aggiunge un elemento alla fine della lista
	ys.append(x**2)
```
in modo tale che l'array `ys` ora sia `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`.

Scrivere tutti i numeri a mano è scomodo, e lo sarà ancora di più quando vorremo avere migliaia di punti.
Iniziamo allora da subito ad usare il pacchetto `numpy`, che permette di semplificare di molto la sintassi di queste operazioni numeriche. Il codice che segue ottiene fondamentalmente lo stesso risultato di quello precedente:
```python
import numpy as np
xs = np.arange(0, 10)
ys = xs ** 2
```

Le funzioni che fanno parte del modulo `numpy` vengono tutte invocate come `np.<nome_funzione>`; `arange` genera un array di numeri equispaziati.

L'array generato (`xs`) è un oggetto flessibile: possiamo applicargli operazioni come se fosse un singolo valore, e queste verranno estese a tutti gli elementi. 

Ora, abbiamo le coppie $(x, y)$ da mettere nel nostro grafico. Per visualizzarle useremo il modulo `matplotlib`: la sintassi per generare il più semplice grafico che mostri questi punti è 
```python
import matplotlib.pyplot as plt
plt.plot(xs, ys)
```

A seconda dell'interfaccia che stiamo usando per generare i grafici può essere necessario aggiungere il comando `plt.show()` dopo la generazione del grafico. 

#### Esercizio

Ora, possiamo migliorare questo grafico in diversi modi. 
Ecco alcune idee:
- la funzione `np.arange` può essere sostituita da [`np.linspace`](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html#numpy.linspace), che genera un array di punti equispaziati fra un minimo e un massimo. Come si può leggere nella documentazione, la si può chiamare, ad esempio, come `np.linspace(0, 9, num=100)`. In questo modo avremo più punti a disposizione e la curva apparirà più liscia. Nella descrizione della funzione della documentazione gli argomenti che appaiono come `argomento=valore` hanno un valore di _default_: possiamo modificarli se ne abbiamo bisogno, se non lo facciamo saranno inizializzati al default.
- Possiamo aggiungere delle _etichette_ per i nostri assi: il comando è `plt.xlabel` per l'asse x (e rispettivamente `ylabel`), da dare dopo `plt.plot`, e al quale passare una _stringa_ come `'asse $x$'` (testo delimitato da degli apici singoli o doppi, i dollari invece sono i delimitatori di un ambiente "equazione" nel quale possiamo usare simboli matematici).
- Possiamo aggiungere un _titolo_ con il comando `plt.title('Grafico cartesiano')`.
- Possiamo aggiungere una _griglia_ con il comando `plt.grid('on')`
- Possiamo aggiungere una _legenda_ (anche se in questo caso, con una sola curva, è un po' ridondante): per farlo dobbiamo dare un'etichetta alla curva, aggiungendo l'opzione `label = '$y=x^2$'` al comando `plot`, e generare la legenda alla fine con il comando `plt.legend()`. 

Il risultato di queste manipolazioni dovrebbe essere 
```python
xs = np.linspace(0, 9, num=100)
ys = xs**2

plt.plot(xs, ys, label='$y = x^2$')
plt.xlabel('asse x')
plt.ylabel('asse y')
plt.title('Grafico cartesiano')
plt.grid('on')
plt.legend()
```

### Sigarette e serie temporali

Vediamo allora un esempio pratico!
Vogliamo fare un grafico per investigare il problema del fumo; utilizzeremo i dati degli Stati Uniti. 
Ci servono dei dati! Un ottimo posto dove trovarne, specie per questioni sociali come queste, è Our World in Data, un progetto dell'[Università di Oxford](https://ourworldindata.org/about) per la diffusione e comunicazioni dei dati riguardanti i principali problemi del mondo moderno.
È un'ottima risorsa in generale, e spesso lì possiamo trovare grafici che già illustrano molto bene i temi che ci interessano. 

Per oggi, però, ciò che ci fa comodo è che i loro dati
1) arrivano da [fonti](https://ourworldindata.org/smoking#data-sources) attendibili (paper su Nature, The Lancet, il New England Journal of Medicine)
2) sono facilmente scaricabili in formato `csv` (comma-separated values)

Un *dataset* che possiamo scaricare in questo modo è già stato preparato nella cartella `data`: si chiama `lung-cancer-deaths-per-100000-by-sex-1950-2002.csv`.
Aprendolo con un semplice editor di testo possiamo vedere che contiene dati in colonne separate da virgole (da cui "comma-separated"), e che ogni dato corrisponde a una singola riga. 

La prima riga è la nostra chiave di lettura per le colonne; verbosa, sì, ma ci permette di capire senza ambiguità cosa sono i numeri che stiamo leggendo. 

#### Versione 1: due grafici

Prima di tutto includiamo tre pacchetti che ci serviranno:
```python
import pandas as pd # lettura di file csv
import numpy as np # gestione di numeri e array
import matplotlib.pyplot as plt # grafici
```

Per fare il nostro grafico ci serve importare questi dati in python: i dettagli di come fare ciò non sono rilevanti per questo modulo, quindi useremo un modulo di nome `pandas` che lo fa per noi, con questo codice:

```python
CODE = 'USA'

# creiamo un "dataframe" che contenga i dati
deaths_df = pd.read_csv('data/lung-cancer-deaths-per-100000-by-sex-1950-2002.csv')

# selezioniamo solo quelli corrispondenti alla nazione selezionata
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
```

Così, abbiamo creato due array, `years_deaths` e `deaths`, che contengono rispettivamente una serie di anni e una serie di numeri di morti per cancro al polmone ogni 100k persone.

Possiamo mostrare questi dati come abbiamo imparato prima: 

```python
plt.plot(years_deaths, deaths)
```

Possiamo vedere che i dati vanno dal 1950 al 2002, e hanno un massimo attorno al 1990. 
C'è una correlazione con le vendite di sigarette?

Possiamo ricavare degli array per la vendita di sigarette con un metodo analogo a prima.

```python
sales_df = pd.read_csv('data/sales-of-cigarettes-per-adult-per-day.csv')
sales_df = sales_df[sales_df.Code == CODE]
sales = sales_df['Sales of cigarettes per adult per day (International Smoking Statistics (2017)) '].to_numpy()
years_sales = sales_df['Year'].to_numpy()
```

E, di nuovo, il grafico può essere generato con
```python
plt.plot(years_sales, sales)
```

Ora il grafico si estende dal 1900 fino 2014, e ha un picco negli anni '60. 

#### Versione 2: doppio asse y

Quello che dicono questi dati sembra chiaro: il picco delle vendite è specchiato direttamente in un picco nelle morti per cancro ai polmoni.
Vogliamo trasmettere questa informazione con un singolo grafico: come fare? 

Non possiamo semplicemente fare un grafico delle due curve in simultanea: anche se per caso avessero gli stessi valori numerici, i numeri _non sono direttamente comparabili_.
Ci sono diversi modi per risolvere questo problema, in questo caso useremo un _doppio asse y_: a destra e a sinistra della figura ci saranno due assi con valori diversi, e saranno visualizzate due curve, ognuna riferita ad uno degli assi. 

Per chiarire a chi legge quale curva rappresenta cosa possiamo aggiungere una legenda.
Il codice che fa questo è il seguente.
```python
# ci stiamo inoltrando in territorio più avanzato 
# e dobbiamo creare 
fig = plt.figure()
ax = plt.gca()
ax2 = ax.twinx()

ax.plot(years_deaths, deaths, label='deaths', c='red')
ax2.plot(years_sales, sales, label='sales', c='blue')

handles, labels = ax.get_legend_handles_labels()
handles2, labels2 = ax2.get_legend_handles_labels()

ax.legend(handles+handles2, labels+labels2)](<# ci stiamo inoltrando in territorio più avanzato
# e dobbiamo creare l'oggetto "figura"
fig = plt.figure()

# "gca" sta per "get current axes", che nel linguaggio
# di matplotlib sono la "carta millimetrata" sulla quale mettere i dati
ax = plt.gca()

# twinx permette di ottenere un altro "foglio" di carta millimetrata
# corrispondente però agli stessi valori sulle x (ovvero, per noi, anni)
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
```

Già così non è male! Stiamo mostrando i dati contemporaneamente, si vede la correlazione. Ci sono ancora alcuni problemi:
- l'asse y delle vendite parte da 0, quello delle morti no. Questo può creare ambiguità.
- non è chiaro se dobbiamo guardare a destra o a sinistra per trovare i numeri corrispondenti a una curva
- le etichette non sono molto descrittive

#### Versione 3: color-coding

Risolviamo questi problemi con il seguente codice:
```python
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

fig.savefig('cigarettes_cancer_v3.pdf', format = 'pdf', bbox_inches='tight')
fig.show()
```

Ora va sicuramente meglio, ma si può ancora migliorare: 
- è scomodo girare la testa per leggere le etichette degli assi, sarebbe meglio se fossero orizzontali
- gli assi ci sono, ma non è semplice fare riferimento ad essi senza una griglia
	- che griglia usiamo, però? per come abbiamo definito gli assi al momento le griglie dei due assi non si allineano... 
- il riguadro nero attorno alla figura è molto evidente ma non fa molto di utile per noi se aggiungiamo una griglia, possiamo anche rimuoverlo
- i colori "rosso" e "blu" di default sono un po' troppo brillanti per i miei gusti

#### Versione 4 - Æsthetic

Risolviamo questi problemi con il seguente codice:

```python
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
    ha='left')
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
fig.savefig('cigarettes_cancer_v4.pdf', format = 'pdf', bbox_inches='tight')
fig.show()
```

Questa versione è quella che si avvicina di più all'ispirazione di questa parte: 
![big graph](https://ourworldindata.org/uploads/2021/07/Smoking-and-lung-cancer-mortality-US-only-2048x1431.png)
di [Our World in Data](https://ourworldindata.org/smoking-big-problem-in-brief).
[Fonte dei dati](https://ourworldindata.org/smoking#data-sources).

### Esercizi

Idea generale: vengono forniti files csv con dei dataset, e sta a loro "graficarli". 
Se riescono a fare tutto ciò che vogliono implementando effettivamente il codice è meglio, ma per questo modulo quello che conta di più sono le idee: un disegno su carta con il risultato desiderato, magari misto ad un grafico generato ma incompleto, va bene.

Possono scegliere i dati e il tema da trattare fra quelli che si trovano nel [sito di OWiD](https://ourworldindata.org/blog) se le seguenti proposte non sono interessanti:
- [mortalità infantile](https://ourworldindata.org/grapher/child-mortality-around-the-world)
- [vaccinazioni COVID in Israele](https://ourworldindata.org/vaccination-israel-impact), uno dei paesi dove la campagna è stata attivata prima. 
- cambiamenti nelle [ore di lavoro annue](https://ourworldindata.org/working-hours) 
- [gender pay gap e "differenze biologiche"](https://ourworldindata.org/biology-pay-gap) (vedi anche [questo](https://ourworldindata.org/what-drives-the-gender-pay-gap))

Per tutti questi temi, OWiD fornisce delle visualizzazioni oltre ai dati grezzi; per ognuna di queste si possono trovare i dati sotto "Download", e una serie di *dataset* collegati sotto "All our related research and data".

C'è un modo più interessante di unire i dati che si vedono rispetto ai semplici grafici che mostra OWiD?


## Seconda sessione

### Il paradosso di Bertrand, ambiguità e probabilità

Partiamo con un problema che può sembrare poco pertinente, ma che si collega con ciò di cui discuteremo.

> Presa a caso (*) una corda di un cerchio, qual'è la probabilità che questa sia più lunga del lato di un triangolo equilatero inscritto nel cerchio?

(Momento di discussione collaborativa: vediamo che idee vengono fuori per risolvere il problema)

Si può riformulare il problema: le corde lunghe più del lato del triangolo sono quelle che intersecano il cerchio concentrico con raggio dimezzato. 

![[bertrand-chords.pdf]]

Il problema sta nel come interpretiamo il termine "a caso": ci sono diversi metodi per generare una corda, e non c'è motivo di preferirne uno agli altri. 
Tre metodi che potremmo utilizzare sono:
- Scegliere due punti a caso lungo la circonferenza;
![bertrand-1](https://upload.wikimedia.org/wikipedia/commons/9/92/Bertrand1-figure.svg)
- Scegliere un raggio del cerchio, lungo questo scegliere un punto, e prenderlo come punto medio di una corda;
![bertrand-2](https://upload.wikimedia.org/wikipedia/commons/c/c3/Bertrand2-figure.svg)
- Scegliere un punto nel cerchio e prenderlo come punto medio di una corda.
![bertrand-3](https://upload.wikimedia.org/wikipedia/commons/8/8b/Bertrand3-figure.svg)

Con il primo metodo sembra che la probabilità che cerchiamo sia 1/3: fissato un punto, l'altro deve giacere in una di tre sezioni uguali della circonferenza.
Con il secondo metodo sembra che la probabilità sia 1/2: il raggio può essere scelto arbitrariamente, e poi il punto per cui facciamo passare la corda deve cadere nella metà vicina al centro. 
Con il terzo metodo sembra che la probabilità sia 1/4: il punto medio della corda può cadere ovunque, e l'area del cerchio interno è un quarto di quella del cerchio grande.

Qual'è la risposta giusta? Tutte e tre, in un certo senso. 
Il problema sta nel fatto che "a caso" è ambiguo: lo associamo, nel linguaggio comune, con un senso di equi-probabilità, come le facce di un dado, nessuna privilegiata rispetto alle altre. In gergo, questa si chiama una "distribuzione uniforme".

Portando avanti questa interpretazione, però, abbiamo incontrato dei problemi: tutti e tre i metodi cercano di applicare una distribuzione uniforme a formulazioni diverse del problema (posizioni degli estremi della corda, raggio del punto medio, posizione del punto medio), ma queste sono incompatibili. 

#### Istogrammi e assi logaritmici

Non c'è una vera soluzione del problema: è ambiguo per come è posto, ma aiuta ad introdurre il concetto di *distribuzione di probabilità*.

Il suo significato per una variabile discreta, come l'esito del tiro di un dado, è semplice: assegna ad ogni valore la probabilità di ottenerlo. 
Nel caso specifico di un dado a sei facce, ad esempio, la distribuzione assegna ad ognuno dei numeri da 1 a 6 il valore $1/6$. 

Per una variabile *continua*, invece, come il reddito degli abitanti di un paese,[^1] il discorso cambia: non siamo più interessati alla probabilità di uno specifico esito (che non ha un particolare significato: quante persone hanno un reddito annuo di 18.566,57€ l'anno? quante 18.566,58€?) bensì, generalmente, alla probabilità di ottenere un risultato in un certo *intervallo*. 
[^1]: Si potrebbe obiettare che la variabile non è davvero continua - il reddito di ogni persona è un numero discreto di centesimi di euro, ad esempio, e ogni valuta è discretizzata a qualche livello. Tecnicamente questo è vero, tuttavia la discretizzazione è talmente fine in confronto ai valori considerati che l'approssimazione nel considerare continua la variabile è ottima. 
 
Se parliamo di dati empirici, spesso il modo più semplice per rappresentarli sarà tramite un istogramma: dividiamo la regione d'interesse in *bins* ("cestini" in italiano, volendo, la metafora è quella ma il termine sembra un po' strano) e per ognuno di questi disegnamo una barra di altezza corrispondente al numero di persone, ad esempio, che rientrano in quella fascia.

Diamo un esempio concreto, prendendo dei dati fittizi per semplicità: la distribuzione dei redditi mensili, che vanno da 1000 a 100 mila euro. 
Questo è l'istogramma generato direttamente:

![[fictitious-income-linear.png]]

Si può vedere (in questo modello immaginifico, che però è stato scelto per non essere del tutto dissimile dalla realtà) che molte più persone hanno redditi verso l'estremo basso dello spettro. 
Ora, però, nel fare questo istogramma ci possiamo chiedere: perché usare un asse x lineare? I redditi variano per ben due ordini di grandezza, per mostrare meglio questi dati potremmo usare un asse *logaritmico*, ovvero mettere sull'asse non il numero stesso, ma la potenza alla quale dobbiamo elevare 10 per ottenere quel numero. 

In `matplotlib` fare ciò è abbstanza semplice: c'è il comando `plt.set_xscale('log')`. Il risultato è questo:

![[fictitious-income-log1.png]]

Cosa sta succedendo? Innanzitutto, il comando ha funzionato: l'asse varia da $10^0 = 1$ migliaia a $10^2 = 100$ migliaia, con $10^1$ in mezzo. 
Ma cosa è successo ai nostri *bins*? Beh, la larghezza di un bin è costante nell'asse lineare, ma i numeri sono più vicini fra loro all'estremo destro dell'asse logaritmico rispetto all'estremo sinistro.
Perciò, abbiamo questa differenza di larghezza, che falsa il grafico: sul lato sinistro ci sono barre più alte, ma è naturale che lo siano dato che sono associate ad un pezzo più lungo dell'asse! 

Possiamo risolvere questo problema operando il *binning* dopo aver preso il logaritmo dei dati: il risultato è 

![[fictitious-income-log2.png]]

Una distribuzione costante sull'asse logaritmico! 

Il secondo grafico è sicuramente sbagliato a livello tecnico, ma il primo e il terzo sembrano egualmente validi! 

Come nel caso del paradosso di Bertrand, un cambiamento di punto di vista porta ad un cambiamento della distribuzione, e non c'è sempre una scelta privilegiata. Usare l'asse lineare o quello logaritmico è una scelta di *design*.
Ci possono essere lati positivi e negativi da entrambe le parti: (*discussione*). 

- l'asse logaritmico permette di vedere meglio i dettagli per dati che stanno su molti ordini di grandezza
- l'asse logaritmico e quello lineare comunicano messaggi diversi: uno dice "ci sono molte persone che guadagnano poco!", l'altro "il guadagno è ben distribuito fra le possibili fasce di reddito!"

Questo illustra il fatto che non possiamo rimanere del tutto neutrali nella creazione di grafici. I dati sono sempre quelli, ma l'impatto visuale che scegliamo di dare può essere fatto variare molto, specie se siamo faziosi!

Per concludere il discorso, ecco due grafici (sempre della fidata OWiD) che usano uno un asse lineare e l'altro un asse logaritmico.

![global-wealth-inequality](https://ourworldindata.org/uploads/2013/11/4-World-Income-Distribution-2003-to-2035-growth-rates-750x525.png)

![global-wealth-inequality-logscale](https://ourworldindata.org/uploads/2019/10/Global-inequality-in-1800-1975-and-2015-324x550.png)

### Grafici ingannevoli

Ora, guardiamo alcuni grafici e per ognuno di questi discutiamo insieme di cosa non va, e cosa si potrebbe migliorare.

![bush-taxcuts](https://www.statisticshowto.com/wp-content/uploads/2014/01/Bush_cuts2.png)

![federal-welfare](https://www.statisticshowto.com/wp-content/uploads/2014/01/usa-today-2.png)

Iniziamo con una cosa facile: due chiari esempi di manipolazione dell'asse $y$. Questi grafici a barre sottintendono il fatto che l'altezza della barra rappresenti il numero, ma guardando l'asse si nota che in nessuno dei due casi parte da 0.
Anzi, è abbastanza chiaro che i grafici sono faziosi e fatti per amplificare nella mente di chi guarda l'impatto del fenomeno considerato. 

Questo non è per dire che ogni asse $y$ nel mondo debba per forza partire da 0: spesso le fluttuazioni da una media sono rilevanti, e se questo valor medio è grande partire da 0 non aiuterebbe la comprensione. Ad esempio, potremmo disegnare un grafico con le fluttuazioni della temperatura annua di Roma in Kelvin partendo da zero:

![[temperature-kelvin.png]]

Chiaramente questo non ha senso. Torniamo al triste fatto che dobbiamo fare il conto con il significato dei dati, riflettere sull'effetto della fluttuazione che vogliamo mostrare, e far sì che l'impatto visuale nel nostro grafico sia commensurato a tale fluttuazione. 

![piechart-3d](https://upload.wikimedia.org/wikipedia/commons/8/88/Misleading_Pie_Chart.png)

Qui il problema è la prospettiva: l'oggetto D appare più grande dell'oggetto B, ma guardando la torta "dall'alto" si vede che in realtà sono equivalenti.

![piechart-2d](https://upload.wikimedia.org/wikipedia/commons/8/87/Sample_Pie_Chart.png)

![mappa-elezioni-regions](https://pbs.twimg.com/media/DXiln7YWAAAPQAn?format=jpg&name=large)

Articolo sulla [polarizzazione delle elezioni italiane](https://puntofisso.medium.com/le-vere-mappe-delle-elezione-italiane-a0cb89d27d9e).
Qui il problema è più sottile: ogni comune è colorato pienamente sulla base di chi ha vinto le elezioni lì, e questo dà l'idea di un'estrema polarizzazione. 
I dati che sono mostrati sono validi, ma trarre da questi delle conclusioni sulla polarizzazione dell'opinione pubblica può essere affrettato. Ogni regione è colorata in modo definito sulla base di chi ha vinto, ma se invece disegnamo un puntino per ogni 10,000 voti per un certo partito (Rosso=CSX, Azzurro=CDX, Giallo=M5S) l'immagine è molto più colorata:
![mappa-elezioni-dots](https://miro.medium.com/max/1340/1*sSW0pscPFFVp8ZGqexsfBA.jpeg)

Come al solito, nessuno dei due grafici ci dà tutta la verità: uno dice "l'Italia è estremamente polarizzata! il nord vota la destra, il sud i Cinque Stelle, e solo in alcune piccole aree attorno a Bolzano, Bologna e Firenze si vota a sinistra", l'altro dice "i voti per tutti e tre i partiti sono distribuiti su tutta la penisola, le maggioranze non sono così strette, c'è margine per un cambiamento anche significativo".

Al solito, gli stessi dati visualizzati in modo diverso raccontano storie diverse. Io direi che nessuno dei due grafici riesce a catturare tutto il panorama in modo completo, qualcun altro (forse fra di voi!) potrebbe fare un lavoro migliore.

![[nicholas-cage-drowning.png]]

Questa è, in un certo senso, una domanda trabocchetto: il problema sta nel punto "D" del triangolo che abbiamo descritto all'inizio del modulo.
Il grafico, di per sè, non è malvagio: gli assi y non partono da 0, certo, ma come dicevamo prima non è necessariamente un problema.

Il vero problema sta nel fatto che i dati che stiamo mostrando sono risultato di *cherry picking*.
Perché i film di Nicholas Cage dovrebbero avere qualcosa a che fare con gli annegamenti? 
La correlazione, tuttavia, c'è: il "trucco" per ottenere grafici come questo sta nel fatto che possiamo scegliere un grande numero di serie temporali, calcolare le loro correlazioni, prendere quelle più correlate e dire di aver trovato qualcosa. È una [correlazione spuria](http://www.tylervigen.com/spurious-correlations).

L'esempio scelto è qualcosa di palesemente insensato, ma può farci ragionare sul fatto che *correlazione non implica causalità*, un mantra che negli ambienti scientifici si sente spesso. 

Si può anzi fare una lista di opzioni: se A e B sono correlati, potrebbe essere che
- A causi B;
- B causi A;
- A e B siano entrambi causati da C;
- A e B si causino (o amplifichino) a vicenda;
- la correlazione sia una coincidenza.

### Mappe

![[google-maps-mercator.png]]

Dove sta il problema qui? Non stiamo neanche mostrando dei dati! 

Domanda: guardando questa mappa, qual'è il rapporto fra l'area dell'Africa e quella della Groenlandia? 

Nella realtà l'Africa ha un'area di 30 milioni di km^2 circa, la Groenlandia poco più di due (un rapporto di 14 a 1); dalla mappa che mostra Google Maps però verrebbe da dire che le aree siano simili, al più in rapporto di 2 a 1. 

Il problema è che, checché ne dicano i terrapiattisti, la Terra è sferica, e le sue proiezioni su un piano includono sempre un certo livello di distorsione.

In particolare, la proiezione che usa Google Maps è quella di Mercatore (che avete visto anche nel modulo di geometria sferica); una proiezione *conforme*, che preserva gli angoli ma non le aree. 

Per vedere qual'è il problema con Mercatore possiamo usare il metodo dell'*indicatrice di Tissot*: disegnamo piccoli cerchi uguali in diverse posizioni sulla Terra e vediamo come vengono modificati dalle varie proiezioni.

In una proiezione prospettica - quella che vedremmo guardando un globo tridimensionale - le indicatrici appaiono così:
![[tissot-perspective.png]]

Nella proiezione di Mercatore le indicatrici vengono ingrandite alle alte latitudini ma non distorte: 
![[tissot-mercator.png]]
Questo significa che la proiezione di Mercatore è utile per la navigazione e altri ambiti nei quali si lavora con gli angoli; tuttavia se si vuole comparare aree è completamente sbagliata.

Facciamo una breve carrellata di proiezioni.
Con la proiezione di Mollweide, del 1805, i meridiani sono deformati in ellissi e le indicatrici sono meno ingrandite, ma più distorte:
![[tissot-mollweide.png]]

Con la proiezione equirettangolare centrata sull'equatore (o Plate Carrée) meridiani e paralleli sono deformati fino a raggiungere una griglia equispaziata. Le indicatrici sono deformate e ingrandite verso il polo:
![[tissot-equirectangular.png]]

Mappare la Terra su un piano è come appiattire la buccia di un'arancia: questa è l'idea che ricorda la proiezione Goode homolosine, che preserva le aree e distorce poco le indicatrici, al prezzo di spezzare la mappa lungo alcune linee:
![[tissot-goode-homolosine.png]]

Questa è solo una piccola, parziale e riduttiva lista di esempi, la [pagina di wikipedia con la lista di proiezioni](https://en.wikipedia.org/wiki/List_of_map_projections) è molto lunga; per un riferimento più a cuor leggero si può vedere [questo fumetto di xkcd](https://xkcd.com/977/).

Qual è il punto? Una proiezione perfetta non esiste, ogni scelta ha pro e contro, e nell'operarla possiamo enfatizzare alcune regioni a dispetto di altre. 
La proiezione di Mercatore, che amplifica estremamente le regioni vicine ai Poli, è sfortunatamente ancora molto usata anche in contesti geopolitici. 

### Conclusione

Dunque, generare grafici è difficile, non c'è un metodo univoco, bisogna operare scelte difficili.
Eppure, dopo tutto questo, il suggerimento è sempre e comunque PTFD (Plot The F\*\*\*\*\*g Data)! 

Ce lo ricorda il Quartetto di Anscombe:
![Anscombe's quartet](https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Anscombe%27s_quartet_3.svg/2560px-Anscombe%27s_quartet_3.svg.png)

Le statistiche descrittive di questi quattro set di dati - media, varianza, correlazione - sono esattamente gli stessi, eppure con un semplice grafico vediamo subito che le potenziali relazioni sono estremamente diverse fra i vari casi. 
I grafici non sono solo strumenti di comunicazione, ma 