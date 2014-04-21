import modules
import pkgutil
import os
import re
import logging

def getWords():
    words = []
    for im, name, ispkg in pkgutil.iter_modules(modules.__path__):
        try:
            eval("words.extend(modules.%s.WORDS)" % name)
        except AttributeError:
            logging.warn("module %s n'a pas d'attribut WORDS" % name)

    return [word.lower() for word in words]

def g2p(words, outputf):
    dic = open('lmdict/%s.dic' % outputf, 'w')

    for word in words:
       stdin, stdout = os.popen2('phonetisaurus-g2p --model=lmdict/model.fst --input=%s' % word)
       phon = re.search('\t(?P<phon>\D+)\n', stdout.read()).group('phon')
       dic.write('%s %s\n' % (word, phon))
    dic.close()


def ngram(words, outputf):
    ngramf = open('lmdict/tempngram00.train', 'w')
    for word in words:
        ngramf.write('%s ' % word)
    ngramf.close()

    os.popen2('estimate-ngram -s FixKN -t lmdict/tempngram00.train -wl lmdict/%s.arpa' % outputf)

if __name__ == '__main__':
    words = getWords()
    logging.debug('got words %s' % words)
    g2p(words, 'test')
    ngram(words, 'test')
