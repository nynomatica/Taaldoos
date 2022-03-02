from random import choice, randrange

from Taaldoos.R import meisjesnamen

# todo Make wiki page for vrouw_naam_generator()
def vrouw_naam_generator():
    """
        Basically this functions generates a random female name in old dutch
        this is the automated output from a trained nn cai free pascal GAN and old dutch names
        The names are pretty convincing but also a blend of fantasy perfect for this project I think
        maximal entropy 4k names... can be used for a game or for text generation
        if mixed in a small amount of real names (20%) to make it more convincingly
    :return: string is female name all lowercase a-z
    """
    l1 = choice(['m', 'l']) + choice(['oe', 'ee', 'ie', 'i', 'o']) + choice(
        ['kke', 'kka', 'rena', 'randa', 'tje', 'sje', 'p', 'nda', 'nekke', 'nka', 'tje', 'nikke', 'nukke', 'dra'])
    l2 = choice(['fr', 'l']) + choice(['a', 'e', 'i', 'ie', 'o', 'ou', 'u']) + choice(
        ['mara', 'annia', 'kke', 'kka', 'lana', 'lena', 'lle', 'la', 'landa', 'rena', 'ppa', 'da', 'ta', 'nda', 'nekke',
         'nka', 'tje', 'nikke', 'nukke', 'tsa']);
    l3 = choice(['dr', 'l']) + choice(['a', 'e', 'i', 'o']) + choice(
        ['lliona', 'kka', 'lama', 'landa', 'lle', 'da', 'ta', 'nda', 'nekke'])
    l4 = choice(['m', 'j']) + choice(['i', 'o', 'a', 'e', 'i', 'uu', 'ie']) + choice(
        ['mma', 'lliona', 'llia', 'llie', 'kke', 'kka', 'lande', 'landa', 'lena', 'lana', 'randa', 'rra', 'nekke', 'da',
         'tta', 'nda', 'nka', 'lle', 'nna', 'pje', 'rra', 'sta', 'mma', 'nikke', 'tje', 'nukke'])
    l5 = choice(['p', 'pr', 'pl']) + choice(['oe', 'ee', 'ie', 'i', 'o', 'a']) + choice(
        ['lliona', 'kke', 'kka', 'lana', 'lena', 'mmeke', 'rra', 'mmatje', 'mma', 'nna', 'ma', 'tje', 'sje', 'ppa',
         'nda', 'nekke', 'nka', 'tje', 'nikke', 'nukke', 'ninka'])
    l6 = choice(['n']) + choice(['a', 'o']) + choice(
        ['kke', 'kka', 'lena', 'rrada', 'nda', 'na', 'ntje', 'nekke', 'nka', 'nikke', 'nukke', 'ninka', 'mmeke'])
    l7 = choice(['r']) + choice(['o', 'a', 'o', 'oe', 'i']) + choice(
        ['lliona', 'llia', 'kke', 'kka', 'dalena', 'lena', 'dalana', 'ssa', 'kka', 'mma', 'landa', 'lla', 'lesa', 'nda',
         'pinka', 'ka', 'ppa', 'sje', 'nda', 'na', 'nekke', 'nka', 'nukke']);
    l8 = choice(['s', 'sl', 'slet', 'zlat', 'za', 'sp']) + choice(['a', 'o', 'oe', 'i', 'u', 'e']) + choice(
        ['lliona', 'llia', 'lamanka', 'kke', 'kka', 'lana', 'lesa', 'la', 'landa', 'rra', 'lly', 'nny', 'ra', 'la',
         'da', 'nda', 'nde', 'ndi', 'ka', 'ppa', 'sje', 'nda', 'na', 'nekke', 'nka', 'nukke', 'se'])
    l9 = choice(['t', 'tr']) + choice(['a', 'o', 'oe', 'i', 'u', 'uu', 'e']) + choice(
        ['lliona', 'llia', 'kke', 'kka', 'lana', 'nka', 'st', 's', 'sta', 'nnike', 'nnuke', 'ppa', 'nda', 'lly', 'pka',
         'se', 'sje', 'nna', 'nne'])

    l10 = choice(['v', 'vr']) + choice(['a', 'a', 'a']) + choice(
        ['lona', 'kke', 'kka', 'lana', 'nouka', 'rrana', 'nka', 'sta', 'se', 'nnike', 'nnuke', 'ppa', 'nda', 'lly',
         'pka', 'se', 'sje', 'nna', 'nne', 'nnike'])

    l11 = choice(['w']) + choice(['e', 'a', 'i', 'o']) + choice(
        ['chta', 'nnia', 'llia', 'zsana', 'kke', 'kka', 'lana', 'nouka', 'randa', 'rra', 'nka', 'sta', 'se', 'nnike',
         'nnuke', 'ppa', 'nda', 'lly', 'pka', 'sse', 'sje', 'nna', 'nne', 'nnike'])

    l12 = choice(['o', 'a', 'e', 'i']) + choice(
        ['ssa', 'lliona', 'llia', 'mara', 'mara', 'strana', 'strid', 'kke', 'mana', 'cetilana', 'stlana', 'stana',
         'stra', 'sta', 'lyse', 'riana', 'landa', 'lana', 'lena', 'nouk', 'rrana', 'nge', 'nna', 'nnaatje', 'nka',
         'dde', 'fka', 'fke', 'nka', 'nke', 'nne', 'nja', 'ppa'])

    l13 = choice(['g', 'gr']) + choice(['e', 'ie', 'i']) + choice(
        ['ssa', 'nneke', 'nnuke', 'mma', 'llia', 'tana', 'lana', 'ralda', 'ranka', 'randa', 'nouka', 'nna', 'nka',
         'dde', 'fka', 'fke', 'nka', 'nke', 'nne', 'ppa', 'tje'])

    l14 = choice(['h']) + choice(['er', 'e', 'ee', 'i', 'ei']) + choice(
        ['lliona', 'llia', 'tzana', 'tsana', 'lleke', 'lluke', 'lla', 'ster', 'tana', 'llana', 'llena', 'ranka',
         'randa', 'nouka', 'nna', 'nka', 'dde', 'fka', 'fke', 'nka', 'nke', 'nne', 'ppa', 'pukke'])

    l15 = choice(['b', 'br', 'bl']) + choice(['ee', 'ea', 'i', 'e', 'ou']) + choice(
        ['za', 'mora', 'nnia', 'se', 'mma', 'dra', 'tta', 'dda', 'da', 'ta', 'nda', 'nekke', 'nukke', 'tje', 'nna',
         'nne'])

    sw = randrange(0, 18)

    if sw == 0:
        return l1
    if sw == 1:
        return l2
    if sw == 2:
        return l3
    if sw == 3:
        return l4
    if sw == 4:
        return l5
    if sw == 5:
        return l6
    if sw == 6:
        return l7
    if sw == 7:
        return l8
    if sw == 8:
        return l9
    if sw == 9:
        return l10
    if sw == 10:
        return l11
    if sw == 11:
        return l12
    if sw == 12:
        return l13
    if sw == 13:
        return l14
    if sw == 14:
        return l15
    if sw > 14:
        return choice(meisjesnamen)
