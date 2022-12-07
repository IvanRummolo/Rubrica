def verifica_esistenza(lista, elemento):
    indice = 0
    for valore in lista:
        if valore == elemento:
            return indice
        indice += 1
    return -1
    
def login(nome,password):
    # ipotizziamo che esista una funzione che prende queste variabili da un db
    nome_utente_db = ["topolino", "pippo", "minnie"]
    password_db = ["pluto1234", 'paperone4', "paperoga6"]
    # Come faccio a sapere se un nome è presente in una lista?
    nome_presente = verifica_esistenza(nome_utente_db, nome)
    pass_presente = verifica_esistenza(password_db, password)
    # -------------------------------------------------------------------------
    if nome_presente == pass_presente and nome_presente != -1: 
       
        return True
    else:
        return False