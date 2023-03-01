# Text Classification from Scratch with Python Book Review Spoilers

-----CONTENUTO REPOSITORY-----
- relazione_progetto.pdf
- presentaziozne_progetto.pptx
- cartella codici_progetto


-----CONTENUTO CARTELLA codici_progetto-----

- 'utili.py'				--->   librerie e funzioni utili
- 'preproc_pulizia_testi.py'		--->   preprocessing parte 1 (pulizia testi)
- 'mapper.py'				--->   mapper (procedura MapReduce)
- 'reducer.py'				--->   reducer (procedura MapReduce)
- 'preproc_features_selection.py'	--->   preprocessing parte 2 (features selection)
- 'modelli.py'				--->   funzioni per stima e previsione di percettrone e SVM
- 'applicazione_modelli.py'		--->   avvio modelli
- 'percettrone.py'			--->   stima e previsione percettrone sui dati
- 'svm.py'				--->   stima e previsione SVM sui dati




-----DOWNLOAD DATASET GOODREADS-----

E' necessario scaricare il file contenente il dataset dal seguente link:
https://drive.google.com/uc?id=196W2kDoZXRPjzbTjM6uvTidn6aTpsFnS

Il file 'goodreads_reviews_spoiler.json.gz' deve essere poi inserito nella cartella 'codici_progetto'.




-----LIBRERIE NECESSARIE-----

E' necessario installare le seguenti librerie: 'nltk', 'sklearn', 'numpy'.
E' necessario che la macchina sia connessa alla rete affinché il software possa eseguire in automatico 
il download della collezione di stop words presente nella libreria 'nltk'.





-----ESECUZIONE DEL SOFTWARE-----

-- Posizionarsi all'interno della cartella 'codici_progetto'


-- Eseguire: preproc_pulizia_testi.py

	Per replicare l'esperimento descritto nella relazione, bisogna:

	- Rispondere YES (oppure yes, Y, y) alle seguenti domande:
  	  'Vuoi mantenere solamente le recensioni dei libri recensiti almeno 20 volte?'
  	  'Vuoi eliminare le frasi con meno di 10 termini e quelle con più di 30 termini?'



-- Digitare da riga di comando (da terminale): type frasi_pulite_features_selection_set.txt | mapper.py | reducer.py
     NB. Se si sta utilizzando un OS diverso da Windows, sostituire 'type' con 'cat'



-- Eseguire: preproc_features_selection.py

	Per replicare l'esperimento descritto nella relazione, bisogna:

	- Rispondere YES (oppure yes, Y, y) alle seguenti domande:
  	  'Vuoi mantenere solamente i termini che compaiono almeno 5 volte?'
  	  'Vuoi mantenere solamente il 20% dei termini che hanno ottenuto il punteggio più elevato nel test chi quadrato?'
          'Vuoi procedere con la fase di modellazione?'

	- Rispondere P (oppure p) alla seguente domanda:
  	  'Vuoi adattare il percettrone o il SVM?'

	- Rispondere YES (oppure yes, Y, y) alle seguenti domande:
  	  'Vuoi fissare il numero di iterazioni a 23?'
 	  'Vuoi adattare un altro modello?'

	- Rispondere S (oppure s) alla seguente domanda:
  	  'Vuoi adattare il percettrone o il SVM?'

	- Rispondere YES (oppure yes, Y, y) alle seguenti domande:
  	  'Vuoi fissare il numero di iterazioni a 34?'
  	  'Vuoi fissare il learning rate a 1e-08?'
  	  'Vuoi fissare il valore C a 1.1e+09?'




NB. Durante l'esecuzione del software verranno salvati nella cartella di lavoro i seguenti file:
   - features_selection_set.json
   - model_set.json
   - frasi_pulite_features_selection_set.txt
   - conteggio_termini.txt
   - training.json
   - validation.json
   - test.json

NB. Se si è già eseguita la procedura di preprocessing almeno una volta, e dunque nella cartella di lavoro
    sono presenti i file 'training.json', 'validation.json' e 'test.json', è possibile eseguire solamente la 
    procedura di modellazione, eseguendo il file: applicazione_modelli.py

