# Esercizio 4
# Crea un sistema che permetta di ordinare da varie classi 
# figlie di autofficine, ogni autofficina deve avere disponibile una 
# funzione per riparare un tipo specifico di Veicolo.                                                
# Richiede: Classe autofficine (min 2 figli), 
# Classe Veicolo (min 2 figli ), 
# Classe App_Riparazioni (gestore)

from abc import ABC, abstractmethod

class Autofficine(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.veicoli = []
    
    @abstractmethod
    def riparare(self):
        pass
    

class AutoFiat(Autofficine):
    def __init__(self, nome):
        super().__init__(nome)
        
    def riparare(self):
        print(f'{self.nome} riparando auto fiat...')
        
class AutoFord(Autofficine):
    def __init__(self, nome):
        super().__init__(nome)
        
    def riparare(self):
        print(f'{self.nome} riparando auto ford...')
        
        
class Veicoli(ABC):
    def __init__(self, marca, modello, anno_immatricolazione):
        self.marca = marca
        self.modello = modello
        self.anno_immatricolazione = anno_immatricolazione
        
    
    @abstractmethod
    def ordina_veicolo(self):
        pass
    

class VeicoloFiat(Veicoli, AutoFiat):
    def __init__(self, modello, anno_immatricolazione, marca='Fiat', nome='Venditore Fiat'):
        Veicoli.__init__(self, marca, modello, anno_immatricolazione)
        AutoFiat.__init__(self, nome)
        
    def ordina_veicolo(self):
        print(f'Ordinando il veicolo {self.modello} di {self.marca} anno {self.anno_immatricolazione}...')

class VeicoloFord(Veicoli, AutoFord):
    def __init__(self, modello, anno_immatricolazione, marca='Ford', nome='Venditore Ford'):
        Veicoli.__init__(self, marca, modello, anno_immatricolazione)
        AutoFord.__init__(self, nome)
        
    def ordina_veicolo(self):
        print(f'Ordinando il veicolo {self.modello} di {self.marca} anno {self.anno_immatricolazione}...')





class App_Riparazioni():
    def ripara_auto(self, auto):
        auto.riparare()
    
    
panda = VeicoloFiat('Panda', 1992, 'Vendo Fiat')
panda.ordina_veicolo()

fiesta = VeicoloFord('fiesta', 1953, 'Vendo Ford')
fiesta.ordina_veicolo()

app = App_Riparazioni()

app.ripara_auto(panda)
app.ripara_auto(fiesta)