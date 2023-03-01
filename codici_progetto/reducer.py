# REDUCER (PROCEDURA MAPREDUCE)

import sys
 
# dizionario per i conteggi
wordcount = {}
 
# ricezione input
for line in sys.stdin:
    # rimozione spazi prima e dopo la stringa
    line = line.strip()
 
    # valore 1 assegnato ad ogni termine
    word, count = line.split('\t', 1)
    # conversione conteggio in intero
    try:
        count = int(count)
    except ValueError:
        continue
 
    try:
        wordcount[word] = wordcount[word]+count
    except:
        wordcount[word] = count
 
# scrittura output
output_file = open('conteggio_termini.txt','w',encoding='utf8',errors='ignore')
for word in wordcount.keys():
    output_file.write( '%s %s\n'% ( word, wordcount[word] ))
print('\nConteggio dei termini avvenuto correttamente!')
print('I risultati sono stati salvati nella cartella di lavoro (file denominato \'conteggio_termini.txt\').\n\n')
print('Per procedere con la procedura di features selection, digitare dalla riga di comando la seguente stringa:\n')
print('preproc_features_selection.py\n')
