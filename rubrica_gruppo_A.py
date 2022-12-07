# Struttura del progetto

# Il programma è una rubrica che tiene traccia dei nomi, ha diverse funzionalità:
#   Aggiungere un nome
#   Modificare un nome
#   Eliminare un nome
#   Visualizzare tutta la rubrica

#Gruppo A
# Francesco C
# Ivan
# Luca Samuele
# Danila


#Implementare funzioni:

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
    indice = -1
    for i in range(len(lista_nomi)):
        if nome == lista_nomi[i]:
            indice = i
            break
    if indice != -1:
        return lista_numeri[indice]
    else:
        return "numero non trovato"

def modifica(lista, vecchio_nome, nuovo_nome):
    for i in range(len(lista)):
        if lista[i] == vecchio_nome:
            lista[i] = nuovo_nome
    return lista 


#Avviamo il programma
print("Benvenuto nel programma rubrica:")
print("comandi disponibili: lista, aggiungi, elimina, modifica, esci")

comando = input("inserire comando >> ")
esci = False

nomi = []
numeri = []

while not esci:

    match comando:
        case 'lista':
            visualizza_lista(nomi, numeri) 
        case 'aggiungi':
            nome = input("Inserisci nome da aggiungere >> ")
            numero = input("Inserisci numero da aggiungere >> ")
            nomi = aggiungi(nomi, nome)
            numeri = aggiungi(numeri, numero)
        case 'elimina':
            nome = input("Inserisci nome da eliminare >> ")
            numero = trova_numero(nome, nomi, numeri)
            nomi = elimina(nomi, nome)
            numeri = elimina(numeri, numero)
        case 'modifica':
            nome = input("Inserisci il contatto da modificare >> ")
            ris = input("modificare il nome o il numero? nome/numero >> ")
            if ris == 'nome':
                nuovo_nome = input("inserisci nuovo nome >> ")
                nomi = modifica(nomi, nome, nuovo_nome)
            elif ris == 'numero':
                nuovo_numero = input("inserisci nuovo numero >> ")
                numero = trova_numero(nome, nomi, numeri)
                numeri = modifica(numeri, numero, nuovo_numero)
            else:
                print("scelta sbagliata.")
            
        case 'esci':
            print("sto chiudendo il programma")
            esci = True
        case _:
            print("hai inserito un comando sbagliato, riprova")
    
    if not esci:
        comando = input("inserire comando >> ")

    
