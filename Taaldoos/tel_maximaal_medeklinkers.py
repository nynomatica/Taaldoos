
from Taaldoos.is_klinker import is_klinker


def tel_maximaal_medeklinkers(letters):
    seq = 0
    mx = 0
    for letter in letters:
        if is_klinker(letter)==False:
            seq +=1
        else:
            seq = 0
        if seq > mx:
            mx = seq
    return mx
