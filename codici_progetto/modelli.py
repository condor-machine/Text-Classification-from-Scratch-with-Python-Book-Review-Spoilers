# FUNZIONI PER STIMARE PERCETTRONE E SVM, E CALCOLARE PREVISIONI

import numpy as np
from sklearn.metrics import confusion_matrix   
from utili import accuracy,recall,F1



# funzione per stimare un percettrone
def fit_perc(x_tr, y_tr, n_iter):
    # x_tr: lista di liste contenente i valori
    #       delle variabili esplicative sul train set
    #       ultima variabile costante = -1
    # y_tr: lista contenente la classe (-1/1)
    #       della variabile risposta sul train set
    # n_iter: intero rappresentante il numero di
    #         iterazioni dell'algoritmo
    
    
    # passaggio da liste di liste ad array di numpy
    x_tr,y_tr = np.array(x_tr),np.array(y_tr)
    
    # inizializzazione coefficienti: w = 0
    w = np.zeros(np.shape(x_tr)[1])
    
    # algoritmo di stima del percettrone:
        
    # per i=1,...,numero_iterazioni:
    for i in range(1, n_iter):
    
    # per j=1,...,numero_osservazioni:
        for j in range(len(y_tr)):
            
    # risposta prevista = esplicative * coefficienti
            yp = np.dot(x_tr[j],w)
            
    # se risposta prevista e osservata hanno segno opposto:
            if yp*y_tr[j]<=0:
                
    # aggiorna i coefficienti 
                w += np.dot(x_tr[j],y_tr[j])
                
    # stampa il numero di iterazioni (ogni 10)            
        if (i % 5) == 0:
            print(str(i)+' iterazioni...')
            
    # ritorna il vettore dei coefficienti       
    return(w)
    
    

# funzione per stimare un SVM  
def fit_svm(x_tr, y_tr, n_iter, eta, C):
    # x_tr: lista di liste contenente i valori
    #       delle variabili esplicative sul train set
    #       prima variabile costante = 1
    # y_tr: lista contenente la classe (-1/1)
    #       della variabile risposta sul train set
    # n_iter: intero rappresentante il numero di
    #         iterazioni dell'algoritmo
    # eta: tasso di apprendimento
    # C: parametro di regolazione
    
    # passaggio da liste di liste ad array di numpy
    x_tr,y_tr = np.array(x_tr),np.array(y_tr)
    
    # inizializzazione coefficienti: w = 0
    w = np.zeros(x_tr.shape[1])
    
    
    # algoritmo di stima del SVM:
        
    # per j=1,...,numero_iterazioni:
    for j in range(1, n_iter):
    
    # per i in 1,...,numero_osservazioni
    # e xx i-esimo elemento di x_tr:
        for i, xx in enumerate(x_tr):
            Y = np.array([y_tr[i]])
            X = np.array([xx]) 
            dist = 1 - (Y * np.dot(X, np.transpose(w)))
            
    # se max(0, 1 - y * x * w) = 0:
            if max(0, dist) == 0:
    # gradiente della funzione di costo = w
                grad = w
                
    # altrimenti:
            else:
    # gradiente della funzione di costo = w - C * y * x
                grad = w - (C * Y * X)
                
    # aggiorna i coefficienti contro gradiente       
            w = w - (eta * grad)
            
    # stampa il numero di iterazioni (ogni 10)     
        if (j % 5) == 0:
            print(str(j)+' iterazioni...')
            
    # ritorna il vettore dei coefficienti
    return(w)


   
# funzione per ottenere i valori previsti da un percettrone o da un SVM   
def pred(x_ts, y_ts, w):
    # x_ts: lista di liste contenente i valori delle
    #       variabili esplicative sul validation/test set
    # y_ts: lista contenente la classe (-1/1) della
    #       variabile risposta sul validation/test set
    # w: vettore di coefficienti stimato tramite
    #    percettrone o SVM
    
    
    # passaggio da lista di liste ad array di numpy
    x_ts = np.array(x_ts)

    # calcolo previsioni su validation/test set
    pred = np.dot(x_ts,np.transpose(w))
    ypred = []
    
    # alloco le previsioni nelle rispettive classi
    for i in range(len(pred)):
        if pred[i]<=0:
            ypred += [-1]
        else:
            ypred += [1]
    # calcolo la confusion matrix
    cm = confusion_matrix(y_ts,ypred)
    
    # output: [confusion matrix, accuracy, recall e F1 per classe spoiler]
    return [cm,accuracy(cm),recall(1,cm),F1(1,cm)]
   
   
   