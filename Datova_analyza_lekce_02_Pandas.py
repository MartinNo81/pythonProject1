# Cvičení 1 - Vytvoření datového rámce
# Představme si, že jsme si vytvořili business v lichvářství. Každý den půjčíme maximálně jedné osobě finanční částku v rozmezí 1000 Kč až 10 000 Kč.
import calendar
import random

# Vytvořte datový rámec, kde:

# první sloupec (neindexový) bude složen z datumů od 1.2.2022 do 31.2.2022 (ano opravdu)
# druhý sloupec bude složen ze jmen - vymyslete si nějaký seznam jmen a naplňte tento sloupec opakovaným náhodným výběrem z tohoto seznamu
# třetí sloupec bude složen z finanční částky, kterou dané osobě půjčujeme v daný den, částka bude náhodné číslo v rozmezí 1000 až 10000
# čtvrtý sloupec bude složen z pravdivostní hodnoty, zda osoba již svůj dluh z daného dne splatila nebo ne

import pandas as pd
import datetime
import numpy as np



datum = []

for _ in range(1,32):
    datum.append("{0}{1}".format("2022,02,",_))
jmena = []
jmena_zdroj = ["Pavel", "Petr","Jana","Milan","Vlasta","Oto","Tomáš","Valentýn","Rozálie","Tereza"]
for _ in range(31):
    jmena.append(random.choice(jmena_zdroj))

dluh= []
for _ in range(31):
    dluh.append(random.randint(1000,10001))

splatka = []
stav_splaceni = []
for _ in range(31):
    splatka.append(random.randint(1000,10001))
for _ in range(31):
    if splatka[_] > dluh[_]:
        stav_splaceni.append(True)
    else:
        stav_splaceni.append(False)

data = pd.DataFrame({
    "den": datum,
    "dluznik": jmena,
    "dluh": dluh,
    "splaceno":stav_splaceni
})


# Cvičení 2 - Analýza problémů s datovým formátem
# Uvědomili jsme si, že datum v únoru nemůže být do 31.2. Upravte vhodně tyto záznamy. Nechám na vás jak, ale můžu poradit, že můžete záznamy smazat jako nevalidní nebo upravit na nový měsíc.
for _ in data.index:
    (data.loc[_,["den"]]) = (np.datetime64("2022-02-01")+_)




# Cvičení 3 - Analýza problémů s hodnotami
# jsme zjistili, že jsme si i špatně zapsali půjčovanou částku. Každou sobotu a neděli jsme půjčili maximálně 5000. Pokud tedy v nějakou sobotu nebo neděli částka přesahuje 5000, pak ji upravte na 5000 jako maximální hodnotu.
import calendar

d = pd.Timestamp("2022-02-01")
(data.loc[0,["den_v_tydnu"]]) = (d.dayofweek)
i = (d.dayofweek)
print(i)
for _ in range(1,31):
    (data.loc[_,["den_v_tydnu"]]) = i+1
    i +=1
    if i == 6:
        i = -1

for _ in data.index:
    if data.at[_, "dluh"] > 5000 and data.at[_, "den_v_tydnu"] > 4 :
        data.at[_, "dluh"] = 5000
print(data)
