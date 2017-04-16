
def detect_anagrams(word, candidates):
    initial = list(word.lower())
    results = []
    for i in range(len(candidates)):
        if candidates[i].lower() != word.lower():
            c = sorted(candidates[i].lower())
            if c == sorted(initial):
                results.append(candidates[i])
    return results


