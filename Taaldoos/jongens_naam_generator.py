
from random import choice, random, randrange


def jongens_naam_generator():

    l1 =choice(['ij','aa','ee','o','e','i','ei','a','ie']) + \
    choice(['hmerink','hmer','lreus','lman','pasman','vink','sse','mmel','pper','mmelink','melink','zink','link','chter','nald','sse','s','nne','rk','rend','derik','rik','rikke','mas','terman','gott','sgod','zerman'])
    l2 =\
    choice(['l']) + \
    choice(['a','o','oe','u','i','oo','e','uu']) + \
    choice(['strik','stra','hmer','ck','ckermann','ckerman','rkman','mmerlink','mmert','chterman','kkerman','kker','pper','vink','kman','dde','p','nk','nnie','rs'])

    l3 = choice(['d','dr']) +\
    choice(['ij','aa','ee','o','e','i','ei','a','ie']) + \
    choice(['hmerink','hmer','lreus','lman','pasman','vink','sse','mmel','pper','mmelink','melink','zink','link','chter','nald','sse','s','nne','rk','rend','derik','rik','rikke','mas','terman','gott','sgod','zerman'])

    l4 = choice(['b','br','bl']) +\
    choice(['jo','uu','a','o','ee','oe','u','e']) + \
    choice(['melink','hmer','sman','ster','lker','lkman','nneman','n','reuze','lreus','rt','vink','ler','pperman','pper','kkerman','kker','terman','serman','zerman','maszoon','hmer','ming','ling','link','sma','lo','nk','t','m','s','st','ser','do','dor','tor','domas'])

    l5 = choice(['ger','geh','h','fr','f']) + \
    choice(['a','e','o','i']) +\
    choice(['melink','rel','rt','gott','sgodde','sgod','kkerman','kker','terman','zerman','nken','rend','hmer','maszoon','sma','sser','link','ming','nk','ter','ser','dor','tor','domas'])

    l6 = choice('j') + \
    choice(['a','ee','ou','aa','ee','ie','oo']) + \
    choice(['melink','rel','ret','gott','sgodde','sgod','terik','per','rik','rk','sma','kker','hanszoon','hans','han','chter','dde','tte','anneman','onne','on','fkan','dder','p','n','pper','kkerman','kker','terman','zerman','rend','hmer','maszoon','sma','sser','link','ming','nk','ter','ser','dor','tor','domas'])

    l7 = choice(['p','pr','pl'])+\
         choice(['ee','ie','a','i','au'])+\
         choice(['melink','rel','l','ret','vink','sink','zink','zgod','gott','sgodde','sgod','sterik','ster','ningk','ning','nkerman','ffer','llar','l','t','ter','terik','terman','zerman','ts','dor','doma','ser','rend','terzoon','rik','rk','sma','kker','pper','pman','lan','chter','chterman','tte','nneman','fkan','dder','n','kkerman','kker','terman','zerman','rend','hmer','maszoon','sma','sser','link','ming','king','nk','ter','ser','dor','tor','domas'])
    l8 = choice(['r'])+\
         choice(['i','o','a','oe','ij'])+\
         choice(['melink','hmer','ssel','prda','kne','preus','l','ck','nikke','nke','land','lan','derick','das','mm','mmam','lvink','zink','zing','zgod','gott','sgodde','kister','sgod','sterik','ster','nkerman','ffer','llar','n','l','tter','ter','terik','terman','zerman','tser','dor','doma','ser','rend','terzoon','rik','rk','sma','kker','pper','pman','land','chter','chterman','scher','tte','nneman','fkan','dder','n','kkerman','kker','terman','zerman','rend','hmer','maszoon','sma','sser','link','ming','king','nk','ter','ser','dor','tor','domas'])

    l9 =  choice(['v','vr','w']) +\
          choice(['i','o','a','oe','ij','u'])+\
          choice(['lf','lfsman','m','st','k','kke','link','vink','stra','zink','sterik','man','nkerman','ffen','ter','domas','derick','rick','ricke','nikke','nke','lan','lan','mme','stgott','maszoon'])
    l10 = choice(['k'])+\
          choice(['loosterman','osterman','oster','naap','lazenman','laas','necht','nechter','on','leum','arst','irst','eerst','eun','eum','arel','ars','ai','rooch','ikkerman','aster','raster'])
    l = [l1] + [l2] + [l3] + [l4] + [l5] + [l6] + [l7] + [l8] + [l9] + [l10]
    return choice(l)
