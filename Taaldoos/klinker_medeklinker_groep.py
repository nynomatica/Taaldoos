from is_klinker import is_klinker


# todo  : Make wiki page for klinker_medeklinker_groep()

def klinker_medeklinker_groep(woord):
    """
    Grouping is the process of grouping consonants and vowels together in a list
    example :boom  -> ['b','oo','m']
             gans  -> ['g','a','ns']
    A group has either consonants or vowels. we need this for stemming
    in Dutch the last vowel group gets often but not always compressed and the last consonant doubled
    E.g. bomen (plural) to boom (singular)
    Grouping makes finding the stem simpler.
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
