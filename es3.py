#Esercizio 3
# Crea un sistema che permetta di valorizzare una lista di 5 numeri per due volte, 
# dopodiché somma ogni posizione con la corrispettiva dell'altra aggregazione e stampa i risultati, 
# alla fine chiedi se si vuole ripete.
# Richiede: L'uso di due oggetti, ognuno deve contenere una delle due aggregazioni 
# da confrontare il confronto deve avvenire in una funzione polimorfica


class Aggregazione():
    def __init__(self):
        self._lista = []

    def add_elemento(self):
        while len(self._lista)<5:
            num = input("Inserisci un numero: ")
            if num.isdigit():
                num = float(num)
                self._lista.append(num)
            else:
                print("Devi inserire un numero.")
    
    def get_lista(self):
        return self._lista
    
    def get_numero(self, p):
        if p<len(self._lista) and p>=0:
            return self._lista[p]
        else:
            print("Posizione non valida.")
            
    def clear(self):
        self._lista.clear()

class Agg1(Aggregazione):
    def __init__(self):
        super().__init__()
        
class Agg2(Aggregazione):
    def __init__(self):
        super().__init__()


def somma(classe_1: Aggregazione, classe_2: Aggregazione):
    print("Ecco la somma dei corrispettivi.")
    if len(classe_1.get_lista()) == len(classe_2.get_lista()):
        for i in range(len(classe_1.get_lista())):
            print(classe_1.get_numero(i) + classe_2.get_numero(i))
    else:
        print("Le due liste non hanno la stessa lunghezza.")
    

agg1 = Agg1()
agg2 = Agg2()
    
while True:
    print("\nScegli l'operazione")
    if len(agg1.get_lista())<5: print("Riempi lista 1 -> 1")
    if len(agg2.get_lista())<5: print("Riempi lista 2 -> 2")
    print("Visualizza somma dei corrispettivi -> 3")
    print("Cancella lista 1 -> 4")
    print("Cancella lista 2 -> 5")
    print("Esci -> 6")
    scelta = input("Scelta: ")
    
    if scelta == "1" and len(agg1.get_lista())<5:
         agg1.add_elemento()
    elif scelta == "2" and len(agg2.get_lista())<5:
        agg2.add_elemento()
    elif scelta == "3":
        somma(agg1, agg2)
    elif scelta == "4":
        agg1.clear()
    elif scelta == "5":
        agg2.clear()
    elif scelta == "6":
        break
    else:
        print("Scelta non valida.")