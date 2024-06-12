# Cvičení 1 - Vytvoření datového rámce
# Představme si, že jsme si vytvořili business v lichvářství. Každý den půjčíme maximálně jedné osobě finanční částku v rozmezí 1000 Kč až 10 000 Kč.
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
    datum.append("{0}{1}".format(_,".2.2022"))
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
    else: stav_splaceni.append(False)

data = pd.DataFrame({
    "den": datum,
    "dluznik": jmena,
    "dluh": dluh,
    "splaceno":stav_splaceni
})
print(data)

