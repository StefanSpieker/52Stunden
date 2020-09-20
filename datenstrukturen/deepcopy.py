import copy

# Dies ist mein Wörterbuch mit Listen
woerterbuch = {"house": ["Haus", "beherbergen"], "cat": "Katze",
               "black": "schwarz", "flower": ["Blume", "blühen"]}

# das gesamte Woerterbuch lässt sich so ausgeben
print("Beim Start    :", woerterbuch)

w = woerterbuch.copy()  # kopiert das Dictionary
w2 = copy.deepcopy(woerterbuch) # machte eine tiefe Kopie
print("Eintrag ändern")
w["house"][0] = "FEHLER"  # ändert den Eintrag in der Liste

print("woerterbuch   :", woerterbuch)
print("Kopie w       :", w)
print("Tiefe Kopie w2:", w2)
