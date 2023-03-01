### PREPROCESSING - FEATURES SELECTION

# import librerie e funzioni utili
from utili import *


# lettura dati
print('\nSto caricando il features selection set ed il model set...\n')
with open('features_selection_set.json') as json_file:
    features_selection_set = json.load(json_file)

with open('model_set.json') as json_file:
    model_set = json.load(json_file)


# caricamento del file contenente i conteggi dei termini nelle frasi del features selection set (output di MapReduce)
conteggio_spoiler_features_selection = open('conteggio_termini.txt',encoding='utf8') 
conteggio_spoiler_features_selection = conteggio_spoiler_features_selection.readlines()
print('Nel features selection set sono presenti '+str(len(conteggio_spoiler_features_selection))+' diversi termini.\n') 


# rimozione '\n' e separazione dei termini
for j in range(len(conteggio_spoiler_features_selection)):
    conteggio_spoiler_features_selection[j] = conteggio_spoiler_features_selection[j].replace('\n','')
    conteggio_spoiler_features_selection[j] = conteggio_spoiler_features_selection[j].split()
    conteggio_spoiler_features_selection[j][1] = int(conteggio_spoiler_features_selection[j][1])

# ogni sottolista di 'conteggio_spoiler_features_selection' contiene due elementi:
# il primo indicante un termine tra quelli presenti nel features selection set
# il secondo uguale al numero di occorrenze totali del termine



# user_input
i = 0
j = 0
while i < 1:
    user_input = input('Vuoi mantenere solamente i termini che compaiono almeno 5 volte? Digita YES o NO\n')
    if user_input.lower() in ('y', 'yes'):
        i += 1
        soglia = 5
    elif user_input.lower() in ('n', 'no'):
        i += 1
        while j < 1:
            user_input1 = input('Inserire il valore soglia (intero da 1 a 1000)\n')
            try:
                user_input1 = int(user_input1)
                if user_input1 in range(1,1001):
                    soglia = user_input1
                    j += 1
                else:
                   print("\nInput errato, inserire un intero da 1 a 1000.\n")
            except ValueError:
                print("\nInput errato, inserire un intero positivo.\n")
    else:
        print("\nInput errato, per favore digitare YES o NO\n")




# selezione dei termini (del features selection set) con almeno 5 occorrenze 
start = process_time()
cont_vip = []
print('\nSto cercando i termini che compaiono almeno '+str(soglia)+' volte...\n')
for j in range(len(conteggio_spoiler_features_selection)):
    if conteggio_spoiler_features_selection[j][1] >= soglia:
        cont_vip.append(conteggio_spoiler_features_selection[j])
cont_sort = ordina(cont_vip)
cont_sort = cont_sort[::-1]
end = process_time()
time = end - start
print('Ricerca avvenuta correttamente in circa '+str(int(time))+' secondi.\n')
print('Verranno mantenuti solamente i '+str(len(cont_sort))+' termini che compaiono almeno '+str(soglia)+' volte.\n')
print('Ecco i 10 termini più frequenti con le relative occorrenze:')
print(cont_sort[0:10])


# creazione lista dei termini con almeno 5 occorrenze 
termini_frequenti = [x[0] for x in cont_sort]




# test chi quadrato 
# creazione di due liste a partire dal features selection set
# le due liste sono hanno come elementi i termini con più di 5 occorrenze
# presenti in ogni frase no-spoiler (spoil0) ed in ogni frase spoiler (spoil1)
# (se un termine si presenta n volte, sarà presente n volte all'interno della rispettiva lista)
print('\nSto svolgendo il test chi quadrato per selezionare i termini che più discriminano le due classi...\n')
spoil0 = []
spoil1 = []

for i in range(len(features_selection_set)):
    if features_selection_set[i][0] == 0:
        for j in features_selection_set[i][1].split():
            if j in termini_frequenti:
                spoil0 += [j]
    else:
        for j in features_selection_set[i][1].split():
            if j in termini_frequenti:
                spoil1 += [j]


# conteggio della frequenza di ogni termine nelle due liste
spoil0_count = conta_occorrenze(spoil0)
spoil1_count = conta_occorrenze(spoil1)
sum_0 = sum(list(spoil0_count.values()))
sum_1 = sum(list(spoil1_count.values()))

# trasformazione delle frequenze assolute dei termini in frequenze relative 
# (per tenere conto dello sbilanciamento delle classi)
# viene creato un dizionario avente come chiave un termine,
# come valore la frequenza relativa del termine all'interno della rispettiva classe
spoil0_rapp = {k: v/sum_0 for k, v in spoil0_count.items()}
spoil1_rapp = {k: v/sum_1 for k, v in spoil1_count.items()}

