# todo added is_keel_letter CHANGELOG

def is_keel_letter(letter):
    """
    Men gebruikt de keel om deze letter uit te spreken.
    :param letter:
    :return:
    """
    if letter[0] in ['g','h','r']:
        return True
    else:
        return False

