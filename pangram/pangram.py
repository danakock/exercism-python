import re

alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',\
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

def is_pangram(phrase):
    phrase = phrase.lower()
    wordList = re.sub(r'[.!,;?_"[0-9]', ' ', phrase)
    s = {x for x in wordList if x not in [' ', '-']}
    if s == alphabet:
        return True
    else:
        return False


