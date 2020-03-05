# Neuer Bauplan für eine Person:
# Beim Erstellen eines Objekt der Klasse Person
# werden die Instanzvariablen direkt definiert.
import datetime


class Person:
    def __init__(self, name, vorname, geb_datum, groesse):
        self.name = name
        self.vorname = vorname
        self.geb_datum = geb_datum
        self.groesse = groesse

    def alter(self):
        heute = datetime.date.today()
        jahre = heute.year - self.geb_datum.year
        if heute.month < self.geb_datum.month or \
                (heute.month == self.geb_datum.month and heute.day < self.geb_datum.day):
            jahre -= 1
        return jahre

    def __str__(self):
        ret = self.vorname + " " + self.name + " ist "
        ret += str(self.alter()) + " Jahre alt und " + str(self.groesse) + " cm gross"
        return ret


max = Person('Mustermann', 'Max', datetime.datetime(year=2006, month=10, day=23), 169)
tim = Person('Teufel', 'Tim', datetime.datetime(year=2007, month=1, day=13), 157)
print(max)
print(tim)
print("Heute ist: " + str(datetime.date.today()))


class Schueler(Person):
    def __init__(self, name, vorname, geb_datum, groesse, klasse):
        Person.__init__(self, name, vorname, geb_datum, groesse)
        self.klasse = klasse

    def __str__(self):
        ret = Person.__str__(self) + " und besucht die Klasse " + self.klasse
        return ret


eva = Schueler('Engel', 'Eva', 
               datetime.datetime(year=2005, month=2, day=4), 
               152, '9b')
print(eva)
