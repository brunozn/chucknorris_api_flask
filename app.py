from flask import Flask, jsonify, request
import requests

__version__ = '0.0.1'

app = Flask(__name__)

@app.get('/_about')
def version():
  return __version__
  
if __name__ == '__main__':
    app.run()