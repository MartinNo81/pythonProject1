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
import calendar


datum = []

for _ in range(1,32):
    datum.append("{0}{1}".format("2022,02,",_))

jmena_zdroj = ["Pavel", "Petr","Jana","Milan","Vlasta"]

data = pd.DataFrame({
    "den": datum,
    "dluznik": np.random.choice(jmena_zdroj, size=31),
    "dluh": np.random.randint(1000, 10001, size=31),
    "splaceno": np.random.choice((True,False),size=31)
})


# Cvičení 2 - Analýza problémů s datovým formátem
# Uvědomili jsme si, že datum v únoru nemůže být do 31.2. Upravte vhodně tyto záznamy. Nechám na vás jak, ale můžu poradit, že můžete záznamy smazat jako nevalidní nebo upravit na nový měsíc.

data = pd.DataFrame({
    "den": pd.date_range(start="2022-02-01", end="2022-03-03", freq='D'),
    "dluznik": np.random.choice(jmena_zdroj, size = 31),
    "dluh": np.random.randint(1000, 10001, size=31),
    "splaceno": np.random.choice((True,False),size=31)
})

# Cvičení 3 - Analýza problémů s hodnotami
# jsme zjistili, že jsme si i špatně zapsali půjčovanou částku. Každou sobotu a neděli jsme půjčili maximálně 5000. Pokud tedy v nějakou sobotu nebo neděli částka přesahuje 5000, pak ji upravte na 5000 jako maximální hodnotu.


den_0 = pd.Timestamp("2022-02-01")
(data.loc[0,["den_v_tydnu"]]) = (den_0.dayofweek)
i = (den_0.dayofweek)

for _ in range(1,31):
    (data.loc[_,["den_v_tydnu"]]) = i+1
    i +=1
    if i == 6:
        i = -1

for _ in data.index:
    if data.at[_, "dluh"] > 5000 and data.at[_, "den_v_tydnu"] > 4 :
        data.at[_, "dluh"] = 5000

print(data)
#Cvičení 4 - rozsekání
#Následující kód vezme sérii čísel, zadefinuje hranice kategorií (biny), pojmenuje kategorie a rozdělí hodnoty v sérii do příslušných binů s klíčem s názvem kategorie. Takto vzniklou sérii s četnostmi v binech přidá do datového rámce pomocí konkatenace.


vyska = pd.Series(np.random.randint(120,231, size = 20))
kategorie = ("trpasličí","malý","průměrný","vysoký","obří")
biny = (0, 130, 160, 180, 200,231)
skupiny = pd.cut(vyska, bins=biny, labels=kategorie)
#print(skupiny)

#Kolikrát jste vybrané osobě půjčili částku v rozmezí 0 až 2500, 2500 až 5000, 5000 až 7500 a 7500 až 10000.
#Kolik jste půjčili v jednotlivých dnech pomocí liniového grafu.
#Kolik jste půjčili komulativně celkově v průběhu dnů.
import matplotlib.pyplot as plt

jmeno = ["Pavel"]
filtrovana_data = data[data["dluznik"].isin(jmeno)]
plt.hist(filtrovana_data["dluh"], bins=(0,2500,5000,7500,10000), edgecolor='black')

plt.figure(figsize=(10, 5))
plt.plot(filtrovana_data["den"], filtrovana_data["dluh"], marker='o')
plt.grid(True)

plt.figure(figsize=(10, 5))
plt.plot(data["den"], data["dluh"], marker='o')
plt.grid(True)
plt.show()

#Proveďte korelační analýzu a vypočítejte základní statistické údaje k datovému rámci o půjčkách.

print(data.describe())
print(data.corr(numeric_only=True))
