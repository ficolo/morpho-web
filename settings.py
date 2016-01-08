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

FREELINGDIR = "/usr/local/"
DATA = FREELINGDIR + "share/freeling/"
LANG = "es"
