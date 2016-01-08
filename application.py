#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, Response
import json
import freeling
from settings import *

app = Flask(__name__, static_url_path='/static')
freeling.util_init_locale("default");

# Create options set for maco analyzer. Default values are Ok, except for data files.
op = freeling.maco_options(LANG)
op.set_active_modules(0,1,1,1,1,1,1,1,1,1,1)
op.set_data_files("",
        DATA + LANG + "/locucions.dat", 
        DATA + LANG + "/quantities.dat", 
        DATA + LANG + "/afixos.dat", 
        DATA + LANG + "/probabilitats.dat", 
        DATA + LANG + "/dicc.src", 
        DATA + LANG + "/np.dat",
        DATA + "common/punct.dat",
        DATA + LANG + "/corrector/corrector.dat")

# create analyzers
tk = freeling.tokenizer(DATA + LANG + "/tokenizer.dat");
sp = freeling.splitter(DATA + LANG + "/splitter.dat");
mf = freeling.maco(op);
 
def decode_tag(tag):
    """
       Función para decodificar y extender las etiquetas
       generadas por Freeling en codificación EAGLES
    """
    categoria = tag[0]
    decoded = "Esta palabra pertenece a la categoría {} ".format(EAGLES_DICT[categoria]['Categoria'])

    atributos = tag[1:] if len(tag) > 1 else []
    aux = ''
    decoded += "y presenta los siguientes atributos: "
    for idx, atributo in enumerate(atributos):
        if categoria == 'F':
           break
        if categoria == 'N' and idx == 3:
           aux += atributo
           continue
        if categoria == 'N' and idx == 4:
           aux += atributo
           atributo = aux
        if categoria == 'N' and idx >= 3:
           idx -= 1 
        nombre_atributo = EAGLES_DICT[categoria]['Atributos'][idx]['atr']
        if atributo == '0' or atributo == '00':
           valor = 'Indefinido'
        else:
           valor = EAGLES_DICT[categoria]['Atributos'][idx]['values'][atributo]
        decoded += "{}: {}, ".format(nombre_atributo, valor)
    return decoded


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """
      Función para analizar morfológicamente
      los palabras de un texto en español
    """
    columns = [
            { 'title': "Palabra" },
            { 'title': "Lema" },
            { 'title': "Etiqueta" },
            { 'title': "Etiqueta extendida" }
    ]
    text = request.json["text"]
    if text[-1] not in PUNCTUATION: 
        text = text + "."
    tokens = tk.tokenize(text)
    sentences = sp.split(tokens, 0)
    sentences = mf.analyze(sentences)

    output = []
    for sentence in sentences:
        words = sentence.get_words()
        for word in words:
            output.append([word.get_form(), word.get_lemma(), word.get_tag(), decode_tag(word.get_tag())])
    
    return Response(json.dumps(dict(rows=output, columns=columns)), mimetype="application/json")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
