# Dies ist meine Einkaufsliste
einkaufsliste = ["Äpfel", "Bananen", "Brot", "Käse", "Marmelade", "Butter"]

print("Ich habe", len(einkaufsliste), "Dinge einzukaufen.")

print("Diese Dinge sind: ", end="")
for ding in einkaufsliste:
    print(ding, end=", ")

print()
einkaufsliste.append("Reis")
einkaufsliste.sort()

print("Diese Dinge sind: ", end="")
for ding in einkaufsliste:
    print(ding, end=", ")
