# todo added is_mond_letter CHANGELOG

def is_mond_letter(letter):
    """
    Men gebruikt de tong om deze letter uit te spreken.
    :param letter:
    :return:
    """
    if letter[0] in ['b','f','m','p','v','w']:
        return True
    else:
        return False

