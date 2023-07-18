from algemene_functies import mijn_functie_2
def aanbieding_1(smaak, prijs, korting):
    korting_prijs = prijs - (prijs * korting)
    prijsF = '{:.2f}'.format(prijs).replace('.', ',')
    korting_prijsF = '{:.2f}'.format(korting_prijs).replace('.', ',')
    print(f'Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijsF} euro voor {korting_prijsF} euro.')

def inkomsten_totaal(inkomsten, btw):
    inkomsten_totaal = sum(inkomsten)
    totaal_btw = inkomsten_totaal - (inkomsten_totaal / (1 + btw))
    inkomsten_totaalF = '{:.2f}'.format(inkomsten_totaal).replace('.', ',')
    totaal_btwF = '{:.2f}'.format(totaal_btw).replace('.', ',')
    print(f'Het totaal van alle inkomsten van deze week is {inkomsten_totaalF} euro, waarover {totaal_btwF} euro btw betaald dient te worden.')

def laag_en_hoog(mijn_lijst):
    laagste = min(mijn_lijst)
    hoogste = max(mijn_lijst)
    return[hoogste, laagste]

def gemiddelde(mijn_lijst):
    gemiddelde = sum(mijn_lijst) / len(mijn_lijst)
    gemiddeldeF = '{:.2f}'.format(gemiddelde).replace('.', ',')
    print(f'De gemiddelde inkomsten deze week zijn {gemiddeldeF}.')

def meervoudig(invoer_lijst):
    return(laag_en_hoog(invoer_lijst))

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0], korte_lijst[1])
    return uitvoer