# todo added is_multi_klinker CHANGELOG

def is_multi_klinker(letter):
    """

    Men gebruikt de tong om deze letter uit te spreken.
    er wordt hier niets over de stand van de tong gezet alleen dat de
    tong nodig is om letter te vormen in het proces
    :param letter:
    :return:
    """
    if letter in ['aa','ee','oo','uu','au','ou','ei','ie','ij','aai','ooi','oe']:
        return True
    else:
        return False
