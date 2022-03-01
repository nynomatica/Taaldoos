def is_klinker(letter):
    """
        kijkt of letter een klinker of medeklinker is
    :param letter:
    :return:
    """
    if letter == '':
        return True
    else:
        return letter[0] in ['a', 'e', 'i', 'o', 'u']