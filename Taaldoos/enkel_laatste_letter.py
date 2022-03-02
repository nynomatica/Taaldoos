from Taaldoos.maak_homogeen import maak_homogeen
from Taaldoos.tel_klinkers import tel_klinkers


def enkel_laatste_letter(woord):
    """
    zoiets als
    dikk -<dik
    boo -> bo
    maar niet gans gan
    :param woord:
    :return:
    """
    l = tel_klinkers(woord)
    if len(l[-1])>1 and  maak_homogeen(l[-1]):
        l[-1] = l[-1][0]
    return ''.join(l)
