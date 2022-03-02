# todo added is_harde_letter CHANGELOG

def is_harde_letter(letter):
    """
    waar het vooral om gaat is om de definitie ik gebruik erg lange functie namen in het Nederlands en doe dit vooral
    om in context te blijven. ook komen er definities voor die moeilijk te omschrijven zijn, wat blijkt, is dat het
    verzinnen van woorden voor functies geen goede strategie is dus voor nu laat ik het zoals het is. Een harde
    letter is een letter die actief wordt uitgesproken met open of half open mond 'c k q r s t'. :param letter:
    """
    if letter[0] in ['c','k','q','r','s','t']:
        return True
    else:
        return False
