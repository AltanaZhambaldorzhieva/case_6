def snt(txt):
    cnt = txt.count('.') + txt.count('?') + txt.count('!')
    cnt += - txt.count('...')*2 - txt.count('???')*2 - txt.count('!!!')*2
    return cnt
def wrd(txt):
    a = len(txt.split())
    return a

txt = input().strip()
print(snt(txt))
print(wrd(txt))