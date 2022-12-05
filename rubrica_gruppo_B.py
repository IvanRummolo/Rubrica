# Struttura del progetto

# Il programma è una rubrica che tiene traccia dei nomi, ha diverse funzionalità:
#   Aggiungere un nome
#   Modificare un nome
#   Eliminare un nome
#   Visualizzare tutta la rubrica

#Gruppo B:
# Francesco P
# Irene
# Marco

#Implementare funzioni:

def visualizza_lista(lista):
    return
    #com

def aggiungi_nome(lista, nome):
    return

def elimina_nome(lista, nome):
    return

def modifica_nome(lista, vecchio_nome, nuovo_nome):
    return

#Avviamo il programma
print("Benvenuto nel programma rubrica:")
print("comandi disponibili: lista, aggiungi, elimina, modifica, esci")

comando = input("inserire comando >> ")
esci = False
nomi = []

while not esci:

    match comando:
        case 'lista':
            visualizza_lista(nomi)
        case 'aggiungi':
            nome = input("Inserisci nome da aggiungere >> ")
            aggiungi_nome(nomi, nome)
        case 'elimina':
            nome = input("Inserisci nome da eliminare >> ")
            elimina_nome(nomi, nome)
        case 'modifica':
            nome = input("Inserisci nome da modificare >> ")
            nuovo_nome = input("Inserisci il nuovo nome >> ")
            modifica_nome(nomi, nome, nuovo_nome)
        case 'esci':
            print("sto chiudendo il programma")
            esci = True
        case _:
            print("hai inserito un comando sbagliato, riprova")
    
    if not esci:
        comando = input("inserire comando >> ")