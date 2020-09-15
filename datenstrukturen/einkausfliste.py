# Dies ist meine Einkaufsliste
einkaufsliste = ["Äpfel", "Bananen", "Brot", "Käse", "Marmelade", "Butter"]

print("Ich habe", len(einkaufsliste), "Dinge einzukaufen.")

print("Diese Dinge sind: ", end="")
for ding in einkaufsliste:
    print(ding, end=", ")  # das end=", " führt zu einem Komma nach jedem Element ohne Zeilenumbruch

print()  # neue Zeile ausgeben

einkaufsliste.append("Reis") 

einkaufsliste.sort() # sortiert die einkausliste alphabetisch

print("Ich habe", len(einkaufsliste), "Dinge einzukaufen.")

print("Diese Dinge sind: ", end="")
for ding in einkaufsliste:
    print(ding, end=", ")
