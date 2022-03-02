from Taaldoos import maak_homogeen


def verdubbel_laatste_letter(l):
    """
    wil check if the last item in the list has one letter and will duplicate is so
    ['d','i','k'] -> ['d','i','kk']
    """
    if len(l[-1]) == 1 and maak_homogeen(l[-1]):
        l[-1] = l[-1] + l[-1]
    return l
