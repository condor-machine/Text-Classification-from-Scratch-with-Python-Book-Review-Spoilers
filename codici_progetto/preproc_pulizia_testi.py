### PREPROCESSING DEI TESTI

# import librerie e funzioni utili
from utili import *


# lettura dati
print('\nSto caricando il file \'goodreads_reviews_spoiler.json.gz\'...\n')
spoiler = carica_json_gz('goodreads_reviews_spoiler.json.gz')


# vengono mantenute solamente le recensioni che contengono almeno una frase spoiler,
# indicate dai dizionari con la coppia chiave:valore 'has_spoiler': True
spoil = []

for j in range(len(spoiler)):
    if spoiler[j]['has_spoiler'] == True:
        spoil.append(spoiler[j])
print('Sono state mantenute solamente le '+str(len(spoil))+' recensioni contententi almeno una frase spoiler.\n')
del(spoiler)
# si è passati da 1378033 a 89627 recensioni 


# creazione di una lista contenente gli identificativi univoci dei libri,
# indicati dalla chiave book_id nei dizionari
books = []

for i in range(len(spoil)):
    books.append(spoil[i]['book_id'])

print('Le 89627 recensioni sono relative a '+str(len(set(books)))+' diversi libri.\n')
# le 89627 recensioni sono relative a 24558 diversi libri


# conteggio delle occorrenze di ogni libro tra tutte le recensioni
print('Sto contando quante volte è stato recensito ogni diverso libro...')
print('La procedura richiede circa 5 minuti.\n')
dict_books = conta_occorrenze(books)


# user_input
i = 0
j = 0
while i < 1:
    user_input = input('Vuoi mantenere solamente le recensioni dei libri recensiti almeno 20 volte? Digita YES o NO\n')
    if user_input.lower() in ('y', 'yes'):
        i += 1
        N = 20
    elif user_input.lower() in ('n', 'no'):
        i += 1
        while j < 1:
            user_input1 = input('Inserire il valore N (intero da 1 a 150)\n')
            try:
                N = int(user_input1)
                if N in range(1,151):
                    j += 1
                else:
                   print("\nInput errato, inserire un intero da 1 a 150.\n") 
            except ValueError:
                print("\nInput errato, inserire un intero da 1 a 150.\n")
    else:
        print("\nInput errato, per favore digitare YES o NO\n")



# vengono mantenute solamente le recensioni relative ai libri con almeno 20 occorrenze (recensiti almeno 20 volte)
# N = 20
filt_books = {k: v for k, v in dict_books.items() if v >= N}

spoiler = []
for j in range(len(spoil)):
    if spoil[j]['book_id'] in list(filt_books.keys()):
        spoiler.append(spoil[j])

print('\nSono state mantenute solamente '+str(len(spoiler))+' recensioni, relative ai '+str(len(filt_books))+' libri recensiti almeno '+str(N)+' volte.\n')
# la lista di dizionari è passata da 89627 elementi a 24798
# le 24798 recensioni sono relative a 574 diversi libri


# ad ogni frase viene aggiunta una lista, contentente un valore indicante il libro a cui si riferisce,
# in formato di variabile categoriale (573 elementi di cui al più 1 elemento uguale a 1)
print('Sto inserendo le variabili relative al libro alla quale si riferisce la recensione, ed alla posizione della frase all\'interno della recensione...\n')
libri_filt =  list(filt_books.keys())[1:]

for i in range(len(spoiler)):
    for j in range(len(spoiler[i]['review_sentences'])):
        spoiler[i]['review_sentences'][j] += [0]*len(libri_filt)
       
        
for i in range(len(spoiler)):
    for j in range(len(spoiler[i]['review_sentences'])):
        for k in range(len(libri_filt)):
            if libri_filt[k] == spoiler[i]['book_id']:
                spoiler[i]['review_sentences'][j][k+2] += 1
        

del(spoil,books,filt_books,dict_books,libri_filt,N)


