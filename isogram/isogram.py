def is_isogram(word):
    word = word.lower()
    l = list(word)
    l = [x for x in l if x not in [' ', '-']]
    s = {x for x in l if x not in [' ', '-']}
    if len(s) == len(l):
        return True
    else:
        return False



