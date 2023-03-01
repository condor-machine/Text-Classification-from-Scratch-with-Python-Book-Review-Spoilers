# AVVIO MODELLI


# se il training set ed il test set non sono presenti in memoria, bisogna caricarli
if 'train' not in locals():
    
    import json
    
    # caricamento training set
    print('\nSto caricando il training set...')
    with open('training.json') as json_file:
        train = json.load(json_file)
        
    for i in range(len(train)):
            train[i] = [float(x) for x in train[i]]
        
                   
    # caricamento test set
    print('\nSto caricando il test set...')
    with open('test.json') as json_file:
        test = json.load(json_file)
        
    for i in range(len(test)):
            test[i] = [float(x) for x in test[i]]
    
       
    print('\nCaricamento effettuato con successo!\n')
    print('Il training set è composto da '+str(len(train))+' frasi.')
    print('Il test set è composto da '+str(len(test))+' frasi.')




# user_input
i = 0
while i < 1:
    user_input = input('\nVuoi adattare il percettrone o il SVM? Digita P per il percettrone oppure S per il SVM\n')
    if user_input.lower() in ('p'):
        i += 1
        exec(open('percettrone.py').read())
    elif user_input.lower() in ('s'):
        i += 1
        exec(open('svm.py').read())
    else:
        print("\nInput errato, per favore digitare P o S")


