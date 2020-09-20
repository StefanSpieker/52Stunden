# Dies ist mein Wörterbuch
woerterbuch = {"house": "Haus", "cat": "Katze", "black": "schwarz"}

# das gesamte Woerterbuch lässt sich so ausgeben
print(woerterbuch)

print("Die Übersetzung von house ist: ", woerterbuch["house"])

# prüfen ob flower im Wörterbuch fehlt
if "flower" not in woerterbuch:
    # flower hinzufügen
    woerterbuch["flower"] = "Blume"

print("Die Übersetzung von flower ist: ", woerterbuch["flower"])