# viene inserito in ogni sottolista (ossia una frase della recensione)
# un numero tra 0 e 1, indicante la posizione relativa della frase all'interno della recensione
for i in range(len(spoiler)):
    for j in range(len(spoiler[i]['review_sentences'])):
        spoiler[i]['review_sentences'][j].append((j+1)/len(spoiler[i]['review_sentences']))

print('Valori aggiunti correttamente.\n')


# viene modificata la lista di dizionari per ottenere una lista di liste,
# in cui ogni sottolista ha 576 elementi: 
# 0/1 (frase spoiler o no-spoiler)
# stringa contenente una frase della recensione
# 573 valori di cui al più uno vale 1 e gli altri 0 (variabile categoriale libro)
# numero da 0 a 1 indicante la posizione relativa della frase all'interno della recensione
# eliminando quindi tutte le informazioni relative a:
# ("user_id","timestamp","rating","review_id","has_spoiler","book_id")
spoil = []

for j in range(len(spoiler)):
    spoil += spoiler[j]['review_sentences']

print('Le '+str(len(spoiler))+' recensioni selezionate sono composte in totale da '+str(len(spoil))+' frasi.\n')
# la lista è formata da 636861 liste, ciascuna con le informazioni relative ad un'unica frase
        
del(spoiler)






# procedura di pulizia dei testi
print('Sto eliminando le stop words ed i caratteri speciali...\n')

# lista delle stop words
nltk.download('stopwords')
from nltk.corpus import stopwords

stop_words = stopwords.words('english')

# aggiunta delle singole lettere alla lista delle stop words 
alfabeto = [chr(i) for i in range(ord('a'),ord('z')+1)]
stop_words = stop_words + alfabeto + ['-']
del(alfabeto) # è contenuto in stop_words


# tupla contenente i caratteri speciali da rimuovere nei testi
caratteri_speciali = (',','.',':',';','#','*','"','\'','!','$','?','\\n','(',')','[',']','/',
                      '+','^','|','{','}','~','<','>','0','1','2','3','4','5','6','7','8','9')

# eliminazione dei caratteri speciali e conversione delle parole in minuscolo
for i in caratteri_speciali:
    for j in range(len(spoil)):
        spoil[j][1] = spoil[j][1].lower().replace(i,'')

# sostituzione del 'doppio trattino' e della 'chiocciola' con lo 'spazio'
for j in range(len(spoil)):
    spoil[j][1] = spoil[j][1].replace('--',' ')
    spoil[j][1] = spoil[j][1].replace('@',' ')

# separazione delle parole per poterle eliminare se presenti nella lista delle stop words
for j in range(len(spoil)):
    spoil[j][1] = spoil[j][1].split()

# eliminazione delle stop words
for j in range(len(spoil)):
    spoil[j][1] = [i for i in spoil[j][1] if i not in stop_words]


# stemming delle parole utilizzando l'algoritmo 'Porter stemmer'
print('\nSto effettuando lo stemming delle parole...\n')
stemmer = PorterStemmer()

for j in range(len(spoil)):
    spoil[j][1] = [stemmer.stem(i) for i in spoil[j][1]]



# user_input
i = 0
j = 0
while i < 1:
    user_input2 = input('Vuoi eliminare le frasi con meno di 10 termini e quelle con più di 30 termini? Digita YES o NO\n')
    if user_input2.lower() in ('y', 'yes'):
        i += 1
        minimo = 10
        massimo = 30
    elif user_input2.lower() in ('n', 'no'):
        i += 1
        while j < 1:
            user_input3 = input('Quanti termini deve contenere minimo una frase? (intero da 1 a 20)\n')
            user_input4 = input('Quanti termini deve contenere massimo una frase? (intero da 21 a 50)\n')
            try:     
                user_input3 = int(user_input3)
                user_input4 = int(user_input4)
                if user_input3 in range(1,21) and user_input4 in range(21,51):
                    j += 1
                    minimo = user_input3
                    massimo = user_input4
                else:
                    print("\nInput errati.\n")
            except ValueError:
                print("\nInput errati.\n")
    else:
        print("\nInput errato, per favore digitare YES o NO\n")




