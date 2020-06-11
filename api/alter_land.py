import requests

url = "https://api.agify.io/"

print("Bitte gib deinen Namen ein: ")
name = input()
print("Aus welchem Land kommst du? (Gib den Ländercode ein, z.B. DE oder NL): ")
land = input()

myResponse = requests.get(url + "?name=" + name + "&country_id=" + land)

# Wenn alles OK ist
if myResponse.ok:
    print("Dein geschätztes Alter ist:", myResponse.json()["age"])

else:
    # Falls es nicht OK ist, gebe den Fehlercode aus
    myResponse.raise_for_status()