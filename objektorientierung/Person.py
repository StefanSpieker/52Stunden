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

    def ausgeben(self):
        print(self.vorname + " " + self.name + " ist " +
              str(self.alter()) + " Jahre alt und " + str(self.groesse) + " cm gross.")


max = Person('Mustermann', 'Max', datetime.datetime(year=2006, month=10, day=23), 169)
tim = Person('Teufel', 'Tim', datetime.datetime(year=2007, month=1, day=13), 157)
max.ausgeben()
tim.ausgeben()
print("Heute ist: " + str(datetime.date.today()))
