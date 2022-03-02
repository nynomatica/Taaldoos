# todo added is_blaas_letter CHANGELOG
def is_blaas_letter(letter):
    """
            Bij deze letters worden geblazen
            tong komt actief naar voren
            :param letter:
            :return:
            """
    if letter[0] in ['c', 'f', 'g', 'h', 'r', 's', 'v', 'w','z']:
        return True
    else:
        return False