# todo added is_lange_letter CHANGELOG

def is_lange_letter(letter):
    """
Een lange letter is een letter die eindeloos kan duren alle klinkers zijn lange letters.
    :param letter:
    """
    if letter in ['a','c','e','f','l','m','n','r','s','u','v','w','z']:
        return True
    else:
        return False
