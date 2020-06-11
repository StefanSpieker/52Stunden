import requests

url = "https://api.agify.io/"

print("Bitte gib deinen Namen ein: ")
name = input()

myResponse = requests.get(url + "?name=" + name)

# Wenn alles OK ist
if myResponse.ok:
    print("Dein geschätztes Alter ist:", myResponse.json()["age"])

else:
    # Falls es nicht OK ist, gebe den Fehlercode aus
    myResponse.raise_for_status()