# per ogni termine comune alle due classi viene calcolato il punteggio ottenuto dal test chi quadrato
# viene creato un dizionario avente come chiave un termine,
# come valore il punteggio ottenuto dal test chi quadrato
chisq = {}

for i in list(spoil0_rapp.keys()):
    for j in list(spoil1_rapp.keys()):
        if i == j:
            chisq[i] = chisq2(spoil0_rapp[i],spoil1_rapp[j])


# ordinamento dei termini in ordine decrescente in base al punteggio ottenuto dal test
chisq_sort = {k: v for k, v in sorted(chisq.items(), key=lambda item: item[1], reverse=True)}

print('I 20 termini che più discriminano tra le due classi sono:\n')
print(list(chisq_sort.keys())[0:20])

# creazione dell'insieme dei termini che compaiono solamente in una classe
termini_diff = set(spoil0_rapp.keys()).symmetric_difference(spoil1_rapp.keys())
# vi sono 559 termini che compaiono solamente in una classe



# user_input
i = 0
j = 0
while i < 1:
    user_input2 = input('\nVuoi mantenere solamente il 20% dei termini che hanno ottenuto il punteggio più elevato nel test chi quadrato? Digita YES o NO\n')
    if user_input2.lower() in ('y', 'yes'):
        i += 1
        p = 0.2
    elif user_input2.lower() in ('n', 'no'):
        i += 1
        while j < 1:
            user_input3 = input('Inserire il valore percentuale (intero da 1 a 100)\n')
            try:
                user_input3 = int(user_input3)
                if user_input3 in range(1,101):
                    p = user_input3/100
                    j += 1
                else:
                    print("\nInput errato, inserire un intero da 1 a 100.\n")
            except ValueError:
                print("\nInput errato, inserire un intero da 1 a 100.\n")
    else:
        print("\nInput errato, per favore digitare YES o NO\n")




# creazione della lista del 20% dei termini che hanno ottenuto il punteggio più alto nel test chi quadrato (1853 termini)
# oltre agli 559 termini che compaiono solamente in una classe (e non nell'altra)
parole_chi2 = list(chisq_sort.keys())[0:int((len(chisq_sort))*p)] + list(termini_diff)
print('\nSono stati selezionati i '+str(len(parole_chi2))+' termini che più discriminano tra le due classi, di cui:')
print('- '+str(int((len(chisq_sort))*p))+' termini con punteggio più elevato ottenuto nel test chi quadrato;')
print('- '+str(len(termini_diff))+' termini che compaiono esclusivamente in una classe ma non nell\'altra.\n')
# vengono selezionati 2412 termini in totale
 

# creazione di un dizionario che ha come chiave i termini selezionati
dizio_chi2 = {}
for j in parole_chi2: 
        dizio_chi2[j] = []


# inserimento nel dizionario della frequenza di ogni termine sul model set
print('Sto contando le occorrenze di ogni termine selezionato sul model set, composto da '+str(len(model_set))+' frasi...')
print('La procedura richiede circa 5 minuti.\n')
for i in range(len(model_set)):
    for j in parole_chi2: 
        dizio_chi2[j].append(model_set[i][1].split().count(j))


# trasformazione del dizionario in una lista di liste,
# dove ogni sottolista contiene due elementi: 
# il primo elemento è uno dei 2412 termini selezionati
# il secondo è una lista della lunghezza del model set, dove ogni elemento
# indica il conteggio del termine in ogni frase del model set
model_chisq = [[k,v] for k,v in list(dizio_chi2.items())]


# creazione di un'unica lista contenente le occorrenze di tutti i termini in tutte le frasi del model_set
x_matrix = []
for k in range(len(model_set)):
    for j in range(len(model_chisq)):
        x_matrix.append(model_chisq[j][1][k])


# passaggio da una lista unica ad una lista di liste
# ogni sottolista contiene 2412 valori, ognuno dei quali rappresenta il numero
# di occorrenze di ogni termine all'interno di una frase del model set
x_espl = [x_matrix[x:x+len(parole_chi2)] for x in range(0, len(x_matrix), len(parole_chi2))]      


# conteggio delle frasi 'vuote', ovvero quelle frasi che
# non presentano nemmeno un termine tra quelli selezionati
count_vuote = 0
for i in range(len(x_espl)):
    if sum(x_espl[i]) < 1:
        count_vuote += 1
