# todo added is_tong_letter CHANGELOG

def is_tong_letter(letter):
    """
    Men gebruikt de tong om deze letter uit te spreken.
    er wordt hier niets over de stand van de tong gezet alleen dat de
    tong nodig is om letter te vormen in het proces
    :param letter:
    :return:
    """
    if letter[0] in ['c','d','e','i','j','k','l','n','q','s','t','u','x','z']:
        return True
    else:
        return False

