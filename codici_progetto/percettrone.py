# PREVISIONI CON PERCETTRONE

from modelli import *


# se la matrice X ed il vettore y relativi al percettrone non sono presenti in memoria, bisogna caricarli
if 'x_tr_p' not in locals():

    # separazione predittori e risposta training set
    x_tr_p = [i[0:len(i)-1] for i in train]
    y_tr_p = [i[-1] for i in train]
        
    # aggiunto predittore costante = -1 sul training set
    # per poter incorporare il parametro soglia del percettrone nel vettore dei coefficienti
    for k in range(len(x_tr_p)):
        x_tr_p[k].append(-1)
        
            
    # separazione predittori e risposta test set
    x_ts_p = [i[0:len(i)-1] for i in test]
    y_ts_p = [i[-1] for i in test]
        
    # aggiunto predittore costante = -1 sul test set
    # per poter incorporare il parametro soglia del percettrone nel vettore dei coefficienti
    for k in range(len(x_ts_p)):
        x_ts_p[k].append(-1)
    


# user_input
i = 0
j = 0
while i < 1:
    user_input = input('\nVuoi fissare il numero di iterazioni a 23? Digita YES o NO\n')
    if user_input.lower() in ('y', 'yes'):
        i += 1
        n_iter = 23
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



# stima percettrone su training set
print("Sto adattando il percettrone ai dati...\n")
w = fit_perc(x_tr_p, y_tr_p, n_iter)

# calcolo previsioni su test set
print("Sto calcolando le previsioni...\n")
res = pred(x_ts_p, y_ts_p, w)

print('Per '+str(n_iter)+' iterazioni, sul test set si sono ottenuti i seguenti risultati:\n')
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
    

