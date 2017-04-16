dna_dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}

def to_rna(dna):
    dna = dna.upper()
    dna_list = []
    for d in dna:
        if d in dna_dict:
            dna_list.append(dna_dict[d])
    if len(dna_list) == len(dna):
        return ''.join(dna_list)
    else:
        return ''
