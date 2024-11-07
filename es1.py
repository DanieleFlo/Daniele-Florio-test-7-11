#Esercizio 1
#Crea un sistema ripetibile che si occupi di dividere su tre 
# possibili liste i tipi basilari di dato che riceve in entrata. 
# Deve poter stampare una lista singola o tutte.   
# Richiede: un oggetto come esecutore

class DivisoreDati():
    def __init__(self):
        self._numeri = []
        self._boleani = []
        self._stringhe = []
        
    
    def aggigungi_dato(self, dato):
        if isinstance(dato, bool): # Controllo prima sui buleani
            self._numeri.append(dato)
        elif isinstance(dato, int):
            self._boleani.append(dato)
        elif isinstance(dato, str):
            self._stringhe.append(dato)
        else:
            print(f'Tipo di dato non supportato: {type(dato).__name__}')
            
    def get_numeri(self):
        print(f'Stampo boleani:')
        for n in self._numeri:
            print(n)
            
    def get_boleani(self):
        print(f'Stampo numeri:')
        for n in self._boleani:
            print(n)
            
    def get_stringhe(self):
        print(f'Stampo stringhe')
        for n in self._stringhe:
            print(n)
            
    def get_all(self):
        self.get_numeri() 
        self.get_boleani()
        self.get_stringhe()
        
        
esempio = DivisoreDati()

esempio.aggigungi_dato(10)
esempio.aggigungi_dato(11)
esempio.aggigungi_dato(9)
esempio.aggigungi_dato('a')
esempio.aggigungi_dato('ciao')
esempio.aggigungi_dato(True)
esempio.aggigungi_dato(False)

esempio.get_all()