from Taaldoos.is_klinker import is_klinker


def maskeer_klinkers(letters, out=''):
    for letter in letters:
        if is_klinker(letter):
            out = out + '.'
        else:
            out = out + letter
    return out
