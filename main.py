# Case_6
# Developers: Zhambaldorzhieva A., Makarenko K.
#
import ru_local as ru


def sent(txt):
    count = txt.count('.') + txt.count('?') + txt.count('!')
    count += - txt.count('...')*2 - txt.count('???')*2 - txt.count('!!!')*2
    return count


def wrd(txt):
    count = len(txt.split())
    return count


count = 0
txt = input().strip()
print(sent(txt))
print(wrd(txt))