print('Il '+str(round(100*count_vuote/len(x_espl), 2))+'% delle frasi del model set non contiene nessun termine tra quelli selezionati.\n')
# Lo 0.04% del totale delle frasi del model set non non contiene nessun termine tra quelli selezionati 



# creazione del vettore y (variabile risposta), contenente 0 o 1 
# in base alla classe della frase (no-spoiler o spoiler)
print('Sto creando la matrice delle esplicative X ed il vettore risposta y...\n')
y = []
for j in range(len(model_set)):
    y.append(model_set[j][0])


# sostituzione del valore 0 con il valore -1, in quanto +1 e -1 sono i valori 
# predefiniti della variabile risposta per il percettrone ed il SVM
y_corretto = []
for i in range(len(y)):
    if y[i] == 0:
        y_corretto += [-1]
    else:
        y_corretto += [1]


# aggiunta delle variabili categoriali relative al libro a cui la frase si riferisce
# e della variabile indicante la posizione relativa della frase all'interno della recensione
for i in range(len(x_espl)):
    x_espl[i] += model_set[i][2:]
# la 'matrice' è formata da 87753 righe e 2986 colonne


#calcolo numero di frasi spoiler-no spoiler sul model set
uni = sum(y)
zeri = len(y)-uni
uni_perc = uni/len(y)*100
zeri_perc = zeri/len(y)*100
print('Nel model set sono presenti '+str(uni)+' frasi spoiler (il '+str(round(uni_perc, 2))+'% sul totale).')
print('Nel model set sono presenti '+str(zeri)+' frasi no-spoiler (il '+str(round(zeri_perc, 2))+'% sul totale).\n')
# nel model_set sono presenti 27386 frasi spoiler (il 31.21% sul totale) e 60367 frasi no-spoiler (il 68.79% sul totale).



# creazione degli indici per creazione training, validation e test set
# il model set viene diviso nella seguente maniera:
# 50% per il training set, 25% per il validation set ed il 25% per il test set
# il seed viene fissato per rendere replicabile l'esperimento
print('Sto separando casualmente il model set negli insiemi di training, validation e test nella proporzione 50/25/25...\n')
seed(123)
indice_tr = sample(range(len(x_espl)), int(0.5*len(x_espl)))
indice_val_test = set(range(len(x_espl))) - set(indice_tr)
indice_val = sample(indice_val_test, int(0.5*len(indice_val_test)))
indice_ts = list(set(indice_val_test) - set(indice_val))


# creazione delle liste formate dalle variabili esplicative e dalla variabile risposta
x_train = [x_espl[i] for i in indice_tr]
y_train = [y_corretto[i] for i in indice_tr]

x_valid = [x_espl[i] for i in indice_val]
y_valid = [y_corretto[i] for i in indice_val]

x_test = [x_espl[i] for i in indice_ts]
y_test = [y_corretto[i] for i in indice_ts]


# unione delle variabili esplicative e della variabile risposta per i tre insiemi
train = [x +[y] for x, y in zip(x_train, y_train)]
validation = [x +[y] for x, y in zip(x_valid, y_valid)]
test = [x +[y] for x, y in zip(x_test, y_test)]


# salvataggio dei tre insiemi in formato json
with open('training.json', 'w') as outfile:
    json.dump(train, outfile)
print('Nella cartella di lavoro è stato salvato il training set (file denominato \'training.json\')')
print('Il training set è composto da '+str(len(train))+' frasi.')
# il training set è composto da 43876 frasi

with open('validation.json', 'w') as outfile:
    json.dump(validation, outfile)
print('Nella cartella di lavoro è stato salvato il validation set (file denominato \'validation.json\')')
print('Il validation set è composto da '+str(len(validation))+' frasi.')
# il validation set è composto da 21938 frasi

with open('test.json', 'w') as outfile:
    json.dump(test, outfile)
print('Nella cartella di lavoro è stato salvato il test set (file denominato \'test.json\')')
print('Il test set è composto da '+str(len(test))+' frasi.')
# il test set è composto da 21939 frasi



# AVVIO MODELLAZIONE

# user_input
i = 0
while i < 1:
    user_input2 = input('\nVuoi procedere con la fase di modellazione? Digita YES o NO\n')
    if user_input2.lower() in ('y', 'yes'):
        i += 1
        exec(open('applicazione_modelli.py').read())
    elif user_input2.lower() in ('n', 'no'):
        i += 1
    else:
        print("\nInput errato, per favore digitare YES o NO")
    

