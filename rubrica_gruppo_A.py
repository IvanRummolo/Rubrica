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

def visualizza_lista(lista):
    for nome in lista:
        print(nome)

def aggiungi_nome(lista, nome):
    lista.append(nome)
    return lista

def elimina_nome(nomi, nome):
    nuova_lista = []
    for a in nomi:
        if a != nome:
            nuova_lista.append(nome)
    return nuova_lista

def modifica_nome(lista, vecchio_nome, nuovo_nome):
    for i in range(len(lista)):
        if lista[i] == vecchio_nome:
            lista[i] = nuovo_nome
    return lista 


#Avviamo il programma
print("Benvenuto nel programma rubrica:")
print("comandi disponibili: lista, aggiungi, elimina, modifica, esci")

comando = input("inserire comando >> ")
esci = False
lista = []
while not esci:

    match comando:
        case 'lista':
            visualizza_lista(lista) 
        case 'aggiungi':
            nome = input("Inserisci nome da aggiungere >> ")
            aggiungi_nome(lista, nome)
        case 'elimina':
            nome = input("Inserisci nome da eliminare >> ")
            elimina_nome(lista, nome)
        case 'modifica':
            nome = input("Inserisci nome da modificare >> ")
            nuovo_nome = input("Inserisci il nuovo nome >> ")
            modifica_nome(lista, nome, nuovo_nome)
        case 'esci':
            print("sto chiudendo il programma")
            esci = True
        case _:
            print("hai inserito un comando sbagliato, riprova")
    
    if not esci:
        comando = input("inserire comando >> ")

    
