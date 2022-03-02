import os
import re

def removenonutf8(l):
    pass

def filetolist(fname):


    my_file = open(f"{testpath}{fname}", "r")

    # reading the file
    data = my_file.read()

    data_into_list = data.replace('\n', ' ').split(" ")
    my_file.close()

    return list(data_into_list)

#regexp = re.compile(r'[^\x00-\x7f]')

testpath = "/home/ray/PycharmProjects/Sprookjesgenerator/res/"

regexp = re.compile(r'[^\x00-\x7f]')

meisjesnamen=filetolist("meisjesnamen.txt")

meisjesnamen = [str for str in meisjesnamen if not  regexp.search(str) ]


jongensnamen=filetolist("jongensnamen.txt")
jongensnamen = [str for str in jongensnamen if not regexp.search(str) ]

zelfstandigenaamwoorden=filetolist("zelfstandigenaamwoorden.txt")
werkwoorden=filetolist('werkwoorden.txt')
persoonlijkevoornaamwoorden=['ik','jij','hij','wij','jullie','zij']
unspeakable=['luul','laal','lool','rld','oow','uich','urts','uirts','lkk','lol','lal','lil','rar',
             'rir','rer','rmm','rll','uimm','oomm','aamm','rtt','rkk','rss','rch','rtt','brj','blj',
             'lel','aaa','uuu','iii','ooo','eee','bluu','lile','lul','liel','bruu','luul','aach','eech','uuch','ooch']
