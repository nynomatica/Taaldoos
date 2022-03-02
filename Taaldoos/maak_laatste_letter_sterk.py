def maak_laatste_letter_sterk(letters):
    """

    will make the last letter strong
    slaaf ->  slaav
    baas -> baaz
    :param letters:

    :return list:
    """
    l = list(letters)
    if l[-1] == 's':
        l[-1] = 'z'
    if l[-1] == 'f':
        l[-1] = 'v'
    return ''.join(l)
