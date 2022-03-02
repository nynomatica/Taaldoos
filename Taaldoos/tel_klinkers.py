from Taaldoos.is_klinker import is_klinker


def tel_klinkers(letters):
    buf = ''
    lout = []
    if letters != "":
        last = is_klinker(letters[0])
    for i in letters:
        n = is_klinker(i)
        if n != last:
            lout.append(buf)
            buf = ''
        last = n
        buf += i
    if buf != '':
        lout.append(buf)
    return lout