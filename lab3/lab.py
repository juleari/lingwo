import math, string

TEXT_FILE_NAME = 'pride.txt'
LAMBDA = 0.5

def ln(x):
    return math.log(x, 2)

class WordCount(dict):
    def __missing__(self, key):
        return 0

class Ngramm(object):
    def __init__(self, word, count, N, B):
        self.word  = word
        self.count = count
        self.prob  = (count + LAMBDA) / (N + B * LAMBDA) 

class Text(object):

    def splitWords(self):
        
        return  string.join(string.join(string.join(string.join(
                string.join(string.join(string.join(string.join(
                string.join(string.join(string.join(string.join(
                string.join(string.join(string.join(string.join(
                self.text.lower().split(',')).split('"')).split(':'))
               .split(';')).split('?')).split('!')).split(' - '))
               .split('- ')).split(' -')).split('*')).split('+')).split('('))
               .split(')')).split('\\')).split('\/')).split('.')).split()

    def countWords(self):
        
        words  = WordCount()
        
        for i in range(self.length):
            words[ self.arr[i] ] += 1

        return words
            
    def countCoups(self):

        coups = WordCount()
        
        for i in range(self.length - 1):
            coups[self.arr[i] + ' ' + self.arr[i+1]] += 1

        return coups

    def probAndPp(self, number):

        N     = self.length
        LnSum = 0

        if number == 1:
            
            B = len(self.words)

            for i in range(self.length):

                word = self.arr[i]
                
                self.uni.append( Ngramm(word, self.words[ word ], N, B) )

            for i in self.uni:
                print i.word, i.count, i.prob
                LnSum  += ln(i.prob)

        if number == 2:

            B = len(self.coups)

            for i in range(self.length - 1):

                word = self.arr[i]
                bigramm = word + ' ' + self.arr[i + 1]

                self.bi.append( Ngramm(bigramm, self.coups[ bigramm ], self.words[ word ], B) )

            for i in self.bi:
                print i.word, i.count, i.prob
                LnSum  += ln(i.prob)

        print LnSum

        return 2**(-LnSum/N)


    def __init__(self, text, proc):
        
        self.text  = text
        self.arr   = self.splitWords()
        self.length= int(len(self.arr) * proc)
        self.words = self.countWords()
        self.coups = self.countCoups()
        self.uni   = []
        self.bi    = []
        self.PPuni = self.probAndPp(1)
        self.PPbi  = self.probAndPp(2)

t = Text( open(TEXT_FILE_NAME).read(), 0.8)
print t.PPuni, t.PPbi, t.length, len(t.arr), len(t.words), len(t.coups), t.words['quite']