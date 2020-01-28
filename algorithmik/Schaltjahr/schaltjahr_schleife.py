def jahreszahl_einlesen():
    eingabe = input()
    jahr = int(eingabe)
    # Berechnung mit dem Wert jahr
    if jahr < 0:
        print("Es sind Nur positive Jahreszahlen erlaubt")
        exit(1)
    return jahr


def ist_schaltjahr(jahreszahl):
    schaltjahr = False
    if jahreszahl % 4 == 0:
        if jahreszahl % 100 == 0:
            if jahreszahl % 400 == 0:
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
    return schaltjahr


print("Bitte Start-Jahreszahl eingeben:")
start = jahreszahl_einlesen()
print("Bitte End-Jahreszahl eingeben:")
ende = jahreszahl_einlesen()

print("Es werden", ende - start, "Jahre berechnet")
# Dein Programmcode
jahr = start
print("Folgende Jahre sind Schaltjahre:")
while jahr <= ende:
    if (ist_schaltjahr(jahr)):
        print(jahr, end=', ')
    jahr = jahr + 1

