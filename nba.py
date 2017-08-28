import orodja
import requests
import re
import csv




def poberi_podatke():
    for stran in range (2,243,40):
        osnovni_naslov = 'http://www.espn.com/nba/statistics/player/_/stat/scoring-per-game/sort/avgPoints/count/'
        naslov = '{}{}'.format(osnovni_naslov,stran)
        ime = 'StatLeaders1617/ StatLeaders,{}.html.txt'.format(stran)
        orodja.shrani(naslov, ime)



def zbrisi_pojavitev(pojavitev):
    podatki = pojavitev.groupdict()
    podatki ['id'] = int(podatki['id'])
    podatki ['odigrane_igre'] = int(podatki['odigrane_igre'])
    podatki ['minute_natekmo'] = float(podatki['minute_natekmo'])
    podatki ['točke_na_tekmo'] = float(podatki['točke_na_tekmo'])
    podatki ['met_iz_igre'] = int(podatki['met_iz_igre'])
    podatki ['trojke'] = int(podatki['trojke'])
    podatki ['prosti_meti'] = int(podatki['prosti_meti'])
    return podatki


def pripravi_nba():
    regex_nba = re.compile(
        r'<a href="http://www.espn.com/nba/player/_/id/(?P<id>\d+)/.*?>(?P<igralec>.*?)</a>.*?align="left">(?P<ekipa>.*?)</td><td >(?P<odigrane_igre>\d+)</td><td >(?P<minute_natekmo>.*?)<.*?class="sortcell">(?P<točke_na_tekmo>.*?)<.*?/td><td >.(?P<met_iz_igre>\d+)<.*?</td><td >.(?P<trojke>\d+)<.*?</td><td >.(?P<prosti_meti>\d+)<.*?>',
        flags = re.DOTALL
    )



               #<a href="http://www.espn.com/nba/player/_/id/6583/anthony-davis">Anthony Davis</a>, PF</td><td align="left">NO</td><td >37</td><td >37.1</td><td  class="sortcell">29.1</td><td >10.5-21.2</td><td >.496</td><td >0.6-1.9</td><td >.300</td><td >7.6-9.5</td><td >.796</td></tr><tr class="evenrow player-46-3992" align="right"><td align="left">3</td><td align="left">





    pojavitve = []
    for html_datoteka in orodja.datoteke('StatLeaders1617/'):
        vsebina = orodja.vsebina_datoteke(html_datoteka)
        for pojavitev in re.finditer(regex_nba, vsebina):
            pojavitve.append(zbrisi_pojavitev(pojavitev))

    orodja.zapisi_tabelo(pojavitve, ['id', 'igralec', 'ekipa', 'odigrane_igre', 'minute_natekmo', 'točke_na_tekmo', 'met_iz_igre', 'trojke', 'prosti_meti'], 'pojavitve7.csv')




pripravi_nba()

