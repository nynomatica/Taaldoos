# todo added is_huig_letter CHANGELOG

def is_huig_letter(letter):
    """
        Bij deze letters blokkeer de huig actief de keel
        tong komt actief naar voren
        :param letter:
        :return:
        """
    if letter[0] in ['i', 'u', 'j','l','n','r','k','x']:
        return True
    else:
        return False
