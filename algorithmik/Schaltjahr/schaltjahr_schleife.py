def jahreszahl_einlesen():
    eingabe = input()
    jahr = int(eingabe)
    # Berechnung mit dem Wert jahr
    if jahr < 0:
        print("Es sind Nur positive Jahreszahlen erlaubt")
        exit(1)
    return jahr

print("Bitte Start-Jahreszahl eingeben:")
start = jahreszahl_einlesen()
print("Bitte End-Jahreszahl eingeben:")
ende = jahreszahl_einlesen()

print("Es werden", ende-start, "Jahre berechnet")
# Dein Programmcode


schaltjahr = False
if jahr % 4 == 0:
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            schaltjahr = False
        else:
            # nicht durch 400 teilbar.
            schaltjahr = True
    else:
        # nicht durch 100 teilbar.
        schaltjahr = True
else:
    # nicht durch 4 teilbar.
    schaltjahr = False

if schaltjahr:
    print("Es ist ein Schaltjahr!")
else:
    print("Kein Schaltjahr!")
