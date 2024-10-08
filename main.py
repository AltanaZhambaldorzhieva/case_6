# Case_6
# Developers: Zhambaldorzhieva A., Makarenko K.
#
import ru_local as ru
from translate import Translator
from textblob import TextBlob


def sent(txt):
    """
        The function returns the number of sentences in the text.
    """
    count = txt.count('.') + txt.count('?') + txt.count('!')
    count += - txt.count('...') * 2 - txt.count('???') * 2 - txt.count('!!!') * 2
    return count


def wrd(txt):
    """
        The function returns the number of words in the text.
    """
    count = len(txt.split())
    return count


def syl(txt):
    """
        The function returns the number of syllables of words in the text.
    """
    vowels = 'euioayыуеаоияэюё'
    count = 0
    for i in txt.lower():
        for j in vowels:
            if i == j:
                count += 1
                break
    return count


def avg_sent(wrd, sent):
    """
        The function returns the average sentence length in words.
    """
    avg = wrd / sent
    return avg


def avg_wrd(wrd, syl):
    """
        The function returns the average word length in syl.
    """
    avg = syl / wrd
    return avg


def index_Flesh_eng(avg_sent, avg_wrd):
    """
        The function returns the Flash Index of the english text.
    """
    index = 206.835 - (1.015 * avg_sent) - (84.6 * avg_wrd)
    return index


def index_Flesh_rus(avg_sent, avg_wrd):
    """
        The function returns the Flash Index of the russian text.
    """
    index = 206.835 - (1.3 * avg_sent) - (60.1 * avg_wrd)
    return index


def ton(txt):
    """
        The function returns the tonality of text.
    """
    pol = TextBlob(txt).sentiment.polarity
    if pol > 0:
        return (f'{ru.TON_POS}')
    elif pol < 0:
        return (f'{ru.TON_NEG}')
    else:
        return (f'{ru.TON_NORM}')


def subjectivity(txt):
    """
        The function returns the subjectivity of the text.
    """
    sub = TextBlob(txt).subjectivity
    return sub * 100


def detect_lang(txt):
    gs = goslate.Goslate()
    language_id = gs.detect(txt)
    return language_id


def translate(txt):
    translator = Translator(from_lang="ru", to_lang="en")
    translation = translator.translate(txt)
    return translation


count = 0
print(f'{ru.TXT}:')
txt = input().strip()
print(translate(txt))
print(f'{ru.SENT}:', sent(txt))
print(f'{ru.WRD}:', wrd(txt))
print(f'{ru.SYL}:', syl(txt))
print(f'{ru.SENT_AVR_LEN}:', avg_sent(wrd(txt), sent(txt)))
print(f'{ru.WRD_AVR_LEN}:', avg_wrd(wrd(txt), syl(txt)))
print(f'{ru.IND_FLASH}:', index_Flesh_eng(avg_sent(wrd(txt), sent(txt)), avg_wrd(wrd(txt), syl(txt))))
print(f'{ru.TON}:', ton(txt))
print(f'{ru.OBJCT}:', subjectivity(txt), '%')
