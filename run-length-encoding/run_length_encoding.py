from re import sub

def decode(word):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),word)


def encode(word):
    return sub(r'(.)\1+', lambda m: str(len(m.group(0))) + m.group(1),word)

