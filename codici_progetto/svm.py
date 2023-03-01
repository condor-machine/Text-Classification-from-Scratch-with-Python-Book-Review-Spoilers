# PREVISIONI CON SVM

from modelli import *


# se la matrice X ed il vettore y relativi al SVM non sono presenti in memoria, bisogna caricarli
if 'x_tr_s' not in locals():
    
    # separazione predittori e risposta training set
    x_tr_s = [i[0:len(i)-1] for i in train]
    y_tr_s = [i[-1] for i in train]
        
    # aggiunto predittore costante = 1 sul training set
    # per poter incorporare l'intercetta nel modello
    for k in range(len(x_tr_s)):
        x_tr_s[k] = [1] + x_tr_s[k]
        
        
    # separazione predittori e risposta test set 
    x_ts_s = [i[0:len(i)-1] for i in test]
    y_ts_s = [i[-1] for i in test]
    
    # aggiunto predittore costante = 1 sul test set
    # per poter incorporare l'intercetta nel modello    
    for k in range(len(x_ts_s)):
        x_ts_s[k] = [1] + x_ts_s[k]
      
      

# user_input
i = 0
j = 0
while i < 1:
    user_input = input('\nVuoi fissare il numero di iterazioni a 34? Digita YES o NO\n')
    if user_input.lower() in ('y', 'yes'):
        i += 1
        n_iter = 34
    elif user_input.lower() in ('n', 'no'):
        i += 1
        while j < 1:
            user_input1 = input('\nInserire il valore N (intero positivo)\n')
            try:
                n_iter = int(user_input1)
                if n_iter > 0:
                    j += 1
                else:
                   print("\nInput errato, inserire un intero positivo.") 
            except ValueError:
               print("\nInput errato, inserire un intero positivo.")
    else:
        print("\nInput errato, per favore digitare YES o NO")
        
print("\nNumero di iterazioni fissato a "+str(n_iter)+".\n")


# user_input
i = 0
j = 0
while i < 1:
    user_input2 = input('Vuoi fissare il learning rate a 1e-08? Digita YES o NO\n')
    if user_input2.lower() in ('y', 'yes'):
        i += 1
        eta = 1e-08
    elif user_input2.lower() in ('n', 'no'):
        i += 1
        while j < 1:
            user_input3 = input('\nInserire il valore del learning rate\n')
            try:
                eta = float(user_input3)
                j += 1
            except ValueError:
               print("Input errato, inserire un numero.\n")
    else:
        print("\nInput errato, per favore digitare YES o NO")

print("\nLearning rate fissato a "+str(eta)+".\n")



# user_input
i = 0
j = 0
while i < 1:
    user_input4 = input('Vuoi fissare il valore C a 1.1e+09? Digita YES o NO\n')
    if user_input4.lower() in ('y', 'yes'):
        i += 1
        C = 1.1e+09
    elif user_input4.lower() in ('n', 'no'):
        i += 1
        while j < 1:
            user_input5 = input('\nInserire il valore di C\n')
            try:
                C = float(user_input5)
                j += 1
            except ValueError:
               print("Input errato, inserire un numero.\n")
    else:
        print("\nInput errato, per favore digitare YES o NO")

print("\nC fissato a "+str(C)+".\n")


# stima SVM su training set
print("Sto adattando il SVM ai dati...\n")
w = fit_svm(x_tr_s, y_tr_s, n_iter, eta, C)

# calcolo previsioni su test set
print("Sto calcolando le previsioni...\n")
res = pred(x_ts_s, y_ts_s, w)

print('Per '+str(n_iter)+' iterazioni, learning rate = '+str(eta)+', C = '+str(C)+', nel test set si sono ottenuti i seguenti risultati:\n')
print('Accuracy: '+str(res[1])+'\nRecall: '+str(res[2])+'\nF1-score: '+str(res[3]))
print('\nMatrice di confusione:')
print('\n'+str(res[0])+'\n')
     
    
    
# user_input
i = 0
while i < 1:
    user_input2 = input('Vuoi adattare un altro modello? Digita YES o NO\n')
    if user_input2.lower() in ('y', 'yes'):
        i += 1
        exec(open('applicazione_modelli.py').read())
    elif user_input2.lower() in ('n', 'no'):
        i += 1
    else:
        print("\nInput errato, per favore digitare YES o NO")


