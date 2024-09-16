# Case_6
# Developers: Zhambaldorzhieva A., Makarenko K.
#
import ru_local as ru

text = input().strip()
sent = -text.count('...')*2 + text.count('?') + text.count('!') + text.count('.')

