from Taaldoos.R import unspeakable

# unspeakable=['luul','laal','lool','rld','oow','uich','urts','uirts','lkk','lol','lal','lil','rar',
#              'rir','rer','rmm','rll','uimm','oomm','aamm','rtt','rkk','rss','rch','rtt','brj','blj',
#              'lel','aaa','uuu','iii','ooo','eee','bluu','lile','lul','liel','bruu','luul','aach','eech','uuch','ooch']

def IsUnspeakable(letters):
    return verboden_combinatie(letters) == ""


def verboden_combinatie(letters):
    for group in unspeakable:
        if group in letters:
            return ""
    return letters
