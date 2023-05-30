# Text Classification from Scratch with Python Book Review Spoilers (ITA)

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
     N.B. Se si sta utilizzando un OS diverso da Windows, sostituire 'type' con 'cat'



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




N.B. Durante l'esecuzione del software verranno salvati nella cartella di lavoro i seguenti file:
   - features_selection_set.json
   - model_set.json
   - frasi_pulite_features_selection_set.txt
   - conteggio_termini.txt
   - training.json
   - validation.json
   - test.json

N.B. Se si è già eseguita la procedura di preprocessing almeno una volta, e dunque nella cartella di lavoro
    sono presenti i file 'training.json', 'validation.json' e 'test.json', è possibile eseguire solamente la 
    procedura di modellazione, eseguendo il file: applicazione_modelli.py
    
   
   
   
   
    
# Text Classification from Scratch with Python Book Review Spoilers (EN)

-----REPOSITORY CONTENT-----
- relazione_progetto.pdf
- presentaziozne_progetto.pptx
- cartella codici_progetto


-----CONTENTED FOLDER codici_progetto-----

- 'utili.py' ---> useful libraries and functions
- 'preproc_pulizia_testi.py' ---> preprocessing part 1 (text cleaning)
- 'mapper.py' ---> mapper (MapReduce procedure)
- 'reducer.py' ---> reducer (MapReduce procedure)
- 'preproc_features_selection.py' ---> preprocessing part 2 (features selection)
- 'modelli.py' ---> functions for perceptron and SVM estimation and prediction
- 'applicazione_modelli.py' ---> models startup
- 'perceptron.py' ---> perceptron estimation and prediction on data
- 'svm.py' ---> SVM estimation and prediction on data




-----DOWNLOAD DATASET GOODREADS-----

It is necessary to download the file containing the dataset from the following link:
https://drive.google.com/uc?id=196W2kDoZXRPjzbTjM6uvTidn6aTpsFnS

The file 'goodreads_reviews_spoiler.json.gz' must then be placed in the 'codici_progetto' folder.




-----LIBRARIES NEEDED-----

It is necessary to install the following libraries: 'nltk', 'sklearn', 'numpy'.
It is necessary that the machine be connected to the network so that the software can automatically perform 
download the collection of stop words present in the 'nltk' library.





----- RUNNING THE SOFTWARE-----

-- Position yourself inside the 'codici_progetto' folder.


-- Run: preproc_pulizia_testi.py

	To replicate the experiment described in the report, you must:

	- Answer YES (or yes, Y, y) to the following questions:
  	  'Do you want to keep only the reviews of books reviewed at least 20 times?'
  	  'Do you want to delete sentences with less than 10 terms and those with more than 30 terms?'



-- Type from command line (from terminal): type frasi_pulite_features_selection_set.txt | mapper.py | reducer.py
     N.B. If you are using an OS other than Windows, replace 'type' with 'cat'



-- Run: preproc_features_selection.py

	To replicate the experiment described in the report, you must:

	- Answer YES (or yes, Y, y) to the following questions:
  	  'Do you want to keep only the terms that appear at least 5 times?'
  	  'Do you want to keep only the 20% of terms that scored highest in the chi square test?'
          'Do you want to proceed with the modeling phase?'

	- Answer P (or p) to the following question:
  	  'Do you want to adapt the perceptron or SVM?'

	- Answer YES (or yes, Y, y) to the following questions:
  	  'Do you want to set the number of iterations to 23?'
 	  'Do you want to fit another model?'

	- Answer YES (or s) to the following question:
  	  'Do you want to adapt the perceptron or SVM?'

	- Answer YES (or yes, Y, y) to the following questions:
  	  'Do you want to set the number of iterations to 34?'
  	  'Do you want to fix the learning rate at 1e-08?'
  	  'Do you want to fix the C-value at 1.1e+09?'
	  
N.B. During the execution of the software the following files will be saved in the working folder:
   - features_selection_set.json
   - model_set.json
   - frasi_pulite_features_selection_set.txt
   - conteggio_termini.txt
   - training.json
   - validation.json
   - test.json

N.B. If you have already performed the preprocessing procedure at least once, and therefore in the working directory
    files 'training.json', 'validation.json' and 'test.json' are present, you can only run the 
    modeling procedure, by running the file: applicazione_modelli.py

