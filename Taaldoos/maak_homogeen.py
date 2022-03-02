def maak_homogeen(letters, last=None):
    """
    looks if letters is homogene has only one character
    :param letters:
    :param last:
    :return:
    """
    last = str(letters)[0]
    for i in letters:
        if i != last:
            return False
    return True
