# todo make function for generating cityname in dutch

from random import choice, uniform

from Taaldoos.tel_maximaal_medeklinkers import tel_maximaal_medeklinkers
from Taaldoos.verboden_combinatie import verboden_combinatie


def stads_naam_generator():
    out = ''
    while out == '':
        out = verboden_combinatie(stads_naam_generator2())
        if tel_maximaal_medeklinkers(out) > 3:
            out = ''
    return out


def stads_naam_generator2(name=''):
    numbers = ['helle', 'ander', 'zand', 'steen', 'wees', 'ieder', 'een', 'twee', 'drie', 'vier', 'vijf', 'zes',
               'zeven', 'acht', 'negen', 'tien', 'elf', 'twaalf', 'dertien', 'veertien', 'vijftien', 'zestien',
               'zeventien', 'achtien', 'negentien', 'twintig']

    _1 = ['a', 'e', 'i', 'o', 'u', 'oo', 'aa', 'oo', 'ee', 'oe', 'ui', 'ar', 'ij', 'oer', 'are', 'pij', 'hei', 'hel',
          'ha', 'hui', 'ho', 'hop', 'hoe', 'zee', 'bree', 'bronk', 'bro', 'zomp', 'zwi'
        , 'mark', 'drek', 'drie', 'helle', 'vier', 'fro', 'po', 'ko', 'kro']
    _2 = ['wegge', 'weg', 'ker', 'tten', 'tte', 'selo', 'sel', 'ster', 'st', 'mmen', 'ssen', 'rts', 'pert', 'l',
          'chter', 'cht', 'mme', 'kel', 'k', 'kke', 'lst', 'lle', 'melo', 'ter']
    _post = ['drap', 'dam', 'dam', 'dam', 'dam', 'veld', 'veld', 'velde', 'dorp', 'dorp', 'dorp', 'dorp', 'gat', 'gat',
             'gat', 'gat', 'gat',
             'stad', 'stad', 'stad', 'stad', 'dijk', 'hekse', 'trol', 'broek', 'broeke', 'huizen', 'huizen', 'brug',
             'brug', 'brugge', 'braak'
                               'berg', 'berg', 'berg', 'berg', 'donk', 'reus', 'bos', 'bos', 'bos', 'struik', 'struik',
             'stoof', 'stoof', 'steen', 'geest', 'geest', 'reus', 'reus',
             'veen', 'veen', 'veen', 'veen', 'meer', 'meer', 'meer', 'meer', 'vecht', 'vecht', 'vecht', 'bos', 'bos',
             'bos', 'bos', 'bos', 'akker', 'akker', 'akker', 'bij den gat', ' bij het bos', ' bij de rivier', 'hove',
             'hove'
             ]
    _pre = ['hoog', 'klein', 'groot', 'boven', 'neder', 'laag', 'smal ']
    _dir = ['oost', 'west', 'noord', 'zuid']

    if uniform(0, 1) > 0.8:
        Prefix = choice(_pre)
    else:
        Prefix = ''

    if uniform(0, 1) > 0.8:
        Postfix = choice(_post)
    else:
        Postfix = ''

    if uniform(0, 1) > 0.95:
        direction = choice(_dir) + ' '
    else:
        direction = ''

    if uniform(0, 1) > 0.1:
        out = direction + Prefix + choice(_1) + choice(_2) + Postfix
    else:
        out = choice(numbers) + 'huizen'
    return out
