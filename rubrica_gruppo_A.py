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

#importazione delle funzioni:
from funzioni import *


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

    
