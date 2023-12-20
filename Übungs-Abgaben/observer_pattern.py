# Author @Tom ; @Felix ; @Gina
# Version 1.0
# Date 19.12.2023

"""
inspired by:
https://github.com/faif/python-patterns/blob/master/patterns/behavioral/observer.py
http://code.activestate.com/recipes/131499-observer-pattern/

*TL;DR
Maintains a list of dependents and notifies them of any state changes.

"""
from abc import abstractmethod
from contextlib import suppress
from typing import Generic, TypeVar


# define a generic observer type
T = TypeVar("T")
class Observer(Generic[T]):
    @abstractmethod
    def update(self, subject: T) -> None:...


# Klasse der Datentypen
class Subject:
    """
    CLASS Subject, 
    das auf Veränderung zu beobachtende Subject (später ein Datentyp)
    """
    def __init__(self) -> None:
        self._observers: list[Observer[Subject]] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        with suppress(ValueError):
            self._observers.remove(observer)

    # notifyer Methode, welche die Observer, welche das Subject beobachten auf die Änderung des Daten-Werts hinzuweisen und die Beobachtungssituation zu updaten
    def notify(self, modifier: Observer | None = None) -> None:         # Es werden keine Observer ausgeschlossen, Klausel redundant
        for observer in self._observers:                                # Für alle Observer der Liste, außer der, der außgeschlossen werden soll
            if modifier != observer:                                    # 
                observer.update(self)

    def clear_observers(self):
        while len(self._observers) != 0:
            self._observers.clear()

class Data(Subject):
    """
    Unter-Klasse der zu beobachtenden Daten Subjekten
    """
    def __init__(self, name: str = "") -> None:
        super().__init__()
        self.name = name
        self._data = 0
        self._type = ""

    #`Getter` Methode um den Wert des Data-Objekts auszugeben
    @property
    def data(self):
        return self._data
    
    #Setter-Methode um dem Data-Objekt auch Werte zuzuweisen
    @data.setter
    def data(self, value) -> None:    
        try:
            #Die Einmalige Überprüfung der Liste auf einen ReadonlyWatcher ist ausreichend, da bei Existenz weitere Aufrufe nicht zustande kommen können
            for j in range(1, len(self._observers)):
                if isinstance(self._observers[j], ReadonlyWatcher):
                    self._observers[j].update(self)

            #Die verschieden Möglichen Daten-Typen, Es werden bedingt das Werte und Daten-Typen gespeichert und die benachrichtungsmethode der Observer getrigert
            if(type(value) == int):
                self._data = value
                self._type = "INT"
                self.notify()  
            elif(type(value) == float):
                self._data = value
                self._type = "FLOAT"
                self.notify()  
            elif(type(value) == str):
                self._data = value 
                self._type = "STRING"
                self.notify()  
            else:
                value / 1 

        # Exeption, falls ein nicht gestatteter Datentyp übergeben wird
        except TypeError as e:
            print("Nicht gestatteter Datentyp: ")
            print(e)                  



class DataViewer(Observer[Data]):
    #Deklaration der ehem. abstrakten Update-Methode die ausgibt, zu welchem Wert und Typ sich ein Data-Subject geändert hat, das der Observer beobachtet
    def update(self, subject: Data) -> None:                        
        print(f"DataViewer: Subject {subject.name}, {subject._type} changed to '{subject.data}'")
    # Hier wäre denkbar gewesen, {subject.type} und das zugehörige If-Konklomerat durch einen String bearbeitung vom Type ... type(subject.data)... zu verweden


class ReadonlyWatcher(Observer[Data]):
    """
    Observer, der bei einer beobachteter Veränderung einen Error raised und so vrehindert, dass Subjecte verändert werden können.
    """
    #Update Methode, Kern der Klasse und der Aufgabe des Observers, der Veränderungen registriert
    def update(self, subject: Data) -> None:
        print("Sorry, du hast was geändert, das ist verboten!!!")
        raise ÄnderungenVerboten
    
# Die erstellte Exeption, ohne jede Bedeutung, Existens nur um der Existens willen
class ÄnderungenVerboten(Exception):
    pass

d = Data("myDataObj1")
view1 = DataViewer()
d.attach(view1)


# 1) Kommentieren und Dokumentieren Sie das hier gezeigt Observer pattern
# 2) Erweitern Sie den Code und die typehints, so dass Sie einem Data object auch ein float oder string anstatt eines int geben können. 
#    Werfen Sie einen Fehler, falls ein anderer Datentyp übergeben wird. Änderungen sollten den Datentyp angeben. 
#    Folgender Code sollte also fehlerfrei funktionieren und die in den Kommentaren gezeigten Outputs liefern:

d.data = 5.6        #should print: "DataViewer: Subject myDataObj1, FLOAT changed to 5.6"
d.data = 5          #should print: "DataViewer: Subject myDataObj1, INT changed to 5"
d.data = "hello"    #should print: "DataViewer: Subject myDataObj1, STRING changed to 'hello'"
#d.data = [1,2,3]

# 3) Schreiben Sie ein zweite Data-Observer Klasse namens "ReadonlyWatcher" der bei Änderungen auf Data einen Fehler wirft. Nachfolgender Code sollte also fehlerfrei funktionieren.

#d.attach(ReadonlyWatcher())
d.data = 7          #should raise error

# 4) Erweitern Sie die Subject Klasse um eine "clear_observers" Methode, die sofort alle attached observers entfernt. Nachfolgender Code sollte also fehlerfrei funktionieren.
d.clear_observers()
d.data = 10         #should work but not raise any errors nor print anything