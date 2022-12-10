from flask import Flask, jsonify, request
import requests

__version__ = '0.0.1'
app = Flask(__name__)

URL_BASE = 'https://api.chucknorris.io/jokes'

@app.get('/_about')
def version():
  return __version__

@app.route('/api/jokes/random', methods=["GET"])
def get_jokes_random():
    response = requests.get(URL_BASE + '/random')
    dados = response.json()
    if response:
        return jsonify(dados, {"status": 200})
    else:
        return jsonify({'mensagem': 'Erro ao consumir a API', "status": 404})
  
if __name__ == '__main__':
    app.run()