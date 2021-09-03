### Codice per il modulo di visualizzazione dati - SSA 2021

#### Prima lezione

Useremo due notebooks i cui contenuti sono all'incirca quelli dei files `intro.py` e `smoking.py`, 
ma in due nuove versioni implementate in Google Colab, con più commenti. 

- [Intro notebook](https://colab.research.google.com/drive/1FksVfusUPYSQc3KE3ZCXYHXhEfErl8yk?usp=sharing)
- [Smoking notebook](https://colab.research.google.com/drive/1Zf2vH47RrQuISRhskR9vKmnacqPpqg8m?usp=sharing)

[Slides prima lezione qui](https://docs.google.com/presentation/d/1uQI1e3Q7WsXNNu5FlnID5YXbpNbSDEYFBs4s1SpoJ-A/edit?usp=sharing).

[Simulatore di daltonia](http://www.color-blindness.com/coblis-color-blindness-simulator/).

##### Esercizio

Creare una nuova visualizzazione di un dataset!
Scelta libera del tema, consigliati quelli che si trovano nel [blog di OWiD](https://ourworldindata.org/blog) in quanto sono associati ad articoli esplicativi e a dataset ordinati, in particolare 
- [mortalità infantile](https://ourworldindata.org/grapher/child-mortality-around-the-world)
- [vaccinazioni COVID in Israele](https://ourworldindata.org/vaccination-israel-impact), uno dei paesi dove la campagna è stata attivata prima. 
- cambiamenti nelle [ore di lavoro annue](https://ourworldindata.org/working-hours) 
- [gender pay gap e "differenze biologiche"](https://ourworldindata.org/biology-pay-gap) (vedi anche [questo](https://ourworldindata.org/what-drives-the-gender-pay-gap))

Idealmente, generare la visualizzazione con uno script in python + matplotlib; non c’è problema se non riuscite a fare tutto ciò che volete, in tal caso un programma parziale con spiegazione a voce / disegno su carta del grafico desiderato va benissimo: la cosa importante è l’idea. 

#### Seconda lezione

Gli altri files contenuti in questa cartella servono a generare alcune delle figure utilizzate nelle slides, tranne `SSA 2021 - Notes.md`, appunti per questo corso non particolarmente ben tenuti ma che magari possono essere utili per qualcosa.

Nello specifico abbiamo:
- `bertrand.py`, che può generare distribuzioni di corde e figure per discutere il  [paradosso di Bertrand](https://it.wikipedia.org/wiki/Paradosso_di_Bertrand);
- `italia-elezioni.py` genera un grafico tripartito che rappresenta in modo alternativo i risultati delle elezioni nel 2018;
- `log-scaling.py` genera alcuni grafici fittizi, stile [xkcd](https://xkcd.com/), che illustrano i problemi di assi logaritmici, specie per gli istogrammi - vedi anche [questo articolo](http://arxiv.org/abs/2003.14327);
- `temperature-kelvin.py` illustra un piccolo punto riguardo al mettere lo zero dell'asse y a zero;
- `projections.py` genera mappe e proiezioni complete di indicatrici di Tissot con il modulo [cartopy](https://scitools.org.uk/cartopy/docs/latest/).

[Slides seconda lezione qui](https://docs.google.com/presentation/d/13D0DWYi2gg94ug22RvxYdW3UsLSK50RgLkk36ptcvBo/edit?usp=sharing).

Per alcune altre informazioni su come fare grafici digitalmente potete leggere ["Data Visualisation Heuristics for the physical sciences"](http://www.sciencedirect.com/science/article/pii/S0264127519303065) oppure un articolo simile dal titolo più clickbait-y, ["Ten simple rules for better figures"](https://dx.plos.org/10.1371/journal.pcbi.1003833). 

Per chi avesse voglia di qualcosa di più esteso consiglio lo storico libro di [Tufte, "The Visual Display of Quantitative Information"](https://www.edwardtufte.com/tufte/books_vdqi), quello che parlava del grafico sulla ritirata di Napoleone in Russia.

Infine, per il tema della distorsione dell'informazione c'è l'ottimo "How to lie with statistics" di Huff e Geis; se non volete leggere l'intero libro però [questo post](https://towardsdatascience.com/lessons-from-how-to-lie-with-statistics-57060c0d2f19) riassume alcuni dei suoi punti salienti.


#### Extra

Con il notebook `attractors.ipynb` si possono generare visualizzazioni tridimensionali 
di attrattori strani (per il modulo sul Caos tenuto da [Leonardo](https://github.com/lzampieri)).