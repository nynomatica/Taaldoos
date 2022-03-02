# todo added is_zachte_letter CHANGELOG
def is_zachte_letter(letter):
    """
Zachte letter is 'voice less' geen wrijving
    :param letter:
    """
    if letter[0] in ['b', 'd', 'f', 'g', 'h', 'p','v','w']:
        return True
    else:
        return False
