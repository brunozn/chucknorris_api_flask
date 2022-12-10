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


@app.route('/api/jokes/category/<category>', methods=["GET"])
def get_jokes_per_category(category):
  url = URL_BASE + '/random?category=' + category
  response = requests.get(url)
  if response.status_code == 404:
    return jsonify({'mensagem': 'Categoria não existe', "status": 404})
  data = response.json()
  return jsonify(data)


@app.route('/api/jokes/filter', methods=["GET"])
def get_jokes_search():
  search = request.args['search']
  limit = request.args.get('limit', default=5, type=int)
  params = {'query': search}
  url = URL_BASE + '/search'
  response = requests.get(url, params)
  data = response.json()
  if data['total'] == 0:
    return jsonify({'mensagem': 'Não existe nenhuma piada com o filtro utilizado', "status": 404})
  return jsonify({'status': 200, 'limit': limit}, data['result'][:limit])
  
  
if __name__ == '__main__':
    app.run()