### LIBRERIE E FUNZIONI UTILI

# importazione librerie utili per la lettura e il preprocessing dei dati
import gzip
import json
from time import process_time
from random import sample, seed
import nltk
from nltk.stem.porter import *
import numpy as np


# funzione per leggere un file .json.gz
def carica_json_gz(nome_file):
    start = process_time()
    count = 0
    data = []
    with gzip.open(nome_file) as fin:
        for l in fin:
            d = json.loads(l)
            count += 1
            data.append(d)
    end = process_time()
    time = end - start
    print('Caricamento file avvenuto in circa '+str(int(time))+' secondi.'+'\nIl file contiene '+str(len(data))+' diverse recensioni.\n')
    return data


# funzione per contare le occorrenze degli elementi di una lista
# l'output è un dizionario con coppie elemento:num_occorrenze
def conta_occorrenze(lista):
   dizio={}
   for x in lista:
       if not x in dizio:        
          dizio[x] = lista.count(x)
   return dizio


# funzione per ordinare le sottoliste di una lista di liste
# in base al secondo elemento delle sottoliste
def ordina(sub_li): 
    l = len(sub_li) 
    for i in range(l): 
        for j in range(l-i-1): 
            if (sub_li[j][1] > sub_li[j + 1][1]): 
                tempo = sub_li[j] 
                sub_li[j]= sub_li[j + 1] 
                sub_li[j + 1]= tempo 
    return sub_li 


# funzione per il calcolo del test chi quadrato
def chisq2(parola0, parola1):
    att = (parola0 + parola1)/2
    chi0 = (parola0-att)**2/att
    chi1 = (parola1-att)**2/att
    return chi0+chi1


# funzione che, data una confusion matrix, ne calcola l'accuracy
def accuracy(conf_matr):
    diag_sum = conf_matr.trace()
    tot_sum = conf_matr.sum()
    return(diag_sum / tot_sum) 


# funzione che, data una classe e una confusion-matrix, 
# calcola la recall per quella classe
def recall(classe, conf_matr):
    positivi = sum(conf_matr[classe, :])
    veri_positivi = conf_matr[classe, classe]
    return(veri_positivi / positivi)


# funzione che, data una classe e una confusion-matrix, 
# calcola la precision per quella classe
def precision(classe, conf_matr):
    veri_positivi = conf_matr[classe, classe]
    falsi_negativi = conf_matr[1-classe, classe]
    return(veri_positivi / (veri_positivi+falsi_negativi))


# funzione che, data una classe e una confusion-matrix, 
# calcola l'F1-score per quella classe
def F1(classe, conf_matr):
    prec = precision(classe, conf_matr)
    rec = recall(classe, conf_matr)
    f1 = 2*prec*rec/(prec+rec)
    return(f1)


