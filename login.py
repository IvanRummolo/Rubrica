import {'funzioni.py'}

# Esecuzione --------------------------

nome_utente = input("nome utente >> ")
password = input("password >> ")
esito = False


# verifica esito --> false
while esito == False: 
    #esito = false
    esito = login(nome_utente, password)

    if esito:
        print("login effettuato con successo, benvenuto:", nome_utente)
    else:
        print("dati sbagliati, riprova")
        print("Inserisci i nuovi dati")
        nome_utente = input("nome utente >> ")  
        password = input("password >> ")