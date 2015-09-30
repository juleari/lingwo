# -*- coding: utf-8 -*-

import json, codecs, math

TEXT_BASE = "doc"
RUBRICS   = ["culture", "politics"]

class WordCount(dict):
    def __missing__(self, key):
        return 0

def Train():

    textMorf = {}
    text     = {}
    idfs     = {}
    coss     = {}

    for r in RUBRICS:

        textMorf[r] = []

        for i in range(10):

            fp = codecs.open( r + "/morf/doc" + str(i+1), "r", "utf-8" )
            textMorf[r].append( json.load(fp) )
            fp.close()

    for r in RUBRICS:

        text[r] = WordCount()
        
        for d in textMorf[r]:
            
            for word in d:

                try:
                    fL           = word[u"analysis"][0][u"lex"]
                    text[r][fL] += 1
                except:
                    fL           = word[u"text"]
                    text[r][fL] += 1

        fp = codecs.open( r + "/morf/doc", "w", "utf-8" )
        for v in text[r]:
            fp.write(v + ": " + str(text[r][v]) + "\n")
        fp.close()

    words = {}
    tcount= {}

    for r in RUBRICS:

        words[r]  = WordCount()
        tcount[r] = 0.0
        
        for v in text[r]:
            tcount[r] += text[r][v] + 1

        for t in text[r]:
            words[r][t] = float(text[r][t] + 1) / tcount[r]

    for r in RUBRICS:
        fp = codecs.open( r + "/morf/train", "w", "utf-8" )
        for w in words[r]:
            fp.write(w + ": " + str(words[r][w]) + "\n")
        fp.close()

    return words

words = Train()

def Classify(textName, words):

    N       = 20
    p       = 0.5
    weights = {}
    text    = WordCount()

    fp       = codecs.open( textName, "r", "utf-8" )
    textMorf = json.load(fp)
    fp.close()

    for t in textMorf:
        try:
            fL        = t[u"analysis"][0][u"lex"]
            text[fL] += 1
        except:
            fL        = t[u"text"]
            text[fL] += 1

    for r in RUBRICS:

        weights[r] = math.log(p, 10)

        for t in text:
            print words[r][t]
            if words[r][t]:
                weights[r] += math.log(words[r][t], 10)

    print weights

Classify("culture/morf/short1", words)