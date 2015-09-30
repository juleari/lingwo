# -*- coding: utf-8 -*-

import json, codecs, math

TEXT_FILE_NAMES = ["cor2013", "corhavi", "end", "euro2013", "euro2015", "fccashley", "fin2013", "fra2011", "future2010", "gpfinal", "gulin", "lipnickaya", "medalewinners", "ogplush", "pairs", "pass", "plush", "season", "world2012", "world2014"]
QUERY_VECTOR    = {u"парный": 1, u"катание": 1}

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
    idfs     = {}
    weights  = {}
    coss     = {}

    for fn in TEXT_FILE_NAMES:

        fp = codecs.open( "news/morf/" + fn, "r", "utf-8" )
        textMorf[fn] = json.load(fp)
        fp.close()

    for fn in TEXT_FILE_NAMES:

        vectors[fn] = WordCount()
        for word in textMorf[fn]:

            try:
                fL               = word[u"analysis"][0][u"lex"]
                vectors[fn][fL] += 1
            except:
                fL               = word[u"text"]
                vectors[fn][fL] += 1

        fp = codecs.open( "news/morf/d" + fn, "w", "utf-8" )
        for v in vectors[fn]:
            fp.write(v + ": " + str(vectors[fn][v]) + "\n")
        fp.close()

    N     = len(TEXT_FILE_NAMES)
    words = WordCount()
    for v in vectors:
        for w in vectors[v]:
            words[w] += 1

    for w in words:
        idfs[w] = math.log(float(N) / words[w], 10)

    for v in vectors:
        weights[v] = WordCount()
        for w in vectors[v]:
            weights[v][w] = idfs[w] * vectors[v][w]

        fp = codecs.open( "news/morf/w" + v, "w", "utf-8" )
        for w in vectors[v]:
            fp.write(w + ": " + str(weights[v][w]) + ": " + str(words[w]) + "\n")
        fp.close()

    for v in vectors:
        coss[v] = cos(QUERY_VECTOR, weights[v])

    fp = codecs.open( "cosinuses", "w", "utf-8" )
    for v in sorted(vectors, key = coss.__getitem__):
        fp.write(v + ": " + str(coss[v]) + "\n")
    fp.close()

loadJSON()