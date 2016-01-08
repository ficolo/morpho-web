#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, Response
import json
import freeling


app = Flask(__name__, static_url_path='/static')

GENERO = {'atr': 'Género', 'values': {'M': 'Masculino', 'F': 'Femenino', 'C': 'Común', 'N': 'Neutro'}}
NUMERO = {'atr': 'Número', 'values': {'S': 'Singular', 'P': 'Plural', 'N': 'Invariable'}}
GRADO = {'atr': 'Grado', 'values': {'A': 'Aumentativo', 'D': 'Diminutivo', 'C': 'Comparativo', 'S': 'Superlativo'}}
PERSONA =  {'atr': 'Persona', 'values': {'1': 'Primera', '2': 'Segunda', '3': 'Tercera'}}
POSEEDOR =     {'atr': 'Poseedor', 'values': {'S': 'Singular', 'P': 'Plural'}}

EAGLES_DICT = {
    'A': {'Categoria': 'Adjetivo', 'Atributos': [
    {'atr': 'Tipo', 'values': {'Q': 'Calificativo', 'O': 'Ordinal'}},
    GRADO,
    GENERO,
    NUMERO,
    {'atr': 'Función', 'values': {'0': '-', 'P': 'Participativo'}}
    ]},
    'R': {'Categoria': 'Adverbio', 'Atributos': [
    {'atr': 'Tipo', 'values': {'G': 'General', 'N': 'Negativo'}}
    ]},
    'D': {'Categoria': 'Determinante', 'Atributos': [
    {'atr': 'Tipo', 'values': {'D': 'Demostrativo', 'P': 'Posesivo', 'T': 'Interrogativo', 'E': 'Exclamativo', 'I': 'Indefinido', 'A': 'Artículo'}},
    PERSONA,
    GENERO,
    NUMERO,
    POSEEDOR
    ]},
    'N': {'Categoria': 'Nombre', 'Atributos': [
    {'atr': 'Tipo', 'values': {'C': 'Común', 'P': 'Propio'}},
    GENERO,
    NUMERO,
    {'atr': 'Clasificación semántica', 'values': {'SP': 'Persona', 'G0': 'Lugar', 'O0': 'Organización', 'V0': 'Otros'}},
    GRADO
    ]},
    'V': {'Categoria': 'Verbo', 'Atributos': [
    {'atr': 'Tipo', 'values': {'M': 'Principal', 'A': 'Auxiliar', 'S': 'Semiauxiliar'}},
    {'atr': 'Modo', 'values': {'I': 'Indicativo', 'S': 'Subjuntivo', 'M': 'Imperativo', 'N': 'Infinitivo', 'G': 'Gerundio', 'P': 'Participio'}},
    {'atr': 'Tiempo', 'values': {'P': 'Presente', 'I': 'Imperfecto', 'F': 'Futuro', 'S': 'Pasado', 'C': 'Condicional', '0': '-'}},
    PERSONA,
    NUMERO,
    GENERO
    ]},
    'P': {'Categoria': 'Pronombre', 'Atributos': [
    {'atr': 'Tipo', 'values': {'P': 'Personal', 'D': 'Demostrativo', 'X': 'Posesivo',
    'I': 'Indefinido', 'T': 'Interrogativo', 'R': 'Relativo', 'E': 'Exclamativo'}},
    PERSONA,
    GENERO,
    NUMERO,
    {'atr': 'Caso', 'values': {'N': 'Nominativo', 'A': 'Acusativo', 'D': 'Dativo', 'O': 'Oblicuo'}},
    POSEEDOR,
    {'atr': 'Politeness', 'values': {'P': 'Polite'}}
    ]},
    'C': {'Categoria': 'Conjunción', 'Atributos': [
    {'atr': 'Tipo', 'values': {'C': 'Coordinada', 'S': 'Subordinada'}}
    ]},
    'I': {'Categoria': 'Interjección', 'Atributos': []},
    'S': {'Categoria': 'Adposición', 'Atributos': [
    {'atr': 'Tipo', 'values': {'P': 'Preposición'}},
    {'atr': 'Forma', 'values': {'S': 'Simple', 'C': 'Contraìda'}},
    GENERO,
    NUMERO
    ]},
    'F': {'Categoria': 'Puntuación', 'Atributos': []},
    'Z': {'Categoria': 'Numerables', 'Atributos': [
    {'atr': 'Tipo', 'values': {'d': 'Paritivo', 'm': 'Moneda', 'p': 'Porcentaje', 'u': 'Unidad'}}
    ]},
    'W': {'Categoria': 'Fechas y horas', 'Atributos': []}
}

PUNCTUATION = u""".,;:!? """

## Modify this line to be your FreeLing installation directory
FREELINGDIR = "/usr/local/"
DATA = FREELINGDIR + "share/freeling/"
LANG = "es"
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
    """"""
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
