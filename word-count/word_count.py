import re
from collections import Counter

def word_count(phrase):
    phrase = phrase.lower()
    pattern = re.compile('[\W+\/.!,;?_]')
    string = re.sub(pattern, ' ', phrase).split()
    count = Counter(string)
    return count

