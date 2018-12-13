def LoadIgnores(d):
    f = open('ignore.list','r')
    words = f.read().splitlines()
    for w in words: d[w] = 1

def RemoveIgnores(l, d):
    # l is a list of strings, i.e. a sentence broken into its words
    # d is a dictionary of words to remove from the sentence
    nl = []
    for w in l:
        if w not in d:
            w = w.lower().replace("?","").replace("!","").replace(",","")
            nl.append(w)
    return nl

def MakeDict(list, d):
    if len(list) == 0: return
    if len(list) == 1: d[list[0]] = 1
    elif list[0] not in d: d[list[0]] = {}
    MakeDict(list[1:], d[list[0]])

# main
dict = {}
ignore = {}
LoadIgnores(ignore)

f = open('cards.dat','r')
cards = f.read().splitlines()
for c in cards:
    words = RemoveIgnores(c.split(), ignore)
    MakeDict(words, dict)

print json.dumps(dict)