# eliminazione delle frasi che contengono meno di 10 termini e di quelle che ne contengono più di 30
spoiler = []
for i in range(len(spoil)):
    if len(spoil[i][1]) >= minimo and len(spoil[i][1]) <= massimo:
        spoiler.append(spoil[i])
print('\nSono state eliminate le frasi con meno di '+str(minimo)+' termini e quelle con più di '+str(massimo)+' termini.\n')        
print('Il dataset è ora formato da '+str(len(spoiler))+' diverse frasi.\n')
# il numero di frasi è passato da 636861 a 175505

# ricompattamento dei termini in unica stringa
for j in range(len(spoiler)):
    spoiler[j][1] = (' ').join(spoiler[j][1])


#calcolo numero di frasi spoiler-no spoiler sul totale
uni = 0
for i in spoiler:
    uni += i[0]
zeri = len(spoiler)-uni
uni_perc = uni/len(spoiler)*100
zeri_perc = zeri/len(spoiler)*100
print('Sono presenti '+str(uni)+' frasi spoiler (il '+str(round(uni_perc, 2))+'% sul totale).\n')
print('Sono presenti '+str(zeri)+' frasi spoiler (il '+str(round(zeri_perc, 2))+'% sul totale).\n')
# nel dataset ridotto sono presenti 54752 frasi spoiler (il 31.2% sul totale) e 120753 frasi no-spoiler (il 68.8% sul totale).


del(spoil,caratteri_speciali,stopwords,stop_words)






# campionamento casuale semplice per selezionare il features selection set ed il model set;
# scegliamo di prendere il 50% del campione totale per ognuno dei due insiemi
# il seed viene fissato per rendere replicabile l'esperimento
print('Sto separando casualmente le frasi in due insiemi di egual dimensione...\n')
seed(123)
indice_feat = sample(range(len(spoiler)), int(0.5*len(spoiler)))
indice_mod = set(range(len(spoiler))) - set(indice_feat)

# creazione del features selection set e del model set
features_selection_set = [spoiler[i] for i in indice_feat]
model_set = [spoiler[i] for i in indice_mod]


del(indice_feat,indice_mod,spoiler)


# salvataggio dei due insiemi in formato json
with open('features_selection_set.json', 'w', encoding='utf-8') as f:
    json.dump(features_selection_set, f, ensure_ascii=False, indent=4)

print('Nella cartella di lavoro è stato salvato l\'insieme per la procedura di features selection (file denominato \'features_selection_set.json\')\n')

with open('model_set.json', 'w', encoding='utf-8') as f:
    json.dump(model_set, f, ensure_ascii=False, indent=4)
    
print('Nella cartella di lavoro è stato salvato l\'insieme per la procedura di modellazione (file denominato \'model_set.json\')\n')


# scrittura su file delle frasi 'pulite' presenti nel features selection set
# il file servirà a conteggiare le occorrenze di ogni termine nel totale delle frasi
# (procedura da svolgere tramite MapReduce (vedi readme.txt))
frasi_pulite = open('frasi_pulite_features_selection_set.txt','w',encoding='utf8')
for j in range(len(features_selection_set)):
    frasi_pulite.write(features_selection_set[j][1]+' ')

print('Nella cartella di lavoro sono stati salvati i testi delle frasi presenti nell\'insieme per la features selection (file denominato \'frasi_pulite_features_selection_set.txt\')\n\n')
print('Per procedere con il conteggio dei termini tramite MapReduce, digitare dalla riga di comando la seguente stringa:\n')
print('\ntype frasi_pulite_features_selection_set.txt | mapper.py | reducer.py')
print('\nNB. Se si sta utilizzando un OS diverso da Windows, sostituire \'type\' con \'cat\'\n')


