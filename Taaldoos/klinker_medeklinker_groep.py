from is_klinker import is_klinker


def klinker_medeklinker_groep(woord):
    """
    Grouping is the process of grouping consonants and vowels together in a list
    example :boom  -> ['b','oo','m']
             gans  -> ['g','a','ns']
     a group has either consonants or vowels
    :param woord:
    :return: list
    """
    buf = ''
    lout = []
    if woord != "":
        last = is_klinker(woord[0])
    for i in woord:
        n = is_klinker(i)
        if n != last:
            lout.append(buf)
            buf = ''
        last = n
        buf += i
    if buf != '':
        lout.append(buf)
    return lout