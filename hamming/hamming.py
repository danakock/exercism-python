
def distance(strand1, strand2):
    ham = 0
    if len(strand1) == len(strand2):
            for i in range(len(strand1)):
                if strand1[i] != strand2[i]:
                    ham += 1
    else:
        raise ValueError

    return ham
