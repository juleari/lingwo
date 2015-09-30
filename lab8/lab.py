# -*- coding: utf-8 -*-

import json, codecs, math

FILES = {"kosa": 3, "kluch": 7, "rak": 2, "rock": 2, "ruchka": 3}
WORDS = {"kosa": u"коса", "kluch": u"ключ", "rak": u"рак", "rock": u"рок", "ruchka": u"ручка"}

class WordCount(dict):
    def __missing__(self, key):
        return 0

def cos(v1, v2):
    return scal(v1, v2) / (module(v1) * module(v2))

def scal(v1, v2):
    p = 0
    
    for w in v1:
        p += v1[w] * v2[w]

    return p

def module(v):
    m = 0

    for w in v:
        m += v[w]**2

    return math.sqrt(m)

def loadJSON():

    textMorf = {}
    vectors  = {}
    words    = {}
    idfs     = {}
    weights  = {}
    coss     = {}

    for f in FILES:

        textMorf[f] = {}
        
        fp = codecs.open( f + "/morf/sentence", "r", "utf-8" )
        textMorf[f]["sentence"] = json.load(fp)
        fp.close()

        for i in range(FILES[f]):

            fp = codecs.open( f + "/morf/v" + str(i + 1), "r", "utf-8" )
            textMorf[f]["v" + str(i + 1)] = json.load(fp)
            fp.close()

    for f in FILES:

        vectors[f] = {}
        for d in textMorf[f]:

            vectors[f][d] = WordCount()
            for word in textMorf[f][d]:

                try:
                    fL = word[u"analysis"][0][u"lex"]
                    vectors[f][d][fL] += 1
                except:
                    fL                 = word[u"text"]
                    vectors[f][d][fL] += 1

        for d in textMorf[f]:
            fp = codecs.open( f + "/morf/d" + d, "w", "utf-8" )
            for v in vectors[f][d]:
                fp.write(v + ": " + str(vectors[f][d][v]) + "\n")
            fp.close()

    for f in FILES:

        N          = FILES[f]
        words[f]   = WordCount()
        weights[f] = {}
        idfs[f]    = WordCount()
        coss[f]    = {}

        for v in vectors[f]:

            if v != "sentence":
                for w in vectors[f][v]:
                    if w != WORDS[f]:
                        words[f][w] += 1

        for w in words[f]:
            idfs[f][w] = math.log(float(N) / words[f][w], 10)

        for v in vectors[f]:
            weights[f][v] = WordCount()
            for w in vectors[f][v]:
                weights[f][v][w] = idfs[f][w] * vectors[f][v][w]

        for v in vectors[f]:
            if v != "sentence":
                coss[f][v] = cos(vectors[f]["sentence"], weights[f][v])

        fp = codecs.open( f + "cosinuses", "w", "utf-8" )
        for v in sorted(coss[f], key = coss[f].__getitem__):
            fp.write(v + ": " + str(coss[f][v]) + "\n")
        fp.close()

loadJSON()