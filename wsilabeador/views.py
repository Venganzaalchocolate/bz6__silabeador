from wsilabeador import app
from pipapilapibra.pilengua import *
from flask import jsonify

@app.route('/<frase>')

def index(frase):
    diccionario={}
    diccionario['Response'] = True
    diccionario['result'] = {'original': frase, 'traducido': pilengua(frase)}
    
    
    return jsonify(diccionario)

@app.route('/decodifica/<frase>')
    diccionario={}
    diccionario['Response'] = True
    diccionario['result'] = {'original': frase, 'traducido': inversa(frase)}
    
    return jsonify(diccionario)