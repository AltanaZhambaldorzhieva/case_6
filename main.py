# Case_6
# Developers: Zhambaldorzhieva A., Makarenko K.
#
import ru_local as ru
from textblob import TextBlob


def sent(txt):
    """
        The function returns the number of sentences in the text.
    """

    count = txt.count('.') + txt.count('?') + txt.count('!')
    count += - txt.count('...')*2 - txt.count('???')*2 - txt.count('!!!')*2
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
                count+=1
                break
    return count

def avg_sent(wrd,sent):
    avg = wrd/sent
    return avg

def avg_wrd(wrd,syl):
    avg = syl/wrd
    return avg

def index_Flesh_eng(avg_sent,avg_wrd):
    index = 206.835 - (1.015 * avg_sent) - (84.6 * avg_wrd)
    return index

def ton(txt):
    blob = TextBlob(txt)
    pol = blob.sentiment.polarity

    if pol > 0:
        print(f'{ru.TON}: {ru.TON_POS}')
    elif pol < 0:
        print(f'{ru.TON}: {ru.TON_NEG}')
    else:
        print(f'{ru.TON}: {ru.TON_NORM}')

    return pol


count = 0
txt = input().strip()
print(sent(txt))
print(wrd(txt))
print(avg_sent(wrd(txt),sent(txt)))
print(avg_wrd(wrd(txt),syl(txt)))
print(index_Flesh_eng(avg_sent(wrd(txt),sent(txt)),avg_wrd(wrd(txt),syl(txt))))