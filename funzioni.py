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

def visualizza_lista(nomi, numeri):
    print("Lista nomi: -----------------")
    for i in range(len(nomi)):
        print("nome:", nomi[i] ,"numero: ", numeri[i])
    print("-----------------------------")

def aggiungi(lista, elemento):
    lista.append(elemento)
    return lista

def elimina(lista, elemento):
    nuova_lista = []
    for el in lista:
        if el != elemento:
            nuova_lista.append(el)
    return nuova_lista

def trova_numero(nome, lista_nomi, lista_numeri):
    indice = verifica_esistenza(lista_nomi, nome)
    if indice != -1:
        return lista_numeri[indice]
    else:
        return "numero non trovato"

def modifica(lista, vecchio_nome, nuovo_nome):
    for i in range(len(lista)):
        if lista[i] == vecchio_nome:
            lista[i] = nuovo_nome
    return lista 