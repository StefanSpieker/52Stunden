from flask import Flask, json

verzeichnis = [{"stichwort": "Suchmaschinen", "text": "Woher beziehen wir ..."},
               {"stichwort": "Wikis", "text": "Das Internet ..."}]

api = Flask(__name__)


@api.route('/verzeichnis', methods=['GET'])
def get_companies():
    return json.dumps(verzeichnis)


if __name__ == '__main__':
    api.run()