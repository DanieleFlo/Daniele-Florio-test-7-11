#Esercizio 2
# Crea una sistema ripetibile che dopo aver preso in input X parole 
# e/o numeri e li aggiunga a una collezione, 
# si deve ripetere tante volte quante l'utente richiede 
# e poi stampare tutti gli elementi nella lista che non si ripetono. 
# Richiede: Che ogni valore o aggregazione dell'oggetto siano incapsulati


class ElementiUnici():
    def __init__(self):
        self._elementi = []
        
    def start(self):
        while True:
            nav = input("Vuoi aggiungere un altro elemento 1, stampare quelli unici 2, uscire 3: ")
            if nav == '1':
                elemento = input('Dammi un elemento stringa o numero: ')
                if elemento.isdigit():
                    self.__aggiungi_elemento(int(elemento))
                else:
                    self.__aggiungi_elemento(elemento)
            elif nav == '2':
                self.stampa_unici()
            elif nav == '3':
                break
            else:
                print("Scelta non valida.")
    
    def __aggiungi_elemento(self, elemento):
        self._elementi.append(elemento)
    
    def stampa_unici(self):
        for elemento in set(self._elementi):
            print(elemento)

esempio = ElementiUnici()
esempio.start()
    