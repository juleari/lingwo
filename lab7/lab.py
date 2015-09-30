# -*- coding: utf-8 -*-

import json, codecs, math, string

class WordCount(dict):
    def __missing__(self, key):
        return 0

def loadJSON():

    fp       = codecs.open( "morf", "r", "utf-8" )
    text     = fp.read()
    textJSON = string.join(text.split("]\n["), ",")
    pairs    = WordCount()

    JSON     = json.loads(textJSON)

    for i in range(len(JSON) - 1):

        try:
            if  JSON[i][u"analysis"][0][u"gr"][0] == "A" and \
              JSON[i+1][u"analysis"][0][u"gr"][0] == "S" and \
              JSON[i+1][u"analysis"][0][u"gr"][1] == ",":
                pair = JSON[i][u"analysis"][0][u"lex"] + " " + JSON[i+1][u"analysis"][0][u"lex"]
                pairs[ pair ] += 1
        except:
            e = 0

    fp = codecs.open( "pairsfreq", "w", "utf-8" )
    
    for p in sorted(pairs, key = pairs.__getitem__):
        fp.write(p + ": " + str(pairs[p]) + "\n")
    fp.close()

    I    = WordCount()
    text = WordCount()

    for word in JSON:

        try:
            fL        = word[u"analysis"][0][u"lex"]
            text[fL] += 1
        except:
            fL        = word[u"text"]
            text[fL] += 1

    N = len(JSON)

    for p in pairs:

        pair = p.split()

        I[p] = math.log((float(N)/ pairs[p]) / text[pair[0]] / (float(text[pair[0]] * text[pair[1]]) / N**2), 2)

    fp = codecs.open( "pairsweight", "w", "utf-8" )
    for p in sorted(I, key = I.__getitem__):
        fp.write(p + ": " + str(I[p]) + "\n")
    fp.close()


#    for r in RUBRICS:

#        text[r] = WordCount()
        
#        for d in textMorf[r]:
            
#            for word in d:

#                try:
#                    fL           = word[u"analysis"][0][u"lex"]
#                    text[r][fL] += 1
#                except:
#                    fL           = word[u"text"]
#                    text[r][fL] += 1

#        fp = codecs.open( r + "/morf/doc", "w", "utf-8" )
#        for v in text[r]:
#            fp.write(v + ": " + str(text[r][v]) + "\n")
#        fp.close()

#    words = {}
#    tcount= {}

#    for r in RUBRICS:

#        words[r]  = WordCount()
#        tcount[r] = 0.0
        
#        for v in text[r]:
#            tcount[r] += text[r][v] + 1

#        for t in text[r]:
#            words[r][t] = float(text[r][t] + 1) / tcount[r]

#    for r in RUBRICS:
#        fp = codecs.open( r + "/morf/train", "w", "utf-8" )
#        for w in words[r]:
#            fp.write(w + ": " + str(words[r][w]) + "\n")
#        fp.close()

#    return words

loadJSON()